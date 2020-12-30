#!/usr/bin/env python3
#
# Copyright 2020 Graviti. All Rights Reserved.
#
# pylint: disable=invalid-name

"""This file define the Kenyan Food datasets Dataloader"""

import os

from ...dataset import Data, Dataset
from ...label import Classification
from .._utility import glob

DATASET_NAME_FOOD_TYPE = "KenyanFoodType"
DATASET_NAME_FOOD_OR_NONFOOD = "KenyanFoodOrNonfood"
SEGMENTS_FOOD_TYPE = ["test", "train", "val"]
SEGMENTS_FOOD_OR_NONFOOD = {"test": "test.txt", "train": "train.txt"}


def KenyanFoodOrNonfood(path: str) -> Dataset:
    """
    Kenyan Food or Nonfood open dataset dataloader
    :param path: Path to KenyanFoodOrNonfood dataset
    the file structure should be like:
    <path>
            images/
                food/
                    236171947206673742.jpg
                    ...
                nonfood/
                    168223407.jpg
                    ...
            data.csv
            split.py
            test.txt
            train.txt

    :return:load `Dataset` object
    """
    root_path = os.path.abspath(os.path.expanduser(path))
    dataset = Dataset(DATASET_NAME_FOOD_OR_NONFOOD)
    dataset.load_catalog(os.path.join(os.path.dirname(__file__), "catalog_food_or_nonfood.json"))

    for segment_name, filename in SEGMENTS_FOOD_OR_NONFOOD.items():
        segment = dataset.create_segment(segment_name)
        with open(os.path.join(root_path, filename)) as fp:
            for image_path in fp:
                image_path = os.path.join(root_path, image_path)
                data = Data(image_path.strip())
                category = image_path.split("/")[1]
                data.append_label(Classification(category))
                segment.append(data)
    return dataset


def KenyanFoodType(path: str) -> Dataset:
    """
    Kenyan Food Type open dataset dataloader
    :param path:Path to KenyanFoodType dataset
    the file structure should be like:
    <path>
        test.csv
        test/
            bhaji/
                1611654056376059197.jpg
                ...
            chapati/
                1451497832469337023.jpg
                ...
            ...
        train/
            bhaji/
                190393222473009410.jpg
                ...
            chapati/
                1310641031297661755.jpg
                ...
        val/
            bhaji/
                1615408264598518873.jpg
                ...
            chapati/
                1553618479852020228.jpg
                ...

    :return:load `Dataset` object
    """

    root_path = os.path.abspath(os.path.expanduser(path))
    dataset = Dataset(DATASET_NAME_FOOD_TYPE)
    dataset.load_catalog(os.path.join(os.path.dirname(__file__), "catalog_food_type.json"))

    for segment_name in SEGMENTS_FOOD_TYPE:
        segment = dataset.create_segment(segment_name)
        segment_path = os.path.join(root_path, segment_name)
        for category in sorted(os.listdir(segment_path)):
            image_paths = glob(os.path.join(segment_path, category, "*.jpg"))
            label = Classification(category)
            for image_path in image_paths:
                data = Data(image_path)
                data.append_label(label)
                segment.append(data)
    return dataset
