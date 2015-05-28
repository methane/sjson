data = [None, True, False] + list(range(10))
N = 1000000

import timeit
from sjson import sjson_pyx, sjson_py

print("pure Python:", sjson_py.serialize(data))
print(timeit.timeit(lambda: sjson_py.serialize(data),  number=N))

print("pyx:", sjson_pyx.serialize(data))
print(timeit.timeit(lambda: sjson_pyx.serialize(data), number=N))
