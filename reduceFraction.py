def reduceFraction(numerator, denominator):
    def gcd(a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
    if denominator == 0:
        print("integer division by zero!")
    greatest = gcd(numerator, denominator)
    numerator = int(numerator/greatest)
    denominator = int(denominator/greatest)
    print("The lowest terns if the fraction is: ", str(numerator), "/", str(denominator))

number  = str(input("Enter a fraction: "))
num, den = number.split('/')
num = int(num)
den = int(den)
reduceFraction(num, den)
