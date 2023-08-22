# Playfy Music Player 

#### Creating a simple music player with playlist management using Python and Streamlit is a great idea! Streamlit is a user-friendly library that allows you to create interactive web applications with minimal code. Here's an outline of how you can achieve this:

## Preview Project
![output](https://github.com/yogesh-hack/playfy_music_player_python_project/assets/83384315/ce1bc933-984b-4f84-a7eb-0062e4347647)


1. **Install Streamlit:**
   Make sure you have Streamlit installed. You can install it using pip:
   ```
   pip install streamlit
   ```

2. **Create Project Structure:**
   Create a directory for your project and organize it like this:
   ```
   music_player/
    ├── mp3_files/
    │   ├── song1.mp3
    │   ├── song2.mp3
    │   └── ...
    ├── default_album_art.jpg
    └── app.py

   ```

3. **Add MP3 Files:**
   Place your MP3 files inside the `mp3_files` folder.

4. **Create Playlist Files:**
   You can create plain text files inside the `playlists` folder to define your playlists. Each line in the file can represent an MP3 file's relative path.

5. **Create the Streamlit App:**
   In the `app.py` file, you can use Streamlit to build the music player interface. Here's a simple example to get you started:

```python
import streamlit as st
import os
from pygame import mixer

def play_song(song_path):
    mixer.init()
    mixer.music.load(song_path)
    mixer.music.play()

def main():
    st.title("Simple Music Player")

    # Get list of playlists
    playlists = os.listdir("playlists")

    selected_playlist = st.sidebar.selectbox("Select Playlist", playlists)

    playlist_path = os.path.join("playlists", selected_playlist)
    songs = open(playlist_path).readlines()

    selected_song = st.selectbox("Select Song", songs)

    song_path = os.path.join("mp3_files", selected_song.strip())

    play_button = st.button("Play")
    if play_button:
        play_song(song_path)

if __name__ == "__main__":
    main()
```

In this example, the Streamlit app allows you to select a playlist from the sidebar, then choose a song from that playlist to play using the "Play" button.

6. **Run the App:**
   Navigate to your project directory in the terminal and run the Streamlit app:
   ```
   streamlit run app.py
   ```

Remember, this is a basic implementation to give you an idea of how to create a music player using Streamlit. You can expand this project by adding more features such as creating new playlists, shuffling songs, volume control, and more. Additionally, you can improve the UI by using Streamlit's interactive widgets and design options.
