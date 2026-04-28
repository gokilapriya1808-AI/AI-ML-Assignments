import re
vowels = ['a','e','i','o','u']
input_string = (input("enter a sentence:"))

for i in vowels:
	space = re.findall(i,input_string)
	print(f"count of vowel '{i}' is {len(space)}")
