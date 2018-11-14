#Name: Chloe Ho
#Project8
#11/14/2018
'''
Given the following CFG and the LR Parsing table. Write a program to trace input strings
(1) (i+i)*i$
(2) (i*)$
'''
def LR_Parser(input_string, LR_table, production):
    print('Parsing: ' + input_string)
    stack = [0]  # start at state 0
    i = 0  # Keeps track of incoming inputs

    while True:
        top = stack[len(stack)-1]
        incoming_input = input_string[i]
        x = LR_table[top][incoming_input]

        if x[0] == 'S':
            stack.append(incoming_input)  
            stack.append(int(x[1:]))  # Enter the state by pushing it onto the stack
            i = i + 1
            
        elif x[0] == 'R': 
            right_side = production[int(x[1:])][1]  
            left_side = production[int(x[1:])][0] 
            pop_number = 2 * len(right_side)
            
            for j in range(0, pop_number):
                stack.pop()
            new_top = stack[len(stack) - 1]
            stack.append(left_side)
            stack.append(LR_table[new_top][left_side])

        elif x == 'A': 
            print('Input string ' + input_string + ' has been accepted')
            return 1
        else:  
            print('Input string: ' + input_string + ' is rejected')
            return -1

        print(stack)
        print(x)
        print('')


def main():
    string1 = '(i+i)*i$'
    string2 = '(i*)$'
    LR_table = {
        0:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 1,   'T': 2,   'F': 3},
        1:  {'i': 'a',  '+': 'S6', '-': 'S7', '*': 'a',  '/': 'a',  '(': 'a',  ')': 'a',  '$': 'A',  'E': 'a', 'T': 'a', 'F': 'a'},
        2:  {'i': 'a',  '+': 'R3', '-': 'R3', '*': 'S8', '/': 'S9', '(': 'a',  ')': 'R3', '$': 'R3', 'E': 'a', 'T': 'a', 'F': 'a'},
        3:  {'i': 'a',  '+': 'R6', '-': 'R6', '*': 'R6', '/': 'R6', '(': 'a',  ')': 'R6', '$': 'R6', 'E': 'a', 'T': 'a', 'F': 'a'},
        4:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 10,  'T': 2,   'F': 3},
        5:  {'i': 'a',  '+': 'R8', '-': 'R8', '*': 'R8', '/': 'R8', '(': 'a',  ')': 'R8', '$': 'R8', 'E': 'a', 'T': 'a', 'F': 'a'},
        6:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 11,  'F': 3},
        7:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 12,  'F': 3},
        8:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 'a', 'F': 13},
        9:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 'a', 'F': 14},
        10: {'i': 'a',  '+': 'S6', '-': 'S7', '*': 'a',  '/': 'a',  '(': 'a',  ')': 'S15','$': 'a',  'E': 'a', 'T': 'a', 'F': 'a'},
        11: {'i': 'a',  '+': 'R1', '-': 'R1', '*': 'S8', '/': 'S9', '(': 'a',  ')': 'R1', '$': 'R1', 'E': 'a', 'T': 'a', 'F': 'a'},
        12: {'i': 'a',  '+': 'R2', '-': 'R2', '*': 'S8', '/': 'S9', '(': 'a',  ')': 'R2', '$': 'R2', 'E': 'a', 'T': 'a', 'F': 'a'},
        13: {'i': 'a',  '+': 'R4', '-': 'R4', '*': 'R4', '/': 'R4', '(': 'a',  ')': 'R4', '$': 'R4', 'E': 'a', 'T': 'a', 'F': 'a'},
        14: {'i': 'a',  '+': 'R5', '-': 'R5', '*': 'R5', '/': 'R5', '(': 'a',  ')': 'R5', '$': 'R5', 'E': 'a', 'T': 'a', 'F': 'a'},
        15: {'i': 'a',  '+': 'R7', '-': 'R7', '*': 'R7', '/': 'R7', '(': 'a',  ')': 'R7', '$': 'R7', 'E': 'a', 'T': 'a', 'F': 'a'},
    }

    productions = {
        1: ['E', 'E+T'],
        2: ['E', 'E-T'],
        3: ['E', 'T'],
        4: ['T', 'T*F'],
        5: ['T', 'T/F'],
        6: ['T', 'F'],
        7: ['F', '(E)'],
        8: ['F', 'i'],
    }

    LR_Parser(string1, LR_table, productions)
    print('')
    LR_Parser(string2, LR_table, productions)
    
if __name__ == '__main__':
    main()
