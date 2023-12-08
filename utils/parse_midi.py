import queue
from collections import OrderedDict

import mido
from mido import MetaMessage, Message, parse_all

from utils.convert import num2note


midi_filepath = "../static/midi/torikago.mid"


class NoteMessage:
    type = None
    channel = 0
    note = 0
    velocity = 64
    time = 0

    def __repr__(self):
        return f"<{self.type} channel={self.channel} " \
               f"note={self.note} velocity={self.velocity} time={self.time}>"


class NoteQueue(queue.Queue):
    pass


def get_note_queue(midi_filepath):
    mid = mido.MidiFile(midi_filepath)

    note_start_times = {}   # 存储音符开始时间的字典
    notes_with_durations = []   # 存储音符及其持续时间的列表

    # 解析MIDI文件中的所有事件
    for msg in mid:
        if not msg.is_meta:
            # 当音符开始时
            if msg.type == 'note_on' and msg.velocity > 0:
                note_start_times[msg.note] = msg.time
            # 当音符结束时
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                start_time = note_start_times.pop(msg.note, None)
                if start_time is not None:
                    duration = msg.time - start_time
                    notes_with_durations.append((msg.note, start_time, duration))

    for note, start_time, duration in notes_with_durations:
        print(f"音符: {num2note(note)}, 开始时间: {start_time}, 持续时间: {duration}")

    count = 1
    note_dict = {}
    for note, start_time, duration in notes_with_durations:
        note_dict[count] = [num2note(note), start_time, duration]   # 音符 开始时间 持续时间
        count = count + 1
    return note_dict


def get_note_or_msg_queue(midi_filepath, get_note=False):
    note_queue = NoteQueue()
    order_dict = OrderedDict()

    with open(midi_filepath, mode='rb') as mfp:
        bytes_mfp = mfp.read()
        parsed_mid = parse_all(bytes_mfp)

    for mi in parsed_mid:
        if mi.type == "note_on" or mi.type == "note_off":
            note_msg = NoteMessage()
            note_msg.type = mi.type
            note_msg.channel = mi.channel
            note_msg.note = num2note(mi.note)
            note_msg.velocity = mi.velocity
            note_msg.time = mi.time
            note_queue.put(note_msg)

    if get_note:
        return note_queue

    count = 1
    while not note_queue.empty():
        note_msg = note_queue.get()
        order_dict[count] = (note_msg.type, note_msg.note, note_msg.time)
        count = count + 1
    return order_dict


def __display():
    note_queue = get_note_or_msg_queue(midi_filepath, get_note=True)

    while not note_queue.empty():
        note_msg = note_queue.get()
        print(note_msg)


if __name__ == "__main__":
    # __display()
    get_note_queue(midi_filepath)
