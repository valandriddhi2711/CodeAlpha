let secretWord = "";
let displayWord = [];
let guessedLetters = [];
let wrongGuesses = 0;
const maxGuesses = 6;

async function startGame() {
  const response = await fetch("/get_word");
  const data = await response.json();
  secretWord = data.word.toLowerCase();

  displayWord = Array(secretWord.length).fill("_");
  guessedLetters = [];
  wrongGuesses = 0;

  document.getElementById("displayWord").textContent = displayWord.join(" ");
  document.getElementById("guessedLetters").textContent = "None";
  document.getElementById("wrongCount").textContent = "0";
  document.getElementById("message").textContent = "";
}

function guessLetter() {
  const input = document.getElementById("letterInput");
  const letter = input.value.toLowerCase();
  input.value = "";

  if (!letter.match(/[a-z]/i)) {
    alert("Please enter a valid letter!");
    return;
  }
  if (guessedLetters.includes(letter)) {
    alert("You already guessed that letter!");
    return;
  }

  guessedLetters.push(letter);
  document.getElementById("guessedLetters").textContent = guessedLetters.join(", ");

  if (secretWord.includes(letter)) {
    for (let i = 0; i < secretWord.length; i++) {
      if (secretWord[i] === letter) displayWord[i] = letter;
    }
  } else {
    wrongGuesses++;
  }

  document.getElementById("displayWord").textContent = displayWord.join(" ");
  document.getElementById("wrongCount").textContent = wrongGuesses;

  if (!displayWord.includes("_")) {
    document.getElementById("message").textContent = "🎉 You won! The word was " + secretWord;
  } else if (wrongGuesses >= maxGuesses) {
    document.getElementById("message").textContent = "💀 Game Over! The word was " + secretWord;
  }
}

// Start automatically on load
window.onload = startGame;
