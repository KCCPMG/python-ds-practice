def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dct = {}
    for num in nums:
        if num in dct:
            dct[num] += 1
        else:
            dct[num] = 1
    
    mode = None
    maxCount = 0
    for (key, val) in dct.items():
        if val > maxCount:
            maxCount = val
            mode = key

    return mode