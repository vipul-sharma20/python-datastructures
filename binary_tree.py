def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, new):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new, t, []])
    else:
        root.insert(1, [new, [], []])
    return root

def insertRight(root, new):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new, [], t])
    else:
        root.insert(2, [new, [], [])

r = BinaryTree(5)
"""
insertLeft(r, 6)
insertRight(r, 12)
"""
print l
