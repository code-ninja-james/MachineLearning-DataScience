#password checker
username=input('what is your username?')
password=input('what is your password?')

password_length=len(password)
hidden_password='*'*password_length
username_capital=username.capitalize()

print(f'{username_capital} , your password ,{hidden_password}, is {password_length} characters long')