def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    non_vowels = []
    vowels = []
    for i in range(len(s)):
        if s[i].upper() in ["A", "E", "I", "O", "U"]:
            vowels.append(s[i])
            non_vowels.append(None)
        else:
            non_vowels.append(s[i])

    for i in range(len(non_vowels)):
        if non_vowels[i] == None:
            non_vowels[i] = vowels.pop()
    
    return "".join(non_vowels)
