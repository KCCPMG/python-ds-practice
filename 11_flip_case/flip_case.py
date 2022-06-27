def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    chList = list(phrase)
    for i in range(len(chList)):
        if chList[i].upper() == to_swap.upper():
            if chList[i] == chList[i].upper():
                chList[i] = chList[i].lower()
            else:
                chList[i] = chList[i].upper()

    return "".join(chList)
