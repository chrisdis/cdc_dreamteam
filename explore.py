import pandas

df = pandas.read_csv('./datasets/nfl2013stats.csv')

df["Win"] = False
df["Cover"] = False
df["Over"] = False
#print(df.loc[0])
for index, row in df.iterrows():
    if (row['ScoreOff'] > row['ScoreDef']):
        df.loc[index, "Win"] = True
    if ((row['ScoreOff'] + row['ScoreDef']) > row['TotalLine']):
        df.loc[index, 'Over'] = True
    if (row['ScoreOff'] + row['Line'] > row['ScoreDef']):
        df.loc[index, 'Cover'] = True
    if (row['ScoreOff'] > 50):
        print(f"{row['TeamName']} {row['ScoreOff']} {row['Opponent']} {row['ScoreDef']}")

#sanity checks
#print(sum(df["Win"])/len(df["Win"]) * 100)
#print(sum(df["Cover"])/len(df["Cover"]) * 100)
#print(sum(df["Over"])/len(df["Over"]) * 100)

#with open('./datasets/nfl2013stats.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
