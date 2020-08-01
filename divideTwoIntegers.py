def divide(dividend, divisor):
    neg = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = div = abs(divisor)
    count = 1
    ans = 0
    while dividend >= divisor:
        dividend -= div
        ans += count
        count += count
        div += div
        if dividend < div:
            div = divisor
            count = 1

    if neg:
        return max(-ans, -2147483648)
    else:
        return min(ans, 2147483647)


dividend = 16
divisor = -3
print(divide(dividend, divisor))
