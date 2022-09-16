def set_dimension(dims, index, value):
    if len(dims) > index:
        if dims[index] < value:
            dims[index] = value
    else:
        dims.append(value)
    return dims


list1 = [[1, 2, 3], [1, 2], [[2, 3, 4], [1, 3], 1], 9, [1, 2, 3]]

dims = []
set_dimension(dims, 0, len(list1))
print(dims)

for i in range(len(list1)):
    if isinstance(list1[i], list):
        dims = set_dimension(dims, 1, len(list1[i]))
        for j in range(len(list1[i])):
            if isinstance(list1[i][j], list):
                dims = set_dimension(dims, 2, len(list1[i][j]))
                for k in range(len(list1[i][j])):
                    if isinstance(list1[i][j][k], list):
                        dims = set_dimension(dims, 3, len(list1[i][j][k]))
                        print('four dimensions')
print('number of dimensions', len(dims))
print('maximum shape', dims)