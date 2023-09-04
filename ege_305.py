def from_base_to_ten(n, base):
    n = str(n)
    res = 0
    letters = 'ABCDEF'
    for i in range(len(n)):
        if n[::-1][i] in letters:
            res += int(letters.index(n[::-1][i]) + 10) * (base ** i)
        else:
            res += int(n[::-1][i]) * (base ** i)
    return str(res)

def from_ten_to_base(n, base):
    res = ''
    letters = 'ABCDEF'
    while n != 0:
        if n % base > 9:
            res += letters[(n % base) - 10]
        else:
            res += str(n % base)
        n //= base
    return res[::-1]

def transformations(n):
    res = from_ten_to_base(n, 16)

    if n % 2 == 0:
        if res.isdigit():
            max = 0
            for i in res:
                if int(i) > max:
                    max = int(i)
        else:
            max = 0
            letters = 'ABCDEF'
            for i in res:
                if i.isdigit():
                    if int(i) > max:
                        max = int(i)
                else:
                    num = letters.index(i) + 10
                    if num > max:
                        max = num
        if max > 9:
            max = 'ABCDEF'[max - 10]
        res += str(max)
    else:
        res += '0'

    for _ in range(2):
        total = 0
        letters = 'ABCDEF'
        for i in res:
            if i in letters:
                total += (letters.index(i) + 10)
            else:
                total += int(i)
        if total % 16 > 9:
            res += letters[total % 16 - 10]
        else:
            res += str(total % 16)
    return res

min_ = 9999999
for i in range(131059, 12, -1):
    num = transformations(i)
    max_figure = max(num, key=lambda x:'ABCDEF'.index(x) + 10 if x in 'ABCDEF' else int(x))
    min_figure = min(num, key=lambda x:'ABCDEF'.index(x) + 10 if x in 'ABCDEF' else int(x))
    if num.count(max_figure) // num.count(min_figure) == 5:
        min_ = i
        break
print(min_)
