def find_nb(m):
    cubes = 0
    while m > 0:
        cubes += 1
        m -= cubes**3
        if m < 0:
            return -1
    return cubes


print(find_nb(4183059834009))  # 2022
print(find_nb(24723578342962))  # -1
print(find_nb(135440716410000))  # 4824
print(find_nb(40539911473216))  # 3568
print(find_nb(26825883955641))  # 3218
