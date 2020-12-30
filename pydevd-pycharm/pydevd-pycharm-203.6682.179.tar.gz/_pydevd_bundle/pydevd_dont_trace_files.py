# Important: Autogenerated file.

# DO NOT edit manually!
# DO NOT edit manually!

from _pydevd_bundle.pydevd_constants import IS_PY3K

LIB_FILE = 1
PYDEV_FILE = 2

DONT_TRACE = {
    # commonly used things from the stdlib that we don't want to trace
    'Queue.py':LIB_FILE,
    'queue.py':LIB_FILE,
    'socket.py':LIB_FILE,
    'weakref.py':LIB_FILE,
    '_weakrefset.py':LIB_FILE,
    'linecache.py':LIB_FILE,
    'threading.py':LIB_FILE,
    'dis.py':LIB_FILE,

    #things from pydev that we don't want to trace
    '_pydev_BaseHTTPServer.py': PYDEV_FILE,
    '_pydev_SimpleXMLRPCServer.py': PYDEV_FILE,
    '_pydev_SocketServer.py': PYDEV_FILE,
    '_pydev_calltip_util.py': PYDEV_FILE,
    '_pydev_completer.py': PYDEV_FILE,
    '_pydev_execfile.py': PYDEV_FILE,
    '_pydev_filesystem_encoding.py': PYDEV_FILE,
    '_pydev_getopt.py': PYDEV_FILE,
    '_pydev_imports_tipper.py': PYDEV_FILE,
    '_pydev_inspect.py': PYDEV_FILE,
    '_pydev_jy_imports_tipper.py': PYDEV_FILE,
    '_pydev_log.py': PYDEV_FILE,
    '_pydev_pkgutil_old.py': PYDEV_FILE,
    '_pydev_saved_modules.py': PYDEV_FILE,
    '_pydev_sys_patch.py': PYDEV_FILE,
    '_pydev_tipper_common.py': PYDEV_FILE,
    '_pydev_xmlrpclib.py': PYDEV_FILE,
    'django_debug.py': PYDEV_FILE,
    'fix_getpass.py': PYDEV_FILE,
    'jinja2_debug.py': PYDEV_FILE,
    'pycompletionserver.py': PYDEV_FILE,
    'pydev_app_engine_debug_startup.py': PYDEV_FILE,
    'pydev_code_executor.py': PYDEV_FILE,
    'pydev_console_commands.py': PYDEV_FILE,
    'pydev_console_types.py': PYDEV_FILE,
    'pydev_console_utils.py': PYDEV_FILE,
    'pydev_import_hook.py': PYDEV_FILE,
    'pydev_imports.py': PYDEV_FILE,
    'pydev_io.py': PYDEV_FILE,
    'pydev_ipython_code_executor.py': PYDEV_FILE,
    'pydev_ipython_console.py': PYDEV_FILE,
    'pydev_ipython_console_011.py': PYDEV_FILE,
    'pydev_is_thread_alive.py': PYDEV_FILE,
    'pydev_localhost.py': PYDEV_FILE,
    'pydev_log.py': PYDEV_FILE,
    'pydev_monkey.py': PYDEV_FILE,
    'pydev_monkey_qt.py': PYDEV_FILE,
    'pydev_override.py': PYDEV_FILE,
    'pydev_protocol.py': PYDEV_FILE,
    'pydev_rpc.py': PYDEV_FILE,
    'pydev_server.py': PYDEV_FILE,
    'pydev_stdin.py': PYDEV_FILE,
    'pydev_transport.py': PYDEV_FILE,
    'pydev_umd.py': PYDEV_FILE,
    'pydev_versioncheck.py': PYDEV_FILE,
    'pydevconsole.py': PYDEV_FILE,
    'pydevconsole_code_for_ironpython.py': PYDEV_FILE,
    'pydevd.py': PYDEV_FILE,
    'pydevd_additional_thread_info.py': PYDEV_FILE,
    'pydevd_additional_thread_info_regular.py': PYDEV_FILE,
    'pydevd_breakpointhook.py': PYDEV_FILE,
    'pydevd_breakpoints.py': PYDEV_FILE,
    'pydevd_bytecode_utils.py': PYDEV_FILE,
    'pydevd_collect_try_except_info.py': PYDEV_FILE,
    'pydevd_comm.py': PYDEV_FILE,
    'pydevd_comm_constants.py': PYDEV_FILE,
    'pydevd_command_line_handling.py': PYDEV_FILE,
    'pydevd_concurrency_logger.py': PYDEV_FILE,
    'pydevd_console.py': PYDEV_FILE,
    'pydevd_console_integration.py': PYDEV_FILE,
    'pydevd_console_pytest.py': PYDEV_FILE,
    'pydevd_constants.py': PYDEV_FILE,
    'pydevd_custom_frames.py': PYDEV_FILE,
    'pydevd_cython_wrapper.py': PYDEV_FILE,
    'pydevd_dont_trace.py': PYDEV_FILE,
    'pydevd_dont_trace_files.py': PYDEV_FILE,
    'pydevd_exec.py': PYDEV_FILE,
    'pydevd_exec2.py': PYDEV_FILE,
    'pydevd_extension_api.py': PYDEV_FILE,
    'pydevd_extension_utils.py': PYDEV_FILE,
    'pydevd_file_utils.py': PYDEV_FILE,
    'pydevd_frame.py': PYDEV_FILE,
    'pydevd_frame_eval_cython_wrapper.py': PYDEV_FILE,
    'pydevd_frame_eval_main.py': PYDEV_FILE,
    'pydevd_frame_tracing.py': PYDEV_FILE,
    'pydevd_frame_utils.py': PYDEV_FILE,
    'pydevd_helpers.py': PYDEV_FILE,
    'pydevd_import_class.py': PYDEV_FILE,
    'pydevd_io.py': PYDEV_FILE,
    'pydevd_kill_all_pydevd_threads.py': PYDEV_FILE,
    'pydevd_modify_bytecode.py': PYDEV_FILE,
    'pydevd_plugin_numpy_types.py': PYDEV_FILE,
    'pydevd_plugin_utils.py': PYDEV_FILE,
    'pydevd_plugins_django_form_str.py': PYDEV_FILE,
    'pydevd_process_net_command.py': PYDEV_FILE,
    'pydevd_pycharm.py': PYDEV_FILE,
    'pydevd_referrers.py': PYDEV_FILE,
    'pydevd_reload.py': PYDEV_FILE,
    'pydevd_resolver.py': PYDEV_FILE,
    'pydevd_save_locals.py': PYDEV_FILE,
    'pydevd_signature.py': PYDEV_FILE,
    'pydevd_stackless.py': PYDEV_FILE,
    'pydevd_thread_wrappers.py': PYDEV_FILE,
    'pydevd_thrift.py': PYDEV_FILE,
    'pydevd_trace_api.py': PYDEV_FILE,
    'pydevd_trace_dispatch.py': PYDEV_FILE,
    'pydevd_trace_dispatch_regular.py': PYDEV_FILE,
    'pydevd_traceproperty.py': PYDEV_FILE,
    'pydevd_tracing.py': PYDEV_FILE,
    'pydevd_utils.py': PYDEV_FILE,
    'pydevd_vars.py': PYDEV_FILE,
    'pydevd_vm_type.py': PYDEV_FILE,
    'pydevd_xml.py': PYDEV_FILE,
}

DONT_TRACE['pydev_jupyter_plugin.py'] = PYDEV_FILE
DONT_TRACE['pydev_jupyter_utils.py'] = PYDEV_FILE

if IS_PY3K:
    # if we try to trace io.py it seems it can get halted (see http://bugs.python.org/issue4716)
    DONT_TRACE['io.py'] = LIB_FILE

    # Don't trace common encodings too
    DONT_TRACE['cp1252.py'] = LIB_FILE
    DONT_TRACE['utf_8.py'] = LIB_FILE
