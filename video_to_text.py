from video_to_text_transcript.video_to_audio import VidToAud
from video_to_text_transcript.audio_text import AudioToText

class TranscriptionProcess:
    def __init__(self, input_path):
        self.v2a = VidToAud(input_path)
        self.a2t = AudioToText(input_path)