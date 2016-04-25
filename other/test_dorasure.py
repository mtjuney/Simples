import random


def dice(plus=False):
    success_count = 0
    d = random.randint(1, 6)
    if d >= 4 or (plus and d >= 2):
        success_count += 1
        if d == 6:
            success_count += dice(plus=True)
    elif d == 1:
        success_count -= 1

    return success_count


def role(num):
    success_count = 0
    for i in range(num):
        success_count += dice()

    return success_count


if __name__ == '__main__':

    sample_num = 1000000
    minus_count = 0

    for i in range(sample_num):
        result = role(6)
        if result < 0:
            minus_count += 1

    print(minus_count / sample_num)
