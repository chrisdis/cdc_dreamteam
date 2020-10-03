from typing import Counter
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression

def basic_model(team1, team2, date= "12/31/2013", year= "2013"):
    df = pd.read_csv('./datasets/nfl2013stats.csv')
    df['n'] = 0

    model = LinearRegression().fit(df[["PassYdsOff", "RushYdsOff"]], df["ScoreOff"])

    #print(model.score(df[["PassYdsOff", "RushYdsOff"]], df["ScoreOff"]))

    y_pred = model.predict([[300, 100]])
    #print(y_pred)

    date = datetime.datetime.strptime(date, '%m/%d/%Y')
    teamName = "Baltimore Ravens"
    year = 2013
    result = last_n_games(year, teamName, date, 5)
    opponent = last_n_games(year, "Detroit Lions", date, 5)
    cleaned_result = clean(result)
    #print(cleaned_result)
    #print(cleaned_result.shape())

    new_df = clean(df)
    #print(new_df)
    #print(new_df.applymap(np.isreal))
    #print(new_df["ScoreDef"])
    #new_df.applymap(np.isreal).to_csv('findthisfuckingstring.csv')
    model_off = LinearRegression().fit(new_df, new_df["ScoreOff"])
    model_def = LinearRegression().fit(new_df, new_df["ScoreDef"])

    #smodel1, model2 = model()
    team1score, team2score = linear_reg(team1, team2, date, year, model_off, model_def)
    o1 = np.mean(team1score)
    o2 = np.mean(team2score)
    return o1, o2
    #print(cleaned_result["ScoreOff"])
    #print(y_pred)

    #date = datetime.datetime.strptime('12/20/2013', '%m/%d/%Y')
    #test = last_n_games(year, teamName, date, 1)
    #test2 = find_game("Detroit Lions",teamName, date, year)
    #print(test)
    #print(test2)
    
    #cleaned_opponent = clean(opponent)

    #print(cleaned_opponent)
    #both = pd.concat([cleaned_result, cleaned_opponent.reindex(cleaned_result.index)], axis = 1)
    #print(both)
    #model = LinearRegression().fit(cleaned_result, cleaned_result["ScoreOff"])
    #model2 = LinearRegression().fit(cleaned_opponent, cleaned_opponent["ScoreDef"])

    #y_pred = model.predict(clean(test))
    #y2_pred = model2.predict(clean(test2))
    #print(f'prediction: {y_pred[0]}')
    #print(test["ScoreOff"])
    #print(f'prediction2: {y2_pred[0]}')
    #print(test2["ScoreDef"])
   
    #print(result)

def last_n_games(year, teamName, date, n):
    #get data for the last 5 games a team played. this will be input data for the model.
    df = pd.read_csv(f'./datasets/nfl{year}stats.csv')

    output = pd.DataFrame()
    temp = pd.DataFrame()
    count = 1
    for index, row in df.iterrows():
     
        row["Date"] = datetime.datetime.strptime(row["Date"], '%m/%d/%Y')
        if (row["Date"] < date and row["TeamName"] == teamName):
            temp = temp.append(row)
            temp.loc[index, "n"] = count
            count += 1

    total_games = len(temp)
    for _index, row in temp.iterrows():
        #print(row["n"])
        if (row["n"] > total_games - n):
            output = output.append(row)
    return output

def clean(input):
    #input['TimePossOff']
    #input['TimePossDef']
    input = input.drop(['Date', 'TeamName', 'Opponent', 'Site', 'n', 'TimePossOff', 'TimePossDef', "ThirdDownPctOff", "ThirdDownPctDef", "PuntAvgOff"], axis=1)
    #for index, row in input.iterrows():
    #    for column in row:
    #        try:
    #            float(row[column])
    #        except:
    #            input[index, column] = 0
                #row[column] = 0

    return input
    #return input.loc[:, input.columns not in ('Date', 'TeamName', 'Opponent', 'Site', 'n', 'TimePossOff', 'TimePossDef')]

def find_game(teamName, opponentName, date, year):
    df = pd.read_csv(f'./datasets/nfl{year}stats.csv')
    out = pd.DataFrame()
    for _index, row in df.iterrows():
        row["Date"] = datetime.datetime.strptime(row["Date"], '%m/%d/%Y')
        if (row["Date"] < date and row["TeamName"] == teamName and row["Opponent"] == opponentName):
            out = pd.DataFrame()
            out = out.append(row)
            out['n'] = 1
    return out

def model():
    df = pd.read_csv(f'./datasets/nfl2013stats.csv')
    new_df = clean(df)
    model_off = LinearRegression().fit(new_df, new_df["ScoreOff"])
    model_def = LinearRegression().fit(new_df, new_df["ScoreDef"])
    return model_off, model_def

def linear_reg(team1, team2, date, year, modeloff, modeldef):
    result = last_n_games(year, team1, date, 5)
    opponent = last_n_games(year, team2, date, 5)
    cleaned_result = clean(result)
    cleaned_opponent = clean(opponent)
    predictionoff1 = modeloff.predict(cleaned_result)
    #print(predictionoff1)
    
    predictionoff2 = modeldef.predict(cleaned_opponent)
    #print(predictionoff2)
    #predictionoff = (predictionoff1 + predictionoff2)/2
    predictionoff = predictionoff1

    predictiondef1 = modeloff.predict(cleaned_opponent)
    predictiondef2 = modeldef.predict(cleaned_result)
    #predictiondef = (predictiondef1 + predictiondef2)/2
    predictiondef = predictiondef1

    return predictionoff, predictiondef

print(basic_model("Detroit Lions", "Baltimore Ravens"))