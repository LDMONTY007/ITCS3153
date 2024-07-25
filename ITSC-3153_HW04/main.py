# This is a sample Python script.
import copy
import queue
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# class used to
# easily store cell data.
# class Cell:
#     x: int
#     y: int
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# python has a built in priority queue. Bruh
# class PriorityQueue(object):
#     def __init__(self, d):
#         self.data = d
#
#     # here item should be a
#     # 3 element array with the
#     # 3rd element being an int
#     # representing its priority.
#     def enqueue(self, item):
#         self.data.append(item)
#
#     def dequeue(self):
#         try:
#             #get the item with
#             #highest priority (lowest value)
#             temp = self.data[0]
#             for item in self.data:
#                 if item[2] < temp[2]:
#                     temp = item
#             #remove item from queue
#             self.data.remove(temp)
#             #return item.
#             return temp
#         except Exception as error:
#             print("An Exception occured: ", error)
#
#     def peek(self):
#         try:
#             #get the item with
#             #highest priority (lowest value)
#             temp = self.data[0]
#             for item in self.data:
#                 if item[2] < temp[2]:
#                     temp = item
#             #return item.
#             return temp
#         except:
#             print("An error has ocurred")

def gen_grid(r, c):
    return [["." for i in range(c)] for j in range(r)]


def print_grid(g):
    for i in g:
        # print("R: ", end=" ")
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
def input_in_bounds(lower_lim, upper_lim, prompt):
    num = input_int(prompt)
    while True:
        if num > upper_lim:
            print("Input must be less than or equal to " + str(upper_lim))
            num = input_int(prompt)
            continue
        elif num < lower_lim:
            print("Input must be greater than or equal to " + str(lower_lim))
            num = input_int(prompt)
            continue
        else:
            return num


# upper and lower limit are inclusive.
def is_valid(c, g):
    if c[0] < 0 or c[1] < 0:
        return False
    elif c[0] > len(g) - 1 or c[1] > len(g[0]) - 1:
        return False
    else:
        # if there's a wall
        # say it isn't valid.
        if g[c[0]][c[1]] == "#":
            return False
        return True


def print_cell(c):
    print("(" + str(c[0]) + ", " + str(c[1]) + ")")


def breadth_first_search(gr, s, g):
    print("BFS: ")
    print("Start: ", end="")
    print_cell(s)
    print("Goal: ", end="")
    print_cell(g)
    # start at start point
    # check neighbour cells (Cells 1 index up of the current cell)
    # check goal
    # if no goal check neighbours of new frontier.

    # init grid_parent
    grid_parent = [[None] * len(gr[0]) for _ in range(len(gr))]

    # init reached
    reached = []

    # init frontier big enough to hold every cell in the search area.
    frontier = [s]

    # counter = 0
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(frontier) > 0:
        # counter += 1
        c = frontier.pop(0)
        # print("counter: " + str(counter) + " \nFronter empty: " + str(frontier.empty()) + "\nCell: " + str(grid[c.x][c.y]))
        # print()
        # print_grid(grid)
        # goal check
        if c == g:
            p = []
            cur_path = c
            print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            while cur_path is not None:
                p.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]

            # return tuple.
            return p, reached
        reached.append(c)

        # enqueue cell neighbours.
        for act in actions:
            next_c = (c[0] + act[0], c[1] + act[1])
            if not is_valid(next_c, gr):
                continue
            if next_c in reached:
                continue
            if next_c in frontier:
                continue
            # if (grid[next_c[0]][next_c[1]] != "G"):
            # grid[next_c[0]][next_c[1]] = "X"
            frontier.append(next_c)
            grid_parent[next_c[0]][next_c[1]] = c
    print("Failure")
    print("Frontier: ", frontier)
    return None


def reverse_arr(arr):
    temp_arr = []
    for i in range(len(arr) - 1, -1, -1):
        temp_arr.append(arr[i])
    return temp_arr


