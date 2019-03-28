def isharshad(number):
    sum1 = 0
    variable = number
    digit = 0
    while number > 0:
        digit = number % 10
        sum1 = sum1 + digit
        number = number // 10
    if variable % sum1 == 0:
        return (True,sum1)
    else:
        return (False, sum1)

numbertosum = int (input ('Enter the number'))
flag, sumofnumber = isharshad(numbertosum)
if flag == True:
    print("It is harshad number.")
    print("Sum is: ", sumofnumber)
else:
    print("It is not harshad number")
    print("Sum is: ", sumofnumber)
