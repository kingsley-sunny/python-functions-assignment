import datetime 
date = d atetime.datetime.now()

name = input('what is your name: \n')
admin = ['sunny', 'tony', 'mary']
adminPassword = ['sun', 'ton', 'maryj']

if name in admin:
	password = input('what is your password: \n')
	userId = admin.index(name)
	
	if password == adminPassword[userId]:
		print(f' Welcome {name}')
		print ('''

''')
		print(f' Time logged in:  {date}')
		print ('''

''')
		print('This are the following options')
		print('1.   withdraw')
		print('2.   Deposit')
		print('3.   Complain')
		print ('''

''')
		option = int(input('Choose any option \n'))
		if option == 1:
			withdraw = int(input('How much will you like to withdraw \n'))
			print ('''
''')
			print(' Take your cash')
			print('💵' * (withdraw / 1000))
			
		elif option == 2:
			deposit = input('How much will you like to deposit \n') 
			print ('''
''')
			print('current balance')
		
		elif option == 3:
			complaint = input('What issue will you like to report \n')
			print ('''
''')
			print('Thank you for contacting us')
			
		else:
			print('Choose the number that falls with your option')
	else:
		print('your password is not correct')
else: 
	print('Your name is not correct')


print ('''

''')

print ('''
''')
 
