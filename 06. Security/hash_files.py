#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib as hsh


# In[2]:


SIZE=3
hasher=hsh.new('sha512')


# In[3]:


with open("testfile.txt","r") as f:
    buffer=f.read(SIZE).encode('utf-8')
    while len(buffer)>0:
        hasher.update(buffer)
        buffer=f.read(SIZE).encode('utf-8')
print(hasher.hexdigest()) 


# In[ ]:




