
import random
import time

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)

def benchmark(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    return time.time() - start

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]
    for n in sizes:
        random_arr = [random.randint(0, n) for _ in range(n)]
        sorted_arr = list(range(n))
        reversed_arr = list(range(n, 0, -1))
        repeated_arr = [5] * n

        print(f"\nArray size: {n}")
        print("Randomized QS (random):", benchmark(randomized_quicksort, random_arr))
        print("Deterministic QS (random):", benchmark(deterministic_quicksort, random_arr))
        print("Randomized QS (sorted):", benchmark(randomized_quicksort, sorted_arr))
        print("Deterministic QS (sorted):", benchmark(deterministic_quicksort, sorted_arr))
