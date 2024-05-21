# -*- coding: utf-8 -*-
"""
1
"""

from pathlib import Path
from osgeo import gdal
import numpy as np
import glob

#  初始化每个类的数目

for model_path in Path("./model").glob("*.pth"):
    model_path = str(model_path)
    output_dir = "./prediction_result/" + Path(model_path).stem

    print(output_dir)
    label_paths = glob.glob(f"{output_dir}/*.png")

    score = 0

    for label_path in label_paths:
        print(label_path)
        label = gdal.Open(label_path).ReadAsArray(0, 0, 256, 256)
        print(label)
        res = gdal.Open(f"{output_dir}/{Path(label_path).name}").ReadAsArray(
            0, 0, 256, 256
        )
        print(f"{output_dir}/{Path(label_path).name}")
        # print({output_dir}/{Path(label_path).name})
        score += np.sum(label == res) / (256 * 256)
    print(f"正确率: {score/len(label_paths)}")
