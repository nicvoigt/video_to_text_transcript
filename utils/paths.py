import os
import logging
import platform
from pathlib import Path

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
project_folder_dir = os.path.join(desktop_path, "Audio_Transcription")
input_dir = os.path.join(project_folder_dir, "Inputs")
pre_output_dir = os.path.join(project_folder_dir, "Pre_Outputs")
output_dir = os.path.join(project_folder_dir, "Outputs")

paths = [desktop_path, project_folder_dir, input_dir, pre_output_dir, output_dir]

for path in paths:
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)


