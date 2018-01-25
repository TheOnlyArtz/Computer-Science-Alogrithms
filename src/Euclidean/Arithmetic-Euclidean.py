def arth(a, b):
     if (b == 0):
            return a
    return arth(b, a % b)

def main():
    print("Welcome to Euclidean algorithm solver!")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    width = int(input("Please insert the width: "))
    height = int(input("Please insert the height: "))
    
    result = arth(width, height)
    print("We've got the results for the perfect square!")
    print("Width: {width}".format(width = result))
    print("Height: {height}".format(height = result))
    
if __name__ == "__main__":
    main()
