#!/usr/bin/env python
# coding: utf-8

# In[3]:


#This is a program to find the area of rectangle
lenght=int(input("Enter the lenght of rectangle : "))
breath=int(input("Enter the breath of rectangle : "))
print("the area of rectangle is :",lenght*breath)


# In[14]:


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.
l=[]
for i in range(2000,3201):
    if(i%7==0and i%5!=0):
        l.append(str(i))
print(','.join(l))


# In[1]:


#Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name.
f_name=input("Enter first name : ")
l_name=input("Enter last name : ")
print(f_name[::-1],l_name[::-1])


# In[12]:


#Write a Python program to find the volume of a sphere with diameter 12 cm.
diameter=12.0
radius=diameter/2
area=(4.0/3.0)*3.14*(radius**3.0)
print("Area of sphere=",area)


# In[13]:


Task 2:
#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.
s=input()
l=list(map(int,s.split(",")))
print(l)


# In[15]:


for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
for i in range(1,5):
    for j in range(0,5-i):
        print("*",end=" ")
    print("\n")
        


# In[17]:


#Write a Python program to reverse a word after accepting the input from the user.
a=input()
print(a[::-1])


# In[40]:


s=input()
print(s[0:24],"\n     ",s[25:88],"!\n\t   ",s[88:127],"\n\t   ",s[127:])


# In[ ]:




