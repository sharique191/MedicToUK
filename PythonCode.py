# This code automates the process of rephrasing questionbooks

import pandas as pd
import requests
import json

def change(a):                        # this function uses API to reframe the question
    key="a*********" # Key has been masked for confidentiality
    email="drarunavadhar@gmail.com"
    inp=a
    p={"email":email,"key":key,"input":inp,"rewrite_num":1,"uniqueness":1,"return_rewrites":"true"}
    r=requests.post("https://wai.wordai.com/api/rewrite",params=p)
    if r.status_code!=200:           # returning False for error rows
        return False
    r1=r.json()
    r2=r1["rewrites"]
    r2=r2[0]
    r2=r2.split('\n')
    r2=r2[0]
    return r2                          # function returns the rephrased string

a=pd.read_csv("1700Subjectwise 100 Rows - Sheet1.csv")  # a is pandas dataframe that loads original question set
c=a.copy()                                             # c is a copy of a.      We modify in c and do not change a
e=a.copy()                                              # e is also a copy of c meant to store error rows

l=len(c)
for i in range(0,l-1):
    e=e.drop(i)                     # drop every row in e except the first row to keep column names intact

z=0                                # maintaining z to append rows in e

                                                # l is No of columns in a
for i in range(0,l):                                    # we run this loop for l no of columns ie all columns
    k=c["Question"][i]                                         # Extracting Question from Column named "H" and storing in variable k 
    chng=change(k)
    if chng==False:
        e.loc[z]=c.loc[i]          # appending row in e 
        z+=1
        c["Question"][i]="*****Error*********"
    else:
        c["Question"][i]=chng                                 # Rephrasing the Question and saving it
        
e.reset_index(drop=True,inplace=True)  # reseting indexes of e  
c.reset_index(drop=True,inplace=True)  # reseting indexes of c
e=e.drop(0)                            # droping first row from e
e.reset_index(drop=True,inplace=True)
    
c.to_csv(r'C:\Users\Syed Mubashir\Desktop\export_dataframe.csv', index = False, header=True)
e.to_csv(r'C:\Users\Syed Mubashir\Desktop\error_dataframe.csv', index = False, header=True)
         # The above line exports the panda frame as .csv file in the given location
         # Kindly modify the path where you want to save the rephrased .csv file
         # Also you may change the file name. Here the file name is "export_dataframe.csv"
         # eg c.to_csv(r'Path\FileName.csv', index = False, header=True)
