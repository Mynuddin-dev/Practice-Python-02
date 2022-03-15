import random
Upper = "ZXCVBNMASDFGHJKLQWERTYUIOP"
lower = "zxcvbnmasdfghjklqwertyuiop"
number = "123457890"
symbol = "!@#$%^&*()[]{}?~`"
all = Upper + lower + number + symbol
# length = input("Enter password Length :")
password = "".join(random.sample(all , 9))
print("Your Generated password is : " , password)
