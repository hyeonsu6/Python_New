#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# (ai) C:\kd\ws_python\core>python Argu1.py A 3000
#                                       0   1 2  
import sys

print(type(sys.argv)) # <class 'list'>

fname = sys.argv[0]    # 파일명
area = sys.argv[1]     # 지역
pay = int(sys.argv[2]) # 희망 연봉

print('fname:', fname)

if area == 'A':
    print('지역: 서울')
elif area == 'B':
    print('지역: 경기')
elif area == 'C':
    print('지역: 인천')
else:
    print('지역 결정 안됨')

print('연봉:', pay)    


# In[3]:


get_ipython().system('jupyter nbconvert --to python Argu1.ipynb')

