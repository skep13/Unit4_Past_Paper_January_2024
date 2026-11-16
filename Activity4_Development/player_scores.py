# Games Club Player Scores
# Records scores and times then shows highest score and average time and saves to a file

MIN_GAMES = 5
MAX_GAMES = 10
MIN_TIME = 5
MAX_TIME = 60
FILE_NAME = "player_scores.txt"


def get_number(prompt, minimum, maximum):
    # Keeps asking until a whole number in the range is entered
    while True:
        entry = input(prompt)
        if not entry.isdigit():
            print("Please enter a whole number")
        elif int(entry) < minimum or int(entry) > maximum:
            print("Please enter a number from", minimum, "to", maximum)
        else:
            return int(entry)


def get_player_id():
    player_id = input("Enter the player ID: ")
    while player_id == "":
        print("The player ID cannot be blank")
        player_id = input("Enter the player ID: ")
    return player_id


def main():
    player_id = get_player_id()
    number_of_games = get_number("Enter the number of games played: ", MIN_GAMES, MAX_GAMES)

    # Lists used as number of games can change
    scores = []
    times = []
    for game in range(1, number_of_games + 1):
        print("Game", game)
        # The brief gives no score limit so 0 to 1000000 is used
        scores.append(get_number("Enter the score: ", 0, 1000000))
        times.append(get_number("Enter the time in minutes: ", MIN_TIME, MAX_TIME))

    highest_score = max(scores)
    # Rounds halves up as round gave 22 not 23 in test 8
    average_time = int(sum(times) / len(times) + 0.5)

    print()
    print("Player ID:", player_id)
    print("Highest score:", highest_score)
    print("Average time spent playing:", average_time, "minutes")

    # Append so earlier players are kept
    file = open(FILE_NAME, "a")
    file.write("Player ID: " + player_id + "\n")
    file.write("Scores: " + str(scores) + "\n")
    file.write("Times: " + str(times) + "\n")
    file.write("Highest score: " + str(highest_score) + "\n")
    file.write("Average time: " + str(average_time) + " minutes\n\n")
    file.close()
    print("Data saved to", FILE_NAME)


main()
