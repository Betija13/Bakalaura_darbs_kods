import os
from tqdm import tqdm

path = './FreeVC/output/freevc_269/'
if not os.path.exists(path):
    print("Wrong path!")
    exit()
audio_files = os.listdir(f'{path}')
print(len(audio_files))
for k in audio_files:  # k = audio faili pxxx mapītē
    if 'p315' in k:
        os.remove(f'{path}{k}')
        print(f"Removed {path}{k}")
audio_files = os.listdir(f'{path}')
print(len(audio_files))

print("All done! =)")


