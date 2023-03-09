import whisper
import os

model = whisper.load_model("base")
path = './audio_examples'
audio_files = os.listdir(path)
transcripts = open("transcripts.txt", "w")
for i in audio_files:
    result = model.transcribe(audio=f'{path}/{i}', language='en')
    transcripts.write(f'{i}|{result["text"]}\n')
    print(i, ' result: ', result["text"])

transcripts.close()
