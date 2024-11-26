import csv
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


#now for median
#lets sort
n=len(new_data)
new_data.sort()

#using floor division to get the nearest number whole number, n%2== 0 means when n is divided by 2 then remainder is 0. / gives quotient while % gives remainder
# floor division is shown by //
if n % 2 == 0:
    #getting the first number
	median1 = float(new_data[n//2])
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = new_data[n//2]

print("Median is: " + str(median))


#now for mode
#remember that i need number of occurances for mode so i will count it using the counter which i have imported
#Calculating Mode
data = Counter(new_data)
#lets keep all as zero first and will then append
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence
print("so the values with occurances " + str(mode_data_for_range))
mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print("so the range with most "+ str(mode_range))
print("most occurences " + str(mode_occurence))
print(mode)
print(f"Mode is -> " + str(mode))


