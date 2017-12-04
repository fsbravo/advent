def bathroom_code(instructions):

    buttons = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    pos = [1, 1]
    lines = instructions.split('\n')
    code = []
    with open(instructions, 'r') as fin:
        for l in fin:
            for mv in l:
                if mv == 'U':
                    pos[0] = max(pos[0] - 1, 0)
                elif mv == 'D':
                    pos[0] = min(pos[0] + 1, 2)
                elif mv == 'R':
                    pos[1] = min(pos[1] + 1, 2)
                elif mv == 'L':
                    pos[1] = max(pos[1] - 1, 0)
            code.append(buttons[pos[0]][pos[1]])

    return ''.join(str(c) for c in code)


def bathroom_code_2(instructions):
    buttons = [[-1, -1, 1, -1, -1],
               [-1, 2, 3, 4, -1],
               [5, 6, 7, 8, 9],
               [-1, 'A', 'B', 'C', -1],
               [-1, -1, 'D', -1, -1]]

    pos = [2, 0]
    code = []

    with open(instructions, 'r') as fin:
        for l in fin:
            for mv in l:
                tmp = [v for v in pos]
                if mv == 'U':
                    tmp[0] = max(tmp[0] - 1, 0)
                elif mv == 'D':
                    tmp[0] = min(tmp[0] + 1, 4)
                elif mv == 'R':
                    tmp[1] = min(tmp[1] + 1, 4)
                elif mv == 'L':
                    tmp[1] = max(tmp[1] - 1, 0)
                if buttons[tmp[0]][tmp[1]] != -1:
                    pos = tmp
            code.append(buttons[pos[0]][pos[1]])

    return ''.join(str(c) for c in code)
    