sentence=input("enter a sentence: ")
words=sentence.split()
num_words=len(words)
num_char=len(sentence)
vowels="aeiouAEIOU"
vowel_count=0
for i in sentence:
	if i in vowels:
		vowel_count+=1
print("number of words: ",num_words)
print("number of characters: ",num_char)
print("number of vowels: ",vowel_count)		