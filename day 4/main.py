def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    
    def search_from(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    return count

def count_diagonal_mas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(1, rows-1):
        for j in range(1, cols - 1):
            if grid[i][j] == "A":
                if grid[i-1][j-1] == "M" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "S":
                    count+=1
                if grid[i-1][j-1] == "S" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "M":
                    count+=1
                if grid[i-1][j-1] == "M" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "S":
                    count+=1
                if grid[i-1][j-1] == "S" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "M":
                    count+=1
    return count

with open("input.txt", "r") as file:
    grid = [line.strip() for line in file]
    word = "XMAS"

print(count_word_occurrences(grid, word))
print(count_diagonal_mas_occurrences(grid))