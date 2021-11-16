"""
references:
https://notes.burke.libbey.me/ansi-escape-codes/
https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg
"""


def Color(color_r: int, g=0, b=0, expanded=None, bright=False, background=False):
    """
    funktion to make it easier to change a text in color
    :param color_r: color from 0 - 8 or 0 - 265 and if rgb is it the r(red)
    :param g: g(green) from rgb
    :param b: b(blue) from rgb
    :param expanded: False -> 0 - 8 | True -> rgb | None -> 0 - 265
    :param bright: only for 0 - 8
    :param background: False -> text | True -> Background
    :return: the String to do before the String you want to change
    """
    if color_r < 0:
        print("Error: color under 0")
        return ""
    num = 30
    if background:
        num += 10
    if expanded is None:
        color_r %= 256
        num += 8
        return f"\x1b[{num};5;{color_r}m"
    if expanded:
        r = color_r
        if 0 <= g and 0 <= b:
            r %= 256
            g %= 256
            b %= 256
            num += 8
            return "\x1b[%s;2;%s;%s;%sm" % (num, r, g, b)
        else:
            print("g or/and b under 0")
            return ""
    if not expanded:
        color_r %= 8
        num += color_r
        if bright:
            num += 60
            return f"\x1b[{num}m"
        else:
            return f"\x1b[{num}m"


def Reset_color():
    """
    Resets all the changes to the color of the Text
    :return: the String for that
    """
    return "\x1b[0m"


def Thick():
    return "\x1b[1m"


def Underline():
    return "\x1b[4m"


def Italic():
    return "\x1b[3m"
