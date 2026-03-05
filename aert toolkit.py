# AERT - Algorithmic Efficiency & Recursion Toolkit

# ----------
# Stack ADT
# ---------- 

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
# Testing StackADT
def test_stack():
    print("Testing StackADT")
    stack = StackADT()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Stack Size:", stack.size())
    print("Top Element:", stack.peek())
    print("Popped Element:", stack.pop())
    print("Stack size after pop:", stack.size())
    print("Is stack empty?", stack.is_empty())

# -----------
# Factorial
# -----------

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 1
    return n * factorial(n - 1)

def test_factorial():
    print("\nTesting Factorial")
    test_values = [0, 1, 5, 10]
    for n in test_values:
        print(f"factorial({n}) =", factorial((n)))

# ----------------------------
# Fibonacci (Naive Recursion)
# ----------------------------

fib_naive_calls = 0

def fib_naive(n):
    global fib_naive_calls
    fib_naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# -------------------------------
# Fibonacci (Memoized Recursive)
# -------------------------------

fib_memo_calls = 0

def fib_memo(n, memo={}):
    global fib_memo_calls
    fib_memo_calls += 1

    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def test_fibonacci():
    global fib_naive_calls, fib_memo_calls

    print("\nTesting Fibonacci")
    test_values = [5, 10, 20, 30]

    for n in test_values:
        # Naive
        fib_naive_calls = 0
        result_naive = fib_naive(n)
        print(f"\nNaive Fibonacci({n}) =", result_naive)
        print("Naive Call Count:", fib_naive_calls)

        # Memoized
        fib_memo_calls = 0
        result_memo = fib_memo(n, {})
        print(f"Memoized Fibonacci({n}) =", result_memo)
        print("Memoized Call Count:", fib_memo_calls)

# ---------------
# Tower of Hanoi
# ---------------

def hanoi(n, source, auxiliary, destinaton, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destinaton}"
        stack.push(move)
        return
    
    hanoi(n - 1, source, destinaton, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destinaton}"
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destinaton, stack)

def test_hanoi():
    print("\nTower of Hanoi for N = 3")
    stack = StackADT()

    hanoi(3, 'A', 'B', 'C', stack)
    
    # print moves in correct order 
    moves = []
    while not stack.is_empty():
        moves.append(stack.pop())
    
    for move in reversed(moves):
        print(move)

# -------------------------
# Recursive Binary Search
# -------------------------

def binary_search(arr, key, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

def test_binary_search():
    print("\nTesting Recursive Binary Search")
    
    arr = [1, 3, 5, 7, 9, 11, 13]
    test_keys = [7, 1, 13, 2]

    for key in test_keys:
        result = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Searching {key}:", result)

    # Empty array case
    empty_arr = []
    result = binary_search(empty_arr, 5, 0, len(empty_arr) - 1)
    print("Searching in empty array:", result)

def main():
    test_stack()
    test_factorial()
    test_fibonacci()
    test_hanoi()
    test_binary_search()

if __name__ == "__main__":
    main()
    