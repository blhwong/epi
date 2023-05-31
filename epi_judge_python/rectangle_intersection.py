import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    r1_x2 = r1.x + r1.width
    r2_x2 = r2.x + r2.width
    r1_y2 = r1.y + r1.height
    r2_y2 = r2.y + r2.height

    x_intersects = r2.x <= r1.x <= r2_x2 or r1.x <= r2.x <= r1_x2
    y_intersects = r2.y <= r1.y <= r2_y2 or r1.y <= r2.y <= r1_y2

    if not (x_intersects and y_intersects):
        return Rect(0, 0, -1, -1)

    r3_x2 = min(r1_x2, r2_x2)
    r3_y2 = min(r1_y2, r2_y2)
    r3_x = max(r1.x, r2.x)
    r3_y = max(r1.y, r2.y)

    return Rect(r3_x, r3_y, r3_x2 - r3_x, r3_y2 - r3_y)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
