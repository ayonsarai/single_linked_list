#Sarai Ayon 
#4/16/2024
#CS240 Data Structures HW 1: Linked Lists
#Singly Linked List


from typing import List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

file_path = r"C:\Users\Sarai Ayon\OneDrive - Whatcom Community College\Spring 2024\CS240 Database Structure & Algorithms\Week 2 Linked List\numbers-2.txt"

linked_list = LinkedList()

with open(file_path, 'r') as f:
    for num in f.read().split():
        linked_list.append(int(num))
