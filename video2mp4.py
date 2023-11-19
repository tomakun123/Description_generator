from pytube import YouTube

# URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=l3qWU_EAZnQ&t=4s&ab_channel=DevynJohnston"

# Create a YouTube object
yt = YouTube(video_url)

# Choose the stream with the highest resolution
stream = yt.streams.get_highest_resolution()

# Specify the output file path
output_path = ""

# Download the video
stream.download(output_path=output_path, filename="video_file.mp4")

print("Video downloaded successfully!")