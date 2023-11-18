let kv_map = new Map([
    ["1", "C2"],
    ["2", "D2"],
    ["3", "E2"],
    ["4", "F2"],
    ["5", "G2"],
    ["6", "A2"],
    ["7", "B2"],
    ["8", "C3"],
    ["9", "D3"],
    ["0", "E3"],

    ["Q", "F3"],
    ["W", "G3"],
    ["E", "A3"],
    ["R", "B3"],
    ["T", "C4"],
    ["Y", "D4"],
    ["U", "E4"],
    ["I", "F4"],
    ["O", "G4"],
    ["P", "A4"],

    ["A", "B4"],
    ["S", "C5"],
    ["D", "D5"],
    ["F", "E5"],
    ["G", "F5"],
    ["H", "G5"],
    ["J", "A5"],
    ["K", "B5"],
    ["L", "C6"],

    ["Z", "D6"],
    ["X", "E6"],
    ["C", "F6"],
    ["V", "G6"],
    ["B", "A6"],
    ["N", "B6"],
    ["M", "C7"],
    ["SHIFT", " "],
    // ["虫洞OG80", " "]
]);
let vk_map = new Map();
for (let k of kv_map.keys()) {
    vk_map.set(kv_map.get(k), k);
}

window.onload = function(){
    document.onkeydown = function(event) {
        let current_key = event.key.toUpperCase();
        let switch_btn = document.querySelector("#switch");
        if (current_key == " ") { return }
        if (switch_btn.name == "keyboard") {
            let keys = document.querySelectorAll(".keys");
            let input_array = new Array();
            for (let key of keys) {
                for (let input of key.children) {
                        input_array.push(input);
                }
            }
            for (let input of input_array) {
                if (current_key == "!" && input.value == "1") {
                    input.style.backgroundColor = "red";
                }
                if (current_key == "@" && input.value == "2") {
                    input.style.backgroundColor = "red";
                }
                if (current_key == "$" && input.value == "4") {
                    input.style.backgroundColor = "red";
                }
                if (current_key == "%" && input.value == "5") {
                    input.style.backgroundColor = "red";
                }
                if (current_key == "^" && input.value == "6") {
                    input.style.backgroundColor = "red";
                }
                if (current_key == "*" && input.value == "8") {
                    input.style.backgroundColor = "red";
                }
                if (current_key == "(" && input.value == "9") {
                    input.style.backgroundColor = "red";
                }
                if (input.value == current_key) {
                    input.style.backgroundColor = "red";
                }
            }
        }
        if (switch_btn.name == "music_note") {
            let keys = document.querySelectorAll(".keys");
            let input_array = new Array();
            for (let key of keys) {
                for (let input of key.children) {
                        input_array.push(input);
                }
            }
            for (let input of input_array) {
                if (input.value == kv_map.get(current_key)) {
                    input.style.backgroundColor = "red";
                }
            }
        }
    };

    document.onkeyup = function(event) {
        let current_key = event.key.toUpperCase();
        let switch_btn = document.querySelector("#switch");
        if (switch_btn.name == "keyboard") {
            let keys = document.querySelectorAll(".keys");
            let input_array = new Array();
            for (let key of keys) {
                for (let input of key.children) {
                        input_array.push(input);
                }
            }
            for (let input of input_array) {
                if (current_key == "!" && input.value == "1") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (current_key == "@" && input.value == "2") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (current_key == "$" && input.value == "4") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (current_key == "%" && input.value == "5") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (current_key == "^" && input.value == "6") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (current_key == "*" && input.value == "8") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (current_key == "(" && input.value == "9") {
                    input.style.backgroundColor = "#dde1e7";
                }
                if (input.value == current_key) {
                    input.style.backgroundColor = "#dde1e7";
                    if (current_key == "SHIFT") {
                        input.style.backgroundColor = "#A0A0A0";
                        input.style.width = "10.75%";
                    }
                }
            }
        }
        if (switch_btn.name == "music_note") {
            let keys = document.querySelectorAll(".keys");
            let input_array = new Array();
            for (let key of keys) {
                for (let input of key.children) {
                        input_array.push(input);
                }
            }
            for (let input of input_array) {
                if (input.value == kv_map.get(current_key)) {
                    input.style.backgroundColor = "#dde1e7";
                    if (current_key == "SHIFT") {
                        input.style.backgroundColor = "#A0A0A0";
                        input.style.width = "10.75%";
                    }
                }
            }
        }
    }

    let switch_btn = document.querySelector("#switch");
    switch_btn.onclick = function(event) {
        if (switch_btn.name == "keyboard") {
            let keys = document.querySelectorAll(".keys");
            let input_array = new Array();
            for (let key of keys) {
                for (let input of key.children) {
                    input_array.push(input);
                }
            }
            for (let input of input_array) {
                if (kv_map.has(input.value)) {
                    console.log(input.value);
                    input.value = kv_map.get(input.value);
                }
            }
            switch_btn.name = "music_note";
            switch_btn.src = "/static/images/music-note.svg";
            let shift_btn = document.querySelector("#shift");
            shift_btn.style.width = "10.75%";
            return
        }
        if (switch_btn.name == "music_note") {
            let keys = document.querySelectorAll(".keys");
            let input_array = new Array();
            for (let key of keys) {
                for (let input of key.children) {
                    input_array.push(input);
                }
            }
            console.log(input_array);
            for (let input of input_array) {
                if (vk_map.has(input.value)) {
                    console.log(input.value);
                    input.value = vk_map.get(input.value);
                }
            }
            switch_btn.name = "keyboard";
            switch_btn.src = "/static/images/keyboard.svg";
            let shift_btn = document.querySelector("#shift");
            shift_btn.style.width = "10.75%";
            return
        }
    }
};