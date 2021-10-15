from collections import namedtuple
fields = namedtuple('fields', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name'])
import csv
import os
import requests
import logging
import argparse
from operator import attrgetter

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

fileHandle = logging.FileHandler('autompg2.log', 'w')
fileHandle.setLevel(logging.DEBUG)
logger.addHandler(fileHandle)

streamHandle= logging.StreamHandler()
streamHandle.setLevel(logging.INFO)
logger.addHandler(streamHandle)


class AutoMPG:
    """Class that represents the attrributes available for each record in a data set"""

    def __init__(self, make, model, year, mpg):

        self.make=str(make)
        self.model=str(model)
        self.year=1900+int(year)
        self.mpg=float(mpg)


    def __str__(self):
        #string representation of the record
        return f'AutoMPG({self.make},{self.model}, {self.year}, {self.mpg})'

    def __repr__(self):
        #string representation of the record
        return self.__str__()

    def __eq__(self, other):
        #compare the make model year and mpg of two records (equal)

        #ensure types are the same
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and self.year==other.year and self.mpg==other.mpg
        else:
            return NotImplemented

    def __lt__(self, other):
        #compare the make model year and mpg of two records (less than)

        #ensure types are the same
        if type(self) == type(other):
            #compare the first attribute: make
            if self.make != other.make:
                return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

            else:
                #compare the second attribute: model
                if self.model != other.model:
                    return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

                else:
                    #compare the third attribute: year
                    if self.year != other.year:
                        return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

                    else:
                        #compare the fourth attribute: mpg
                        if self.mpg != other.mpg:
                            return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)
                        #if all 4 attributes are the same, comparision not implemented
                        else:
                            return NotImplemented
        else:
            return NotImplemented

    def __hash__(self):
        #returns the hash of all the attributes
        return hash((self.make, self.model, self.year, self.mpg))


class AutoMPGData:
    """Class that represents the entire AutoMPG data set. Data is a list of AutoMPG objects"""
    def __init__(self):
        self.data=self._load_data()



    def __iter__(self):
        #allow iteration through the list
        self._iter = 0
        return self

    def __next__(self):
        #next is each record in the list
        if self._iter == len(self.data):
            raise StopIteration
        ret = self.data[self._iter]
        self._iter +=1
        return ret

    def _load_data(self):

        if os.path.exists("auto-mpg.data.txt")== False:
            logging.debug('checking auto-mpg.data.txt')
            self._get_data()


        #check if the file already exists
        if os.path.exists("auto-mpg.clean.txt")== False:
            logging.debug('checking auto-mpg.clean.txt')
            #if file DNE, send to clean data
            self._clean_data()
        else:
            logging.debug('auto-mpg.clean.txt exits')
            #used cleaned data to create the data list
            data=[]
            #take the data from the cleaned CSV
            with open('auto-mpg.clean.txt', 'r', newline='') as csvfile:
                dataReader = csv.reader(csvfile)
                logging.debug('Parsing auto-mpg.clean.txt into AutoMPG objects')
                for row in dataReader:
                    #put record into a tuple and unpack the tuple
                    field = fields(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name = field

                    #add the record to the data list
                    car=Record(mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name)
                    data+=[car.pass_into_autoMPG()]
                return data

    def _clean_data(self):
        #create a new data file with the cleaned data
        #remove the tab
        data_file = csv.register_dialect("space",delimiter='\t', skipinitialspace = True)
        with open('auto-mpg.clean.txt', 'w', newline='') as outputfile:
            cleanwriter = csv.writer(outputfile, quoting=csv.QUOTE_NONE)
            #take the data from the original AutoMPG CSV file
            with open('auto-mpg.data.txt', 'r', newline='') as csvfile:
                dataReader = csv.reader(csvfile, "space")
                for row in dataReader:
                    #split all attributes other than car_name
                    clean=row[0].split() + [row[1]]
                    cleanwriter.writerow(clean)
        self._load_data()

    def _get_data(self):
        logging.debug('getting auto-mpg.data.txt')
        url='https://autompgdata.azurewebsites.net/api/assignment7data'

        r = requests.get(url, allow_redirects = True)
        code=r.status_code

        logging.debug('Responce code: %s', r.status_code)



        with open('auto-mpg.data.txt', 'wb') as output:
            output.write(r.content)
        self._load_data()
        return code

    def sort_by_default(self):
        logging.debug('Sorting AutoMPG objects by default')
        self.data.sort()
        return self.data

    def sort_by_year(self):
        logging.debug('Sorting AutoMPG objects by year')
        self.data.sort(key= attrgetter('year', 'make', 'model', 'mpg'))
        return self.data

    def sort_by_mpg(self):
        logging.debug('Sorting AutoMPG objects by mpg')
        self.data.sort(key= attrgetter('mpg', 'make', 'model', 'year'))
        return self.data




class Record:
    """Class that passes the appropriate attributes into the AutoMPG class"""
    def __init__(self, mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name):
        self.mpg=mpg
        self.cylinders=cylinders
        self.displacement=displacement
        self.horsepower=horsepower
        self.weight=weight
        self.acceleration=acceleration
        self.model_year=model_year
        self.origin=origin
        self.car_name=car_name

    def pass_into_autoMPG(self):
        #split car_name into make and model
        split_names=self.car_name.split(" ", 1)
        make=split_names[0]
        if split_names[-1]== split_names[0]:
            model=''
        else:
            model=split_names[-1]
        #pass attributes into AutoMPG
        auto=AutoMPG(make,model,self.model_year , self.mpg)
        return auto



def main():
    parser =argparse.ArgumentParser(description='Parse the data from specificed access log')
    parser.add_argument ('command', metavar='command' , type=str, help='command to execute', choices=['print'])
    parser.add_argument('-s', '--sort',metavar= '<sort order>', type=str, choices=[None, 'mpg', 'year'])
    arguments= parser.parse_args()
    car=AutoMPGData()

    if arguments.sort== None:
        output=car.sort_by_default()
    if arguments.sort == 'mpg':
        output=car.sort_by_mpg()
    if arguments.sort == 'year':
        output=car.sort_by_year()

    for a in output:
        logging.info(a)



if __name__=='__main__':
    main()
