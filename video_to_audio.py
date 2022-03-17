import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import time
import datetime
import os
from video_to_text_transcript.utils import paths
import warnings

class VidToAud:
    def __init__(self, input_path):
        self.input_path = input_path


    def check_if_input_exists(self):
        isExist = os.path.exists(self.input_path)
        print(isExist)
        return isExist


    def create_audio_file(self, isExist):
        if isExist:
            try:
                n = datetime.datetime.now()
                date_time = n.strftime("%d-%m-%Y_%H-%M-%S")

                audioclip = AudioFileClip(self.input_path)
                audio_len = audioclip.duration

                max_dur = 150

                transcribed_audio_file_name = os.path.join(paths.output_dir, f"barbara_medico{date_time}_part.wav")

                if audio_len > max_dur:
                    no_files = math.ceil(audio_len / max_dur)
                    for file_no in range(len(no_files)):
                        clip = audioclip.subclip(max_dur * file_no, max_dur * (file_no + 1))
                        transcribed_audio_file_name = os.path.join(paths.output_dir,f"barbara_medico{date_time}_part{file_no}.wav")
                        clip.write_audiofile(transcribed_audio_file_name, bitrate="50k", fps=8000)
                else:
                    audioclip.write_audiofile(transcribed_audio_file_name, bitrate="50k", fps=8000)
            except:
                return "Patho ok, but some other Error, try again"

            return "Worked out, see the result"

        elif isExist==False:
            return "Some Error, try again"

