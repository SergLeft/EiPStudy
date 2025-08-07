# EiP Study Guide: Key Concepts Checklist

## Introduction

This comprehensive study guide consolidates all key concepts from Vorlesungen 1-14 of the Einführung in die Programmierung (EiP) course. Use this as a learning checklist to identify knowledge gaps and focus your study efforts.

### How to Use This Guide

- **Self-Assessment**: Use checkboxes `- [ ]` to track your understanding of each concept
- **Difficulty Levels**: 
  - 🟢 **Beginner**: Fundamental concepts every programmer should know
  - 🟡 **Intermediate**: Building on basics, requires practice to master
  - 🔴 **Advanced**: Complex concepts requiring deep understanding
- **Exam Markers**: ⚠️ indicates concepts that are critical for exam success
- **Cross-References**: Links connect related concepts across lectures
- **Code Examples**: Practical examples to reinforce understanding

### Quick Navigation

1. [Vorlesung 1-3: Programming Fundamentals](#vorlesung-1-3-programming-fundamentals)
2. [Vorlesung 4-6: Functions and Data Processing](#vorlesung-4-6-functions-and-data-processing)
3. [Vorlesung 7-9: Advanced Programming](#vorlesung-7-9-advanced-programming)
4. [Vorlesung 10-11: Data Structures](#vorlesung-10-11-data-structures)
5. [Vorlesung 12: Advanced OOP](#vorlesung-12-advanced-oop)
6. [Vorlesung 13: Game Programming](#vorlesung-13-game-programming)
7. [Vorlesung 14: Advanced Algorithms](#vorlesung-14-advanced-algorithms)
8. [Quick Reference](#quick-reference)

---

## Vorlesung 1-3: Programming Fundamentals

### Vorlesung 1: Introduction and Basic I/O 🟢

#### Core Concepts
- [ ] ⚠️ **Program structure and execution** - Understanding how Python programs run
- [ ] ⚠️ **Variable declaration and assignment** - Creating and storing data
- [ ] **Input/Output operations** - `input()` and `print()` functions
- [ ] **Basic debugging** - Reading error messages and fixing syntax errors

#### Code Example: Basic I/O
```python
# Variable assignment and basic I/O
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

#### Practical Applications
- [ ] **Interest calculation** - Apply mathematical formulas in programming
- [ ] **User interaction** - Create programs that respond to user input

### Vorlesung 2: Data Types and Operations 🟢

#### Fundamental Data Types
- [ ] ⚠️ **Integer (int)** - Whole numbers and arithmetic operations
- [ ] ⚠️ **Float** - Decimal numbers and precision considerations
- [ ] ⚠️ **String (str)** - Text manipulation and basic string methods
- [ ] ⚠️ **Boolean (bool)** - True/False values and logical operations

#### Operators
- [ ] ⚠️ **Arithmetic operators** - `+`, `-`, `*`, `/`, `//`, `%`, `**`
- [ ] ⚠️ **Comparison operators** - `==`, `!=`, `<`, `>`, `<=`, `>=`
- [ ] ⚠️ **Logical operators** - `and`, `or`, `not`
- [ ] **Assignment operators** - `=`, `+=`, `-=`, `*=`, `/=`

#### Code Example: Data Types and Operations
```python
# Arithmetic operations
a, b = 10, 3
print(f"Division: {a / b}")      # 3.333...
print(f"Integer division: {a // b}")  # 3
print(f"Modulo: {a % b}")        # 1
print(f"Power: {a ** b}")        # 1000

# String operations
text = "Python"
print(f"Length: {len(text)}")    # 6
print(f"Uppercase: {text.upper()}")  # PYTHON
```

#### Advanced Topics
- [ ] **Type conversion** - `int()`, `float()`, `str()`, `bool()`
- [ ] **Euclidean algorithm** - Greatest common divisor calculation
- [ ] **Compound interest calculation** - Mathematical programming applications

### Vorlesung 3: Control Structures 🟢

#### Conditional Statements
- [ ] ⚠️ **if-else statements** - Making decisions in programs
- [ ] ⚠️ **elif chains** - Multiple condition handling
- [ ] **Nested conditionals** - if statements inside if statements

#### Loops
- [ ] ⚠️ **for loops** - Iterating over sequences and ranges
- [ ] ⚠️ **while loops** - Condition-based repetition
- [ ] ⚠️ **Loop control** - `break` and `continue` statements
- [ ] **Nested loops** - Loops inside loops

#### Code Example: Control Structures
```python
# Prime number check with for loop
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Using the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
```

#### Algorithms Introduced
- [ ] ⚠️ **Bubble Sort** - Basic sorting algorithm with nested loops
- [ ] **Prime number testing** - Applying loops and conditionals
- [ ] **Number generation** - Creating sequences with loops

---

## Vorlesung 4-6: Functions and Data Processing

### Vorlesung 4: Functions and Modular Programming 🟡

#### Function Fundamentals
- [ ] ⚠️ **Function definition** - `def` keyword and function syntax
- [ ] ⚠️ **Parameters and arguments** - Passing data to functions
- [ ] ⚠️ **Return values** - Getting results from functions
- [ ] **Local vs global scope** - Variable visibility rules

#### Advanced Function Concepts
- [ ] **Default parameters** - Functions with optional arguments
- [ ] **Multiple return values** - Returning tuples
- [ ] **Function documentation** - Docstrings and comments
- [ ] 🟡 **Recursive thinking** - Functions calling themselves (preview)

#### Code Example: Functions
```python
def binary_search(arr, target):
    """Search for target in sorted array using binary search."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

#### Practical Applications
- [ ] **Binary search implementation** - Efficient searching in sorted data
- [ ] **Matrix operations** - Working with 2D data structures
- [ ] **City distance calculations** - Real-world data processing

### Vorlesung 5: File I/O and Data Processing 🟡

#### File Operations
- [ ] ⚠️ **Opening and closing files** - `open()` function and file modes
- [ ] ⚠️ **Reading from files** - `read()`, `readline()`, `readlines()`
- [ ] ⚠️ **Writing to files** - `write()` and `writelines()`
- [ ] **File context managers** - `with` statement for safe file handling

#### Data Processing
- [ ] **CSV file handling** - Reading and writing structured data
- [ ] **String parsing** - Extracting information from text
- [ ] **Data filtering** - Selecting relevant information
- [ ] 🟡 **Breadth-First Search (BFS)** - Graph traversal algorithm

#### Code Example: File I/O
```python
# Reading and processing data from file
def process_cities_file(filename):
    cities = []
    with open(filename, 'r') as file:
        for line in file:
            # Parse city data (name, coordinates, etc.)
            parts = line.strip().split(',')
            cities.append({
                'name': parts[0],
                'latitude': float(parts[1]),
                'longitude': float(parts[2])
            })
    return cities

# Usage
cities = process_cities_file('cities.csv')
```

#### Advanced Topics
- [ ] **Matrix multiplication** - Implementing mathematical operations
- [ ] **Graph representation** - Adjacency lists and matrices
- [ ] **Algorithm complexity** - Understanding Big O notation basics

### Vorlesung 6: Advanced Functions and Algorithms 🟡

#### Function Design Patterns
- [ ] **Helper functions** - Breaking complex problems into smaller parts
- [ ] **Function composition** - Combining functions to solve problems
- [ ] **Error handling basics** - Preventing and managing errors
- [ ] 🟡 **Algorithm optimization** - Improving efficiency

#### Graph Algorithms
- [ ] 🟡 **Graph traversal** - Systematic exploration of connected data
- [ ] 🟡 **Path finding** - Finding routes in networks
- [ ] **Data structure design** - Choosing appropriate representations

#### Code Example: London Tube System
```python
def find_shortest_path(graph, start, end):
    """Find shortest path using BFS."""
    from collections import deque

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found
```

#### Real-World Applications
- [ ] **London Tube navigation** - Practical graph algorithm application
- [ ] **Network analysis** - Understanding connected systems
- [ ] **Route optimization** - Finding efficient paths

---

## Vorlesung 7-9: Advanced Programming

### Vorlesung 7: Recursion and Advanced Algorithms 🔴

#### Recursion Fundamentals
- [ ] ⚠️ **Recursive function structure** - Base case and recursive case
- [ ] ⚠️ **Call stack understanding** - How recursive calls are managed
- [ ] ⚠️ **Recursion vs iteration** - When to use each approach
- [ ] 🔴 **Tail recursion** - Optimized recursive patterns

#### Classic Recursive Algorithms
- [ ] **Tower of Hanoi** - Classic recursion problem
- [ ] ⚠️ **Merge Sort** - Divide-and-conquer sorting algorithm
- [ ] **Factorial calculation** - Simple recursive example
- [ ] **Fibonacci sequence** - Understanding recursive patterns

#### Code Example: Merge Sort
```python
def merge_sort(arr):
    """Sort array using merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

#### Advanced Concepts
- [ ] 🔴 **Complexity analysis** - Time and space complexity of recursive algorithms
- [ ] **Variable scope in recursion** - Understanding local, global, and recursive contexts
- [ ] **Memory considerations** - Stack overflow and optimization

### Vorlesung 8: Backtracking and Problem Solving 🔴

#### Backtracking Fundamentals
- [ ] 🔴 **Backtracking principle** - Systematic trial and error
- [ ] 🔴 **Search space exploration** - Finding all possible solutions
- [ ] **Pruning strategies** - Eliminating invalid branches early
- [ ] **State management** - Tracking and undoing changes

#### Classic Backtracking Problems
- [ ] **N-Queens problem** - Placing queens on a chessboard
- [ ] **Sudoku solver** - Constraint satisfaction problem
- [ ] **Graph coloring** - Assigning colors with constraints
- [ ] **Maze solving** - Finding paths through obstacles

#### Code Example: N-Queens
```python
def solve_n_queens(n):
    """Solve N-Queens problem using backtracking."""
    board = [-1] * n  # board[i] = column of queen in row i
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if (board[i] == col or 
                board[i] - i == col - row or
                board[i] + i == col + row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    backtrack(0)
    return solutions
```

#### Problem-Solving Strategies
- [ ] **Constraint identification** - Understanding problem limitations
- [ ] **Solution validation** - Checking if solutions are correct
- [ ] **Optimization techniques** - Making backtracking more efficient

### Vorlesung 9: Object-Oriented Programming Basics 🟡

#### OOP Fundamentals
- [ ] ⚠️ **Class definition** - Creating custom data types
- [ ] ⚠️ **Object instantiation** - Creating instances of classes
- [ ] ⚠️ **Attributes and methods** - Data and behavior in objects
- [ ] ⚠️ **Constructor method** - `__init__` method for object initialization

#### Advanced OOP Concepts
- [ ] **Instance vs class attributes** - Understanding scope and sharing
- [ ] **Method types** - Instance, class, and static methods
- [ ] **Encapsulation basics** - Private attributes and methods
- [ ] 🟡 **Object relationships** - Composition and aggregation

#### Code Example: Fraction Class
```python
class Fraction:
    """Represents a mathematical fraction."""

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # Reduce fraction to lowest terms
        gcd = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        # Handle negative denominators
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def _gcd(self, a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        """Add two fractions."""
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
```

#### Practical Applications
- [ ] **Fraction arithmetic** - Mathematical operations with objects
- [ ] **Polynomial representation** - Complex mathematical structures
- [ ] **Data modeling** - Representing real-world entities

---

## Vorlesung 10-11: Data Structures

### Vorlesung 10: Lists and Linear Data Structures 🟡

#### List Operations and Methods
- [ ] ⚠️ **List creation and initialization** - Different ways to create lists
- [ ] ⚠️ **List indexing and slicing** - Accessing and modifying elements
- [ ] ⚠️ **List methods** - `append()`, `insert()`, `remove()`, `pop()`, `extend()`
- [ ] **List comprehensions** - Concise list creation syntax

#### Advanced List Concepts
- [ ] **Nested lists** - Lists containing other lists
- [ ] **List vs tuple** - Mutable vs immutable sequences
- [ ] 🟡 **Memory considerations** - How lists are stored and managed
- [ ] **Performance characteristics** - Time complexity of list operations

#### Code Example: List Operations
```python
# List comprehension examples
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]
evens = [x for x in numbers if x % 2 == 0]  # [2, 4]

# Nested list operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Working with dynamic lists
shopping_list = []
shopping_list.append("bread")
shopping_list.extend(["milk", "eggs"])
item = shopping_list.pop()  # Removes and returns "eggs"
```

#### Practical Applications
- [ ] **Dynamic data storage** - Managing changing collections
- [ ] **Matrix operations** - 2D data manipulation
- [ ] **Algorithm implementation** - Using lists for complex algorithms

### Vorlesung 11: Trees and Recursive Data Structures 🔴

#### Binary Tree Fundamentals
- [ ] ⚠️ **Tree terminology** - Node, root, leaf, parent, child, height, depth
- [ ] ⚠️ **Binary tree structure** - Each node has at most two children
- [ ] ⚠️ **Tree traversal methods** - Inorder, preorder, postorder
- [ ] 🔴 **Binary search tree (BST)** - Ordered tree structure

#### Tree Operations
- [ ] ⚠️ **Tree insertion** - Adding new nodes while maintaining structure
- [ ] ⚠️ **Tree searching** - Finding elements efficiently
- [ ] ⚠️ **Tree deletion** - Removing nodes with proper restructuring
- [ ] 🔴 **Tree balancing concepts** - Maintaining efficient tree structure

#### Code Example: Binary Search Tree
```python
class TreeNode:
    """Node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary search tree implementation."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the tree."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        # Equal values are ignored

    def search(self, value):
        """Search for a value in the tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Return values in sorted order."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
```

#### Advanced Tree Concepts
- [ ] 🔴 **Tree complexity analysis** - Time and space complexity of operations
- [ ] **Tree applications** - File systems, expression parsing, decision trees
- [ ] **Tree variations** - AVL trees, red-black trees (concepts only)

---

## Vorlesung 12: Advanced OOP

### Advanced Object-Oriented Programming 🟡

#### Inheritance
- [ ] ⚠️ **Class inheritance** - Creating classes based on existing classes
- [ ] ⚠️ **Method overriding** - Redefining parent class methods
- [ ] ⚠️ **super() function** - Calling parent class methods
- [ ] **Multiple inheritance** - Inheriting from multiple classes

#### Advanced OOP Features
- [ ] **Abstract classes and methods** - Defining interfaces
- [ ] **Polymorphism** - Same interface, different implementations
- [ ] **Operator overloading** - Customizing operators for objects
- [ ] 🟡 **Design patterns basics** - Common OOP solutions

#### Code Example: Inheritance
```python
class Animal:
    """Base class for all animals."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        """Override in subclasses."""
        raise NotImplementedError("Subclasses must implement make_sound")

    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal."""

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    """Cat class inheriting from Animal."""

    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring contentedly"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

animals = [dog, cat]
for animal in animals:
    print(f"{animal.info()}: {animal.make_sound()}")
```

### Dictionary Data Structures 🟡

#### Dictionary Fundamentals
- [ ] ⚠️ **Key-value pairs** - Associating data with unique identifiers
- [ ] ⚠️ **Dictionary operations** - Creating, accessing, modifying dictionaries
- [ ] ⚠️ **Dictionary methods** - `keys()`, `values()`, `items()`, `get()`, `pop()`
- [ ] **Dictionary comprehensions** - Concise dictionary creation

#### Advanced Dictionary Concepts
- [ ] 🟡 **Hash table implementation** - How dictionaries work internally
- [ ] **Collision handling** - Dealing with hash conflicts
- [ ] **Performance characteristics** - Average and worst-case complexity
- [ ] **Memory efficiency** - Space considerations for large dictionaries

#### Code Example: Dictionary Applications
```python
# Word frequency counter
def count_words(text):
    """Count frequency of words in text."""
    words = text.lower().split()
    frequency = {}

    for word in words:
        # Remove punctuation
        word = ''.join(c for c in word if c.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Student grade management
class GradeBook:
    """Manage student grades using dictionaries."""

    def __init__(self):
        self.students = {}  # {student_id: {"name": str, "grades": [float]}}

    def add_student(self, student_id, name):
        self.students[student_id] = {"name": name, "grades": []}

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id]["grades"].append(grade)

    def get_average(self, student_id):
        if student_id in self.students:
            grades = self.students[student_id]["grades"]
            return sum(grades) / len(grades) if grades else 0
        return None

    def get_class_statistics(self):
        averages = [self.get_average(sid) for sid in self.students]
        return {
            "class_average": sum(averages) / len(averages),
            "highest": max(averages),
            "lowest": min(averages)
        }
```

---

## Vorlesung 13: Game Programming

### Pygame Framework 🟡

#### Pygame Fundamentals
- [ ] **Pygame installation and setup** - Getting started with game development
- [ ] ⚠️ **Game window creation** - Setting up the display surface
- [ ] ⚠️ **Color systems** - RGB values and color constants
- [ ] **Coordinate systems** - Understanding screen coordinates

#### Event-Driven Programming
- [ ] ⚠️ **Event loop** - Main game loop structure
- [ ] ⚠️ **Event handling** - Responding to keyboard, mouse, and window events
- [ ] **Event types** - QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, etc.
- [ ] 🟡 **Real-time input** - Continuous key/mouse state checking

#### Code Example: Basic Game Structure
```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Game")
clock = pygame.time.Clock()

# Game variables
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle continuous input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 20:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - 20:
        player_y += player_speed

    # Clear screen
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, 20, 20))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Quit
pygame.quit()
sys.exit()
```

### Graphics and Game Development 🟡

#### Graphics Primitives
- [ ] **Drawing shapes** - Rectangles, circles, lines, polygons
- [ ] **Surface manipulation** - Creating and modifying surfaces
- [ ] **Image loading and display** - Working with sprite images
- [ ] **Text rendering** - Displaying text in games

#### Game Development Patterns
- [ ] ⚠️ **Game loop** - Update, render, timing cycle
- [ ] **Sprite management** - Game object representation
- [ ] **Collision detection** - Basic rectangular collision
- [ ] 🟡 **Game state management** - Menus, gameplay, game over states

#### Advanced Game Concepts
- [ ] **Animation techniques** - Frame-based animation
- [ ] **Sound integration** - Adding audio to games
- [ ] **Game mechanics** - Physics, scoring, levels
- [ ] 🔴 **Performance optimization** - Efficient rendering and updates

### Game Examples and Applications

#### Classic Games Implemented
- [ ] **Pong** - Two-player paddle game
- [ ] **15-Puzzle** - Sliding tile puzzle
- [ ] **4-Gewinnt (Connect Four)** - Strategy game
- [ ] **Mühle (Nine Men's Morris)** - Board game
- [ ] **Pacman** - Maze navigation game

#### Code Example: Pong Game (Simplified)
```python
class PongGame:
    """Simple Pong game implementation."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Paddle properties
        self.paddle_width, self.paddle_height = 15, 90
        self.paddle_speed = 5

        # Player positions
        self.player1_y = 300
        self.player2_y = 300

        # Ball properties
        self.ball_x, self.ball_y = 400, 300
        self.ball_dx, self.ball_dy = 5, 3
        self.ball_size = 15

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Player 1 controls (W/S)
        if keys[pygame.K_w] and self.player1_y > 0:
            self.player1_y -= self.paddle_speed
        if keys[pygame.K_s] and self.player1_y < 600 - self.paddle_height:
            self.player1_y += self.paddle_speed

        # Player 2 controls (UP/DOWN)
        if keys[pygame.K_UP] and self.player2_y > 0:
            self.player2_y -= self.paddle_speed
        if keys[pygame.K_DOWN] and self.player2_y < 600 - self.paddle_height:
            self.player2_y += self.paddle_speed

    def update_ball(self):
        # Move ball
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Ball collision with top/bottom
        if self.ball_y <= 0 or self.ball_y >= 600 - self.ball_size:
            self.ball_dy = -self.ball_dy

        # Ball collision with paddles
        # Left paddle
        if (self.ball_x <= 25 and 
            self.player1_y <= self.ball_y <= self.player1_y + self.paddle_height):
            self.ball_dx = -self.ball_dx

        # Right paddle
        if (self.ball_x >= 760 and 
            self.player2_y <= self.ball_y <= self.player2_y + self.paddle_height):
            self.ball_dx = -self.ball_dx

        # Reset if ball goes off screen
        if self.ball_x < 0 or self.ball_x > 800:
            self.ball_x, self.ball_y = 400, 300

    def render(self):
        self.screen.fill((0, 0, 0))

        # Draw paddles
        pygame.draw.rect(self.screen, (255, 255, 255), 
                        (10, self.player1_y, self.paddle_width, self.paddle_height))
        pygame.draw.rect(self.screen, (255, 255, 255), 
                        (775, self.player2_y, self.paddle_width, self.paddle_height))

        # Draw ball
        pygame.draw.rect(self.screen, (255, 255, 255), 
                        (self.ball_x, self.ball_y, self.ball_size, self.ball_size))

        pygame.display.flip()
```

---

## Vorlesung 14: Advanced Algorithms

### Computational Geometry 🔴

#### Fundamental Concepts
- [ ] 🔴 **Point representation** - Coordinates and point operations
- [ ] 🔴 **Distance calculations** - Euclidean distance in 2D space
- [ ] **Geometric primitives** - Points, lines, polygons
- [ ] **Coordinate transformations** - Rotation, scaling, translation

#### Advanced Geometric Algorithms
- [ ] 🔴 **Closest pair of points** - Finding minimum distance between points
- [ ] **Convex hull algorithms** - Finding the outer boundary of points
- [ ] **Line intersection** - Determining if and where lines cross
- [ ] **Point-in-polygon testing** - Spatial containment queries

#### Code Example: Closest Pair Problem
```python
import math
import random

def closest_pair_brute_force(points):
    """Find closest pair using brute force O(n²) approach."""
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

def closest_pair_divide_conquer(points):
    """Efficient O(n log n) divide and conquer solution."""

    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def closest_pair_rec(px, py):
        n = len(px)

        # Base case: brute force for small arrays
        if n <= 3:
            min_dist = float('inf')
            pair = None
            for i in range(n):
                for j in range(i + 1, n):
                    d = distance(px[i], px[j])
                    if d < min_dist:
                        min_dist = d
                        pair = (px[i], px[j])
            return pair, min_dist

        # Divide
        mid = n // 2
        midpoint = px[mid]

        pyl = [point for point in py if point[0] <= midpoint[0]]
        pyr = [point for point in py if point[0] > midpoint[0]]

        # Conquer
        left_pair, left_dist = closest_pair_rec(px[:mid], pyl)
        right_pair, right_dist = closest_pair_rec(px[mid:], pyr)

        # Find minimum of two halves
        if left_dist <= right_dist:
            min_dist = left_dist
            min_pair = left_pair
        else:
            min_dist = right_dist
            min_pair = right_pair

        # Check points near the dividing line
        strip = [point for point in py if abs(point[0] - midpoint[0]) < min_dist]

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    min_pair = (strip[i], strip[j])
                j += 1

        return min_pair, min_dist

    # Sort points by x and y coordinates
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])

    return closest_pair_rec(px, py)

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
```

### Randomized Algorithms 🔴

#### Randomization Concepts
- [ ] 🔴 **Probabilistic algorithms** - Using randomness for efficiency
- [ ] **Random number generation** - Creating pseudo-random sequences
- [ ] **Expected vs worst-case complexity** - Understanding probabilistic analysis
- [ ] **Monte Carlo methods** - Random sampling for approximation

#### Algorithm Analysis
- [ ] 🔴 **Asymptotic notation** - Big O, Omega, Theta notation
- [ ] **Best, average, worst case** - Comprehensive complexity analysis
- [ ] **Space complexity** - Memory usage analysis
- [ ] **Trade-offs** - Time vs space, accuracy vs efficiency

### Spatial Data Structures 🔴

#### Advanced Data Structures
- [ ] 🔴 **Quadtrees** - 2D space partitioning
- [ ] **KD-trees** - Multi-dimensional binary trees
- [ ] **Spatial hashing** - Efficient spatial queries
- [ ] **Range trees** - Multi-dimensional range queries

#### Applications
- [ ] **Collision detection optimization** - Efficient spatial queries in games
- [ ] **Geographic information systems** - Managing spatial data
- [ ] **Computer graphics** - Rendering optimization
- [ ] **Database indexing** - Multi-dimensional data indexing

---

## Quick Reference

### Essential Python Syntax 🟢

#### Variables and Types
```python
# Basic data types
integer = 42
floating = 3.14
string = "Hello, World!"
boolean = True
list_example = [1, 2, 3, 4]
dict_example = {"key": "value", "number": 42}
```

#### Control Structures
```python
# Conditional statements
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# Loops
for item in iterable:
    pass

while condition:
    pass
```

#### Functions
```python
def function_name(parameter1, parameter2="default"):
    """Function documentation."""
    return result
```

#### Classes
```python
class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter

    def method(self):
        return self.attribute
```

### Common Algorithms Complexity Reference 🟡

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| BST Search | O(log n) | O(log n) | O(n) | O(1) |
| Hash Table | O(1) | O(1) | O(n) | O(n) |

### Exam Preparation Checklist ⚠️

#### Must-Know Concepts
- [ ] ⚠️ Variable types and operations
- [ ] ⚠️ Control structures (if/else, loops)
- [ ] ⚠️ Function definition and calling
- [ ] ⚠️ List operations and methods
- [ ] ⚠️ Basic recursion
- [ ] ⚠️ Class definition and instantiation
- [ ] ⚠️ File I/O operations
- [ ] ⚠️ Binary search trees
- [ ] ⚠️ Inheritance and method overriding

#### Practice Problems
- [ ] Implement sorting algorithms
- [ ] Write recursive solutions
- [ ] Design classes with inheritance
- [ ] Solve tree traversal problems
- [ ] Create simple games with Pygame
- [ ] Implement data structures from scratch

### Study Tips

1. **Practice Coding**: Write code for each concept, don't just read about it
2. **Understand Complexity**: Know when and why to use different algorithms
3. **Debug Systematically**: Learn to read error messages and trace code execution
4. **Connect Concepts**: Understand how different topics relate to each other
5. **Build Projects**: Apply concepts in practical programming projects

---

## Summary

This study guide covers all major concepts from the EiP course. Use the checkboxes to track your progress and focus on areas where you need more practice. Remember that programming is learned by doing - make sure to implement the examples and solve practice problems for each topic.

Good luck with your studies! 🚀