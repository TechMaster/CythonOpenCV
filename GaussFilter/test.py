import numpy as np

for k in np.arange(-2, 3):
    for l in np.arange(-2, 3):
        print(f"({str(k).rjust(2)} {str(l).rjust(2)})", end="  ")
    print()
    print()
