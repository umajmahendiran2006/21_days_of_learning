words = ["eat","tea","tan","ate","nat","bat"]

anagrams = {}

for i in words:
    key = "".join(sorted(i))   
    
    if key in anagrams:
        anagrams[key].append(i)
    else:
        anagrams[key] = [i]

print(list(anagrams.values()))