#probelem1
list1=[12,34,26,22,19]
list2=[15,16,17,18,19]
comblist=list1+list2
print(comblist)
comblist.sort(reverse=True)
print(comblist)
print("highest_value =", comblist[0])
print("lowest_value =", comblist[-1])


# #problem2
data=('Jay','HITAM',20)
print(data)
print("my name is",data[0],",I study at",data[1],",I am ",data[2],"years old" )


#problem3
numbers=[]
for i in range(5):
    num=int(input(f"Enter a number{i+1}: "))
    numbers.append(num)
print(numbers)
actualset=set(numbers)
print(actualset)
print("No. of unique nums entered by user are",len(actualset))

#problem4
teledirec={}
for i in range(3):
    name=input("Enter name:")
    number=int(input("Enter number:"))
    teledirec[name]=number
query=input("enter name to search:")
if query in teledirec:
    print("Name =",query,"number=",teledirec[query] )
else:
    print("Name not found")