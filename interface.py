from tkinter import *
from video_to_text_transcript.video_to_audio import VidToAud

root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")


    # to transcription here
    print(inputValue)
    v2a = VidToAud(inputValue)
    success_message = v2a.create_audio_file(isExist=v2a.check_if_input_exists())
    print(success_message)
    # outputtext.delete('1', 'end-1c')  # clear the outputtext text widget
    # outputtext.insert(tk.end, success_message)

textBox=Text(root, height=20, width=150)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Transcribir",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()



mainloop()