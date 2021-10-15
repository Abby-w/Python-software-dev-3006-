
import sys
import statistics

#define variables
values=[]
data = sys.stdin.read()

#break the text list into the individual lines
line=data.split('\n')

#remove any excess spaces
for i in line[:-1]:
    noSpace=i.strip()

#convert the lines to floats
    values+=[float(noSpace)]

#remove the "missing" values
for i in values:
    if i==-9999.0:
        values.remove(-9999.0)

#calculate the statistics
Average=statistics.mean(values)
max=max(values)
min=min(values)
median=statistics.median(values)

#print the results
print("min:", min , ", max:", max , ", average:", Average, ", median:", median)
