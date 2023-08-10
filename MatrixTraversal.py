from collections import deque
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


def bfs(
        grid: List[List[int]], 
        startpos: Tuple[int, int] = (0, 0), 
        visit: Set[Tuple[int, int]] = set()
):
    """Find the shortest path from top left to bottom right"""
    ROWS, COLS = len(grid), len(grid[0])  # Get grid dimensions
    queue = deque()
    queue.append(startpos)
    visit.add(startpos)

    length = 0
    while queue:
        for _ in range(len(queue)):  # Nested loop tracks graph level-by-level
            x, y = queue.popleft()

            # Reached destination
            if x == ROWS-1 and y == COLS-1:
                return length
            
            # Otherwise continue BFS by enqueueing each direction
            # This time you make the validity check first, only add valid steps
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x1, y1 = x + dx, y + dy

                # Base Case 1 (same as dfs): Out of bounds
                if min(x1, y1) < 0 or x1 >= ROWS or y1 >= COLS:
                    continue
                
                # Base Case 2: Attempting to move to blocked position
                if grid[x1][y1] == 1:
                    continue

                # Base Case 3: Attempting to move to visited position
                if (x1, y1) in visit:
                    continue

                # Add valid movements to the queue
                queue.append((x1, y1))
                visit.add((x1, y1))
        length += 1

    return length            


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]

    print(dfs(grid))
    print(bfs(grid))