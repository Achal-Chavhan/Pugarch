#1.Reverse a string

s=input("Enter a string: ")

rev=s[::-1]

print("The reversed string is:",rev)

#2. Check if a string is palindrome or not

s=input("Enter a string: ")

if s == s[::-1]:
    print("Is a Palindrome")
else:
    print("Is not a Palindrome")

#3.Find the largest Number in a list

numbers = [10, 25, 14, 18, 12]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest:", largest) 

#4.Find second largest number in a list

numbers = [10, 25, 14, 18, 12]
second_largest = numbers[0]

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("Second largest:", second_largest)

#5.Remove duplicates from a list

numbers = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(unique_numbers)

#6.Missing a number in a list

numbers = [1, 2, 4, 5]
missing = []

for i in range(1, len(numbers) + 1):
    if i not in numbers:
        missing.append(i)

print("Missing numbers:", missing)

#7.Duplicate numbers in a list

numbers = [1, 2, 3, 4, 1, 5]
duplicate = None

for i in range(1, len(numbers) + 1):
    if numbers.count(i) > 1:
        duplicate = i
        break 

print("Duplicate numbers:", duplicate)


#8.Count the character frequency in a string

s = input("Enter a string: ")

char_freq = {}

for ch in s:
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1

print("Character frequencies:", char_freq)

#9.First non-repeating character in a string

s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character:", ch)
        break

#10.Merged sorted arrays

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged = sorted(arr1 + arr2)
print("Merged sorted array:", merged)

#11.common elements in two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)

#12.Stack

stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} to stack")

def pop():
    if not stack:
        print("Stack is empty")
        return None
    item = stack.pop()
    print(f"Popped {item} from stack")
    return item

push(15)
push(25)
pop()

#13.Queue

queue = []

def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item} to queue")

def dequeue():
    if not queue:
        print("Queue is empty")
        return None
    item = queue.pop(0)
    print(f"Dequeued {item} from queue")
    return item

enqueue(10)
enqueue(20)
dequeue()

#14.Maximum subarray sum

numbers = [-2,1,-3,4,-1,2,1,-5,4]
current_sum = 0
max_sum = numbers[0]

for n in numbers:
    current_sum += n 
    if current_sum > max_sum:
        max_sum = current_sum 
    if current_sum < 0:
        current_sum = 0

print("Maximum subarray sum:", max_sum) 

#15.Sorting without using built_in sorting

numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted array:", numbers)
