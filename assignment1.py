"""
Name: Choi Myeongseo
Date started: 5 March 2025
GitHub URL: https://github.com/myoungseo/assignment1
"""
import csv
FILENAME = "songs.csv"
LEARNED = "l"
UNLEARNED = "u"

def main():
    """..."""
    print("Song List 1.0 - by Choi Myeongseo")

def load_songs(FILENAME):
    """Load songs from csv file"""
    songs = []
    try:
        with open(FILENAME,'r') as file:
            for line in file:
                title, artist, year, status = line.strip().split(',')
                songs.append([title, artist, int(year), status])

    except FileNotFoundError:
        print(f"Error: {FILENAME} not found.")
    return songs

def save_songs(songs):
    """Save songs to a csv file"""
    with open(FILENAME, "w") as file:
        for song in songs:
            file.write(f"{song[0]},{song[1]},{song[2]},{song[3]}\n")

def display_songs(songs):
    """Display songs sorted by year and title."""
    from operator import itemgetter
    songs.sort(key=itemgetter(0))
    songs.sort(key=itemgetter(2))

    unlearned_count = sum(1 for song in songs if song[3] == UNLEARNED)

    for i, song in enumerate(songs, start=1):
        mark = "*" if song[3] == UNLEARNED else " "
        print(f"{i}. {mark} {song[0]:30} - {song[1]:20} ({song[2]})")

    print(f"\n{len(songs) - unlearned_count} songs learned, {unlearned_count} songs still to learn.")

def add_songs(songs):
    """Add a new song to the song list."""
    title = input("Title: ").strip()
    if title == "":
        print("Input cannot be blank.")
        return

    artist = input("Artist: ").strip()
    if artist == "":
        print("Input cannot be blank.")
        return

    year = validate_song_number("Year: ", 1, 9999)

    songs.append([title, artist, year, UNLEARNED])
    print(f"{title} by {artist} ({year}) added to song list.")

def complete_songs(songs):
    """Mark a song as learned."""
    unlearned_songs = [song for song in songs if song[3] == UNLEARNED]

    if not unlearned_songs:
        print("No more songs to learn!")
        return

    song_number = validate_song_number("Enter the number of a song to mark as learned: ", 1, len(songs))

    if songs[song_number - 1][3] == LEARNED:
        print(f"You have already learned {songs[song_number - 1][0]}")
    else:
        songs[song_number - 1][3] = LEARNED
        print(f"{songs[song_number - 1][1]}'s '{songs[song_number - 1][0]}' learned!")

def validate_song_number(input_str, min_value, max_value):
    """Generic input validation function."""
    try:
        value = int(input(input_str))
        if min_value <= value <= max_value:
            return value
        print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")
    except ValueError:
        print("Invalid input; enter a valid number.")

if __name__ == '__main__':
    main()