def reconstruct_path(g, p):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == "*":
                g[i][j] = "."

    for c in p:
        if g[c[0]][c[1]] != "S" and g[c[0]][c[1]] != "G":
            g[c[0]][c[1]] = "*"


def depth_first_search(gr, s, g):
    print("DFS: ")
    print("Start: ", end="")
    print_cell(s)
    print("Goal: ", end="")
    print_cell(g)
    # start at start point
    # check neighbour cells (Cells 1 index up of the current cell)
    # check goal
    # if no goal check neighbours of new frontier.

    # init grid_parent
    grid_parent = [[None] * len(gr[0]) for _ in range(len(gr))]

    # init reached
    reached = []

    # init frontier big enough to hold every cell in the search area.
    # remember this is a stack so use append() not push().
    frontier_dfs = [s]

    # counter = 0
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(frontier_dfs) > 0:
        # print("Inner BFS: ")
        # print_grid(gr)
        # print(frontier_dfs)
        # counter += 1
        # There was a zero in the pop method
        # and I spent hours trying to figure out
        # why my code acted like a queue instead of a stack.
        c = frontier_dfs.pop()
        # print("counter: " + str(counter) + " \nFronter empty: " + str(frontier.empty()) + "\nCell: " + str(grid[c.x][c.y]))
        # print()
        # print_grid(grid)
        # goal check
        if c[0] == g[0] and c[1] == g[1]:
            p = []
            cur_path = c
            print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            # print_grid(grid_parent)

            while cur_path is not None:
                p.append(cur_path)
                # print("BFS: ", cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]
            return p, reached
        reached.append(c)
        # visualization for debug.
        # X represents reached/explored, A represents Added to frontier.
        # if (gr[c[0]][c[1]] == "G" or gr[c[0]][c[1]] == "g"):
        #     gr[c[0]][c[1]] = "&"
        # elif (gr[c[0]][c[1]] == "S" or gr[c[0]][c[1]] == "s" ):
        #     gr[c[0]][c[1]] = "$"
        # else:
        #     gr[c[0]][c[1]] = "X"
        # print_cell(c)
        # print(frontier)

        for act in actions:
            next_c = (c[0] + act[0], c[1] + act[1])
            if not is_valid(next_c, gr):
                continue
            if next_c in reached:
                continue
            if next_c in frontier_dfs:
                continue
            # Visualization for debug.
            # if (gr[next_c[0]][next_c[1]] == "G"):
            #     gr[next_c[0]][next_c[1]] = "g"
            # elif (gr[next_c[0]][next_c[1]] == "S"):
            #     gr[next_c[0]][next_c[1]] = "s"
            # else:
            #     gr[next_c[0]][next_c[1]] = "A"
            frontier_dfs.append(next_c)
            grid_parent[next_c[0]][next_c[1]] = c
    print("Failure")
    print("Frontier: ", frontier_dfs)
    return None


