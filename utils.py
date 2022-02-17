import math

from constants import *

def rect_displacement(rect1, rect2) -> vec:
    x1_left, y1_top = rect1.topleft
    x1_right, y1_bottom = rect1.bottomright
    x2_left, y2_top = rect2.topleft
    x2_right, y2_bottom = rect2.bottomright

    left = x2_right < x1_left
    top = y1_bottom > y2_top

    dx = 0
    dy = 0

    if left:
        dx = x2_left - x1_right
    else:
        dx = x2_right - x1_left

    if top:
        dy = y2_top - y1_bottom
    else:
        dy = y2_bottom - y1_top

    return vec(dx, dy)
