# Technical Challenge 1: Playlist Management with a Singly
# Linked List.
# Scenario: You’re tasked with developing the back-end for
# a music app’s playlist feature. The app should allow
# users to add songs to the end of their playlist and skip to
# the next song.
# Task: Implement a singly linked list to manage the songs in
# a user’s playlist. The list should support adding songs to the
# end and retrieving the next song to play.
# Operations to be performed on the playlist, such as “add song”
# and “play next”.
# Author: Adriel Ildefonso
# Created: 07/30/2025

import json
import os

json_file = "playlist.json"


class Songs:
    def __init__(self, song_title):
        self.song_title = song_title
        self.next = None


class Playlist:
    def __init__(self):
        self.current = None
        self.last = None

    def add_song(self, song_title):
        new_song = Songs(song_title)
        if not self.current:  # Empty playlist
            self.current = self.last = new_song
        else:
            self.last.next = new_song
            self.last = new_song
        self.save_to_json()
        print(f"\n ✅ Added Song: {song_title} \n")

    def play_next(self):
        if not self.current:
            print(" \n 🛑 No songs left. \n")
            return None
        next_song = self.current.song_title
        self.current = self.current.next
        if not self.current:
            self.tail = None
        self.save_to_json()
        print(f"\n ▶️ Now playing: {next_song} \n")
        return next_song

    def traverse(self):
        if not self.current:
            print("\n ⛔️ Playlist empty \n")
            return None
        current = self.current
        while current:
            print(f"\n - {current.song_title} ")
            current = current.next
        print()

    def to_list(self):
        songs = []
        current = self.current
        while current:
            songs.append(current.song_title)
            current = current.next
        return songs

    def save_to_json(self):
        with open(json_file, 'w') as f:
            json.dump(self.to_list(), f)

    def load_from_json(self):
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                try:
                    song_titles = json.load(f)
                    for title in song_titles:
                        self.add_song(title)
                except json.JSONDecodeError:
                    print("Error Reading 'playlist.json'. "
                        "Starting with an empty playlist")


# Main Program:

playlist = Playlist()
playlist.load_from_json()

while True:
    print("=== Playlist Management ===")
    print("1. Add Song")
    print("2. Play Song")
    print("3. Next Song")
    print("4. Show Playlist")
    print("5. EXIT")
    user_choice = input("Select an option: ")

    if user_choice == "1":
        song = input("Song title: ")
        playlist.add_song(song)
    elif user_choice == "2":
        playlist.play_next()
    elif user_choice == "3":
        playlist.play_next()
    elif user_choice == "4":
        playlist.traverse()
    elif user_choice == "5":
        print("\n ⏹️ Playlist ended. \n")
        break
    else:
        print("\n ❌ Option not valid. \n")