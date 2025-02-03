# audio-suite

## Audio Processing Pipeline

This document describes the steps involved in the audio processing pipeline.

### Step 1: Individual Packets of Audio Data
Audio data is received in individual packets. Each packet contains a small segment of the audio signal.

### Step 2: Concatenation and Preprocessing
The stream of audio packets is concatenated to form a continuous audio sequence. This sequence is then preprocessed to remove noise and enhance the quality of the audio signal.

### Step 3: Segmentation and Classification
The preprocessed audio sequence is segmented into smaller chunks. Each segment is classified to determine the type of audio content it contains (e.g., speech, music, silence).

### Step 4: Speech and Phonemes Extraction
Segments identified as human speech are processed to extract text and phonemes. This involves converting the audio signal into a textual representation and identifying the phonetic components.

### Step 5: Alignment with Original Audio Signal
The sequences of text and phonemes are aligned with the original audio signal. This ensures that the textual and phonetic representations correspond accurately to the audio.

### Step 6: Evaluation by LLM Model
The complete sequence is evaluated by a Large Language Model (LLM) to construct coherent sentences. The model aims to preserve the expression and meaning of the original extracted text as much as possible.


## LLM recommendation

### Step 3: Segmentation and Classification
pyannote.audio: A toolkit for speaker diarization and segmentation.
Wave-U-Net: A model for end-to-end audio source separation.
VGGish: A feature extraction model for audio classification.

### Text and Phoneme Extraction
DeepSpeech: An open-source Speech-To-Text engine.
Wav2Vec 2.0: A framework for self-supervised learning of speech representations.
Tacotron 2: A neural network architecture for speech synthesis.




General Points
- The Text and Phoneme extraction are seperate
- Bidirectional Models are not applicable
- Phoneme recognition and speech activation recognition can be combined ?
- Vave2Vec2Phoneme is a model that exist


## Datasets

### [Audio Set](https://paperswithcode.com/dataset/audioset)
- 2 Million, 10s Video clips, 632 Classes
- classification can be aided by this but the youtube videos have to be downloaded I assume, also the video is not very usefull for my use case

### [Common Voice](https://paperswithcode.com/dataset/common-voice)
- MP3/Text, 9283 Hours, Demographic Data, 60 Languages
- Common Voice German is very interesting for a german finetuning dataset

### [Speech Commands](https://paperswithcode.com/dataset/speech-commands) - Keyword spotting
- not relevant for the beginning
- later on I can use this for training a zero shot classifier with generalization to unseen commands from a generalized pre-trained vector encoding, maybe.

### [ESC-50](https://paperswithcode.com/dataset/esc-50) - 2000 Environmental Recordings, 5s, 50 classes
- Very usefull for step 2 - preprocessing
- The sound can be choped up and toknized to train a audio classification model on my own

### [VGG-Sound](https://paperswithcode.com/dataset/vgg-sound)
- 210k videos, 310 audio classes

### [FSD50K Freesound Database 50K](https://paperswithcode.com/dataset/fsd50k)
- 50,197 Freesound CLips, 200 Classes

### [Clotho](https://paperswithcode.com/dataset/clotho)
- 4981 Audio Samples, 15-30s
- 5 Captions per clip, 8-20 Words long captions

### [TED-LIUM](https://paperswithcode.com/dataset/ted-lium-3)
- TED Talks, 16kHz, 118-452H Transcribed Speech Data
