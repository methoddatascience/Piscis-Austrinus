In this prototype, the Alabama city and health statistics are considered.

The data folder contains formatted and collected data for previous years 2011 to 2015 in season.csv.
Processed data derived confidence score for different locations are in conf.csv.
zfile.txt refers to different zones and holds the different location information.

All the 3 derived dataset is used as the knowledge base in this model and do not modify them.

Dependencies:
Please, install pandas and gmplot python packages.

To run the program:
simply run main.py and it will ask you to enter a week number from 1 to 52. If you enter a wrong week number, it will
work for the marginal week values by itself (e.g. input 0 will work for week 1 and 87 will work for week 52).

A .html file is produced as output on Google maps.
Red circles refer to zones with highly risky zones for babies to get flu, blue refers to moderately risky zones,
and yellow refers to lowly risky zones.

You may notice Goole maps watermark if the output is not produced standing on a server system.

Some example outputs are already provided in the root directory for week 10, 18, 22, 33 and 52.