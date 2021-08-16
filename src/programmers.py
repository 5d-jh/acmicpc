def get_children(matrix, pos):
    y, x = pos
    parent = matrix[y][x]
    
    width = len(matrix[y])
    
    children = []
    if x > 0 and matrix[y][x-1] == parent:
        children.append((y, x-1))
        
    if y > 0 and matrix[y-1][x] == parent:
        children.append((y-1, x))
        
    if x < width - 1 and matrix[y][x+1] == parent:
        children.append((y, x+1))
        
    if y < width - 1 and matrix[y+1][x] == parent:
        children.append((y+1, x))
        
    return children


def do_dfs(matrix, start_pos):
    y, x = start_pos
    stk = [(y, x)]
    visited = [(y, x)]
    travels_length = [0]
    
    while len(stk) > 0:
        parent = stk.pop()
        
        children = get_children(matrix, parent)

        valid_child = 0
        for child in children:
            if child not in visited:
                visited.append(child)
                stk.append(child)
                valid_child += 1
        if valid_child == 0:
            travels_length.append(
                len(visited) - travels_length[-1]
            )
    
    result = max(travels_length)
    return result
    

def solution(board):
    return do_dfs(board, (2, 0))
            
solution([[3,2,3,2], [2,1,1,2], [1,1,2,1], [4,1,1,1]])
