import pandas as pd 
import matplotlib.pyplot as plt 

weights = {
    "CP": 5,
    "GT": 3,
    "C": 10,
    "DC": -5,
    "ST": 8,
    "RO": 7,
    "MRO": -7,
    "DH": 6
}

num_players = int(input("Enter the number of players you want to record data for: "))
players = []
for i in range(num_players):
    name = input(f"Enter name of Player {i+1}: ")
    players.append(name)

fielding_data = []

for player in players:
    num_balls = int(input(f"\nEnter number of balls to record for {player}: "))

    for i in range(num_balls):
        print(f"\n--- Ball {i+1} for {player} ---")
        match_no = input("Match No.: ")
        innings = input("Innings: ")
        team = input("Team fielding: ")
        overcount = input("Over number: ")
        ballcount = input("Ball number in over: ")
        venue = input("Venue: ")
        position = input("Player's Position: ")
        short_desc = input("Short Description: ")

        print("\nPick Options:")
        print("CP = Clean Pick")
        print("GT = Good Throw")
        print("C  = Catch")
        print("DC = Dropped Catch")
        print("None")
        pick = input("Pick: ")

        print("\nThrow Options:")
        print("RO  = Run Out")
        print("MRO = Missed Run Out")
        print("ST  = Stumping")
        print("DH  = Direct Hit")
        print("None")
        throw = input("Throw: ")

        runs = int(input("Runs saved/conceded (+/-): "))

        CP = 1 if pick.upper() == "CP" else 0
        GT = 1 if pick.upper() == "GT" else 0
        C = 1 if pick.upper() == "C" else 0
        DC = 1 if pick.upper() == "DC" else 0
        ST = 1 if throw.upper() == "ST" else 0
        RO = 1 if throw.upper() == "RO" else 0
        MRO = 1 if throw.upper() == "MRO" else 0
        DH = 1 if throw.upper() == "DH" else 0

        PS = (CP*weights["CP"]) + (GT*weights["GT"]) + (C*weights["C"]) + \
             (DC*weights["DC"]) + (ST*weights["ST"]) + (RO*weights["RO"]) + \
             (MRO*weights["MRO"]) + (DH*weights["DH"]) + runs

        fielding_data.append({
            "Match No": match_no,
            "Innings": innings,
            "Team": team,
            "Player Name": player,
            "Over": overcount,
            "Ball": ballcount,
            "Position": position,
            "Description": short_desc,
            "Pick": pick,
            "Throw": throw,
            "Runs": runs,
            "PS": PS
        })

df = pd.DataFrame(fielding_data)

excel_file = "Cricket_Fielding_Analysis.xlsx"
df.to_excel(excel_file, index=False)
print(f"\nData saved successfully to {excel_file}!")

summary = df.groupby("Player Name")["PS"].sum().reset_index()
summary = summary.sort_values(by="PS", ascending=False).reset_index(drop=True)

summary.index = summary.index + 1

print("\n--- Player Performance Summary ---")
print(summary)

plt.figure(figsize=(8,5))
plt.bar(summary["Player Name"], summary["PS"], color="skyblue")
plt.xlabel("Player Name")
plt.ylabel("Total Performance Score (PS)")
plt.title("Cricket Fielding Performance Summary")
plt.xticks(rotation=0)
plt.ylim(min(0, summary["PS"].min()-5), summary["PS"].max()+5)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

input("\nPress Enter to exit...")

