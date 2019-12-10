  
import xlrd 


from numpy import dot
from numpy.linalg import norm

#location of the model video data
loc1 = ("C:/Users/Taha/Desktop/model_excel.xlsx")
wb1 = xlrd.open_workbook(loc1) 
sheet1 = wb1.sheet_by_index(0)

#location of user video data
loc2= ("C:/Users/Taha/Desktop/bad_input_excel.xlsx")
wb2 = xlrd.open_workbook(loc2) 
sheet2 = wb2.sheet_by_index(0)

answerList=[]

rows=sheet1.nrows if sheet1.nrows<sheet2.nrows else sheet2.nrows
cols=sheet1.ncols

list1=[]
list2=[]


for row in range(rows):
    for col in range(cols):
        list1.append(sheet1.cell_value(row,col))
        list2.append(sheet2.cell_value(row,col))
    
    cosine = dot(list1, list2)/(norm(list1)*norm(list2))
    cosine=round(cosine,2)
    answerList.append((10000-cosine*10000)%1000)
    #answerList.append(cosine)
    
print(answerList)
#print("hello")

import turtle  
  
t = turtle.Turtle() 

t.begin_fill() 
for i in answerList: 
    if i==300: 
        t.color('blue')
        t.begin_fill()
        t.circle(100)
        t.end_fill()  
    if i==700:
        t.color('green')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
    if i==400:
        t.color('yellow')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
    if i==500:
        t.color('red')
        t.begin_fill()
        t.circle(100)
        t.end_fill()  
    if i==600:
        t.color('orange')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
    if i==800:
        t.color('purple')
        t.begin_fill()
        t.circle(100)
        t.end_fill()

t.end_fill()      
turtle.done()