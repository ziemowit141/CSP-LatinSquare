import numpy as np
import copy


# previous version
def compare_vector(v1, v2, domain):
    temp = 0
    for i in range(len(v1)):
        if (v1[i] == v2[i] and v1[i] in domain):
            temp = temp + 1
    if (temp == len(v1)):
        return 1
    else:
        return 0


# previous version

# previous version
def unique_rows(grid, domain):
    for i in range(np.shape(grid)[0]):
        for j in range(np.shape(grid)[0]):
            if (compare_vector(grid[i], grid[j], domain) and i != j):
                return 0
    return 1


# previous version

# previous version
def unique_columns(grid, domain):
    for i in range(np.shape(grid)[1]):
        for j in range(np.shape(grid)[1]):
            if (compare_vector(grid[:, i], grid[:, j], domain) and i != j):
                return 0
    return 1


# previous version


def create_grid(size):
    return np.zeros(dtype=str, shape=size)


def consecutive_values_rows(grid, domain):
    size = np.shape(grid)
    if (size[1] >= 2):
        for i in range(size[0]):
            for j in range(size[1] - 1):
                for d in domain:
                    if np.array_equal(grid[i, j:j + 2], [d, d]):
                        return 0
    return 1


def consecutive_values_columns(grid, domain):
    size = np.shape(grid)
    if (size[0] >= 2):
        for i in range(size[1]):
            for j in range(size[0] - 1):
                for d in domain:
                    if np.array_equal(grid[j:j + 2, i], [d, d]):
                        return 0
    return 1


def acceptable_solution(grid, domain):
    if consecutive_values_rows(grid, domain) and consecutive_values_columns(grid, domain) \
            and unique_rows(grid, domain) and unique_columns(grid, domain):
        return 1
    else:
        return 0


def acceptable_solution_forward(grid, domain):
    if unique_rows(grid, domain) and unique_columns(grid, domain):
        return 1
    else:
        return 0


def done(grid):
    for i in range(np.shape(grid)[0]):
        for j in range(np.shape(grid)[1]):
            if grid[i][j] == '':
                return 0
    return 1


def copy_grid(grid):
    new_grid = create_grid(np.shape(grid))
    for i in range(np.shape(new_grid)[0]):
        for j in range(np.shape(new_grid)[1]):
            new_grid[i][j] = grid[i][j]
    return new_grid


def backtrack(grid, domain, x_pos, y_pos):
    if done(grid):
        return grid
    x_pos = x_pos + 1
    if x_pos == len(grid):
        x_pos = 0
        y_pos = y_pos + 1
    for d in domain:
        grid[x_pos][y_pos] = d
        if acceptable_solution(grid, domain):
            solution = backtrack(grid, domain, x_pos, y_pos)
            if isinstance(solution, np.ndarray):
                return solution


def forwardcheck(grid, domain, x_pos, y_pos):
    for i in surrounding(grid, x_pos, y_pos):
        domain.remove(i)
    return domain


def surrounding(grid, x_pos, y_pos):
    list = []
    if x_pos - 1 >= 0:
        list.append(grid[x_pos - 1][y_pos])
    if y_pos - 1 >= 0:
        if grid[x_pos][y_pos - 1] not in list:
            list.append(grid[x_pos][y_pos - 1])
    return list


def backtrack_forwardcheck(grid, domain, x_pos, y_pos):
    if done(grid):
        return grid
    x_pos = x_pos + 1
    if x_pos == len(grid):
        x_pos = 0
        y_pos = y_pos + 1
    reduced_domain = forwardcheck(grid, copy.copy(domain), x_pos, y_pos)
    for d in reduced_domain:
        grid[x_pos][y_pos] = d
        if acceptable_solution_forward(grid, domain):
            solution = backtrack_forwardcheck(grid, domain, x_pos, y_pos)
            if isinstance(solution, np.ndarray):
                return solution
