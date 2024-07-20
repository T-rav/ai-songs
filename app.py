from moviepy.editor import *

# Function to create a video from an image and multiple audio files
def create_video_with_multiple_audios(image_path, audio_paths, output_path, fps=24, fade_duration=2.5):
    
    image_clip = ImageClip(image_path)
    
    # Combine audio clips
    audio_clips = [AudioFileClip(audio) for audio in audio_paths]
    
    # Apply fade out to the last audio clip
    if fade_duration > 0:
        audio_clips[-1] = audio_clips[-1].fx(afx.audio_fadeout, fade_duration)
        
    combined_audio = concatenate_audioclips(audio_clips)
    
    image_clip = image_clip.set_duration(combined_audio.duration)
    video_clip = image_clip.set_audio(combined_audio)
    video_clip = video_clip.set_fps(fps)
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

# Paths to the image, multiple audios, and output video file
image_path = "images/tiny terror/Sovereign Slumber.webp"
audio_paths = ["mp3/Sovereign Slumber.m4a"]
output_path = "Mr Fluffles' Sovereign Slumber.mp4"

# Create the video
create_video_with_multiple_audios(image_path, audio_paths, output_path, 0.1)
