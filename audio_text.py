import os
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from video_to_text_transcript.utils import paths


name_audio_file = "barbara_medico.wav"

class AudioToText:
    def __init__(self, input_name):
        pass

    def clean_input_name(self, input_name):
        return input_name.split(".")[0]

    def create_text_from_audio(self, input_name):

        with contextlib.closing(wave.open(input_name,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            total_duration = math.ceil(duration / 60)
        r = sr.Recognizer()
        cleaned_name = self.clean_input_name(input_name)
        for i in range(0, total_duration):
            with sr.AudioFile(input_name) as source:
                audio = r.record(source, offset=i*60, duration=60)
            f = open(os.path.join(paths.output_dir,cleaned_name), "a")
            f.write(r.recognize_google(audio,language="pt-BR"))
            f.write(" ")
        f.close()


a2t = AudioToText()
a2t.clean_input_name(name_audio_file)