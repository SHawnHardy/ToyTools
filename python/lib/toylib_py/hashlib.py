# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Version: v0.1
import hashlib
import os

import cv2
import numpy as np
from PIL import Image


def get_hash(algorithms='md5'):
    if algorithms == 'echo':
        return lambda x: x
    if algorithms == 'filename':
        return lambda x: os.path.split(x)[1]

    if algorithms in hashlib.algorithms_available:

        def hash_func(x):
            _hash = getattr(hashlib, algorithms)()
            if isinstance(x, (str, os.PathLike)):
                with open(x, 'rb') as fp:
                    x = fp.read()
            _hash.update(x)
            return _hash.hexdigest()

        return hash_func

    img_hash_map = {
        'img:average': cv2.img_hash.averageHash,
        'img:block_mean': cv2.img_hash.blockMeanHash,
        'img:marr_hildreth': cv2.img_hash.marrHildrethHash,
        'img:phash': cv2.img_hash.pHash,
        'img:radial_variance': cv2.img_hash.radialVarianceHash
    }
    if algorithms in img_hash_map:

        def img_hash_func(x):
            if isinstance(x, (str, os.PathLike)):
                x = np.array(Image.open(x))
            elif not isinstance(x, np.ndarray):
                x = np.array(x)
            return img_hash_map[algorithms](x)

        return img_hash_func
    return None
