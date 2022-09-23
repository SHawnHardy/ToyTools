# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Version: v0.1
import argparse
import filecmp
import os

from toylib_py.hashlib import get_hash
from toylib_py.path import get_files, safe_copy
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser(description='super merge')
    parser.add_argument('base', help='base')
    parser.add_argument('--income', default='', help='income')
    parser.add_argument('--img', action='store_true', help='use img hash?')
    parser.add_argument(
        '--base_chksum', default='./md5_chksum', help='base chksum'
    )
    parser.add_argument(
        '--new_mv', default='./inbox', help='move new file to path'
    )
    parser.add_argument(
        '--redundancy_mv',
        default='./trash',
        help='move redundancy file to path'
    )
    parser.add_argument(
        '--skip_info_chk', action='store_true', help='skip base info check?'
    )
    parser.add_argument(
        '--redundancy_drop', action='store_true', help='drop redundancy file?'
    )
    parser.add_argument('--flatten', action='store_true', help='flatten?')
    return parser.parse_args()


def main():
    args = parse_args()
    hash_func = get_hash('img:phash' if args.img else 'md5')

    base_checksum = {}
    if os.path.exists(args.base_chksum):
        with open(args.base_chksum, 'r', encoding='utf8') as fp:
            base_checksum.update({
                filepath: hash
                for filepath, hash in [x.split(maxsplit=1) for x in fp]
                if os.path.exists(filepath)
            })

    if not args.skip_info_chk:
        base_checksum = {
            os.path.realpath(filepath): hash_value
            for filepath, hash_value in base_checksum.items()
        }
        base_checksum = {
            filepath:
            base_checksum.get(os.path.realpath(filepath), hash_func(filepath))
            for filepath in get_files(args.base)
        }

    with open(args.base_chksum, 'w', encoding='utf8') as fp:
        for filepath, hash_value in sorted(
            list(base_checksum.items()), key=lambda x: x[0]
        ):
            fp.write(f'{hash_value}\t{filepath}\n')

    if not args.income:
        return

    checksum_map = {}
    for filepath, hash_value in base_checksum.items():
        if hash_value not in checksum_map:
            checksum_map[hash_value] = []
        checksum_map[hash_value].append(filepath)

    for filepath in tqdm(get_files(args.income)):
        hash_value = hash_func(filepath)
        is_redundancy = False
        for base_path in checksum_map.get(hash_value, []):
            if filecmp.cmp(base_path, filepath, shallow=False):
                is_redundancy = True
                break
        if is_redundancy and args.redundancy_drop:
            os.remove(filepath)
            continue

        destination = args.redundancy_mv if is_redundancy else args.new_mv
        if not args.flatten:
            destination = os.path.join(
                destination, os.path.relpath(filepath, args.income)
            )
        safe_copy(filepath, destination)
        os.remove(filepath)


if __name__ == '__main__':
    main()
