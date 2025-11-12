list1=list(map(int,input("enter 1st:").split()))
list2=list(map(int,input("enter 2nd:").split()))
print("same length:",len(list1)==len(list2))
print("sum eqaul:",sum(list1)==sum(list2))
common=False
for x in list1:
    if x in list2:
        common=True
        break
print("common values present:",common)