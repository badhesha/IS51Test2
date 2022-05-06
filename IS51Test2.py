"""
structured-english

Start
Download the text file titled Final.txt, which has the list of
students grade. Next create function that will show the total 
number of grade, the average grade, and the percentage of grades
that are above average. The final percentages the function should 
output for average grade is 83.25%. The percentage for the grade above 
average is 54.17%. The total number of grades is 24. 
End

"""

"""
pseudo-code

Open "Final.txt"
create variable grades to strip from list
len(grades) #return length of list
Initalize counter and sum to 0
add the grade to the sum
average function = sum(grades)/len(grades)
Initalize counter and sum to 0
num = 0 #for number of grades above average
if grade > average
num +=1
use {0:2f}%
(100*num)/len(grades) #format percentage
print "Number of grades"
print "Average Grade"
print "Percentage of grades above average"

"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades)/len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades)) 
print("Average grade:", average) 
print("Percentage of grades above average: {0:.2f}%" 
                    .format(100 * num / len(grades)))