#Chloe Ho
#Assignment 7
#write a program to trace input strings. show the content of the stack after each match

def trace(words):
	stack = []
	index = 0

	stack.append('$')
	stack.append('E')

	while len(stack) > 0:
		top = stack.pop()

		if top == words[index]:
			print("Match '{}': Stack:{}".format(words[index], stack))
			if words[index] == '$':
				print("Word is accepted")
				break
			index += 1

		if top == 'E':
			if words[index] == 'a':
				stack.append('Q')
				stack.append('T')
				continue
			elif words[index] == '(':
				stack.append('Q')
				stack.append('T')
				continue
			else:
				print("Word is not accepted")
				break
		elif top == 'Q':
			if words[index] == '+':
				stack.append('Q')
				stack.append('T')
				stack.append('+')
				continue
			elif words[index] == '-':
				stack.append('Q')
				stack.append('T')
				stack.append('-')
				continue
			elif words[index] == ')' or words[index] == '$':
				continue
			else:
				print("Word is not accepted")
				break
		elif top == 'T':
			if words[index] == 'a':
				stack.append('R')
				stack.append('F')
				continue
			elif words[index] == '(':
				stack.append('R')
				stack.append('F')
				continue
			else:
				print("Word is not accepted")
				break
		elif top == 'R':
			if words[index] == '+' or words[index] == '-' or words[index] == ')' or words[index] == '$':
				continue
			elif words[index] == '*':
				stack.append('R')
				stack.append('F')
				stack.append('*')
				continue
			elif words[index] == '/':
				stack.append('R')
				stack.append('F')
				stack.append('/')
				continue
			else:
				print("Word is not accepted")
				break
		elif top == 'F':
			if words[index] == 'a':
				stack.append('a')
				continue
			elif words[index] == '(':
				stack.append(')')
				stack.append('E')
				stack.append('(')
				continue
			else:
				print("Word is not accepted")
				break
print("\n(a+a)*a$")
trace('(a+a)*a$')
print("\na*(a/a)$")
trace('a*(a/a)$')
print("\n(a+a)$")
trace('a(a+a)$')
