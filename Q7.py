#Calculate tanh output for [-2, -1, 0, 1, 2].

import numpy as np

values = np.array([-2, -1, 0, 1, 2])

result = np.tanh(values)

print("Input:", values)
print("Tanh Output:", result)