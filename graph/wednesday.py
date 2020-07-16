    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
​
        Creates that number of users and a randomly distributed friendships
        between those users.
​
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
​
        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")
​
        # Create friendships
        possible_friendships = []
​
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
​
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
​
        # Add friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

"""
Connected components
"""
​
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]  # 4
​
islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]  # 13
​
"""
visited = [[F, T, F, F, F],
           [T, T, F, F, F],
           [F, F, F, F, F],
           [F, F, F, F, F],
           [F, F, F, F, F]]
"""
​
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
​
def island_counter(islands):
    row_count = len(islands)
    col_count = len(islands[0])
​
    # Create a visited matrix
    visited = []
​
    for _ in range(row_count):
        visited.append([False] * col_count)
​
    island_count = 0
​
    # Walk through each cell of the matrix
    for row in range(row_count):
        for col in range(col_count):
​
            if not visited[row][col]:
                if islands[row][col] == 1:
                    # Traverse and mark each as visited
                    dft(row, col, islands, visited)
​
                    # Increment counter
                    island_count += 1
​
    return island_count
​
def dft(row, col, islands, visited):
    s = Stack()
​
    s.push((row, col))
​
    while s.size() > 0:
        r, c = s.pop()
​
        if not visited[r][c]:
            visited[r][c] = True
​
            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)
​
def get_neighbors(row, col, islands):
    neighbors = []
​
    row_count = len(islands)
    col_count = len(islands[0])
​
    # Check North
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))
​
    # Check South
    if row < row_count - 1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))
​
    # Check West
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))
​
    # Check east
    if col < col_count - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))
​
    return neighbors
​
​
print(island_counter(islands)) # returns 4
Collapse