def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """


    vowelDict = {}
    vowelArr = ["a", "e", "i", "o", "u"]
    for ch in phrase.lower():
        if ch in vowelArr:
            vowelDict[ch] = vowelDict.get(ch, 0) + 1

    return vowelDict