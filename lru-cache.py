"""[lru_cache - how cache unperformance function]
[Author: prakasa<prakasa@devetek.com>]
"""
import timeit
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for x in range(100):
    print(timeit.timeit('fibonacci(35)', globals=globals(), number=1))

print(fibonacci.cache_info())
