import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats


def main():
    print("NBA Three-Point Strategy Analyzer")
    print("---------------------------------")

    print("Connecting to NBA statistics database...")

    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season="2025-26",
        season_type_all_star="Regular Season",
        per_mode_detailed="PerGame",
        timeout=60
    )

    stats_df = team_stats.get_data_frames()[0]

    print("Successfully retrieved team statistics!")
    print("Number of teams:", len(stats_df))

    print("\nAvailable statistics:")
    print(stats_df.columns.tolist())

    print("\nFirst five teams:")
    print(stats_df.head())


if __name__ == "__main__":
    main()
