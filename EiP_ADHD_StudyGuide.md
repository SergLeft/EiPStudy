# EiP Master Study Guide ✅

Welcome! This guide is designed for ADHD-friendly, self-paced learning. It covers all Vorlesungen and Übungsblätter (2–12) with checklists, cross-references, code examples, and exam-critical concepts.

---
## 📚 Table of Contents
- [Programming Fundamentals](#programming-fundamentals)
- [Functions & Data Processing](#functions--data-processing)
- [Object-Oriented Programming](#object-oriented-programming)
- [Data Structures](#data-structures)
- [Advanced Algorithms](#advanced-algorithms)
- [Game Programming](#game-programming)
- [Übungsblätter Quick Reference](#übungsblätter-quick-reference)

---
# Programming Fundamentals 🟢🟡
**(Übungsblätter 2–4, Vorlesungen 1–4)**
- [ ] Variables, types, assignment ⚠️
- [ ] Arithmetic & basic operators
- [ ] Input/Output (print, input)
- [ ] Loops (for, while)
- [ ] Conditional statements (if/elif/else) ⚠️
- [ ] Code blocks & indentation

**Code Example:**
```python
for i in range(5):
    if i % 2 == 0:
        print(i)
```

---
# Functions & Data Processing 🟡
**(Übungsblätter 4–8, Vorlesungen 5–7)**
- [ ] Defining and calling functions ⚠️
- [ ] Parameters & return values
- [ ] File I/O (open, read, write)
- [ ] Lists & basic list operations ⚠️
- [ ] Slicing, indexing, iterating
- [ ] Dictionaries & basic usage
- [ ] Simple error handling

**Code Example:**
```python
def sum_list(lst):
    return sum(lst)
```

---
# Object-Oriented Programming 🟡🔴
**(Übungsblätter 9–12, Vorlesungen 8–10)**
- [ ] Classes & objects ⚠️
- [ ] Methods & attributes
- [ ] Inheritance
- [ ] Overriding methods
- [ ] Encapsulation

**Code Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
```

---
# Data Structures 🟡🔴
**(Übungsblätter 7, 10, Vorlesungen 11–12)**
- [ ] Linked lists ⚠️
- [ ] Binary trees
- [ ] Stacks & queues
- [ ] Searching & sorting algorithms

**Code Example:**
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

---
# Advanced Algorithms 🔴
**(Übungsblätter 5, 7, 8, Vorlesungen 13–14)**
- [ ] Recursion ⚠️
- [ ] Computational geometry (Kreise.py, vector.py)
- [ ] Pathfinding (BFS, DFS)
- [ ] Performance complexity (O(n), O(log n))

**Code Example:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---
# Game Programming 🟡🔴
**(Übungsblätter 6, 12)**
- [ ] Event loops (hurdles.py, move.py)
- [ ] State management (dnd.py)
- [ ] Graphics basics (Pygame, not covered in detail)
- [ ] Random events (dice rolls, bingo)

---
# Übungsblätter Quick Reference ⚡
**Exam-critical files, cross-references, and checklists:**

## Blatt 2–4 (Fundamentals & Functions)
- BFS.py, kleine_functionen.py
- [ ] Understand BFS and queue usage
- [ ] Write and trace small helper functions

## Blatt 5–8 (Data, Recursion, Algorithms)
- binary_search.py, hurdles.py, rekursionen.py, longest_route.py, mensa.py
- [ ] Implement binary search (O(log n)) ⚠️
- [ ] Navigate hurdles/grid logic
- [ ] Write and trace recursive functions ⚠️

## Blatt 9–12 (OOP, Data Science, Games)
- Molekule.py, vector.py, Data Science.py, dnd.py, tiere.py
- [ ] Build and use classes for real-world objects ⚠️
- [ ] Manipulate vectors and geometric data
- [ ] Load, process, and visualize data (Data Science.py)
- [ ] Simulate game logic (dnd.py)
- [ ] Model and inherit animal behaviors (tiere.py)

---
# Quick Reference: Syntax & Complexity

**Common Syntax:**
```python
# List comprehension
squares = [x*x for x in range(10)]

# Dictionary iteration
for key, value in my_dict.items():
    print(key, value)

# Function with default parameter
def greet(name, msg="Hello"):
    print(msg, name)
```

**Complexity Notes:**
- Linear search: O(n)
- Binary search: O(log n)
- BFS/DFS: O(V+E)
- Sorting: O(n log n)

---
# Self-Assessment & Progress Tracking
Use the checkboxes above to track your progress. Focus first on ⚠️ exam-critical points and 🔴 advanced topics if aiming for top grades. Cross-reference Übungsblätter with Vorlesungen for deeper understanding.

---
# Feedback & Customization
Let me know if you want more examples, deeper explanations, or a different organization! This guide is here to adapt to your needs.

---
**Good luck! You’ve got this. 🚀**