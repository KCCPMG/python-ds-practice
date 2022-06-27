def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens.replace(" ", "")) % 2 == 1 or parens[0] == ")":
        return False
    par_opps = ["(", ")"]
    lst = list(parens)
    while len(lst) > 0:
        beginning = lst.pop(0)
        ending = lst.pop()
        if not par_opps.index(ending) == (1 - par_opps.index(beginning)):
            print(beginning, ending)
            return False
    return True

