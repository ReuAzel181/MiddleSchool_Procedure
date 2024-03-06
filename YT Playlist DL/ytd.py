import os
import youtube_dl

# URL of the playlist
playlist_url = 'https://www.youtube.com/watch?v=BNYJQaZUDrI&list=PL8dPuuaLjXtNgK6MZucdYldNkMybYIHKR'

# Directory to save the downloaded videos
output_dir = 'videos'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Options for downloading videos and thumbnails
ydl_opts = {
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'writeinfojson': True,
    'writethumbnail': True,
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
}

# Download the playlist
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

    
    
    