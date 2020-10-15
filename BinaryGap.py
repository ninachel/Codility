def binary(n):
    result = ''
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    while n > 0:
        digit = n % 2
        result += str(digit)
        return binary(n // 2) + result


def solution(n):
    binary_num = str(binary(n))
    if binary_num[-1] == '0':
        index = binary_num[::-1].index('1')
        binary_num = binary_num[:len(binary_num) - index]

    if binary_num.count('0') == 0:
        return 0
    elif binary_num.count('0') == 1:
        return 1
    else:
        binary_gap = 1
        current_gap = 1
        for i in range(1, len(binary_num) - 2):
            if binary_num[i] == binary_num[i + 1] == '0':
                current_gap += 1
                if current_gap > binary_gap:
                    binary_gap = current_gap
            else:
                current_gap = 1
        return binary_gap
