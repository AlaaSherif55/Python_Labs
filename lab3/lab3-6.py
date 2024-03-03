def divide(dividend, divisor):
    if divisor == 1:
        return dividend
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    positive_result = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    while dividend >= divisor:
        multiple = divisor
        count = 1
        while multiple >= (-(2**31) >> 1) and dividend <= (multiple << 1):
            multiple <<= 1
            count <<= 1
        quotient += count
        dividend -= multiple
    return quotient if positive_result else -quotient

print(divide(10, 3))