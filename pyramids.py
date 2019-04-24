import numpy as np
import random
import copy


def create_grid(size):
    return np.zeros(shape=(size, size), dtype=int)


def create_visibility(size):
    list_x = [np.zeros(shape=size, dtype=int), np.zeros(shape=size, dtype=int)]
    list_y = [np.zeros(shape=size, dtype=int), np.zeros(shape=size, dtype=int)]
    while np.count_nonzero(list_x[0]) != int(size / 2):
        list_x[0][random.randint(0, size - 1)] = random.randint(0, size - 1) + 1
    while np.count_nonzero(list_x[1]) != int(size / 2):
        list_x[1][random.randint(0, size - 1)] = random.randint(0, size - 1) + 1
    while np.count_nonzero(list_y[0]) != int(size / 2):
        list_y[0][random.randint(0, size - 1)] = random.randint(0, size - 1) + 1
    while np.count_nonzero(list_y[1]) != int(size / 2):
        list_y[1][random.randint(0, size - 1)] = random.randint(0, size - 1) + 1
    return list_x, list_y


def done(grid):
    if grid[len(grid) - 1][len(grid) - 1] == 0:
        return 0
    return 1


def visibility(grid, arr):
    for i in range(len(grid)):
        tallest = 0
        count = 0
        if arr[i] != 0 and np.count_nonzero(grid[i]) == len(grid[i]):
            for j in range(len(grid)):
                if tallest < grid[i][j]:
                    tallest = grid[i][j]
                    count = count + 1
            if count != arr[i]:
                return 0
    return 1


def visibility_reverse(grid, arr):
    for i in range(len(grid)):
        tallest = 0
        count = 0
        if arr[i] != 0 and np.count_nonzero(grid[i]) == len(grid[i]):
            for j in range(len(grid)):
                if tallest < grid[i][len(grid) - j - 1]:
                    tallest = grid[i][len(grid) - j - 1]
                    count = count + 1
            if count != arr[i]:
                return 0
    return 1


def check_visibility(grid, vis_col, vis_row):
    if visibility(grid, vis_row[0]) and visibility_reverse(grid, vis_row[1]):
        temp_grid = np.copy(grid)
        temp_grid = np.rot90(temp_grid)
        if visibility(temp_grid, vis_col[0]) and visibility_reverse(temp_grid, vis_col[1]):
            return 1
    return 0


def unique_values(arr):
    list = []
    for i in range(len(arr)):
        if arr[i] in list:
            return 0
        if arr[i] != 0:
            list.append(arr[i])
    return 1


def unique_grid(grid):
    for i in range(len(grid)):
        if not unique_values(grid[i]) or not unique_values(grid[:, i]):
            return 0
    return 1


def acceptable_solution(grid, vis_col, vis_row):
    return unique_grid(grid) and check_visibility(grid, vis_col, vis_row)


def backtrack(grid, domain, x_pos, y_pos, vis_col, vis_row):
    if done(grid):
        return grid
    x_pos = x_pos + 1
    if x_pos == len(grid):
        x_pos = 0
        y_pos = y_pos + 1
    for i in domain:
        grid[x_pos][y_pos] = i
        if acceptable_solution(grid, vis_col, vis_row):
            solution = backtrack(grid, domain, x_pos, y_pos, vis_col, vis_row)
            if isinstance(solution, np.ndarray):
                return solution
        else:
            grid[x_pos][y_pos] = 0


def show_results(grid, vis_col, vis_row):
    result = np.zeros(shape=(len(grid) + 2, len(grid) + 2), dtype=int)
    v1 = np.flip(vis_col[1])
    v2 = np.flip(vis_col[0])
    for i in range(len(vis_col[0])):
        result[len(grid) + 1][i + 1] = v1[i]
        result[0][i + 1] = v2[i]
        result[i + 1][0] = vis_row[0][i]
        result[i + 1][len(grid) + 1] = vis_row[1][i]
    for i in range(len(grid)):
        for j in range(len(grid)):
            result[i + 1][j + 1] = grid[i][j]

    for i in range(len(result)):
        for j in range(len(result)):
            if result[i][j] != 0:
                print(result[i][j], end='\t')
            else:
                print("\t", end='')
        print("\n", end='')

    return result


def vis_check1(vis):
    for i in range(len(vis[0])):
        if vis[0][i] == len(vis[0]):
            if vis[1][i] != 0:
                return 0
        elif vis[1][i] == len(vis[1]):
            if vis[0][i] != 0:
                return 0
    return 1


def vis_check2(vis):
    for i in range(len(vis[0])):
        if vis[0][i] == 1 and vis[1][i] == 1:
            return 0
    return 1


def forwardcheck_vis(vis):
    return vis_check1(vis) and vis_check2(vis)


def initial_var(grid, x_pos, y_pos, vis_col, vis_row):
    list = []
    v1 = np.flip(vis_col[0])
    if x_pos == 0:
        if vis_row[0][y_pos] == 1:
            for i in range(len(grid) - 1):
                list.append(i + 1)
        else:
            for i in range(vis_row[0][y_pos] - 1):
                list.append(len(grid) - i)
    if y_pos == 0:
        if v1[x_pos] == 1:
            for i in range(len(grid) - 1):
                list.append(i + 1)
        else:
            for i in range(v1[x_pos] - 1):
                list.append(len(grid) - i)
    return list


def forward_check(grid, domain, x_pos, y_pos, vis_col, vis_row):
    for i in set(initial_var(grid, x_pos, y_pos, vis_col, vis_row)):
        domain.remove(i)
    return domain


def backtrack_forward_check(grid, domain, x_pos, y_pos, vis_col, vis_row):
    if done(grid):
        return grid
    x_pos = x_pos + 1
    if x_pos == len(grid):
        x_pos = 0
        y_pos = y_pos + 1
    reduced_domain = forward_check(grid, copy.copy(domain), x_pos, y_pos, vis_col, vis_row)
    for i in reduced_domain:
        grid[x_pos][y_pos] = i
        if acceptable_solution(grid, vis_col, vis_row):
            solution = backtrack(grid, domain, x_pos, y_pos, vis_col, vis_row)
            if isinstance(solution, np.ndarray):
                return solution
        else:
            grid[x_pos][y_pos] = 0
