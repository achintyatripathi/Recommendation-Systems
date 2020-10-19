# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:00:45 2020

@author: Neetu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:04:32 2020

"""
#final user click data for 1000 users and 2916 articles
import random
import numpy as np
from sklearn.mixture import GaussianMixture
import pandas as pd
#import matplotlib.pyplot as plt

###data generation for clicks
num_of_users=1000
ids=list(range(1,num_of_users+1))
session_id=np.random.poisson(4,num_of_users)
#session_id=[]  ##avg no. of visits=3
#session_id=[1 if session1_id==0 else session1_id]
for i in range(len(session_id)):
    if session_id[i] > 0: # If an element with index i is greater than 0,
        session_id[i] = session_id[i] # then it is replaced by 1.
    elif session_id[i] == 0: # If an element with index i is less than 0,
        session_id[i] = 1         
total_session=np.sum(session_id)
total_articles=2916##pick size of final combined articles web scrap
articles_offer=np.random.choice(range(total_articles),total_session*10)#10 articles in each session
click=np.random.binomial(1,.5,total_session*10) 


mu = [40, 76, 115]
sigma = [6, 9, 11]
p_i = [0.2, 0.5, 0.3]
n = total_session*10

time = []
for i in range(n):
    z_i = np.argmax(np.random.multinomial(1, p_i))
    x_i = np.random.normal(mu[z_i], sigma[z_i])
    time.append(x_i)
    
user_id_new=np.repeat(ids,session_id*10)

sess=[]
for i in range(len(session_id)):
    ses_rep=list(np.repeat(range(1,session_id[i]+1),10))
    sess.append(ses_rep)
session=list(sess)
import itertools
session_ids = list(itertools.chain.from_iterable(session)) #flat list from list of list
#article_str=char(articles_offer) 

arti=map(str,articles_offer)
article_str=list(arti)
nn={'user_id':user_id_new,'session':session_ids,'article_id':article_str,'clicked_or_not':click,'time':time}
data_rough=pd.DataFrame(nn)
#data_rough['time_spent']=[time if data_rough['clicked_or_not']==1 else 0]
time_new=np.zeros((data_rough.shape[0],1))
for i in range(data_rough.shape[0]):
    if data_rough['clicked_or_not'][i]==1:
        time_new[i]= data_rough['time'][i]
    else:
        time_new[i]=0
data_rough['time_spent']=time_new
final_user_click_data=data_rough[['user_id','session','article_id','clicked_or_not','time_spent']]
rating=[]
for i in range(final_user_click_data.shape[0]):
    if final_user_click_data['time_spent'][i]!=0:
        r=np.random.randint(1,6)
        rating.append(r)
    else:
        r=0
        rating.append(r)
len(rating)       
final_user_click_data['rating_article']=rating
final_user_click_data.to_csv("C:\\Users\\Neetu\\Desktop\\study material DS\\sabudh_assignment\\machine learning\\news recommender system group assignment\\user_click_data.csv")
