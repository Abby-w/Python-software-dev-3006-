
from collections import namedtuple
fields = namedtuple('fields', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name'])
import csv
import os


class AutoMPG:

    def __init__(self, make, model, year, mpg):

        self.make=str(make)
        self.model=str(model)
        self.year=1900+int(year)
        self.mpg=mpg


    def __str__(self):
        #string representation of hand
        return f'AutoMPG: ({self.make},{self.model}, {self.year}, {self.mpg})'

    def __repr__(self):
        #string representation of hand
        return f'AutoMPG: car={self.__str__()})'

    def __eq__(self, other):
        print(f"debug: {str(self)} == {str(other)}")
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and self.year==other.year and self.mpg==other.mpg
        else:
            return NotImplemented

    def __lt__(self, other):
        print(f"debug: {str(self)} < {str(other)}")
        if type(self) == type(other):
            if self.make != other.make:
                return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

            else:
                if self.model != other.model:
                    return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

                else:
                    if self.year != other.year:
                        return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

                    else:
                        if self.mpg != other.mpg:
                            return (self.make, self.model, self.year, self.mpg) < (other.make, other.model, other.year, other.mpg)

                        else:
                            return NotImplemented
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.make, self.model, self.year, self.mpg))


class AutoMPGData:

    def __init__(self):
        self.data=self._load_data()


    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self._iter == len(self.data):
            raise StopIteration
        ret = self.data[self._iter]
        self._iter +=1
        return ret

    def _load_data(self):
        if os.path.exists("auto-mpg.clean.txt")== False:
            self._clean_data()
        else:
            data=[]
            with open('auto-mpg.clean.txt', 'r', newline='') as csvfile:
                dataReader = csv.reader(csvfile)
                for row in dataReader:

                    field = fields(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name = field

                    car=Record(mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name)
                    data+=[car.pass_into_autoMPG()]

                return data

    def _clean_data(self):
        data_file = csv.register_dialect("space",delimiter='\t', skipinitialspace = True)
        with open('auto-mpg.clean.txt', 'w', newline='') as outputfile:
            cleanwriter = csv.writer(outputfile, quoting=csv.QUOTE_NONE)
            with open('auto-mpg.data.txt', 'r', newline='') as csvfile:
                dataReader = csv.reader(csvfile, "space")
                for row in dataReader:
                    clean=row[0].split() + [row[1]]
                    cleanwriter.writerow(clean)
        self._load_data()

class Record:
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
        split_names=self.car_name.split(" ", 1)
        make=split_names[0]

        model=split_names[-1]
#needs to be fixed
        auto=AutoMPG(make,model,self.model_year , self.mpg)
        return auto

def main():
    car=AutoMPGData()
    for a in car:
        print(a)


if __name__=='__main__':
    main()

test=AutoMPGData()
#a1 = AutoMPG('a', 'b', 3, 4)
#a2 = AutoMPG('a', 'b', 3, 4)
#print(a1.__eq__(a2))
