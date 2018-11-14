#Assignment 7 - part 2

def trace(words):
	index = 0
	stack = []
	stack.append('$')
	stack.append('S')

	while len(stack) > 0:
		top = stack.pop()

		if top == words[index]:
			print("Matched '{}'!, Stack:{}".format(words[index], stack))
			if words[index] == '$':
				print("Word is accepted")
				break
			index += 1

		if top == 'S':
			if words[index:index+2] == 'a=':
				stack.append('E')
				print("Matched '{}': Stack:{}".format(words[index:index+2], stack))
				index += 2
				continue
			else:
				print("Word is not accepted")
				break
		if top == 'E':
			if words[index] == '(' or words[index] == 'a' or words[index] == 'b':
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
			if words[index] == '(' or words[index] == 'a' or words[index] == 'b':
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
			elif words[index] == 'b':
				stack.append('b')
			elif words[index] == '(':
				stack.append(')')
				stack.append('E')
				stack.append('(')
				continue
			else:
				print("Word is not accepted")
				break

print("\na=(a+a)*b$")
trace('a=(a+a)*b$')
print("\na=a*(b-a)$")
trace('a=a*(b-a)$')
print("\na=(a+a)b$")
trace('a=(a+a)b$')

