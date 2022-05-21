# MedicToUK
Assignment on Reframing Question-Bank

import docx
import requests as rq
import json

def change(a):                        # this function uses API to reframe the question
    key="a35281adb8b0bf2e80679c9cce0d032b"
    email="drarunavadhar@gmail.com"
    inp=a
    p={"email":email,"key":key,"input":inp,"rewrite_num":1,"uniqueness":1,"return_rewrites":"true"}
    r=requests.post("https://wai.wordai.com/api/rewrite",params=p)
    r1=r.json()
    r2=r1["rewrites"]
    r2=r2[0]
    r2=r2.split('\n')
    r2=r2[0]
    return r2
    

d=docx.Document('Original.docx')        # importing the original question-bank
p=d.paragraphs                         # separating the paragraphs         

for i in p:                            # removing extra paragraphs or empty paragraphs
    if i.text==None or i.text=="\n" or i.text=='' or i.text==" ":
        p.remove(i)
        
d2=docx.Document()                      # creating new blank file                          

for i in p:                             # copying everything from original file to new file
    d2.add_paragraph(i.text)

p2=d2.paragraphs

a=p[2].text                            # extracting the question
p2[2].text=change(a)                   # reframing the question and puting that in new file    

a=p[12].text                           ## Note: the index 2,12 has to be decided based on number of options
p2[12].text=change(a)

d2.save("RePhrased.docx")               # Exporting and Saving the Reframed Question-Bank
