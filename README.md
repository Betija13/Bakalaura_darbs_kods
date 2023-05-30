# Bakalaura_darbs

Koda lapa bakalaura darbam

# Conda envs

See current enviornments: conda info --envs

Create a new env: conda create --name `env_name`

Activate environment: conda activate `env_name`

# Requirements

- python 3.9 (?) at least that is what I did/use
- torch (conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia `https://pytorch.org/get-started/locally/`)
- evaluate (pip install evaluate)
- Whisper (pip install -U openai-whisper)
  - Install base.en model in folder pretrained_models (from: `https://huggingface.co/openai/whisper-base.en/tree/main`)
- transformers (pip install transformers)
- audioread (conda install -c conda-forge audioread)
- tqdm (conda install -c conda-forge tqdm)
- pandas (conda install -c anaconda pandas)
- ffmpeg (conda install -c conda-forge ffmpeg) 
- jpeg(?) (conda install -c conda-forge jpeg)
- pillow(?) (conda install -c anaconda pillow)
- numpy(?) (conda install -c anaconda numpy)
- soundfile (conda install -c conda-forge pysoundfile)
- librosa (install -c conda-forge librosa)
-  (pip install jiwer)
-  (pip install --upgrade accelerate)
- tensorboard (conda install -c conda-forge tensorboard)
- FreeVC (https://github.com/OlaWod/FreeVC/archive/refs/heads/main.zip)
  - under wavlm folder download WavLM Large model
    - https://github.com/microsoft/unilm/tree/master/wavlm
  - webrtcvad (conda install -c conda-forge webrtcvad)
  - create a folder checkpoints and add freevc.pth to it (https://huggingface.co/spaces/OlaWod/FreeVC/tree/main/checkpoints)
- datasets (conda install -c conda-forge datasets)
- DEMUCS DENOISER
  - pip install sphfile
  - pip install pystoi
  - pip install pesq

# Lai pārveidotu audio failus uz mērķa runātāju:
file_for_FreeVC.py <- sataisa failu (nepieciešams lai val.txt un val mapītē atrodas tikai mērķa runātājs un pārējie runātāji ir train/test)

Palaiž convert.py nomainot ... uz iepriekš definēto mapīti (pēc noklusējuma convert_to_pxxx.txt). Var norādīt arī output mapīti (by default freevc_pxxx)

Mapītē freevc_pxxx(?) būs visi pārveidotie faili 

pārvieto arī mērķa runātāja mapīti uz output mapīti (freevc_pxxx)


# Lai iegūtu transcriptus (palaistu whisper_transcripts.py)
Kods, kurš caur whisper uzģenerē atpazīto tekstu


## Pēc pārveidošanas uz target runātāju

Palaiž write_metdata




