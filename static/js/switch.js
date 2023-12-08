let selected = document.querySelector("#mid_sec");
let selected_index = selected.selectedIndex;
let selected_value = selected.options[selected_index].value;

let midi_filename = selected_value;
let auto_piano_btn = document.querySelector("#autopiano");

auto_piano_btn.addEventListener("click", function () {
    let xhr = new XMLHttpRequest();
    xhr.open("get", "/api/midi/" + midi_filename);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            try {
                // 处理数据
                let res = JSON.parse(xhr.responseText);
                playMidi(res);
                console.log(res);
            } catch (e) {
                console.error("解析MIDI数据时发生错误:", e);
            }
        }
    };
    xhr.send();
});

function playMidi(midiData) {
    let currentTime = 0;
    for (let key in midiData) {
        let note_value_array = midiData[key];
        let note = note_value_array[0];
        let start_time = note_value_array[1];
        let duration = note_value_array[2];
        if (note === "null") { continue; }
        // 使用闭包来保持每个setTimeout的note和duration
        (function(note, duration) {
            setTimeout(function () {
                let piano_key = document.querySelector(`.piano-key[data-name="${note}"]`);
                if (piano_key) {
                    // 模拟按下钢琴键
                    piano_key.classList.add('active');
                    // 设置一个定时器来模拟松开钢琴键
                    setTimeout(function() {
                        piano_key.classList.remove('active');
                    }, duration);
                }
            }, currentTime + start_time);
        })(note, duration);
        currentTime += start_time;
    }
}
