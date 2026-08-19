#list of square values between 1-1000
num=list(range(1,1001,1))
for i in num:
    if i*i in num:
        print(i*i)
