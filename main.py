import math, random

def getOTP(n):
    digits = '0123456789'
    otp=""
    for i in range(n):
        otp += digits[math.floor(random.random() * 10)]
    return f'your {n} digit otp is {otp}'

if __name__ == "__main__":
    while True:
        otplen = int(input('Enter otp length : '))
        print(f'{getOTP(otplen)}')
