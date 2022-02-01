import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip

transcribed_audio_file_name = "transcribed_speech_test.wav"
zoom_video_file_name = "video.mp4"

audioclip = AudioFileClip(zoom_video_file_name)
# audioclip # getting only first 5 seconds
clip = audioclip.subclip(0, 60)
clip.write_audiofile(transcribed_audio_file_name,bitrate="50k", fps=8000)