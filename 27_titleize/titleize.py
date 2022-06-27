def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split(" ")
    for i in range(len(words)):
        firstLetter = words[i][:1][0].upper()
        remainingLetters = "".join(words[i][1:]).lower()
        words[i] = firstLetter + remainingLetters
    return " ".join(words)