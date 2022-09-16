def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other): #using zip
            if not same_structure_as(o1, o2): return False #recursion
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)

''' another interesting version
def nones(itr):
    return [nones(a) if isinstance(a, (list, tuple)) else None for a in itr]


def same_structure_as(a, b):
    return nones(a) == nones(b) if type(a) == type(b) else False
'''
''' and another one
def same_structure_as(a, b): # inline recursive call ia a lambda, fancy
    structure = lambda arr: [ 0 if type(e) != list else structure(e) for e in arr ]
    return type(a) == type(b) and structure(a) == structure(b)
'''
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))  # T
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))  # F
print(same_structure_as([[[], []]], [[[], []]]))  # T
print(same_structure_as([[[], []]], [[1, 1]]))  # F
