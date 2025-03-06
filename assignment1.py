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

def complete_songs(songs):
    """Mark a song as learned."""

def get_valid_input():
    """Generic input validation function."""

if __name__ == '__main__':
    main()