def uniform_cost_search(gr, s, g):
    print("UCS: ")
    print("Start: ", end="")
    print_cell(s)
    print("Goal: ", end="")
    print_cell(g)
    # start at start point
    # check neighbour cells (Cells 1 index up of the current cell)
    # check goal
    # if no goal check neighbours of new frontier.

    # init grid_parent
    grid_parent = [[None] * len(gr[0]) for _ in range(len(gr))]

    # init reached
    reached = []

    # init frontier priority queue
    frontier = queue.PriorityQueue()
    frontier.put((0, s))
    # print(str(frontier.queue))
    # counter = 0
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(frontier.queue) > 0:
        # pop frontier
        c = frontier.get()[1]
        # print(c)
        # print("counter: " + str(counter) + " \nFronter empty: " + str(frontier.empty()) + "\nCell: " + str(grid[c.x][c.y]))
        # print()
        # print_grid(grid)
        # goal check
        if c == g:
            p = []
            cur_path = c
            print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            while cur_path is not None:
                p.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]

            # for some reason
            # I have to use parentheses here
            # even though the other methods return a tuple
            # without these.
            # there is even a warning about how these parentheses
            # SHOULD be redundant.
            return p, reached
        # reached.append(c)

        # # num = 0
        # while cur_path is not None and cur_path not in path:
        #     path.append(cur_path)
        #     cur_path = grid_parent[cur_path[0]][cur_path[1]]
        #     # num += 1
        #     # print(str(num) + " " + str(len(path)) + str(cur_path))
        #
        #     if c == goal_c:
        #         print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
        #         return path
        # print("Current Path: " + str(reverse_arr(path)) + " dist: " + str(len(path)))
        # reconstruct_path(grid, path)
        # print_grid(grid)
        # I wasn't sure if I was supposed to ever modify
        # the reached spaces.
        # I only add them after we're
        # going to begin exploring from c
        # so it doesn't make sense to do so.
        reached.append(c)

        # enqueue cell neighbours.
        for act in actions:
            # declare it this way so it is
            # seen as a list and not a tuple.
            next_c = [c[0] + act[0], c[1] + act[1]]
            if not is_valid(next_c, gr):
                continue
            if next_c in reached:
                continue
            if next_c in frontier.queue:
                continue
            # if (grid[next_c[0]][next_c[1]] != "G"):
            # grid[next_c[0]][next_c[1]] = "X"

            # we need to set the priority
            # of next_c before we enqueue it.
            # getting the total cost of the current
            # path to this node.
            # path = []
            # cur_path = c
            # # print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            # while cur_path is not None:
            #     path.append(cur_path)
            #     cur_path = grid_parent[cur_path[0]][cur_path[1]]
            # len(path)

            # if there is an integer stored here in the grid
            # we put the cell in the priority queue with that
            # int value
            # if not, then we just say it's priority is 0.
            try:
                # maaan, in HWO3 I accidentally had
                # int(gr[next_c[0]][next_c][0]
                # instead of the following line
                # that's why my UCS was taking years to complete before.
                frontier.put((int(gr[next_c[0]][next_c[1]]), next_c))
            except Exception as error:
                frontier.put((0, next_c))
            grid_parent[next_c[0]][next_c[1]] = c
    print("Failure")
    return None

def greedy_best_first_search(gr, s, g):
    print("GBFS: ")
    print("Start: ", end="")
    print_cell(s)
    print("Goal: ", end="")
    print_cell(g)
    # start at start point
    # check neighbour cells (Cells 1 index up of the current cell)
    # check goal
    # if no goal check neighbours of new frontier.

    # init grid_parent
    grid_parent = [[None] * len(gr[0]) for _ in range(len(gr))]

    # init reached
    reached = []

    # init frontier priority queue
    frontier = queue.PriorityQueue()
    frontier.put((0, s))
    # print(str(frontier.queue))
    # counter = 0
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(frontier.queue) > 0:
        # pop frontier
        c = frontier.get()[1]
        # print(c)
        # print("counter: " + str(counter) + " \nFronter empty: " + str(frontier.empty()) + "\nCell: " + str(grid[c.x][c.y]))
        # print()
        # print_grid(grid)
        # goal check
        if c == g:
            p = []
            cur_path = c
            print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            while cur_path is not None:
                p.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]

            # for some reason
            # I have to use parentheses here
            # even though the other methods return a tuple
            # without these.
            # there is even a warning about how these parentheses
            # SHOULD be redundant.
            return p, reached
        # reached.append(c)

        # # num = 0
        # while cur_path is not None and cur_path not in path:
        #     path.append(cur_path)
        #     cur_path = grid_parent[cur_path[0]][cur_path[1]]
        #     # num += 1
        #     # print(str(num) + " " + str(len(path)) + str(cur_path))
        #
        #     if c == goal_c:
        #         print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
        #         return path
        # print("Current Path: " + str(reverse_arr(path)) + " dist: " + str(len(path)))
        # reconstruct_path(grid, path)
        # print_grid(grid)
        # I wasn't sure if I was supposed to ever modify
        # the reached spaces.
        # I only add them after we're
        # going to begin exploring from c
        # so it doesn't make sense to do so.
        reached.append(c)

        # enqueue cell neighbours.
        for act in actions:
            # declare it this way so it is
            # seen as a list and not a tuple.
            next_c = [c[0] + act[0], c[1] + act[1]]
            if not is_valid(next_c, gr):
                continue
            if next_c in reached:
                continue
            if next_c in frontier.queue:
                continue
            # if (grid[next_c[0]][next_c[1]] != "G"):
            # grid[next_c[0]][next_c[1]] = "X"

            # we need to set the priority
            # of next_c before we enqueue it.
            # getting the total cost of the current
            # path to this node.
            # path = []
            # cur_path = c
            # # print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            # while cur_path is not None:
            #     path.append(cur_path)
            #     cur_path = grid_parent[cur_path[0]][cur_path[1]]
            # len(path)

            # if there is an integer stored here in the grid
            # we put the cell in the priority queue with that
            # int value
            # if not, then we just say it's priority is 0.

            # my heuristic here is supposed to be the manhattan
            # distance for the path.
            # does this mean I ignore the values of spaces on the grid?
            # I feel like doing so defeats the purpose but I think
            # if I add the value and the heuristic function then I'd
            # end up with A* so I'll stick with just the manhattan.

            # I think that means my priority value for the priority queue
            # should just be the manhattan distance from that cell
            # to the goal.

            # That's what the textbook describes at least.
            #h(cell) = manhattanDist(cell, goal)
            manhattan = abs(next_c[0] - g[0]) + abs(next_c[1] - g[1])
            frontier.put((manhattan, next_c))
            grid_parent[next_c[0]][next_c[1]] = c
    print("Failure")
    return None

