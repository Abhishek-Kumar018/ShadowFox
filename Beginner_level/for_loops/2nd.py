total = 100
done = 0

while done < total:
    done = done + 10
    print("You did", done, "jumping jacks")

    if done == total:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/no): ")
    if tired == "yes" or tired == "y":
        print("You completed a total of", done, "jumping jacks")
        break
    else:
        print(total - done, "jumping jacks remaining")
