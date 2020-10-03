import csv
import pandas

df = pandas.read_csv('./datasets/nfl2013stats.csv')
print(df)

#with open('./datasets/nfl2013stats.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
