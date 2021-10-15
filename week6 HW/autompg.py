from collections import namedtuple
fields = namedtuple('fields', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name'])
import csv
import os


class AutoMPG:
    """Class that represents the attrributes available for each record in a data set"""

    def __init__(self, make, model, year, mpg):

        self.make=str(make)
        self.model=str(model)
        self.year=1900+int(year)
        self.mpg=mpg


    def __str__(self):
        #string representation of the record
        return f'AutoMPG: ({self.make},{self.model}, {self.year}, {self.mpg})'

    def __repr__(self):
        #string representation of the record
        return f'AutoMPG: car={self.__str__()})'

    def __eq__(self, other):
        #compare the make model year and mpg of two records (equal)
        print(f"debug: {str(self)} == {str(other)}")
        #ensure types are the same
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and self.year==other.year and self.mpg==other.mpg
        else:
            return NotImplemented

    def __lt__(self, other):
        #compare the make model year and mpg of two records (less than)
        print(f"debug: {str(self)} < {str(other)}")
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
    """Class that represents the entire AUtoMPG data set. Data is a list of AutoMPG objects"""
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
        #check if the file already exists
        if os.path.exists("auto-mpg.clean.txt")== False:
            #if file DNE, send to clean data
            self._clean_data()
        else:
            #used cleaned data to create the data list
            data=[]
            #take the data from the cleaned CSV
            with open('auto-mpg.clean.txt', 'r', newline='') as csvfile:
                dataReader = csv.reader(csvfile)
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
        model=split_names[-1]
        #pass attributes into AutoMPG
        auto=AutoMPG(make,model,self.model_year , self.mpg)
        return auto

def main():
    car=AutoMPGData()
    #iterate through each record in the data set
    for a in car:
        print(a)


if __name__=='__main__':
    main()
