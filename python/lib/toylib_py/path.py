# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Version: v0.1
import os
import shutil


def safe_copy(src, dst, follow_symlinks=True, marker='-'):
    if not os.path.exists(src):
        raise FileNotFoundError(src)
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    def _get_dst(dst):
        yield dst
        num = 0
        base_name, file_ext = os.path.splitext(dst)
        while True:
            num += 1
            yield f'{base_name}{marker}{num}{file_ext}'

    for new_dst in _get_dst(dst):
        if not os.path.exists(new_dst):
            shutil.copy2(src, new_dst, follow_symlinks=follow_symlinks)
            return new_dst


def get_files(path):
    for dirpath, _, filenames in os.walk(path, followlinks=True):
        for filename in filenames:
            yield os.path.join(dirpath, filename)
