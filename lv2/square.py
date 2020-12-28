from decimal import Decimal


def solution(w, h):
    squares = w * h
    return squares - (w + h - biggest_common_factor(w, h))


def biggest_common_factor(w, h):
    if w < h:
        w, h = h, w
    if h == 0:
        return w
    else:
        return biggest_common_factor(h, w % h)


print(solution(8, 12))
