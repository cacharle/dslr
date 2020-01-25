import math


def _none_if_null_len(func):
    def tmp(xs, *args, **kwargs):
        if len(xs) == 0:
            return None
        return func(xs, *args, **kwargs)
    return tmp


@_none_if_null_len
def mean(xs):
    return sum(xs) / len(xs)

@_none_if_null_len
def std(xs):
    xs_mean = mean(xs)
    return math.sqrt(sum(
        [(x - xs_mean) ** 2 for x in xs]) / (len(xs) - 1))

@_none_if_null_len
def _pick(xs, compar):
    m = xs[0]
    for t in xs[1:]:
        if compar(t, m):
            m = t
    return m

def min(xs):
    return _pick(xs, lambda x, y: x < y)

def max(xs):
    return _pick(xs, lambda x, y: x > y)

def _qsort(xs):
    if len(xs) < 2:
        return xs
    xs = list(xs)
    pivot = xs[0]
    body = xs[1:]
    return (_qsort([x for x in body if x < pivot])
            + [pivot]
            + _qsort([x for x in body if x >= pivot]))

def _need_sorted(func):
    return lambda xs, *args, **kwargs: func(_qsort(xs), *args, **kwargs)

@_none_if_null_len
@_need_sorted
def q25(xs):
    return xs[len(xs) // 4]

@_none_if_null_len
@_need_sorted
def median(xs):
    return xs[len(xs) // 2 ]

@_none_if_null_len
@_need_sorted
def q75(xs):
    return xs[3 * (len(xs) // 4)]
