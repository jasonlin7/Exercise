#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random as rand;

x = rand.randint(1, 3)
# 1=rock
# 2=paper
# 3=scissors

if x == 1:
    xx = "Rock"
elif x == 2:
    xx = "Paper"
elif x == 3:
    xx = "Scissors"


yy = input("Rock, Paper or Scissors?")

if yy.lower() == "rock":
    y = 1
elif yy.lower() == "paper":
    y = 2
elif yy.lower() == "scissors":
    y = 3
else:
    print("You didn't input correctly!")

if x == 3 and y ==1:
    print (f"Your {yy} beats my {xx}")
    print ("You win!")
elif x == 1 and y ==3:
    print (f"My {xx} beats your {yy}")
    print ("I win!")    
elif y > x:
    print (f"Your {yy} beats my {xx}")
    print ("You win!")
elif x > y:
    print (f"My {xx} beats your {yy}")
    print ("I win!")
elif x == y:
    print ("Tied")


# In[ ]:





# In[ ]:




