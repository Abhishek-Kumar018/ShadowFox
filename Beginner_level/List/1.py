justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# the number of members in the Justice League.
num_members = len(justice_league)
print("Number of members:", num_members)

#2) Adding Batgirl and Nightwing 
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding new members:", justice_league)

#3)remove the wonder women from list and add her at the beginning of the list 
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)

#4) Separate Aquaman and Flash
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Superman")
print("After separating Flash and Aquaman:", justice_league)

#5)Replacing the existing list with the new list 
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
justice_league[:] = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

#6)after sorting and the 0th index will be the new leader
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("The new leader is:", justice_league[0])





