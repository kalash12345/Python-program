#Assigning Elements to different lists
a=7
b=[1,2,3,4,5,6,7]
c=[6,90,45,23,-45]
l1=[]
for i in range(a):
    x=int(input("Enter a value : "))
    l1.append(x)
print("List 1: " , l1)
y=b.insert(2,"Rock")
print("List 2 : " , b)
c.extend(b)
print("List 3 : " , c)

#Accessing elements from a tuple
tup=(1,2,3,3,5,6,77,"String",-343,"Stack")
print("Tuple 1 : " , tup)
print(tup[5])
print(tup[2:11])
print(tup[4: :-2])
print(tup[-3:-10:-1])
          
#Deleting different dictionary elements
Dic = {"Name":"Ram","Class":"XII","Age":17,"Address":"Delhi"}
print("Dictionary 1 : " , Dic)
x= Dic.pop("Address")
print(Dic)
del Dic["Class"]
print(Dic)
