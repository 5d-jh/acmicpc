def preorder(tree):
    node_stack = [list(tree.keys())[0]]

    while len(node_stack) > 0:
        root = node_stack.pop()

        if root != '.':
            print(root, end='')
            node_stack.extend(reversed(tree[root]))


def inorder(tree, node = None):
    if node != '.' and node != None:
        left, right = tree[node]
        inorder(tree, left)
        print(node, end='')
        inorder(tree, right)


def postorder(tree, node = None):
    if node != '.' and node != None:
        left, right = tree[node]
        inorder(tree, left)
        inorder(tree, right)
        print(node, end='')


def solution(arr_tree):
    tree_dict = dict()

    for subtree in arr_tree:
        root, left, right = subtree
        tree_dict[root] = (left, right)
    
    preorder(tree_dict)
    print()
    inorder(tree_dict, arr_tree[0][0])
    print()
    postorder(tree_dict, arr_tree[0][0])
    print()
        

n = int(input())
arr_tree = []

for _ in range(n):
    arr_tree.append(input().split(' '))
    
solution(arr_tree)
