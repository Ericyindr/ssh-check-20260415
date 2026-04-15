def bubble_sort(items):
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items
