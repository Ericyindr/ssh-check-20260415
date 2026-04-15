from __future__ import annotations


def quicksort(a: list) -> list:
    n = len(a)
    if n < 2:
        return a

    INSERTION_SORT_THRESHOLD = 16
    stack: list[tuple[int, int]] = [(0, n - 1)]

    while stack:
        lo, hi = stack.pop()

        while hi - lo > INSERTION_SORT_THRESHOLD:
            pivot = a[(lo + hi) >> 1]

            lt = lo
            i = lo
            gt = hi
            while i <= gt:
                ai = a[i]
                if ai < pivot:
                    a[lt], a[i] = ai, a[lt]
                    lt += 1
                    i += 1
                elif ai > pivot:
                    a[i], a[gt] = a[gt], ai
                    gt -= 1
                else:
                    i += 1

            left_lo, left_hi = lo, lt - 1
            right_lo, right_hi = gt + 1, hi

            if left_hi - left_lo < right_hi - right_lo:
                if right_lo < right_hi:
                    stack.append((right_lo, right_hi))
                lo, hi = left_lo, left_hi
            else:
                if left_lo < left_hi:
                    stack.append((left_lo, left_hi))
                lo, hi = right_lo, right_hi

        for idx in range(lo + 1, hi + 1):
            x = a[idx]
            j = idx - 1
            while j >= lo and a[j] > x:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = x

    return a
