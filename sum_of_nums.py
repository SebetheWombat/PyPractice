'''sum_up() returns the sum of all decimal numbers in a given string.
If there are no decimal numbers it informs the user'''

def sum_up():
    alphaNum = input("Give me something to work with! ")
    sumUp = 0
    nonInts = ""
    for i in alphaNum:
        try:
            sumUp += int(i)
        except ValueError:
            nonInts += i
            continue
    if len(nonInts) == len(alphaNum):
        print("There were no numbers in your string")
    else:
        print(sumUp)

sum_up()
