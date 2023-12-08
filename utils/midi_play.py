import mido
from pygame import mixer
import time
from convert import num2note

# 初始化pygame混音器
mixer.init()

# 加载音符对应的音频文件
note_sounds = {
    'C2': 'a49.mp3',
    'D2': 'a50.mp3',
    'E2': 'a51.mp3',
    'F2': 'a52.mp3',
    'G2': 'a53.mp3',
    'A2': 'a54.mp3',
    'B2': 'a55.mp3',
    'C3': 'a56.mp3',
    'D3': 'a57.mp3',
    'E3': 'a48.mp3',
    'F3': 'a81.mp3',
    'G3': 'a87.mp3',
    'A3': 'a69.mp3',
    'B3': 'a82.mp3',
    'C4': 'a84.mp3',
    'D4': 'a89.mp3',
    'E4': 'a85.mp3',
    'F4': 'a73.mp3',
    'G4': 'a79.mp3',
    'A4': 'a80.mp3',
    'B4': 'a65.mp3',
    'C5': 'a83.mp3',
    'D5': 'a68.mp3',
    'E5': 'a70.mp3',
    'F5': 'a71.mp3',
    'G5': 'a72.mp3',
    'A5': 'a74.mp3',
    'B5': 'a75.mp3',
    'C6': 'a76.mp3',
    'D6': 'a90.mp3',
    'E6': 'a88.mp3',
    'F6': 'a67.mp3',
    'G6': 'a86.mp3',
    'A6': 'a66.mp3',
    'B6': 'a78.mp3',
    'C7': 'a77.mp3',

    'C#2': 'b49.mp3',
    'D#2': 'b50.mp3',
    'F#2': 'b52.mp3',
    'G#2': 'b53.mp3',
    'A#2': 'b54.mp3',
    'C#3': 'b56.mp3',
    'D#3': 'b57.mp3',
    'F#3': 'b81.mp3',
    'G#3': 'b87.mp3',
    'A#3': 'b69.mp3',
    'C#4': 'b84.mp3',
    'D#4': 'b89.mp3',
    'F#4': 'b73.mp3',
    'G#4': 'b79.mp3',
    'A#4': 'b80.mp3',
    'C#5': 'b83.mp3',
    'D#5': 'b68.mp3',
    'F#5': 'b71.mp3',
    'G#5': 'b72.mp3',
    'A#5': 'b74.mp3',
    'C#6': 'b76.mp3',
    'D#6': 'b90.mp3',
    'F#6': 'b67.mp3',
    'G#6': 'b86.mp3',
    'A#6': 'b66.mp3'
}


# 将MIDI音符编号转换为音符名称
def midi_note_to_name(note_number):
    # 这里应该是将MIDI音符编号转换为音符名称的逻辑
    # 例如：60 -> 'C4'
    return num2note(note_number)


# 播放音符
def play_note(note_name):
    sound_file = "../static/sounds/" + note_sounds.get(note_name)
    if sound_file:
        mixer.music.load(sound_file)
        mixer.music.play()
        while mixer.music.get_busy():  # 等待音频播放完成
            time.sleep(0.1)


# 解析并演奏MIDI文件
def play_midi_file(midi_file_path):
    mid = mido.MidiFile(midi_file_path)
    for msg in mid:
        if not msg.is_meta and msg.type == 'note_on':
            note_name = midi_note_to_name(msg.note)
            play_note(note_name)
            time.sleep(msg.time)  # 根据MIDI文件中的时间间隔等待


# 演奏MIDI文件
play_midi_file('../static/midi/torikago.mid')
