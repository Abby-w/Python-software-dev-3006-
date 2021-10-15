# Final Project: Flu and Covid19 cases noramlized by population Analysis

## Group Members
Abigail Ward
Matthew Cuneo
Chris Hensley

<br /> <br />

## Research Question
Is a correlation between the number of Covid19 cases and influenza cases across different country population sizes, geographic area or mean latitude.

<br /> <br />

## Datasets utilized
  -reads country population and area statistics from https://services.arcgis.com/BG6nSlhZSAWtExvp/ArcGIS/rest/services/Third_Join_Features_to_Second_Join_Features_to_World_Countries_(Generalized)/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token=


  -reads a downloaded dataset of 2020 influenza cases by country from https://apps.who.int/flumart/Default?ReportNo=12

  -reads a hosted dataset that contains 2020 COVID cases and deaths by country from https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/full_data.csv

<br /> <br />

## Program functionality
-print a table of influenza total, strain A and strain B cases to the console
-plot a histogram of influenza total, strain A or strain B cases
-print a table of COVID cases and deaths to the console
-plot a histogram of COVID cases or deaths
-plot two stacked histograms of influenza and covid cases normalized by country population
-plot two stacked histograms of influenza and covid cases normalized by country population density
-plot a histogram of the influenza and covid cases by country mean latitude

## Analysis Conclusion
Due to the mask requirements that were put in place across the global due to Covid19, it has been reported that the number of influenza cases decreased in 2020. Our analysis shows that there is not a clear relationship between the number of Influenza cases in a country in 2020 and the Covid cases in a country.

<br /> <br />

## Usage
```bash
python covid_flu_analysis.py [optional arguments]
```
### Dependencies
  plotly
	pandas
	argparse
	sys
	collections
	inspect
	requests
	json
	logging
	csv
	os

### [optional arguments]

-h, --help            show this help message and exit

-prt_flu, --print_flu
                      print table of flu cases to console; applies sort

-s_flu {total,strain_A,strain_B}, --sort_flu {total,strain_A,strain_B}
                      sort influenza data

-plt_flu {total,strain_A,strain_B}, --plot_flu {total,strain_A,strain_B}
                      plot histogram of flu cases; applies filter

-prt_covid, --print_covid
                      print table of covid data to console; applies sort

-s_covid {cases,deaths}, --sort_covid {cases,deaths}
                      sort covid data by cases or deaths

-plt_covid {cases,deaths}, --plot_covid {cases,deaths}
                      plot histogram of covid cases; applies filter

-c {pop,pop_density,lat}, --comp {pop,pop_density,lat}
                      pop=cases per population; pop_density=cases per population density; lat=cases per latitude

-c_flu {total,strain_A,strain_B}, --comparison_flu {total,strain_A,strain_B}
                      use either the total, strain A or strain B flu cases in the comparison analysis

-c_covid {cases,deaths}, --comparison_covid {cases,deaths}
                      use either cases or deaths in the comparison analysis
