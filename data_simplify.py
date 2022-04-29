from pycochleagram.pycochleagram.utils import wav_to_array
from pycochleagram.pycochleagram.demo import demo_human_cochleagram

def generate_cochleogram(fname):
    demo_stim, demo_sr = wav_to_array(fname)
    demo_n = 38
    demo_human_cochleagram(demo_stim, demo_sr, demo_n)

generate_cochleogram('vis-data/2015-02-16-16-49-06_denoised.wav')
