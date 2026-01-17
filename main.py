def add(x,y):
    # Said Implement Add function
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y
def divade(x,y):
    if(y==0):
        return 'non'
    return x/y

def calculate(operation, x, y):
    match operation:
        case 'add': return add(x, y)
        case 'multiply': return multiply(x, y)
        case 'subtract': return subtract(x, y)