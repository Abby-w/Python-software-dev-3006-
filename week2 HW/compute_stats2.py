#import packages
import sys
import statistics
import csv

def compute_stats(values):
    """Computes the minimum, maximum, mean and median for a list of values

    Parameters
    ----------
    values: a list of the values

    Returns
    -------
    tuple: A tuple of the minimum, maximum, mean and median value of the list
    """
#check if the list is empty
    if len(values)==0:
        Average =None
        maximum =None
        minimum =None
        median =None
#calculate the statistics
    else:
        Average =statistics.mean(values)
        maximum =max(values)
        minimum =min(values)
        median =statistics.median(values)
#return a tuple of the statisitcs
    tuple=(minimum,maximum,Average,median)

    return tuple

def main():
    """Takes a txt file with space seperated columns and creates a list of values
    from a specific row then sorts the list.

    Parameters
    ----------
    No parameters

    Returns
    -------
    values: a list of the values from a specific colum
    """

#define variable
    global values
    values=[]
    column = int(sys.argv[1])-1
    data_file = csv.register_dialect("space",delimiter=' ', skipinitialspace = True)
#add values to list if stdin used
    if len(sys.argv)==2:
        data = csv.reader(sys.stdin, "space")
        for row in data:
           values+=[float(row[column])]
#add values to list if stdin is not used
    if len(sys.argv)==3:
        with open(sys.argv[-1]) as input:
            data = csv.reader(input, "space")
            for row in data:
                values+=[float(row[column])]
#remove the "missing" values
    for i in values:
        if i==-9999.0:
            values.remove(-9999.0)
        if i==-99.000:
            values.remove(-99.000)
#sort values
    values.sort()
    print(compute_stats(values))
    return values


if __name__=='__main__':
    main()
