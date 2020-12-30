# -*- coding: utf-8 -*-
"""Explorepy main module

This module provides the main class for interacting with Explore devices.

Examples:
    Before starting a session, make sure your device is paired to your computer. The device will be shown under the
    following name: Explore_XXXX, with the last 4 characters being the last 4 hex numbers of the devices MAC address

    >>> import explorepy
    >>> explore = explorepy.Explore()
    >>> explore.connect(device_name='Explore_1432')  # Put your device Bluetooth name
    >>> explore.visualize(bp_freq=(1, 40), notch_freq=50)
"""

import os
import time
from appdirs import user_cache_dir
from threading import Timer

import numpy as np

import explorepy
from explorepy.tools import create_exg_recorder, create_orn_recorder, create_marker_recorder, LslServer, PhysicalOrientation
from explorepy.command import MemoryFormat, SetSPS, SoftReset, SetCh, ModuleDisable, ModuleEnable
from explorepy.stream_processor import StreamProcessor, TOPICS


class Explore:
    r"""Mentalab Explore device"""

    def __init__(self):
        self.is_connected = False
        self.stream_processor = None
        self.recorders = {}
        self.device_name = None

    def connect(self, device_name=None, mac_address=None):
        r"""
        Connects to the nearby device. If there are more than one device, the user is asked to choose one of them.

        Args:
            device_name (str): Device name("Explore_XXXX"). Either mac address or name should be in the input
            mac_address (str): The MAC address in format "XX:XX:XX:XX:XX:XX"
        """
        if device_name:
            self.device_name = device_name
        else:
            self.device_name = 'Explore_' + mac_address[-5:-3] + mac_address[-2:]
        self.stream_processor = StreamProcessor()
        self.stream_processor.start(device_name=device_name, mac_address=mac_address)
        while "adc_mask" not in self.stream_processor.device_info:
            print('Waiting for device info packet...')
            time.sleep(.2)
        print('Device info packet has been received. Connection has been established. Streaming...')
        self.is_connected = True
        self.stream_processor.send_timestamp()

    def disconnect(self):
        r"""Disconnects from the device
        """
        self.stream_processor.stop()
        self.is_connected = False

    def acquire(self, duration=None):
        r"""Start getting data from the device

        Args:
            duration (float): duration of acquiring data (if None it streams data endlessly)
        """
        self._check_connection()
        duration = self._check_duration(duration)

        def callback(packet):
            print(packet)

        self.stream_processor.subscribe(callback=callback, topic=TOPICS.raw_ExG)
        time.sleep(duration)
        self.stream_processor.unsubscribe(callback=callback, topic=TOPICS.raw_ExG)

    def record_data(self, file_name, do_overwrite=False, duration=None, file_type='csv', block=False):
        r"""Records the data in real-time

        Args:
            file_name (str): Output file name
            do_overwrite (bool): Overwrite if files exist already
            duration (float): Duration of recording in seconds (if None records endlessly).
            file_type (str): File type of the recorded file. Supported file types: 'csv', 'edf'
        """
        self._check_connection()

        # Check invalid characters
        if set(r'<>{}[]~`*%').intersection(file_name):
            raise ValueError("Invalid character in file name")
        if file_type not in ['edf', 'csv']:
            raise ValueError('{} is not a supported file extension!'.format(file_type))
        duration = self._check_duration(duration)

        exg_out_file = file_name + "_ExG"
        orn_out_file = file_name + "_ORN"
        marker_out_file = file_name + "_Marker"

        self.recorders['exg'] = create_exg_recorder(filename=exg_out_file,
                                                    file_type=file_type,
                                                    fs=self.stream_processor.device_info['sampling_rate'],
                                                    adc_mask=self.stream_processor.device_info['adc_mask'],
                                                    do_overwrite=do_overwrite)
        self.recorders['orn'] = create_orn_recorder(filename=orn_out_file,
                                                    file_type=file_type,
                                                    do_overwrite=do_overwrite)

        if file_type == 'csv':
            self.recorders['marker'] = create_marker_recorder(filename=marker_out_file, do_overwrite=do_overwrite)
        elif file_type == 'edf':
            self.recorders['marker'] = self.recorders['exg']

        self.stream_processor.subscribe(callback=self.recorders['exg'].write_data, topic=TOPICS.raw_ExG)
        self.stream_processor.subscribe(callback=self.recorders['orn'].write_data, topic=TOPICS.raw_orn)
        self.stream_processor.subscribe(callback=self.recorders['marker'].set_marker, topic=TOPICS.marker)
        print("Recording...")
        self.recorders['timer'] = Timer(duration, self.stop_recording)
        self.recorders['timer'].start()
        if block:
            try:
                while self.recorders['timer'].is_alive():
                    time.sleep(.3)
            except KeyboardInterrupt:
                print("Got Keyboard Interrupt!")
                self.stop_recording()

    def stop_recording(self):
        """Stop recording"""
        self.stream_processor.unsubscribe(callback=self.recorders['exg'].write_data, topic=TOPICS.raw_ExG)
        self.stream_processor.unsubscribe(callback=self.recorders['orn'].write_data, topic=TOPICS.raw_orn)
        self.stream_processor.unsubscribe(callback=self.recorders['marker'].set_marker, topic=TOPICS.marker)
        self.recorders['exg'].stop()
        self.recorders['orn'].stop()
        if self.recorders['exg'].file_type == 'csv':
            self.recorders['marker'].stop()
        if self.recorders['timer'].is_alive():
            self.recorders['timer'].cancel()
        print('Recording stopped.')

    def convert_bin(self, bin_file, out_dir='', file_type='edf', do_overwrite=False):
        """Convert a binary file to EDF or CSV file

        Args:
            bin_file (str): Path to the binary file recorded by Explore device
            out_dir (str): Output directory path (must be relative path to the current working directory)
            file_type (str): Output file type: 'edf' for EDF format and 'csv' for CSV format
            do_overwrite (bool): Whether to overwrite an existing file

        """
        if file_type not in ['edf', 'csv']:
            raise ValueError('Invalid file type is given!')
        self.recorders['file_type'] = file_type
        head_path, full_filename = os.path.split(bin_file)
        filename, extension = os.path.splitext(full_filename)
        assert os.path.isfile(bin_file), "Error: File does not exist!"
        assert extension == '.BIN', "File type error! File extension must be BIN."
        out_full_path = os.path.join(os.getcwd(), out_dir)
        exg_out_file = out_full_path + filename + '_exg'
        orn_out_file = out_full_path + filename + '_orn'
        marker_out_file = out_full_path + filename + '_marker'
        self.stream_processor = StreamProcessor()
        self.stream_processor.read_device_info(bin_file=bin_file)
        self.recorders['exg'] = create_exg_recorder(filename=exg_out_file,
                                                    file_type=self.recorders['file_type'],
                                                    fs=self.stream_processor.device_info['sampling_rate'],
                                                    adc_mask=self.stream_processor.device_info['adc_mask'],
                                                    do_overwrite=do_overwrite)
        self.recorders['orn'] = create_orn_recorder(filename=orn_out_file,
                                                    file_type=self.recorders['file_type'],
                                                    do_overwrite=do_overwrite)

        if self.recorders['file_type'] == 'csv':
            self.recorders['marker'] = create_marker_recorder(filename=marker_out_file, do_overwrite=do_overwrite)
        else:
            self.recorders['marker'] = self.recorders['exg']

        self.stream_processor.subscribe(callback=self.recorders['exg'].write_data, topic=TOPICS.raw_ExG)
        self.stream_processor.subscribe(callback=self.recorders['orn'].write_data, topic=TOPICS.raw_orn)
        self.stream_processor.subscribe(callback=self.recorders['marker'].set_marker, topic=TOPICS.marker)

        def device_info_callback(packet):
            new_device_info = packet.get_info()
            if not self.stream_processor.compare_device_info(new_device_info):
                new_file_name = exg_out_file + "_" + str(np.round(packet.timestamp, 0))
                print("WARNING: Creating a new file:", new_file_name + '.' + self.recorders['file_type'])
                self.stream_processor.unsubscribe(callback=self.recorders['exg'].write_data, topic=TOPICS.raw_ExG)
                self.stream_processor.unsubscribe(callback=self.recorders['marker'].set_marker, topic=TOPICS.marker)
                self.recorders['exg'].stop()
                self.recorders['exg'] = create_exg_recorder(filename=new_file_name,
                                                            file_type=self.recorders['file_type'],
                                                            fs=self.stream_processor.device_info['sampling_rate'],
                                                            adc_mask=self.stream_processor.device_info['adc_mask'],
                                                            do_overwrite=do_overwrite)
                self.recorders['marker'] = self.recorders['exg']
                self.stream_processor.subscribe(callback=self.recorders['exg'].write_data, topic=TOPICS.raw_ExG)
                self.stream_processor.subscribe(callback=self.recorders['marker'].set_marker, topic=TOPICS.marker)

        self.stream_processor.subscribe(callback=device_info_callback, topic=TOPICS.device_info)
        self.stream_processor.open_file(bin_file=bin_file)
        print("Converting...")
        while self.stream_processor.is_connected:
            time.sleep(.1)
        print('Conversion finished.')

    def push2lsl(self, duration=None):
        r"""Push samples to two lsl streams (ExG and ORN streams)

        Args:
            duration (float): duration of data acquiring (if None it streams for one hour).
        """
        self._check_connection()
        duration = self._check_duration(duration)

        lsl_server = LslServer(self.stream_processor.device_info)
        self.stream_processor.subscribe(topic=TOPICS.raw_ExG, callback=lsl_server.push_exg)
        self.stream_processor.subscribe(topic=TOPICS.raw_orn, callback=lsl_server.push_orn)
        self.stream_processor.subscribe(topic=TOPICS.marker, callback=lsl_server.push_marker)
        time.sleep(duration)

        print("Data acquisition finished after ", duration, " seconds.")
        self.stream_processor.stop()
        time.sleep(1)

    def visualize(self, bp_freq=(1, 30), notch_freq=50):
        r"""Visualization of the signal in the dashboard

        Args:
            bp_freq (tuple): Bandpass filter cut-off frequencies (low_cutoff_freq, high_cutoff_freq), No bandpass filter
            if it is None.
            notch_freq (int): Line frequency for notch filter (50 or 60 Hz), No notch filter if it is None
        """
        assert self.is_connected, "Explore device is not connected. Please connect the device first."

        if notch_freq:
            self.stream_processor.add_filter(cutoff_freq=notch_freq, filter_type='notch')

        if bp_freq:
            if bp_freq[0] and bp_freq[1]:
                self.stream_processor.add_filter(cutoff_freq=bp_freq, filter_type='bandpass')
            elif bp_freq[0]:
                self.stream_processor.add_filter(cutoff_freq=bp_freq[0], filter_type='highpass')
            elif bp_freq[1]:
                self.stream_processor.add_filter(cutoff_freq=bp_freq[1], filter_type='lowpass')

        dashboard = explorepy.Dashboard(explore=self)
        dashboard.start_server()
        dashboard.start_loop()

    def measure_imp(self):
        """
        Visualization of the electrode impedances

        Args:
            notch_freq (int): Notch frequency for filtering the line noise (50 or 60 Hz)
        """
        self._check_connection()
        assert self.stream_processor.device_info['sampling_rate'] == 250, \
            "Impedance mode only works in 250 Hz sampling rate!"

        self.stream_processor.imp_initialize(notch_freq=50)

        try:
            dashboard = explorepy.Dashboard(explore=self, mode='impedance')
            dashboard.start_server()
            dashboard.start_loop()
        except KeyboardInterrupt:
            self.stream_processor.disable_imp()

    def set_marker(self, code):
        """Sets a digital event marker while streaming

        Args:
            code (int): Marker code. It must be an integer larger than 7
                        (codes from 0 to 7 are reserved for hardware markers).

        """
        self._check_connection()
        self.stream_processor.set_marker(code=code)

    def format_memory(self):
        """Format memory of the device"""
        self._check_connection()
        cmd = MemoryFormat()
        self.stream_processor.configure_device(cmd)

    def set_sampling_rate(self, sampling_rate):
        """Set sampling rate

        Args:
            sampling_rate (int): Desired sampling rate. Options: 250, 500, 1000
        """
        self._check_connection()
        if sampling_rate not in [250, 500, 1000]:
            raise ValueError("Sampling rate must be 250, 500 or 1000.")
        cmd = SetSPS(sampling_rate)
        self.stream_processor.configure_device(cmd)

    def reset_soft(self):
        """Reset the device to the default settings"""
        self._check_connection()
        cmd = SoftReset()
        self.stream_processor.configure_device(cmd)

    def set_channels(self, channel_mask):
        """Set the channel mask of the device

        The channels can be disabled/enabled by calling this function and passing an integer which represents the
        binary form of the mask. For example in a 4 channel device, if you want to disable channel 4, the adc mask
        should be b'0111' (LSB is channel 1). The integer value of 0111 which is 7 must be given to this function

        Args:
            channel_mask (int): Integer representation of the binary channel mask

        Examples:
            >>> from explorepy.explore import Explore
            >>> explore = Explore()
            >>> explore.connect(device_name='Explore_2FA2')
            >>> explore.set_channels(channel_mask=7)  # disable channel 4 - mask:0111
        """
        if not isinstance(channel_mask, int):
            raise TypeError("Input must be an integer!")
        self._check_connection()
        cmd = SetCh(channel_mask)
        self.stream_processor.configure_device(cmd)

    def disable_module(self, module_name):
        """Disable module

        Args:
            module_name (str): Module to be disabled (options: 'ENV', 'ORN', 'EXG')

        Examples:
            >>> from explorepy.explore import Explore
            >>> explore = Explore()
            >>> explore.connect(device_name='Explore_2FA2')
            >>> explore.disable_module('ORN')
        """
        if module_name not in ['ORN', 'ENV', 'EXG']:
            raise ValueError('Module name must be one of ORN, ENV or EXG.')
        self._check_connection()
        cmd = ModuleDisable(module_name)
        self.stream_processor.configure_device(cmd)

    def enable_module(self, module_name):
        """Enable module

        Args:
            module_name (str): Module to be disabled (options: 'ENV', 'ORN', 'EXG')

        Examples:
            >>> from explorepy.explore import Explore
            >>> explore = Explore()
            >>> explore.connect(device_name='Explore_2FA2')
            >>> explore.enable_module('ORN')
        """
        if module_name not in ['ORN', 'ENV', 'EXG']:
            raise ValueError('Module name must be one of ORN, ENV or EXG.')
        self._check_connection()
        cmd = ModuleEnable(module_name)
        self.stream_processor.configure_device(cmd)

    def calibrate_orn(self, do_overwrite=False):
        """Calibrate orientation module

        This method calibrates orientation sensors in order to get the real physical orientation in addition to raw sensor
        data. While running this function you would need to move and rotate the device. This function will store
        calibration info in the configuration file which will be used later during streaming to calculate physical
        orientation from raw sensor data.

        Args:
            do_overwrite: to overwrite the calibration data if already exists or not

        """
        assert not (PhysicalOrientation.check_calibre_data(device_name=self.device_name) and not(do_overwrite)), \
            "Calibration data already exists!"
        PhysicalOrientation.init_dir()
        print("Start recording for 100 seconds, please move the device around during this time, in all directions")
        file_name = user_cache_dir(appname="explorepy", appauthor="Mentalab") + '//temp_' + self.device_name
        self.record_data(file_name, do_overwrite=do_overwrite, duration=100, file_type='csv')
        time.sleep(105)
        PhysicalOrientation.calibrate(cache_dir=file_name, device_name=self.device_name)

    def _check_connection(self):
        assert self.is_connected, "Explore device is not connected. Please connect the device first."

    @staticmethod
    def _check_duration(duration):
        if duration:
            if duration <= 0:
                raise ValueError("Recording time must be a positive number!")
        else:
            duration = 60 * 60  # one hour
        return duration
