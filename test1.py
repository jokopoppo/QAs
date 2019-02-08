import numpy as np
from tempfile import TemporaryFile
outfile = TemporaryFile()

# x = np.arange(10)
# np.savetxt('test.out', x, delimiter=',')
print(np.loadtxt('test.out'))