'''
Custom Linked List implementation.
'''


class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'(DATA: {self.data} | NEXT: {self.next})'


class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        return f'| Start: {self.start} |'      
