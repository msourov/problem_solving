import numpy as np
a =  [[1, 1, 1, 0, 0, 0], #i=0
      [0, 1, 0, 0, 0, 0], #i = 
      [1, 1, 1, 0, 0, 0], 
      [0, 0, 2, 4, 4, 0], 
      [0, 0, 0, 2, 0, 0], 
      [0, 0, 1, 2, 4, 0]]
x = np.array(a)

sums = []
for i in range(4):
    for j in range(4):
        sums.append(np.sum(x[i:i+3,j:j+3]))
max(sums)
