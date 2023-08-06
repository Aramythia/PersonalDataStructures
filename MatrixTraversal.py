from typing import List, Tuple, Set

def dfs(
        grid: List[List[int]], 
        startpos: Tuple[int, int] = (0, 0), 
        visit: Set[Tuple[int, int]] = set()
):
    """Find amount of paths from a node to the bottom right using DFS"""
    ROWS, COLS = len(grid), len(grid[0])  # Get grid dimensions
    x, y = startpos

    # Base Case 1: start position is out of bounds
    if (min(startpos)) < 0 or x == ROWS or y == COLS:
        return 0
    
    # Base Case 2: reached a blocked/impossible position
    if grid[x][y] == 1:
        return 0
    
    # Base Case 3: turned back to an already visited node
    if startpos in visit:
        return 0
    
    # Base Case 4: reached the destination
    if x == ROWS-1 and y == COLS-1:
        return 1
    
    visit.add(startpos)  # Add to list of visited nodes

    # Continue by trying to go in all 4 directions
    count = 0
    count += dfs(grid, (x+1, y), visit)
    count += dfs(grid, (x-1, y), visit)
    count += dfs(grid, (x, y+1), visit)
    count += dfs(grid, (x, y-1), visit)

    # Remove from set to allow node to be visited by alternate paths
    visit.remove(startpos)
    return count


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]

    print(dfs(grid))