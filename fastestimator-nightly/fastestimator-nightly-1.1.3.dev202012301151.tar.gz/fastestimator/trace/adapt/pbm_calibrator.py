#  Copyright 2020 The FastEstimator Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ==============================================================================
import os
from typing import Set, Union, Optional

import calibration as cal
import dill
import numpy as np

from fastestimator.summary.system import System
from fastestimator.trace.trace import Trace
from fastestimator.util.data import Data
from fastestimator.util.traceability_util import traceable
from fastestimator.util.util import to_number


@traceable()
class PBMCalibrator(Trace):
    """A trace to generate a PlattBinnerMarginalCalibrator given a set of predictions.

    Unlike many common calibration error correction algorithms, this one has actual theoretical bounds on the quality
    of its output: https://arxiv.org/pdf/1909.10155v1.pdf. This trace is commonly used together with the Calibrate
    NumpyOp for postprocessing. This trace will collect data from whichever `mode` it is set to run on in order to
    perform empirical probability calibration. The calibrated predictions will be output on epoch end. The trained
    calibration function will also be saved if `save_path` is provided.

    Args:
        true_key: Name of the key that corresponds to ground truth in the batch dictionary.
        pred_key: Name of the key that corresponds to predicted score in the batch dictionary.
        mode: What mode(s) to execute this Trace in. For example, "train", "eval", "test", or "infer". To execute
            regardless of mode, pass None. To execute in all modes except for a particular one, you can pass an argument
            like "!infer" or "!train".
        output_name: What to call the output from this trace. If None, the default will be '<pred_key>_calibrated'.
        save_path: Where to save the calibrator generated by this Trace. If None, then no saving will be performed.
    """
    system: System

    def __init__(self,
                 true_key: str,
                 pred_key: str,
                 output_name: Optional[str] = None,
                 save_path: Optional[str] = None,
                 mode: Union[str, Set[str]] = "eval") -> None:
        if output_name is None:
            output_name = f"{pred_key}_calibrated"
        super().__init__(inputs=[true_key, pred_key], outputs=output_name, mode=mode)
        self.y_true = []
        self.y_pred = []
        if save_path is not None:
            save_path = os.path.abspath(os.path.normpath(save_path))
        self.save_path = save_path

    @property
    def true_key(self) -> str:
        return self.inputs[0]

    @property
    def pred_key(self) -> str:
        return self.inputs[1]

    def on_epoch_begin(self, data: Data) -> None:
        self.y_true = []
        self.y_pred = []

    def on_batch_end(self, data: Data) -> None:
        y_true, y_pred = to_number(data[self.true_key]), to_number(data[self.pred_key])
        if y_true.shape[-1] > 1 and y_true.ndim > 1:
            y_true = np.argmax(y_true, axis=-1)
        assert y_pred.shape[0] == y_true.shape[0]
        self.y_true.extend(y_true)
        self.y_pred.extend(y_pred)

    def on_epoch_end(self, data: Data) -> None:
        self.y_true = np.squeeze(np.stack(self.y_true))
        self.y_pred = np.stack(self.y_pred)
        calibrator = cal.PlattBinnerMarginalCalibrator(num_calibration=len(self.y_true), num_bins=10)
        calibrator.train_calibration(probs=self.y_pred, labels=self.y_true)
        if self.save_path:
            with open(self.save_path, 'wb') as f:
                dill.dump(calibrator.calibrate, file=f)
            print(f"FastEstimator-PBMCalibrator: Calibrator written to {self.save_path}")
        data.write_without_log(self.outputs[0], calibrator.calibrate(self.y_pred))
