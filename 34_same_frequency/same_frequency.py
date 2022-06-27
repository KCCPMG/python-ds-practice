def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    dct1 = {}
    dct2 = {}
    for ch in str1:
        dct1[ch] = str1.count(ch)
    for ch in str2:
        dct2[ch] = str2.count(ch)
    return dct1 == dct2