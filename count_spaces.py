import re
input_string = (input("enter a sentence:"))
space = re.findall('\s+',input_string)
print(f"Given sentence contains {len(space)} spaces")
