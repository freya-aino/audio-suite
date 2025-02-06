import silero_vad
import torch as T

def load_silero_vad():
    T.set_num_threads(1)
    model, utils = T.hub.load(repo_or_dir='snakers4/silero-vad', model='silero_vad')

    print(utils)
    
    (get_speech_timestamps, _, read_audio, _, _) = utils

    return model, get_speech_timestamps, read_audio

