from moviepy.editor import *

# Function to create a video from an image and an audio file
def create_video(image_path, audio_path, output_path, fps=24):
    
    image_clip = ImageClip(image_path)
    audio_clip = AudioFileClip(audio_path)
    image_clip = image_clip.set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip = video_clip.set_fps(fps)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

# Paths to the image, audio, and output video file
image_path = "images/Mr. Fluffles' Reign of Tiny Terror.png"
audio_path = "mp3/Mr. Fluffles' Reign of Tiny Terror.mp3"
output_path = "Mr. Fluffles' Reign of Tiny Terror.mp4"

# Create the video
create_video(image_path, audio_path, output_path)

