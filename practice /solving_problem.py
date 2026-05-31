""" 1. Longest Substring Without Repeating Characters
Input: "abcabcbb"
Output: 3
"""
# Input= "abcabcbb"
# b = set(Input)
# print(len(b))

"""2. Group Anagrams
Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
 ['eat', 'tea', 'ate'],
 ['tan', 'nat'],
 ['bat']
]"""

# Input=["eat", "tea", "tan", "ate", "nat", "bat"]
# group ={}
# for i in Input:
#    key = ''.join(sorted(i))
   
#    if key not in group:
#        group[key]=[]
#    group[key].append(i)
# result = list(group.values())
# print(result)

"""Valid Parentheses
Input: "{[()]}"
Output: True

Input: "{[(])}"
Output: False"""

# Input = input("ente something :")

# if Input=="{[()]}":
#     print(True)
# else:
#     print(False)


"""4. Rotate Matrix 90°
Input:
1 2 3
4 5 6
7 8 9

Output:
7 4 1
8 5 2
9 6 3"""

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# transposed = list(zip(*matrix))
# rotated = [list(row[::-1]) for row in transposed]

# for i in rotated:
#     print(*i)

"""5. Sudoku Validator
Given a 9×9 Sudoku board, check if it's valid"""
# def is_valid_sudoku(board):
#     row = [set() for _ in range(9)]
#     cols = [set() for _ in range(9)]
#     boxes = [set() for _ in range(9)]
    
#     for r in range(9):
#         for c in range(9):
#             val = board[r][c]
            
#             if val == ".":
#                 continue
            
#             # check row
#             if val in row[r]:
#                 return False
#             row[r].add(val)
            
#             # check column
#             if val in cols[c]:
#                 return False
#             cols[c].add(val)
            
#             # check 3x3 box
#             box_index = (r // 3) * 3 + (c // 3)
            
#             if val in boxes[box_index]:
#                 return False
#             boxes[box_index].add(val)
    
#     return True

# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]

# print(is_valid_sudoku(board))

"""8. Library Management System
Using OOP:
Classes:
Book
Member
Library

Features:
Issue book
Return book
Search book
Track availability"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.book_id}: {self.title} by {self.author} [{status}]"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []

    def __str__(self):
        return f"{self.member_id}: {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ---------- Book Management ----------
    def add_book(self, book):
        self.books[book.book_id] = book

    def search_book(self, keyword):
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    # ---------- Member Management ----------
    def add_member(self, member):
        self.members[member.member_id] = member

    # ---------- Issue Book ----------
    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            return "Book not found"

        if member_id not in self.members:
            return "Member not found"

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_issued:
            return "Book already issued"

        book.is_issued = True
        member.issued_books.append(book)
        return f"Book '{book.title}' issued to {member.name}"

    # ---------- Return Book ----------
    def return_book(self, book_id, member_id):
        if book_id not in self.books or member_id not in self.members:
            return "Invalid book or member ID"

        book = self.books[book_id]
        member = self.members[member_id]

        if book not in member.issued_books:
            return "This member did not issue this book"

        book.is_issued = False
        member.issued_books.remove(book)
        return f"Book '{book.title}' returned successfully"

    # ---------- Show Books ----------
    def show_books(self):
        for book in self.books.values():
            print(book)
            
            
library = Library()

# Add books
library.add_book(Book(1, "Python Basics", "John Doe"))
library.add_book(Book(2, "Data Structures", "Mark Allen"))
library.add_book(Book(3, "Machine Learning", "Andrew Ng"))

# Add members
library.add_member(Member(101, "Sujan"))
library.add_member(Member(102, "Asha"))

# Show all books
print("All Books:")
library.show_books()

# Issue book
print(library.issue_book(1, 101))

# Search book
print("\nSearch Result:")
for b in library.search_book("python"):
    print(b)

# Return book
print(library.return_book(1, 101))

# Final status
print("\nFinal Books:")
library.show_books()
        