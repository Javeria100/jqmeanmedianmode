import csv
import pandas as pd
import plotly.express as px
from collections import Counter
#now to open my data file which is in csv (comma seperated value) format

with open("SOCR-HeightWeight.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

# so here i opened a file as f, assigned it a reader and then asked to save the data in form of list in the variable file_data

# now for any mean median or mode my data is in the form of a list, i will only let the data be there and remove the header. so the 0th row should be removed

file_data.pop(0)
#print(file_data)
#if you print the above you will notice there are multiple lists which got created,lets append and sort it nicely in a new list
new_data=[]
for i in range(len(file_data)):
    n=file_data[i][1]
    new_data.append(float(n))
#so here i have used a for loop, put in the range which is the length of my file_data.Then since my previous multiple list were split i ran the for loop over them and got them to be saved in a new list
#print(n)
#print(new_data)
#now data looks better in the new list, lets move on for the mean

a=len(new_data)
total=0

for x in new_data:
    total= total+x
mean= total / a
print( "the mean is " + str(mean))

#so i ran another for loop in the list and kept adding each number x in the total
#also note that in concatenation you should be having strings. so after my calculation is done, i converted my mean to a str in order to combine my sentence.
import math
#now lets square the values
squared_list=[]
for number in new_data:
    a= int(number) - mean
    a= a**2
    squared_list.append(a)

print(squared_list)

#getting sum
sum =0
for i in squared_list:
    sum =sum + i

#dividing the sum by the total values
result = sum/ (len(new_data)-1)

# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)

#a graph can also be plotted. pandas help read your data so it can be graph and plotly,express hepls you graph it out


df = pd.read_csv("SOCR-HeightWeight.csv")

fig = px.scatter(df,    x="Index",
                        y="Height(Inches)"
            )
fig.show()


