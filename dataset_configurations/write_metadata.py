import csv
import os
import audioread
from tqdm import tqdm
import pandas as pd

rewrite_metadata = False
path = './datasets/VCTK/' # GPU
# path = '../../datasets/VCTK-Corpus-0.92/' #LOCAL
if not os.path.exists(path):
    print("Wrong path!")
    exit()
# VCTK -> test/train/val
# test/train/val -> pxxx
# pxxx -> audio faili
train_test_val_folders = os.listdir(path)
for i in train_test_val_folders: # i = test/train/val
    if i == 'test' or i == 'train' or i =='val':
        speaker_folders = os.listdir(f'{path}{i}')
        print(f"{i} start:")
    else:
        print(f"{i} Not train/test/val")
        continue
    for j in tqdm(speaker_folders):  # j = pxxx
        if j == 'p315':
            print("Text files for p315 do not exist, continue")
            continue
        # path_to_txt = f'{path}txt/{j}' #LOCAL
        path_to_txt = f'./FreeVC/data/txt/{j}' #GPU
        path_to_audio = f'{path}{i}/{j}'
        if not os.path.exists(path_to_txt):
            print("Wrong txt path!")
            print(path_to_txt)
            exit()
        if not os.path.exists(path_to_audio):
            print("Wrong audio path!")
            exit()
        txt_files = os.listdir(path_to_txt)
        audio_files = os.listdir(path_to_audio)
        if os.path.exists(f'{path_to_audio}/metadata.csv') and not rewrite_metadata:
            print(f"Metadata file for {j} already exists")
            if len(audio_files)-1 > len(pd.read_csv(f'{path_to_audio}/metadata.csv')):
                print(" But there are some audio files missing")
            else:
                print(" And all files are there (by count)")
                continue

        f = open(f'{path_to_audio}/metadata.csv', 'w', newline='')

        writer = csv.writer(f)
        header = ['file_name', 'transcription', 'file_len', 'speaker_file']
        writer.writerow(header)


        for k in txt_files:
            file_name = f"{k.split('.')[0]}_mic1.flac"
            if not os.path.exists(f"{path_to_txt}/{k}"):
                print(f"Weird, the path to txt does not exist for {path_to_txt}/{k}")
            transcript_file = open(f"{path_to_txt}/{k}", "r")
            transcription = transcript_file.readlines()[0].rstrip('\n').strip()
            if not os.path.exists(f"{path_to_audio}/{file_name}"):
                print(f"Weird, the audio {file_name} doesn't exist on path: {path_to_audio}/{file_name}")
                transcript_file.close()
                continue
            audio_file = audioread.audio_open(f"{path_to_audio}/{file_name}")
            file_len = audio_file.duration
            speaker_file = k.split('.')[0]
            data = [file_name, transcription, file_len, speaker_file]
            writer.writerow(data)
            transcript_file.close()
            audio_file.close()
        f.close()




