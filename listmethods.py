#printing an initial list
items=['fwr','evg','fb','rw','GVWE','ERG','aewvg']
print("Initial list: ",items)
#1. append
items.append("cherry")
print("After append(): ",items)
#2. insert
items.insert(1,2)
print("After insert(1): ",items)
#extend
items.extend([50,60])
print("After extend: ",items)
pos=items.index(fwr)
print("After index: ",items)
items.reverse()
print("After reverse(): ", items)
items.sort()
print("After sort() : ", items)
items.clear()
print("After clear(): ",items)
