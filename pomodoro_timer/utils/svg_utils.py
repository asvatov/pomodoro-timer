import os
from os.path import isfile, join

from pomodoro_timer.configs.main_configs import IMG_BASE_DIR, IMG_ICON_BASE
from pomodoro_timer.utils.utils import get_random_filename


def get_svg_content(args):
    # 1 - width
    # 2 - height
    # 3 - height
    # 4 - width
    # 5 - back_circle_color
    # 6 - stroke_width
    # 7 - r
    # 8 - cx = width / 2
    # 9 - cy = height / 2
    # 10 - r
    # 11 - cx = width / 2
    # 12 - height / 2
    # 13 - width / 2
    # 14 - height / 2
    # 15 - bar_circle_color
    # 16 - stroke-dasharray = 3.15 * r * 2
    # 17 - stroke_dashoffset

    SVG_CONTENT_PATTERN = '<?xml version="1.0" encoding="utf-8"?>' \
                          '<svg version="1.1"' \
                          ' baseProfile="full"' \
                          ' viewBox="0 0 {} {}"' \
                          ' xmlns="http://www.w3.org/2000/svg"' \
                          ' xmlns:xlink="http://www.w3.org/1999/xlink"' \
                          ' xmlns:ev = "http://www.w3.org/2001/xml-events"' \
                          ' height = "{}px" width = "{}px">' \
                          '<g stroke="{}" stroke-width="{}">' \
                          '<circle r="{}" cx="{}" cy="{}" fill="none"></circle>' \
                          '<circle r="{}" cx="{}" cy="{}" transform="rotate(-90 {} {})" fill="none" stroke="{}" stroke-dasharray="{}" stroke-dashoffset="{}"></circle>' \
                          '</g>' \
                          '</svg>'

    svg_content = SVG_CONTENT_PATTERN.format(*args)

    return svg_content


def generate_custom_icon(height=512, width=512, back_circle_color="#666", bar_circle_color="#FF9F1E", stroke_dashoffset=0.0):
    stroke_width = min(height, width) / 10
    r = min(height, width) / 2 - stroke_width
    c = 3.15 * r * 2
    stroke_dashoffset = (1 - stroke_dashoffset) * c

    svg_content_args = [
        width,
        height,
        height,
        width,
        back_circle_color,
        stroke_width,
        r,
        width / 2,
        height / 2,
        r,
        width / 2,
        height / 2,
        width / 2,
        height / 2,
        bar_circle_color,
        c,
        stroke_dashoffset
    ]
    svg_content = get_svg_content(svg_content_args)

    return svg_content


def get_icon(stroke_dashoffset):
    icon = generate_custom_icon(height=512, width=512, back_circle_color="#666", bar_circle_color="#FF9F1E", stroke_dashoffset=stroke_dashoffset)

    return icon


def init_icon():
    icon = get_icon(0)

    icon_dirpath = IMG_BASE_DIR

    svg_files = [f for f in os.listdir(icon_dirpath) if isfile(join(icon_dirpath, f)) and f.endswith(".svg")]
    if not svg_files:
        filepath = IMG_ICON_BASE
    else:
        svg_file = svg_files[0]
        filepath = os.path.join(icon_dirpath, svg_file)

    with open(filepath, "w") as fp:
        fp.write(icon)

    return filepath


def change_icon(arc, icon_filepath=None):
    icon = get_icon(arc)
    new_filepath = os.path.join(os.path.dirname(icon_filepath), get_random_filename())
    os.rename(icon_filepath, new_filepath)

    with open(new_filepath, "w") as fp:
        fp.write(icon)

    return new_filepath
