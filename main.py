import mosaic
import pyramids
import numpy as np
import time





#Letter Mosaic

#grid_size = (20, 5)

#D = ['a', 'b', 'c', 'd']
#X = mosaic.create_grid(grid_size)

#result = mosaic.backtrack(X, D, -1, 0)
#result = mosaic.backtrack_forwardcheck(X, D, -1, 0)
#print(result)



#Letter Mosaic

#Pyramids
#iter = 0

grid_size = 8

D = []
result = None
for i in range(grid_size):
    D.append(i + 1)
X = pyramids.create_grid(grid_size)
visibility_col, visibility_row = pyramids.create_visibility(grid_size)
start_time = time.time()
result = pyramids.backtrack(X, D, -1, 0, visibility_col, visibility_row)
print ("1:time elapsed: {:.2f}s".format(time.time() - start_time))
X = pyramids.create_grid(grid_size)
start_time2 = time.time()
result = pyramids.backtrack_forward_check(X, D, -1, 0, visibility_col, visibility_row)
print ("2:time elapsed: {:.2f}s".format(time.time() - start_time2))
pyramids.show_results(result, visibility_col, visibility_row)

#result = None
#while (not isinstance(result, np.ndarray)):
#    X = pyramids.create_grid(grid_size)
#    visibility_col, visibility_row = pyramids.create_visibility(grid_size)
#    if pyramids.forwardcheck_vis(visibility_col) and pyramids.forwardcheck_vis(visibility_row):
#        result = pyramids.backtrack_forwardcheck(X, D, -1, 0, visibility_col, visibility_row)
#    iter = iter + 1
#    print(iter)
#r = pyramids.show_results(result, visibility_col, visibility_row)




#print(X)
#print(visibility_col)
#print(visibility_row)
#print(pyramids.done(X))
#print(pyramids.visibility(X, visibility_row[0]))
#print(pyramids.visibility_reverse(a, vis))
#a = np.array([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
#vis_r = np.array([[3, 0, 0], [0, 2, 0]])
#vis_c = np.array([[0, 2, 0], [0, 0, 1]])
#print(pyramids.check_visibility(a, vis_c, vis_r))
#print(pyramids.unique_grid(a))