def a_star_search(gr, s, g):
    print("A*: ")
    print("Start: ", end="")
    print_cell(s)
    print("Goal: ", end="")
    print_cell(g)
    # start at start point
    # check neighbour cells (Cells 1 index up of the current cell)
    # check goal
    # if no goal check neighbours of new frontier.

    # init grid_parent
    grid_parent = [[None] * len(gr[0]) for _ in range(len(gr))]

    # init reached
    reached = []

    # init frontier priority queue
    frontier = queue.PriorityQueue()
    frontier.put((0, s))
    # print(str(frontier.queue))
    # counter = 0
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(frontier.queue) > 0:
        # pop frontier
        c = frontier.get()[1]
        # print(c)
        # print("counter: " + str(counter) + " \nFronter empty: " + str(frontier.empty()) + "\nCell: " + str(grid[c.x][c.y]))
        # print()
        # print_grid(grid)
        # goal check
        if c == g:
            p = []
            cur_path = c
            print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            while cur_path is not None:
                p.append(cur_path)
                cur_path = grid_parent[cur_path[0]][cur_path[1]]

            # for some reason
            # I have to use parentheses here
            # even though the other methods return a tuple
            # without these.
            # there is even a warning about how these parentheses
            # SHOULD be redundant.
            return p, reached
        # reached.append(c)

        # # num = 0
        # while cur_path is not None and cur_path not in path:
        #     path.append(cur_path)
        #     cur_path = grid_parent[cur_path[0]][cur_path[1]]
        #     # num += 1
        #     # print(str(num) + " " + str(len(path)) + str(cur_path))
        #
        #     if c == goal_c:
        #         print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
        #         return path
        # print("Current Path: " + str(reverse_arr(path)) + " dist: " + str(len(path)))
        # reconstruct_path(grid, path)
        # print_grid(grid)
        # I wasn't sure if I was supposed to ever modify
        # the reached spaces.
        # I only add them after we're
        # going to begin exploring from c
        # so it doesn't make sense to do so.
        reached.append(c)

        # enqueue cell neighbours.
        for act in actions:
            # declare it this way so it is
            # seen as a list and not a tuple.
            next_c = [c[0] + act[0], c[1] + act[1]]
            if not is_valid(next_c, gr):
                continue
            if next_c in reached:
                continue
            if next_c in frontier.queue:
                continue
            # if (grid[next_c[0]][next_c[1]] != "G"):
            # grid[next_c[0]][next_c[1]] = "X"

            # we need to set the priority
            # of next_c before we enqueue it.
            # getting the total cost of the current
            # path to this node.
            # path = []
            # cur_path = c
            # # print("Found Goal: " + str(c[0]) + ", " + str(c[1]))
            # while cur_path is not None:
            #     path.append(cur_path)
            #     cur_path = grid_parent[cur_path[0]][cur_path[1]]
            # len(path)

            # if there is an integer stored here in the grid
            # we put the cell in the priority queue with that
            # int value
            # if not, then we just say it's priority is 0.

            # my heuristic here is supposed to be the manhattan
            # distance for the path.
            # does this mean I ignore the values of spaces on the grid?
            # I feel like doing so defeats the purpose but I think
            # if I add the value and the heuristic function then I'd
            # end up with A* so I'll stick with just the manhattan.

            # I think that means my priority value for the priority queue
            # should just be the manhattan distance from that cell
            # to the goal.

            # That's what the textbook describes at least.
            #h(cell) = manhattanDist(cell, goal)

            # now that this is A* the heuristic function is:
            #  f(n) = g(n)+h(n)
            #
            # where g(n) is the path cost from the initial state to node n
            # and
            # where h(n) is the estimated cost from the shortest path to the goal state
            # My understanding:
            # g(n) = sum of the values of each node (or cell) in the current path
            # h(n) = manhattan distance from a node to the goal
            # for the h(n) my reasoning is this: we were asked to implement greedy BFS
            # and that makes me think that we should be using part of it in this,
            # which is why the professor specified using manhattan distance.
            # And in the textbook they call their table of values that they later use
            # in A* the "straight line distance" heuristic which in ours is manhattan
            # distance. This makes me sure that h(n) is just that straight line distance
            # or our manhattan distance.

            manhattan = abs(next_c[0] - g[0]) + abs(next_c[1] - g[1])

            # and here I am getting the total cost of the path of nodes
            # from the current cell so we can add that to our manhattan
            # to create our full heuristic function output.
            # here the path cost is known, unlike our estimation using
            # the manhattan calculation.

            # this if statement isn't necessary but I wanted the
            # variables I declare for the path to be local to this if statement
            path_cost = 0
            if c is not None:
                p = []
                cur_path = c

                while cur_path is not None:
                    p.append(cur_path)
                    cur_path = grid_parent[cur_path[0]][cur_path[1]]
                for i in p:
                    # add the value of the cell
                    # if it has one.
                    try:
                        path_cost += gr[i[0]][i[1]]
                    except Exception as error:
                        # we don't add to the path cost here.
                        # py charm wouldn't let me run this until
                        # I put something in here other than a comment.
                        path_cost += 0

            frontier.put((manhattan + path_cost, next_c))

            grid_parent[next_c[0]][next_c[1]] = c
    print("Failure")
    return None

