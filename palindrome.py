input_string = (input("enter a string:"))
user_string = [input_string]
reverse_string = user_string[0][::-1]
if user_string[0] == reverse_string:
	print(f"given string is palindrom :{user_string[0]}")
else:
	print(f"given string is not palindrom : {user_string[0]}")
