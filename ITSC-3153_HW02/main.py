# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import queue


# class used to
# easily store cell data.
# class Cell:
#     x: int
#     y: int
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


def gen_grid(rows, columns):
    return [["." for i in range(columns)] for j in range(rows)]


def print_grid(g):
    for i in g:
        for j in i:
            print(j, end=" ")
        print()


def input_int(prompt):
    num = 0
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            # we got an integer so break the loop.
            return num
            # break


# lower and upper lim are inclusive.
def input_in_bounds(lowerLim, upperLim, prompt):
    num = input_int(prompt)
    while True:
        if num > upperLim:
            print("Input must be less than or equal to " + str(upperLim))
            num = input_int(prompt)
            continue
        elif num < lowerLim:
            print("Input must be greater than or equal to " + str(lowerLim))
            num = input_int(prompt)
            continue
        else:
            return num


#upper and lower limit are inclusive.
def is_valid(c, grid):
    if c[0] < 0 or c[1] < 0:
        return False
    elif c[0] > len(grid) - 1 or c[1] > len(grid[0]) - 1:
        return False
    else:
        return True

def print_cell(c):
    print("(" + str(c[0]) + ", " + str(c[1]) + ")")

def breadth_first_search(grid, start_c, goal_c):
    print("BFS: ")
    print("Start: ", end="")
    print_cell(start_c)
    print("Goal: ", end="")
    print_cell(goal_c)
    # start at start point
    # check neighbour cells (Cells 1 index up of the current cell)
    # check goal
    # if no goal check neighbours of new frontier.

    #init grid_parent
    grid_parent = [[None]*len(grid[0]) for _ in range(len(grid))]

    # init reached
    reached = []

    # init frontier big enough to hold every cell in the search area.
    frontier = [start_c]

    #counter = 0
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(frontier) > 0:
        #counter += 1
        c = frontier.pop(0)
        #print("counter: " + str(counter) + " \nFronter empty: " + str(frontier.empty()) + "\nCell: " + str(grid[c.x][c.y]))
        #print()
        #print_grid(grid)
        #goal check
        if c == goal_c:
            path = []
            cur_path = c
            print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            while cur_path is not None:
                path.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]

            return path
        reached.append(c)

        # enqueue cell neighbours.
        for act in actions:
            next_c = (c[0] + act[0], c[1] + act[1])
            if not is_valid(next_c, grid):
                continue
            if (next_c in reached):
                continue
            if (next_c in frontier):
                continue
            #if (grid[next_c[0]][next_c[1]] != "G"):
                #grid[next_c[0]][next_c[1]] = "X"
            frontier.append(next_c)
            grid_parent[next_c[0]][next_c[1]] = c
    print("Failure")
    return None

def reverse_arr(arr):
    temp_arr = []
    for i in range(len(arr)-1, -1, -1):
        temp_arr.append(arr[i])
    return temp_arr

def reconstruct_path(grid, path):
    for c in path:
        if grid[c[0]][c[1]] != "S" and grid[c[0]][c[1]] != "G":
            grid[c[0]][c[1]] = "X"





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))
    grid = gen_grid(rows, columns)
    print_grid(grid)

    start_r = input_in_bounds(0, rows - 1, "Enter start row index: ")
    start_c = input_in_bounds(0, columns - 1, "Enter start column index: ")

    # indicate start pos
    grid[start_r][start_c] = "S"

    goal_r = input_in_bounds(0, rows - 1, "Enter goal row index: ")
    goal_c = input_in_bounds(0, columns - 1, "Enter goal column index: ")

    # indicate start pos
    grid[goal_r][goal_c] = "G"

    print_grid(grid)

    path = breadth_first_search(grid, (start_r, start_c), (goal_r, goal_c))
    if (path is not None):
        path = reverse_arr(path)
        reconstruct_path(grid, path)
        print_grid(grid)
        print(path)



    # print_grid(grid)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
