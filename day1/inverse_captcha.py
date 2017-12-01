def solve_inverse_captcha(captcha):

    """
    Finds solution to inverse captcha for puzzle 1 in day 1 of advent of code.

    captcha is a <string> of digits from 0-9. The solution is the sum of digits
    which match the next digit in the list. The list is circular.

    Examples
        1122 = 3 (1 + 2)
        1111 = 4 (1 + 1 + 1 + 1)
        1234 = 0
        91212129 = 9 (9)
    """

    captcha = captcha.strip()

    # solve circular issue
    if captcha[0] == captcha[-1]:
        buff = ""
        for c in captcha:
            if c == captcha[0]:
                buff += c
            else:
                break
        captcha += buff

    sol = 0
    for i, c in enumerate(captcha[0:-1]):
        sol += int(c) if c == captcha[i+1] else 0

    return sol


def solve_inverse_captcha_2(captcha):

    """
    Finds solution to inverse captcha for puzzle 2 in day 1 of advent of code.

    captcha is a <string> of digits from 0-9. The solution is the sum of digits
    which match the digit halfway around the circular list.

    captcha is of even length (assumption)

    Examples:
        1212 = 6 (1 matches 1, 2 matches 2, 1 matches 1, etc)
        1221 = 0
        123425 = 4
        123123 = 12
        12131415 = 4
    """

    captcha = captcha.strip()
    n = len(captcha)

    sol = 0
    for i, c in enumerate(captcha):
        sol += int(c) if c == captcha[(i + n/2) % n] else 0

    return sol

