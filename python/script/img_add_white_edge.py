# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Version: v0.1
import argparse
import math

from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(description='add white edge to img')
    parser.add_argument('img', help='img path')
    parser.add_argument('--output', default='output.jpg', help='output path')
    parser.add_argument('--ratio', default='1:1', help='height:width')
    parser.add_argument(
        '--output_height', default=None, help='output image height'
    )
    parser.add_argument(
        '--output_width', default=None, help='output image width'
    )
    return parser.parse_args()


def add_white_edge(input_path, output_path, width, height):
    input_img = Image.open(input_path)
    bg_width = input_img.width
    bg_height = input_img.height
    if bg_width > bg_height:
        bg_height = math.ceil((bg_width * height) / width)
    bg_img: Image.Image = Image.new(
        "RGB", (bg_width, bg_height), (255, 255, 255)
    )
    bg_img.paste(input_img, (0, round((bg_height - input_img.height) / 2)))

    bg_img.resize((width, height)).save(output_path, quality=95)


def main():
    args = parse_args()
    add_white_edge(args.img, args.output, 800, 800)


if __name__ == "__main__":
    main()
