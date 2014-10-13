def validate_parenthetics(string_to_analyze):

    ''' For a supplied text string, return 1 if there are more open parens
    than closed, 0 if there are an equal number of parentheses open and
    closed in the string, or -1 if there are more closing parens than open. '''

    anticipated_closing_parentheses = 0

    for each_character in string_to_analyze:

        if each_character == ")":

            if anticipated_closing_parentheses <= 0:

                return -1

            else:

                anticipated_closing_parentheses -= 1

        if each_character == "(":

            anticipated_closing_parentheses += 1

    if anticipated_closing_parentheses == 0:

        return 0

    elif anticipated_closing_parentheses >= 1:

        return 1

    return "Error: Unexpected behavior"










