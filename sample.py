# num = int(input('enter the num:'))
# n =[]
# for i in range(num):
#     ni = input('enter the string:')
#     n.append(ni)
    

# letter =[]
# for i in range(len(n)):
#     k = len(n[i])
#     if k % 2 != 0:
#         letter.append(n[i])
        
# if len(letter) > 0:
#     max_letter=[]
#     for i in letter:
#         k = len(i)
#         max_letter.append(k)
#     k = max(max_letter)
#     l =max_letter.index(k)
#     print(letter[l])
# else:
#     print('Better luck next time')

# k =['hi','hello','selja','karthi'] 
# print(max(k))     

# n = int(input("Enter number of strings : "))
# s = input("Enter Your String Here : ")
# l = s.split()
# if len(l) == n:
#     l2 = []
#     for i in l:
#         if len(i) % 2 != 0:
#             l2.append(i)
#     if len(l2) > 0:
#         m = max(l2)
#         print(m)
#     else:
#         print("better luck next time")
# else:
#     print("Given number and string words doesnt match")
    
# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))
# s,a=0,0
# for i in arr:
#     s=s+i   
#     if(s<1):
#         a=a+(-1*s)+1 
#         s=1 
# print(a)

n=int(input())
ar=input()
sorted(ar,reverse=True)
br=[]
s=0 
aa=[]
for i in ar:
    aa.append(int(i))
 
su=sum(aa)
while(s<=su):
    s+=(aa[0])
    su=su-(aa[0])
    br.append(aa.pop(0))
print(sum(br))