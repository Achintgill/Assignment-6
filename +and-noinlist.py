num=[234,-45,45,-435,-4363,-436,3467,896,568,22225,67573]
pos_num=0
neg_num=0
for i in num:
    if i>0:
        pos_num+=1
    elif i<0:
        neg_num+=1
print("Positive Numbers: ", pos_num)
print("Negative Numbers: ", neg_num)
