import sys
import numpy as np
S=range(1000)
print('resultado de lista de python')
print(sys.getsizeof(5)*len(S))
print()
D=np.arange(1000)
print('resultado de array de numpy')
print(D.size*D.itemsize)