import math


def beeramid(bonus, price) -> int:
    levels: int = 0
    cans: int = math.trunc(bonus / price)
    i: int = 1
    while cans >= i ** 2:
        cans -= i ** 2
        i += 1
        levels += 1
    return levels


def main():
    print(beeramid(21, 1.5))


if __name__ == '__main__':
    main()
