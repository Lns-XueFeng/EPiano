# 效果目前不咋地
# 先直接解析midi做出相对应的功能

import sys
import librosa

from sound_to_midi.monophonic import wave_to_midi


file_in = "../static/musics/星空.mp3"
file_out = "../static/midi/星空.mid"

y, sr = librosa.load(file_in, sr=None)
print("载入音乐...")

midi = wave_to_midi(y)
print("音乐转换完成...")

with open(file_out, 'wb') as f:
    midi.writeFile(f)
print("mid文件生产完成...")
