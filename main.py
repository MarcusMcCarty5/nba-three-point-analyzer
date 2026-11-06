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

    cleaned_df.to_csv("data/team_stats.csv", index=False)

    offensive_3PA_correlation = cleaned_df["3PA"].corr(cleaned_df["Wins"])
    plt.figure()
    plt.scatter(cleaned_df["3PA"], cleaned_df["Wins"])
    plt.axvline(cleaned_df["3PA"].mean())
    plt.axhline(41)
    plt.xlabel("3-Pointers Attempted Per Game")
    plt.ylabel("Total Wins")
    plt.title("Offensive Three-Point Attempts vs. Team Wins")   
    plt.figtext(0.5, 0.01, f"Correlation: {offensive_3PA_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/offensive_3PA_scatterplot.png")
    plt.show()

    offensive_3PM_correlation = cleaned_df["3PM"].corr(cleaned_df["Wins"])
    plt.figure()
    plt.scatter(cleaned_df["3PM"], cleaned_df["Wins"])
    plt.axvline(cleaned_df["3PM"].mean())
    plt.axhline(41)
    plt.xlabel("3-Pointers Made Per Game")
    plt.ylabel("Total Wins")
    plt.title("Offensive Three-Pointers Made vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {offensive_3PM_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/offensive_3PM_scatterplot.png")
    plt.show()

    cleaned_df["3P%O"] = cleaned_df["3PM"] / cleaned_df["3PA"]
    offensive_3PP_correlation = cleaned_df["3P%O"].corr(cleaned_df["Wins"])
    plt.figure()
    plt.scatter(cleaned_df["3P%O"], cleaned_df["Wins"])
    plt.axvline(cleaned_df["3P%O"].mean())
    plt.axhline(41)
    plt.xlabel("3-Point Percentage Per Game")
    plt.ylabel("Total Wins")
    plt.title("Three-Point Percentage vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {offensive_3PP_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/offensive_3P_pct_scatterplot.png")
    plt.show()

    defensive_3PA_correlation = cleaned_df["Opponent 3PA"].corr(cleaned_df["Wins"])
    plt.figure()
    plt.scatter(cleaned_df["Opponent 3PA"], cleaned_df["Wins"])
    plt.axvline(cleaned_df["Opponent 3PA"].mean())
    plt.axhline(41)
    plt.xlabel("Opponent 3-Pointers Attempted Per Game")
    plt.ylabel("Total Wins")
    plt.title("Opponent Three-Point Attempts vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {defensive_3PA_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/defensive_3PA_scatterplot.png")
    plt.show()

    defensive_3PM_correlation = cleaned_df["Opponent 3PM"].corr(cleaned_df["Wins"])
    plt.figure()
    plt.scatter(cleaned_df["Opponent 3PM"], cleaned_df["Wins"])
    plt.axvline(cleaned_df["Opponent 3PM"].mean())
    plt.axhline(41)
    plt.xlabel("Opponent 3-Pointers Made Per Game")
    plt.ylabel("Total Wins")
    plt.title("Opponent Three-Pointers Made vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {defensive_3PM_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/defensive_3PM_scatterplot.png")
    plt.show()

    cleaned_df["3P%D"] = cleaned_df["Opponent 3PM"] / cleaned_df["Opponent 3PA"]
    defensive_3PP_correlation = cleaned_df["3P%D"].corr(cleaned_df["Wins"])
    plt.figure()
    plt.scatter(cleaned_df["3P%D"], cleaned_df["Wins"])
    plt.axvline(cleaned_df["3P%D"].mean())
    plt.axhline(41)
    plt.xlabel("Opponent 3-Point Percentage Per Game")
    plt.ylabel("Total Wins")
    plt.title("Opponent Three-Point Percentage vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {defensive_3PP_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/defensive_3P_pct_scatterplot.png")
    plt.show()

    cleaned_df["3PA Differential"] = cleaned_df["3PA"] - cleaned_df["Opponent 3PA"]
    plt.figure()
    combined_3PA_correlation = cleaned_df["3PA Differential"].corr(cleaned_df["Wins"])
    plt.scatter(cleaned_df["3PA Differential"], cleaned_df["Wins"])
    plt.axvline(0)
    plt.axhline(41)
    plt.xlabel("Net 3-Pointers Attempted Per Game")
    plt.ylabel("Total Wins")
    plt.title("Net Three-Point Attempts vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {combined_3PA_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/combined_3PA_scatterplot.png")
    plt.show()

    cleaned_df["3PM Differential"] = cleaned_df["3PM"] - cleaned_df["Opponent 3PM"]
    plt.figure()
    combined_3PM_correlation = cleaned_df["3PM Differential"].corr(cleaned_df["Wins"])
    plt.scatter(cleaned_df["3PM Differential"], cleaned_df["Wins"])
    plt.axvline(0)
    plt.axhline(41)
    plt.xlabel("Net 3-Pointers Made Per Game")
    plt.ylabel("Total Wins")
    plt.title("Net Three-Pointers Made vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {combined_3PM_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/combined_3PM_scatterplot.png")
    plt.show()

    cleaned_df["3P% Differential"] = cleaned_df["3P%O"] - cleaned_df["3P%D"]
    plt.figure()
    combined_3PP_correlation = cleaned_df["3P% Differential"].corr(cleaned_df["Wins"])
    plt.scatter(cleaned_df["3P% Differential"], cleaned_df["Wins"])
    plt.axvline(0)
    plt.axhline(41)
    plt.xlabel("Net 3-Point Percentage Per Game")
    plt.ylabel("Total Wins")
    plt.title("Net Three-Point Percentage vs. Team Wins")
    plt.figtext(0.5, 0.01, f"Correlation: {combined_3PP_correlation:.3f}", ha="center")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig("docs/combined_3P_pct_scatterplot.png")
    plt.show()


if __name__ == "__main__":
    main()