def generate_random_grid_nums(g):
    # I was doing research trying to figure out
    # why my UCS took years to calculate when the grid was
    # a size of 10 or greater.
    # the answer seems to be that I need more variation
    # in costs of tiles so that it can find a "Different"
    # path faster.
    # num_list = [-2, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    # TLDR: That didn't work at all so I'm going back to the
    # path costs from before
    num_list = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
    for i in range(len(g)):
        for j in range(len(g[0])):
            n = random.choice(num_list)
            if n > 0:
                g[i][j] = str(n)
            elif n == 0:
                g[i][j] = "#"
            # for -2 and -1 we ignore changing.


def print_all_types(gr, start_cell, goal_cell):
    # DFS
    print(start_cell)
    grid_dfs = copy.deepcopy(gr)
    # print(id(gr), " Copy: ",  id(grid_dfs))
    dfs1 = depth_first_search(grid_dfs, start_cell, goal_cell)
    if dfs1 is not None:
        path_dfs = dfs1[0]
        reached_dfs = dfs1[1]
        if path_dfs is not None:
            path_dfs = reverse_arr(path_dfs)
            reconstruct_path(grid_dfs, path_dfs)

    # BFS
    grid_bfs = copy.deepcopy(gr)
    bfs1 = breadth_first_search(grid_bfs, start_cell, goal_cell)
    if bfs1 is not None:
        path_bfs = bfs1[0]
        reached_bfs = bfs1[1]
        if path_bfs is not None:
            path_bfs = reverse_arr(path_bfs)
            reconstruct_path(grid_bfs, path_bfs)

    # UCS
    grid_ucs = copy.deepcopy(gr)

    # I honestly have no idea why I have
    # to pass the cell as a list in
    # only UCS but for everything else
    # only tuples will work.

    # Future LD here, but it's got something
    # to do with the priority queue.
    ucs1 = uniform_cost_search(grid_ucs, [start_cell[0], start_cell[1]], [goal_cell[0], goal_cell[1]])
    if ucs1 is not None:
        path_ucs = ucs1[0]
        reached_ucs = ucs1[1]
        if path_ucs is not None:
            path_ucs = reverse_arr(path_ucs)
            reconstruct_path(grid_ucs, path_ucs)


    # GBFS

    grid_gbfs = copy.deepcopy(gr)
    gbfs1 = greedy_best_first_search(grid_gbfs, [start_cell[0], start_cell[1]], [goal_cell[0], goal_cell[1]])
    if gbfs1 is not None:
        path_gbfs = gbfs1[0]
        reached_gbfs = gbfs1[1]
        if path_gbfs is not None:
            path_gbfs = reverse_arr(path_gbfs)
            reconstruct_path(grid_gbfs, path_gbfs)

    # A*

    grid_astar = copy.deepcopy(gr)
    astar1 = a_star_search(grid_astar, [start_cell[0], start_cell[1]], [goal_cell[0], goal_cell[1]])
    if astar1 is not None:
        path_astar = astar1[0]
        reached_ucs = astar1[1]
        if path_astar is not None:
            path_astar = reverse_arr(path_astar)
            reconstruct_path(grid_astar, path_astar)


    print_table(grid_bfs, grid_dfs, grid_ucs, grid_gbfs, grid_astar, bfs1, dfs1, ucs1, gbfs1, astar1)

