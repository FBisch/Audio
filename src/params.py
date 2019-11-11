# General variables
DATA_PATH = '../data/'
AUDIO_FORMAT = '.wav'

# STFT parameters
FS = 16000
WINDOW_SIZE = 128
OVERLAP_PERCENTAGE = 50

# Fast RLS algorithm parameters
d = 12
L = 3
FORGETTING_FACTOR = 0.993
DELTA = 0.1
