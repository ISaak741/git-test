def add(x,y):
    # Said Implement Add function
    pass

def subtract(x,y):
    return x-y

def multiply(x,y):
    # Said Implement Multiply function
    pass
    #pass

def calculate(operation, x, y):
    match operation:
        case 'add': return add(x, y)
        case 'multiply': return multiply(x, y)
        case 'subtract': return subtract(x, y)