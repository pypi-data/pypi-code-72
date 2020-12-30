#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#
# pylint: disable=invalid-name

"""This file handles with the CoinImage dataset"""

import csv
import os
from typing import Dict

from ...dataset import Data, Dataset
from ...label import Classification
from .._utility import glob

DATASET_NAME = "CoinImage"


def CoinImage(path: str) -> Dataset:
    """Coin Image open dataset dataloader

    :param path: Path to Coin Image dataset
    The file structure should be like:
    <path>
        classes.csv
        <imagename>.png
        ...

    :return: load `Dataset` object
    """
    root_path = os.path.abspath(os.path.expanduser(path))

    dataset = Dataset(DATASET_NAME)
    dataset.load_catalog(os.path.join(os.path.dirname(__file__), "catalog.json"))
    segment = dataset.create_segment()

    csv_path = os.path.join(root_path, "classes.csv")
    with open(csv_path, "r") as fp:
        reader = csv.reader(fp, delimiter=";")
        mapping: Dict[str, str] = dict(row for row in reader)  # type: ignore[arg-type, misc]

    image_paths = glob(os.path.join(root_path, "*.png"))

    for image_path in image_paths:
        data = Data(image_path)
        filename = os.path.basename(image_path)
        class_id = filename[5:].split("_", 1)[0]
        label = Classification(category=mapping[class_id])
        data.append_label(label)
        segment.append(data)

    return dataset
