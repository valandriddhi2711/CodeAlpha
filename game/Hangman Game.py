from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

WORDS = ["python", "flask", "hangman", "developer", "programming"]

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Hangman Game</title>
    <style>
        body { font-family: Arial; background-color: #f9f9f9; text-align: center; margin-top: 50px; }
        h1 { color: #333; }
        .word { font-size: 28px; letter-spacing: 10px; margin: 20px; }
        .message { font-size: 22px; color: red; margin: 20px; }
        input { font-size: 18px; padding: 5px; }
        button { font-size: 18px; margin-left: 10px; }
    </style>
</head>
<body>
    <h1>🎯 Hangman Game</h1>
    <div class="word" id="word"></div>
    <p>Wrong guesses: <span id="wrong">0</span>/6</p>
    <input type="text" id="guess" maxlength="1" placeholder="Enter a letter">
    <button onclick="makeGuess()">Guess</button>
    <div class="message" id="message"></div>

    <script>
        let word = "";
        let guessed = [];
        let wrongGuesses = 0;

        async function startGame() {
            const res = await fetch("/new_word");
            const data = await res.json();
            word = data.word;
            guessed = Array(word.length).fill("_");
            wrongGuesses = 0;
            document.getElementById("word").innerText = guessed.join(" ");
            document.getElementById("wrong").innerText = wrongGuesses;
            document.getElementById("message").innerText = "";
        }

        async function makeGuess() {
            const input = document.getElementById("guess");
            const letter = input.value.toLowerCase();
            input.value = "";

            if (!letter.match(/[a-z]/) || letter.length !== 1) return;

            if (word.includes(letter)) {
                for (let i = 0; i < word.length; i++) {
                    if (word[i] === letter) guessed[i] = letter;
                }
            } else {
                wrongGuesses++;
                document.getElementById("wrong").innerText = wrongGuesses;
            }

            document.getElementById("word").innerText = guessed.join(" ");

            if (guessed.join("") === word) {
                document.getElementById("message").innerText = "🎉 You win! Starting new game...";
                setTimeout(startGame, 2000);
            } else if (wrongGuesses >= 6) {
                document.getElementById("message").innerText = "💀 You lost! The word was: " + word + ". Restarting...";
                setTimeout(startGame, 3000);
            }
        }

        startGame();
    </script>
</body>
</html>
''')

@app.route('/new_word')
def new_word():
    return jsonify({"word": random.choice(WORDS)})

if __name__ == "__main__":
    app.run(debug=True)
