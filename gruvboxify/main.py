import os
import numpy as np
from PIL import Image
from argparse import Namespace, ArgumentParser

GRUVBOX = np.array([
  [40, 40, 40],     # #282828 (bg, bg0)
  [204, 36, 29],    # #cc241d (red)
  [152, 151, 26],   # #98971a (green)
  [215, 153, 33],   # #d79921 (yellow)
  [69, 88, 136],    # #455888 (blue)
  [177, 98, 134],   # #b16286 (purple)
  [104, 157, 106],  # #689d6a (aqua)
  [168, 153, 132],  # #a89984 (gray)
  [146, 131, 116],  # #928374 (gray)
  [251, 73, 52],    # #fb4934 (red)
  [184, 187, 38],   # #b8bb26 (green)
  [250, 189, 47],   # #fabd2f (yellow)
  [131, 165, 152],  # #83a598 (blue)
  [211, 134, 155],  # #d3869b (purple)
  [142, 192, 124],  # #8ec07c (aqua)
  [235, 219, 178],  # #ebdbb2 (fg)
  [29, 32, 33],     # #1d2021 (bg0_h)
  [60, 56, 54],     # #3c3836 (bg1)
  [80, 73, 69],     # #504945 (bg2)
  [102, 92, 84],    # #665c54 (bg3)
  [124, 118, 100],  # #7c6f64 (bg4)
  [214, 93, 14],    # #d65d0e (orange)
  [50, 32, 47],     # #32202f (bg0_s)
  [168, 153, 132],  # #a89984 (fg4)
  [189, 174, 147],  # #bdae93 (fg3)
  [213, 196, 161],  # #d5c4a1 (fg2)
  [235, 219, 178],  # #ebdbb2 (fg1)
  [251, 241, 199],  # #fbf1c7 (fg0)
  [254, 128, 25]    # #fe8019 (orange)
])

def closest_color(pixel):
    diffs = GRUVBOX - pixel
    dist = np.sum(diffs ** 2, axis=1)
    closest = GRUVBOX[np.argmin(dist)]
    return closest

def apply_gruvbox(image_path, output_path):
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)

    new_data = np.apply_along_axis(closest_color, 2, data)
    new_img = Image.fromarray(np.uint8(new_data))
    new_img.save(output_path)

def main():
    parser = ArgumentParser()

    # input image path
    parser.add_argument('input_image', help='Absolute path of image that will be converted to Gruvbox palette', type=str)

    # output image path
    parser.add_argument('-o', '--output', help='Absolute path of folder where Gruvboxified image is saved', type=str, required=False)

    args: Namespace = parser.parse_args()

    filename: str = os.path.basename(args.input_image)
    filename = 'gruvboxified_' + filename

    output_path: str = ''

    if not args.output:
        output_path = os.path.dirname(args.input_image) + '/' + filename
    else:
        if not output_path.endswith('/'):
            output_path = args.output + '/' + filename
        else:
            output_path = args.output + filename

    apply_gruvbox(args.input_image, output_path)

if __name__ == "__main__":
    main()