# AERT_Assignment_2501730068_Chakshu_Madan
# Algorithmic Efficiency & Recursion Toolkit (AERT)

This repository contains my **Unit-1 Data Structures assignment** for the course **ETCCDS202 – Foundations & Algorithmic Analysis**.

The project implements several fundamental algorithms using **recursion** and analyzes their efficiency.

## Implemented Components

### 1. Stack ADT

A basic implementation of the **Stack Abstract Data Type** with the following operations:

* push(x)
* pop()
* peek()
* is_empty()
* size()

The stack is used to store and display the **Tower of Hanoi move sequence**.

### 2. Recursive Factorial

A recursive implementation of the factorial function with a proper base case.

Test cases included:

* n = 0
* n = 1
* n = 5
* n = 10

### 3. Fibonacci (Two Recursive Versions)

**Naive Recursive Fibonacci**

* Direct recursive implementation
* Demonstrates exponential growth of recursive calls

**Memoized Fibonacci**

* Uses memoization (Dynamic Programming concept)
* Stores previously computed results to improve efficiency

Both versions include a **call counter** to compare performance.

Test cases:

* n = 5
* n = 10
* n = 20
* n = 30

### 4. Tower of Hanoi

Recursive implementation that prints the move sequence for **N = 3 disks**.

The sequence of moves is stored using the implemented **StackADT**.

### 5. Recursive Binary Search

A recursive implementation of binary search using the **Divide & Conquer paradigm**.

Test cases include:

* Searching existing values
* Searching a non-existing value
* Searching in an empty array

## Repository Files

* **aert toolkit.py**
  Contains the complete Python implementation of all algorithms and test cases.

* **output.txt**
  Contains the console output produced after running the program.

* **report.pdf**
  A short report explaining:

  * Algorithm complexity (Big-O, Big-Ω, Big-Θ)
  * Recursion concepts
  * Algorithm paradigms (Divide & Conquer, Dynamic Programming, Greedy)

## How to Run

Run the program using:

```
python "aert toolkit.py"
```

This will execute all test cases and display the results in the console.
