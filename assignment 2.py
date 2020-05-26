#!/usr/bin/env python
# coding: utf-8

# In[36]:


#Task 1:
#Write a Python Program to implement your own myreduce() function which works exactly like
#Python's built-in function reduce()
def my_reduce(fun,seq):
    f=seq[0]
    for i in seq[1:]:
        a=fun(f,i)
        f=a
    return a
def mul(a,b):
    return a*b
print(my_reduce(mul,[1,2,3,2,5]))


# In[37]:


#Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True
def myfilter(func,seq):
    for i in seq:
        if(func(i)==True):
            yield i    
adults = myfilter(myFunc, ages)
for x in adults:
  print(x)


# In[38]:


#Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
w="ACADGILD"
l=[]
for i in w:
    l.append(i)
print(l)
x="xyz"
l=[]
for i in x:
    for j in range(1,4):
        l.append(i*j)
print(l)
w=[1,2,2,4]
l=[]
for i in w:
    for j in x:
        l.append(j*i)
print(l)
l=[]
for i in range(2,5):
    for j in range(0,3):
        l.append([j+i])
print(l)
l=[]
for i in range(2,6):
        l.append([j+i for j in range(0,4)])
print(l)
l=[]
for i in range(1,4):
    for j in range(1,4):
        l.append((j,i))
print(l)


# In[39]:


#Implement a function longestWord() that takes a list of words and returns the longest one.
l=['abc','abcd','abcde','avd','asxasx','sa']
def longestWord(seq):
    lw=seq[0]
    for i in seq:
        if(len(lw)<len(i)):
            lw=i
    return lw
print("The longest word of sequence is:%s"%(longestWord(l)))


# In[40]:


#Task 2:
#Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula. area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parent
#class and function to calculate the area should be defined in subclass.
class triangle:
    def insert(self):
        print("Enter the sides of triangle")
        self.a=float(input("Enter 1st side"))
        self.b=float(input("Enter 2nd side"))
        self.c=float(input("Enter 3rd side"))
class area(triangle):
    def tri_area(self):
        s=(self.a+self.b+self.c)/2
        a=((s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        print("Area is:",a)
tri=area()
tri.insert()
tri.tri_area()
        
        


# In[41]:


#Write a function filter_long_words() that takes a list of words and an integer n and returns the list
#of words that are longer than n.
def filter_long_words(n,seq):
    l=[]
    for i in seq:
        if(len(i)>n):
            l.append(i)
    return l
print(filter_long_words(5,['scsx','jshdcih','sjsjs','sxs']))
    


# In[42]:


#Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words.
seq=['sds','s','xc']
l=list(map(lambda x : len(x),seq))
print(l)


# In[44]:


#Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
#a vowel, False otherwise.
def check_vowe(ch):
    if(ch==('a' or 'e' or 'i' or 'o' or 'u')):
        return True
    else:
        return False
x=input("enter a character")
print(check_vowe(x))


# In[ ]:





# In[ ]:




