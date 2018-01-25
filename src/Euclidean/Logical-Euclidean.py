def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def maxDivider(width, height):
    width = checkForDivider(width)
    height = checkForDivider(height)
    
    return max(intersect(height, width))

def divide(x, y):
    if (y == 0):
        return
    return x//y if (x//y) * y==x else x/y

def checkForDivider(number):
    
    array = []
    for i in range(number):
        i += 1
        result = divide(number, i)
        if (isinstance(result, int)):
            array.append(i)
        if (i == number):
            return array
        
def main():
    print("Welcome to Euclidean algorithm solver!")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    width = int(input("Please insert the width: "))
    height = int(input("Please insert the height: "))
    
    result = maxDivider(width, height)
    print("We've got the results for the perfect square!")
    print("Width: {width}".format(width = result))
    print("Height: {height}".format(height = result))
    
if __name__ == "__main__":
    main()