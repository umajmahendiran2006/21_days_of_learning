string=["apple","banana","grape","kiwi","pineApple","watermelon"]
largest_word=string[0]
for i in string:
	if len(i)>len(largest_word):
		largest_word=i
print("largest_word:",largest_word)		