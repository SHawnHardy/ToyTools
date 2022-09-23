# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Version: v0.1
import argparse

import toylib_py
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser(description='find duplicate')
    parser.add_argument('--path', default='.', help='path')
    parser.add_argument(
        '--hash_algorithm', default='md5', help='hash algorithm'
    )
    return parser.parse_args()


def main(path, hash_algorithm):
    hash_algorithm = toylib_py.hashlib.get_hash(hash_algorithm)
    dic = {}
    for f in tqdm(toylib_py.path.get_files(path)):
        hash_value = hash_algorithm(f)
        if hash_value not in dic:
            dic[hash_value] = f
        else:
            # print(f'{f},{dic[hash_value]}')
            print(f'{f}, {dic[hash_value]}')


if __name__ == '__main__':
    main(**vars(parse_args()))
