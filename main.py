import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("NBA Three-Point Strategy Analyzer")
    print("---------------------------------")
   
    offensive_df = pd.read_csv("data/offense.csv")

    defensive_df = pd.read_csv("data/defense.csv") 

    records_df = pd.read_csv("data/records.csv")

    offensive_df["Team"] = offensive_df["Team"].str.replace("*", "", regex=False)

    defensive_df["Team"] = defensive_df["Team"].str.replace("*", "", regex=False)

    offensive_df = offensive_df[offensive_df["Team"] != "League Average"]

    defensive_df = defensive_df[defensive_df["Team"] != "League Average"]

    combined_df = pd.merge(offensive_df, defensive_df, on="Team")

    finished_df = pd.merge(combined_df, records_df, on="Team")

    cleaned_df = finished_df[["Team", "Abbreviation", "3P_x", "3PA_x", "3P_y", "3PA_y", "W", "L"]] 

    cleaned_df = cleaned_df.rename(columns={
    "Abbreviation" : "Abbreviation", 
    "3P_x" : "3PM", 
    "3PA_x" : "3PA", 
    "3P_y" : "Opponent 3PM", 
    "3PA_y" : "Opponent 3PA", 
    "W" : "Wins", 
    "L" : "Losses"
    })

    print(cleaned_df.columns)
    print(cleaned_df.head())   

if __name__ == "__main__":
    main()
