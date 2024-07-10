from moviepy.editor import *

# Function to create a video from an image and an audio file
def create_video(image_path, audio_path, output_path, fps=24):
    # Load the image
    image_clip = ImageClip(image_path)
    
    # Load the audio
    audio_clip = AudioFileClip(audio_path)
    
    # Set the duration of the image to match the duration of the audio
    image_clip = image_clip.set_duration(audio_clip.duration)
    
    # Set the audio to the image clip
    video_clip = image_clip.set_audio(audio_clip)
    
    # Set the fps attribute
    video_clip = video_clip.set_fps(fps)
    
    # Write the video file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

# Paths to the image, audio, and output video file
image_path = "images/Mr. Fluffles Fury.png"
audio_path = "mp3/Mr. Fluffles Fury.mp3"
output_path = "Mr. Fluffles Fury.mp4"

# Create the video
create_video(image_path, audio_path, output_path)

