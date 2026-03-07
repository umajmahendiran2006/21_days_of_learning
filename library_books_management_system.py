books=['python','c','c++','java','javascript','data structures']
print("books available in library is:")
for i in books:
	print(i)
choice=input("return or borrow the book: ")
if choice=="borrow":
	book=input("enter the book name: ")
	if book in books:
		books.remove(book)
		print("book borrowed successfully")
	else:
		print("book is not avilable")	
elif choice=="return":
	book=input("enter the book name")
	books.append(book)
	print("book returned successfully")
print("updated book list is :",books)			