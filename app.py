import streamlit as st
import os
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Get list of MP3 files and album art images
mp3_files = [file for file in os.listdir("mp3_files") if file.endswith(".mp3")]
album_art_files = [file for file in os.listdir("album_art") if file.endswith((".jpg", ".png"))]

# Create a dictionary to map song filenames to album art filenames
song_to_album_art = {}
for song in mp3_files:
    song_name = os.path.splitext(song)[0]
    for album_art in album_art_files:
        if song_name in album_art:
            song_to_album_art[song] = album_art


def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()


def main():
    st.title("🎵Playfy Music Player 🎶")

    st.sidebar.title("Search Song")
    search_query = st.sidebar.text_input("Search for a song:")

    filtered_mp3_files = [file for file in mp3_files if search_query.lower() in os.path.splitext(file)[0].lower()]

    st.header("All Songs:")

    current_song_index = st.session_state.get("current_song_index", 0)

    st.sidebar.title("Playlist")
    song_selection = st.radio("Select Song", filtered_mp3_files, index=current_song_index)

    st.sidebar.audio("mp3_files/" + song_selection, format="audio/mp3", start_time=0)

    # Get the current song's album art image
    current_song = filtered_mp3_files[current_song_index]
    album_art_image = song_to_album_art.get(current_song, "default.gif")
    album_art_path = f"album_art/{album_art_image}"

    st.sidebar.image(album_art_path, use_column_width=True)

    st.success(f"Now playing: {song_selection}")

    if st.button("⏮️ Previous") and current_song_index > 0:
        current_song_index -= 1
    if st.button("⏭️ Next") and current_song_index < len(filtered_mp3_files) - 1:
        current_song_index += 1

    st.session_state.current_song_index = current_song_index


if __name__ == "__main__":
    main()
