"""
A NumPy array comes from the NumPy library (import numpy as np).

It is homogeneous (all elements must be the same type).

Optimized for numerical operations and large datasets.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# Multiply each element by 2 directly (vectorized)
arr2 = arr * 2
print(arr2)
# Simulate exam scores
scores = np.array([90, 75, 88, 60, 95])
# Calculate average
average = np.mean(scores)
# Find students with score > 80
top_scores = scores[scores > 80]

print("Average:", average)      
print("Top scores:", top_scores)



#Recursion is when a function calls itself to solve a smaller version of the same problem.
#Every recursive function needs a base case (to stop recursion), otherwise it goes into infinite calls.
#Fibonacci Sequence
def fibonacci(n):
    if n <= 1:   # Base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive calls

print(fibonacci(6))

#Sum of Natural Numbers
def sum_natural(n):
    if n == 0:   # Base case
        return 0
    else:
        return n + sum_natural(n-1)

print(sum_natural(5)) 

#Reverse a String
def reverse_string(s):
    if len(s) == 0:   # Base case
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello")) 

#Find Maximum in a List
def find_max(list):
    if len(list) == 1:   # Base case
        return list[0]
    else:
        return max(list[0], find_max(list[1:]))

print(find_max([3, 8, 2, 5, 10, 7]))





#Advantages
"""
Concise code: Write small functions in one line instead of full def.

Temporary use: Good for short, one-time functions.

Integration: Works well with functions like map(), filter(), sorted().

Readable in simple cases: Makes sense when the logic is short.
"""
#Disadvantages
"""
Very limited: Can only contain a single expression, not multiple statements.

Less readable: Becomes confusing if logic is complex.

Hard to reuse: No name unless assigned to a variable.

Not suitable for big functions: Better to use def.
"""
# Using lambda
add = lambda x, y: x + y
print(add(5, 3))  
#with map
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  
#with filter
numbers = [5, 10, 15, 20]
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(greater_than_10)  

#Make compare between def and lambada
#lambada
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(4))  
print(check_even(7)) 
#def
def check_even1(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even1(4))  
print(check_even1(7))  
#sorting
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# Sort students by score
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(sorted_students)














class Node:
    def _init_(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def print_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.next
        print("None")

    def print_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        
        while current_node:
            print(current_node.data, end=' <-> ')
            current_node = current_node.prev
        print("None")


doubly_linked_list = DoublyLinkedList()


doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)


print("İleri Yönlü:")
doubly_linked_list.print_forward()


print("\nGeriye Doğru:")
doubly_linked_list.print_backward()