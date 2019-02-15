#!/usr/bin/env python3

# A single Parenthesis Matching script

p_match_o = ('{', '[', '(')

p_match_c = {
    '}': '{',
    ']': '[',
    ')': '('
}


def brackets_balance(arg):
    p = []
    for i in arg:
        if i in p_match_o:
            p.append(i)
        if i in p_match_c:
            a = p_match_c[i]

            try:
                if a == p[-1]:
                    p.pop()
                else:
                    return False
            except Exception as e:
                return False
    if p:
        return False
    else:
        return True


if __name__ == "__main__":

    arg = '()'
    print('{} is {}'.format(arg, brackets_balance(arg)))

    arg = '((b)'
    print('{} is {}'.format(arg, brackets_balance(arg)))

    arg = '([)]'
    print('{} is {}'.format(arg, brackets_balance(arg)))

    arg = 'f(e(d))'
    print('{} is {}'.format(arg, brackets_balance(arg)))

    arg = 'f[123(ab)]{[0]9}'
    print('{} is {}'.format(arg, brackets_balance(arg)))

    arg = '{{{'
    print('{} is {}'.format(arg, brackets_balance(arg)))

    arg = 'u}])'
    print('{} is {}'.format(arg, brackets_balance(arg)))