# look, I know this method is horrendous looking
# but it works, and given more time to learn python
# I would totally make something nice and compact
# instead of this.
def print_table(g1, g2, g3, g4, g5, s1, s2, s3, s4, s5):
    p1 = None if s1 is None else s1[0]
    r1 = None if s1 is None else s1[1]
    p2 = None if s2 is None else s2[0]
    r2 = None if s2 is None else s2[1]
    p3 = None if s3 is None else s3[0]
    r3 = None if s3 is None else s3[1]
    p4 = None if s4 is None else s4[0]
    r4 = None if s4 is None else s4[1]
    p5 = None if s5 is None else s5[0]
    r5 = None if s5 is None else s5[1]
    str_lst = ["|" for i in range(len(g1[0]))]
    gg1 = [["." for i in range(len(g1[0]) + 2)] for j in range(len(g1))]
    gg2 = [["." for i in range(len(g2[0]) + 2)] for j in range(len(g2))]
    gg3 = [["." for i in range(len(g3[0]) + 2)] for j in range(len(g3))]
    gg4 = [["." for i in range(len(g4[0]) + 2)] for j in range(len(g4))]
    gg5 = [["." for i in range(len(g5[0]) + 2)] for j in range(len(g5))]
    for i in range(len(g1)):
        for j in range(len(g1[0]) + 2):
            if j == 0:
                gg1[i][j] = "["
                gg2[i][j] = "["
                gg3[i][j] = "["
                gg4[i][j] = "["
                gg5[i][j] = "["
            elif j == len(g1[0]) + 1:
                gg1[i][j] = "]"
                gg2[i][j] = "]"
                gg3[i][j] = "]"
                gg4[i][j] = "]"
                gg5[i][j] = "]"
            else:
                gg1[i][j] = g1[i][j - 1]
                gg2[i][j] = g2[i][j - 1]
                gg3[i][j] = g3[i][j - 1]
                gg4[i][j] = g4[i][j - 1]
                gg5[i][j] = g5[i][j - 1]

    # create the table and store it as a list
    # so that we can print it as a visible table later.
    table = [[gg1[i] + gg2[i] + gg3[i] + gg4[i] + gg5[i]] for i in range(len(g1))]
    # print key
    print("-" * len(gg1[0]) * 5)
    print("Key:")
    print("*=path, #=wall, S=Start, G=Goal, V=Visited")

    # generate centered spacer for words.
    spacer = (" " * len(g1[0]))
    print(spacer + "BFS" + " " + spacer * 2 + "DFS" + " " + spacer * 2 + "UCS" + " " + spacer * 2 + "GBFS" + " " + spacer * 2 + "A*")
    # s1 = "V: " + str(len(r1))
    # if len(s1) < 3:
    #     s1 = spacer + " " * (3 - len(s1)) + s1
    # elif len(s1) > len(spacer):
    #     s1 = " " * (len(s1) - len(spacer)) + s1
    # else:
    #     s1 = spacer + s1
    #two spaces

    n1 = "F"
    if p1 is not None:
        n1 = "*: " + str(len(p1))
    s1 = n1.center(len(gg1[0]) * 2, " ")

    n2 = "F"
    if p2 is not None:
        n2 = "*: " + str(len(p2))
    s2 = n2.center(len(gg2[0]) * 2, " ")

    n3 = "F"
    if p3 is not None:
        n3 = "*: " + str(len(p3))
    s3 = n3.center(len(gg3[0]) * 2, " ")
    # s1 = "| " + "  " * (len(g1[0]) - len(n1)) + n1 + "|" + " "

    n4 = "F"
    if p4 is not None:
        n4 = "*: " + str(len(p4))
    s4 = n4.center(len(gg4[0]) * 2, " ")

    n5 = "F"
    if p5 is not None:
        n5 = "*: " + str(len(p5))
    s5 = n5.center(len(gg5[0]) * 2, " ")

    print(s1 + s2 + s3 + s4 + s5)

    n1 = "F"
    if r1 is not None:
        n1 = "V: " + str(len(r1))
    s1 = n1.center(len(gg1[0]) * 2, " ")

    n2 = "F"
    if r2 is not None:
        n2 = "V: " + str(len(r2))
    s2 = n2.center(len(gg2[0]) * 2, " ")

    n3 = "F"
    if r3 is not None:
        n3 = "V: " + str(len(r3))
    s3 = n3.center(len(gg3[0]) * 2, " ")
    # s1 = "| " + "  " * (len(g1[0]) - len(n1)) + n1 + "|" + " "

    n4 = "F"
    if r4 is not None:
        n4 = "V: " + str(len(r4))
    s4 = n4.center(len(gg4[0]) * 2, " ")

    n5 = "F"
    if r5 is not None:
        n5 = "V: " + str(len(r5))
    s5 = n5.center(len(gg5[0]) * 2, " ")

    print(s1 + s2 + s3 + s4 + s5)
    # print(s1 + spacer * 2 + str(len(r2)) + " " + spacer * 2 + str(len(r3)))
    for i in table:
        # print("R: ", end=" ")
        for j in i:
            for k in j:
                print(k, end=" ")
            # print(j)
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rows = input_int("Enter rows: ")
    columns = input_int("Enter columns: ")
    grid = gen_grid(rows, columns)

    # generate random numbers across the grid for
    # use with the UCS algorithm.
    generate_random_grid_nums(grid)

    print_grid(grid)

    start_r = input_in_bounds(0, rows - 1, "Enter start row index: ")
    start_c = input_in_bounds(0, columns - 1, "Enter start column index: ")

    # indicate start pos
    grid[start_r][start_c] = "S"

    goal_r = input_in_bounds(0, rows - 1, "Enter goal row index: ")
    goal_c = input_in_bounds(0, columns - 1, "Enter goal column index: ")

    # indicate start pos
    grid[goal_r][goal_c] = "G"

    grid_copy = copy.deepcopy(grid)

    print_grid(grid)

    usr_input = input("Select Algorithm ('B' for BFS, 'D' for DFS, 'U' for UCS, 'G' for GBFS, 'A' for A*): ")

    valid_choices = ["b", "d", "u", "g", "a"]
    # make sure user enters a valid input.
    while not usr_input.lower() in valid_choices:
        print("Please enter a valid input.")
        usr_input = input("Select Algorithm ('B' for BFS, 'D' for DFS, 'U' for UCS, 'G' for GBFS, 'A' for A*): ")

    # if the user selects BFS
    if usr_input.lower() == "b":
        bfs = breadth_first_search(grid, (start_r, start_c), (goal_r, goal_c))
        if bfs is not None:
            path = bfs[0]
            if path is not None:
                path = reverse_arr(path)
                reconstruct_path(grid, path)
                print_grid(grid)
                print(path)
    elif usr_input.lower() == "d":
        dfs = depth_first_search(grid, (start_r, start_c), (goal_r, goal_c))
        if dfs is not None:
            path = dfs[0]
            if path is not None:
                path = reverse_arr(path)
                reconstruct_path(grid, path)
                print_grid(grid)
                print(path)
    elif usr_input.lower() == "u":
        ucs = uniform_cost_search(grid, [start_r, start_c], [goal_r, goal_c])
        # function returns none if it fails.
        if ucs is not None:
            path = ucs[0]
            if path is not None:
                path = reverse_arr(path)
                reconstruct_path(grid, path)
                print_grid(grid)
                print(path)
    elif usr_input.lower() == "g":
        gbfs = greedy_best_first_search(grid, [start_r, start_c], [goal_r, goal_c])
        # function returns none if it fails.
        if gbfs is not None:
            path = gbfs[0]
            if path is not None:
                path = reverse_arr(path)
                reconstruct_path(grid, path)
                print_grid(grid)
                print(path)
    elif usr_input.lower() == "a":
        astar = a_star_search(grid, [start_r, start_c], [goal_r, goal_c])
        # function returns none if it fails.
        if astar is not None:
            path = astar[0]
            if path is not None:
                path = reverse_arr(path)
                reconstruct_path(grid, path)
                print_grid(grid)
                print(path)

    # if I pass grid here,
    # grid will have already been
    # modified to be solved.
    # I instead pass a copy of grid
    # from earlier.
    print_all_types(grid_copy, (start_r, start_c), (goal_r, goal_c))

    # Honestly, because BFS and DFS can't look at values
    # of the grid for a cost based search for the paths
    # BFS almost always finds the shortest path,
    # DFS is almost always the same as UCS and that might just be
    # my implementation.

    # but, BFS is so incredibly good as it still obeys walls.
    # so, no cost considered it's the best.
    # Also in my UCS implementation it takes insanely long
    # when the search area is at least 10x10.
    # That HAS to be my implementation, there must be something
    # I'm doing wrong where it's searching over paths it should have
    # pruned.

    # It's hard to debug so I hope it meets the requirements and if
    # it doesn't then I'm sorry but the instructions were unclear
    # and we didn't do any python to "Build up" to larger stuff.
    # we kinda jumped in so I'm learning python and AI at the same
    # time. LMK if there are ways to fix this and I will, regardless
    # of it's a regrade or not. Knowing these algorithms and understanding
    # them will be really important for Game Development in the future.

    # This is the addition to HW04 regarding GBFS and A*
    # In my implementation UCS is the one that visits the most nodes
    # before selecting a goal.

    # Both GBFS and A* are almost always the same and
    # (though they take a longer path) they take into
    # account the distance (GBFS) or both the cost and distance (A*)
    # and both are superior for checking costs of paths.
    # I have yet to get a search where GBFS and A* are different
    # which makes me think that I've done something wrong.a

