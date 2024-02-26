# this class cleans up the input to make it analyzable
class expression:
    def __init__(self, exp):
        self.exp = exp
        self.split_up = []

    # returns parsed expression
    def get_parsed(self):
        self.parse()
        return self.split_up

    # turns expression into analyzable list
    def parse(self):
        temp = ''
        operations = ['(', ')', '+', '-', '/', '*']

        for i in self.exp:
            if i not in operations:
                temp = temp + i
            else:
                self.split_up.append(temp)
                self.split_up.append(i)
                temp = ''

        self.split_up.append(temp)
        for i, x in enumerate(self.split_up):
            if x == '':
                self.split_up.remove(x)

# this class solves things in parentheses
class parentheses_cleared:
    def __init__(self, exp):
        self.exp = expression(exp)
        self.parsed = self.exp.get_parsed()
    
    # goes through parsed expression and solves the first thing in parentheses
    def parentheses(self):
        temp = ''
        inside = 0
        index = None
        for j, i in enumerate(self.parsed):
            if i == '(':
                inside += 1
                index = j
            if i == ')':
                inside += 1
                result = eval(temp[1:])
                self.parsed[index] = result
                self.rem(index + 1, j)
                break
            if not inside % 2 == 0:
                temp = temp + i

    # helper function for parentheses
    def rem(self, start, end):
        while start <= end:
            self.parsed.pop(end)
            end -= 1

    # puts everything together
    def clean(self):
        while '(' in self.parsed:
            self.parentheses()
        return self.parsed

# the main math one
class analyzer:
    def __init__(self, exp):
        # to fix a bug
        if ')' in exp:
            self.exp = exp
        else:
            self.exp = '(' + exp + ')'
    
    # solves all parentheses
    def first(self):
        if '(' in self.exp:
            cleaned = parentheses_cleared(self.exp)
            self.exp = cleaned.clean()
    
    # solves first instance of multiplication
    def second(self):
        if '*' in self.exp:
            for i, k in enumerate(self.exp):
                if k == '*':
                    thing = str(self.exp[i-1]) + str(self.exp[i]) + str(self.exp[i+1])
                    res = eval(thing)
                    self.exp[i-1] = res
                    self.exp.pop(i+1)
                    self.exp.pop(i)
                    break

    # solves first instance of division
    def third(self):
        if '/' in self.exp:
            for i, k in enumerate(self.exp):
                if k == '/':
                    thing = str(self.exp[i-1]) + str(self.exp[i]) + str(self.exp[i+1])
                    res = eval(thing)
                    self.exp[i-1] = res
                    self.exp.pop(i+1)
                    self.exp.pop(i)
                    break

    # solves first instance of addition
    def fourth(self):
        if '+' in self.exp:
            for i, k in enumerate(self.exp):
                if k == '+':
                    thing = str(self.exp[i-1]) + str(self.exp[i]) + str(self.exp[i+1])
                    res = eval(thing)
                    self.exp[i-1] = res
                    self.exp.pop(i+1)
                    self.exp.pop(i)
                    break

    # solves first instance of subtraction
    def fifth(self):
        if '-' in self.exp:
            for i, k in enumerate(self.exp):
                if k == '-':
                    thing = str(self.exp[i-1]) + str(self.exp[i]) + str(self.exp[i+1])
                    res = eval(thing)
                    self.exp[i-1] = res
                    self.exp.pop(i+1)
                    self.exp.pop(i)
                    break

    def analyze(self):
        self.first()
        if '*' in self.exp:
            while '*' in self.exp:
                self.second()
        if '/' in self.exp:
            while '/' in self.exp:
                self.third()
        if '+' in self.exp:
            while '+' in self.exp:
                self.fourth()
        if '-' in self.exp:
            while '-' in self.exp:
                self.fifth()
    
    def solve(self):
        self.analyze()
        result = str(self.exp[0])
        if result[-2:] == '.0':
            print(result[:-2])
        else:
            print(result)

def main():
    x = input("Enter the expression (no blank, no decimals): ")
    operation = analyzer(x)
    operation.solve()

main()