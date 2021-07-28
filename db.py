import pandas as pd
import sqlite3

#Graph1
def get_total_goals_by_rainfall():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "SELECT count(goals.id) as total_goal, rainfall FROM goals JOIN matches ON goals.match_id = matches.id GROUP BY matches.rainfall;"
    df = pd.read_sql(request, con)
    return df
    
def get_mean_goals_by_rainfall():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "select count(goals.id) as mean_goal, rainfall  FROM goals JOIN matches ON goals.match_id = matches.id GROUP BY matches.rainfall, matches.id;"
    df = pd.read_sql(request, con)
    df = df.groupby(['rainfall'],as_index=False).mean()
    return df

#Graph2
def get_total_goals_by_temperature():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "SELECT count(goals.id) as total_goal, temperature FROM goals JOIN matches ON goals.match_id = matches.id GROUP BY matches.temperature;"
    df = pd.read_sql(request, con)
    return df

def get_mean_goals_by_temperature():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "SELECT COUNT(goals.id) as mean_goal, temperature FROM goals JOIN matches ON goals.match_id = matches.id GROUP BY matches.temperature, matches.id;"
    df= pd.read_sql(request, con)
    df = df.groupby(['temperature'],as_index=False).mean()

    return df


#Graph3
def get_total_teams_goals_by_rainfall():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "select goals.id as total_goals, rainfall, teams.name  FROM goals JOIN matches ON goals.match_id = matches.id JOIN matches_teams ON matches.id = matches_teams.matchs_id JOIN teams ON matches_teams.team_id = teams.id ORDER BY date"
    df = pd.read_sql(request, con)
    df =df.groupby(['name','rainfall'],as_index=False).count()
    return df

def get_mean_teams_goals_by_rainfall():
    con = sqlite3.connect('data/football_orm.sqlite')
    request= """SELECT 
    matches.id AS match_id,
    matches_teams.team_goals AS Total_team_goals,
    matches.rainfall, teams.name 
    FROM goals
    JOIN matches ON goals.match_id = matches.id 
    JOIN matches_teams ON matches_teams.matchs_id = matches.id
    JOIN teams ON teams.id = matches_teams.team_id 
    GROUP BY matches.id ,teams.id"""
    df = pd.read_sql(request, con)
    df = df.groupby(['name','rainfall'], as_index=False).mean()
    return df


#Graph4    
def get_total_teams_goals_by_temperature():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "select goals.id as total_goals, temperature, teams.name  FROM goals JOIN matches ON goals.match_id = matches.id JOIN matches_teams ON matches.id = matches_teams.matchs_id JOIN teams ON matches_teams.team_id = teams.id ORDER BY date"
    df = pd.read_sql(request, con)
    df =df.groupby(['name','temperature'],as_index=False).count()
    return df

def get_mean_teams_goals_by_temperature():
    con = sqlite3.connect('data/football_orm.sqlite')
    request= """SELECT 
    matches.id AS match_id,
    matches_teams.team_goals AS Total_team_goals,
    matches.temperature, teams.name 
    FROM goals
    JOIN matches ON goals.match_id = matches.id 
    JOIN matches_teams ON matches_teams.matchs_id = matches.id
    JOIN teams ON teams.id = matches_teams.team_id 
    GROUP BY matches.id ,teams.id"""    
    df = pd.read_sql(request, con)
    df = df.groupby(['name','temperature'], as_index=False).mean()
    return df

#Graph 5

def get_match_note_by_temperature():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "SELECT * FROM matches ;"
    df = pd.read_sql(request, con)
    df= df.groupby(['temperature'], as_index=False)['match_note'].mean()
    return df

def get_match_note_by_rainfall():
    con = sqlite3.connect('data/football_orm.sqlite')
    request = "SELECT * FROM matches ;"
    df = pd.read_sql(request, con)
    df= df.groupby(['rainfall'], as_index=False)['match_note'].mean()
    return df





def get_total_goals_per_players():
    pass