import requests, json, collections
import inspect, logging, csv
import matplotlib.pyplot as plt
import os, argparse, sys

# configure logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# file handler : DEBUG to file
logFile = logging.FileHandler('country_populations.log', 'w')
logFile.setLevel(logging.DEBUG)
logger.addHandler(logFile)

# stream handler : INFO to console
logStream = logging.StreamHandler()
logStream.setLevel(logging.INFO)
logger.addHandler(logStream)

url = 'https://services.arcgis.com/BG6nSlhZSAWtExvp/ArcGIS/rest/services/Third_Join_Features_to_Second_Join_Features_to_World_Countries_(Generalized)/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token='
full_request = requests.get(url)

# create a parser for the module
parser = argparse.ArgumentParser(description="Parse the argument parameters for manipulating the population data")

def __lineno__():
    """Return the line number of the program. For use in debugging"""
    return inspect.currentframe().f_back.f_lineno

class Country_Population:
    """Class to store and calculate basic population statistics for a single country"""
    def __init__(self, country_attributes, country_geometry):
        """Initialize instance of Country_Population"""
        self.name = country_attributes['COUNTRY']
        self.sqmiles = country_attributes['SQMI']
        self.geometry = country_geometry
        self.latitude = self.__meanLat__()
        self.pop_2019 = country_attributes['F2019']
        self.pop_2010 = country_attributes['F2010']
        self.pop_2000 = country_attributes['F2000']
        self.pop_1990 = country_attributes['F1990']
        self.pop_1980 = country_attributes['F1980']
        self.pop_1970 = country_attributes['F1970']
        self.pop_1960 = country_attributes['F1960']
    def __str__(self):
        """Return convenient string representation"""
        return f'{self.name},{self.sqmiles},{self.latitude}'
    def __repr__(self):
        """Return official string representation"""
        return f'{self.name}: {self.sqmiles} miles^2, {self.latitude}'
    def __meanLat__(self):
        """Calculate the latitude of each country based on mean northing of the vertices"""
        # the coordinates provided in the JSON file are in WGS 1984 Web Mercator which is a projected coordinate system.
        # the file CoordinateMapping.txt is a conversion file that contains a decimal degree latitude and the corresponding Web Mercator value
        # I created CoordinateMapping.txt with my GIS knowledge

        # calculate the mean northing
        pointNorthing = list()
        for rings in self.geometry:
            for point in rings:
                pointNorthing.append(point[1])
        meanNorthing = sum(pointNorthing)/len(pointNorthing)


        # load the coordinate mapping into memory
        latMap = collections.OrderedDict()
        with open(os.path.join(os.path.dirname(__file__),'CoordinateMapping.txt'), 'r') as coordMapFile:
            coordMap = csv.reader(coordMapFile)
            for row in coordMap:
                try:
                    latMap[float(row[1])]=float(row[0])
                except:
                    pass

        # if the meanNorthing is positive then the country is in the northern hemisphere and a standard iteration through latMap is appropriate
        if meanNorthing > 0: # northern hemisphere countries
            for north, lat in latMap.items():
                if north > meanNorthing:
                    return lat
                else:
                    pass
        else: # southern hemisphere countries
            for north, lat in reversed(latMap.items()):
                if -north > meanNorthing:
                    return -lat
                else:
                    pass
        return None


class Population_Stats:
    """Class to store population data and basic statistics of multiple countries"""
    def __init__(self):
        """Initialize the instance of Population_Stats to store a collection of population statistics"""
        logging.debug(f'{__lineno__()}:creating Population_Stats instance')
        self.data = []
        self.idx = 0
        self._load_data()

    def __iter__(self):
        """Enable an iterator of the instance of Population_Stats to iterator through the collection county population statistics"""
        return self

    def __next__(self):
        self.idx +=1
        try:
            return self.data[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration

    def _load_data(self):
        """Create a new instances of Country_Population to load into Populations_Stats"""
        logging.debug(f'{__lineno__()}:loading data in Country_Population instances')

        source_data = requests.get(url)
        # check if request to url is successful
        if source_data.status_code == 200:
            json_data = json.loads(full_request.text)

            for d in enumerate(json_data['features']):
                self.data.append(Country_Population(d[1]['attributes'], d[1]['geometry']['rings']))

    def print_data(self):
        """Print each instance of Country_Population"""
        for d in self.data:
            print(d.__repr__())

    def plot_growth(self):
        """Plot a scatter plot of population growth"""

        plt.figure(0)
        for i, ctry in enumerate(self.data):
            x = []
            y = []

            if ctry.sqmiles is not None:
                if ctry.pop_2019 is not None:
                    x.append(2019)
                    y.append(ctry.pop_2019/ctry.sqmiles)
                if ctry.pop_2010 is not None:
                    x.append(2010)
                    y.append(ctry.pop_2010/ctry.sqmiles)
                if ctry.pop_2000 is not None:
                    x.append(2000)
                    y.append(ctry.pop_2000/ctry.sqmiles)
                if ctry.pop_1990 is not None:
                    x.append(1990)
                    y.append(ctry.pop_1990/ctry.sqmiles)
                if ctry.pop_1980 is not None:
                    x.append(1980)
                    y.append(ctry.pop_1980/ctry.sqmiles)
                if ctry.pop_1970 is not None:
                    x.append(1970)
                    y.append(ctry.pop_1970/ctry.sqmiles)
                if ctry.pop_1960 is not None:
                    x.append(1960)
                    y.append(ctry.pop_1960/ctry.sqmiles)

            plt.plot(x,y)
        plt.savefig('pop_growth')


def main(arguments):
    #print(arguments.latitude)

    pop_stats = Population_Stats()

    #pop_stats._print_data()
    #pop_stats.plot_histogram()

    #pop_stats.plot_growth()

    return pop_stats

def add_arguments(parser):
    """Add parser agruments for use when running script from the command line"""
    #parser.add_argument('-lat', '--latitude', action ='store_true')

if __name__=='__main__':
    add_arguments(parser)
    arguments = parser.parse_args()
    main(sys.argv)
