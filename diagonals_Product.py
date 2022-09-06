def sum_prod_diags(mat: list) -> int:
    m, n = len(mat), len(mat[0])
    k = m + n - 1
    a, b = [1] * k, [1] * k
    for i in range(m):
        for j in range(n):
            a[i - j] *= mat[i][j]
            b[i + j] *= mat[i][j]
    return sum(a) - sum(b)


def main():
    M1 = [[1, 4, 7, 6, 5],
          [-3, 2, 8, 1, 3],
          [6, 2, 9, 7, -4],
          [1, -2, 4, -2, 6],
          [3, 2, 2, -4, 7]]

    print(sum_prod_diags(M1))


if __name__ == '__main__':
    main()


