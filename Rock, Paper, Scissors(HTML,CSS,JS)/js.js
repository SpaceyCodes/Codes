let userScore = 0;
let computerScore = 0;
const userScore_span = document.getElementById('user-score');
const computerScore_span = document.getElementById('computer-score');
const scoreBoard_div = document.querySelector('.score-board');
const result_div = document.querySelector('.result > p');
const rock_div = document.getElementById('r');
const paper_div = document.getElementById('p');
const scissors_div = document.getElementById('s');

function getComputerChoice() {
    const choices = ['r', 'p', 's'];
    const randomNumber = (Math.floor(Math.random() * 3));
    return choices[randomNumber];
}

function convertToWord(letter) {
    if (letter == 'r') return 'Rock';
    if (letter == 'p') return 'Paper';
    return 'Scissors';

}

function win(userChoice, computerChoice) {
    userScore++;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    const smallUserWord = 'user'.fontsize(3).sub();
    const smallCompWord = 'Comp'.fontsize(3).sub();
    document.getElementById(userChoice).classList.add('green-glow')
    setTimeout(function() {document.getElementById(userChoice).classList.remove('green-glow')}, 300)
    result_div.innerHTML = `${convertToWord(userChoice)}${smallUserWord} beats ${convertToWord(computerChoice)}${smallCompWord}. You win!`
}
function lose(userChoice, computerChoice) {
    computerScore++;
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    const smallUserWord = 'user'.fontsize(3).sub();
    const smallCompWord = 'Comp'.fontsize(3).sub();
    document.getElementById(userChoice).classList.add('red-glow')
    setTimeout(function() {document.getElementById(userChoice).classList.remove('red-glow')}, 300)
    result_div.innerHTML = `${convertToWord(userChoice)}${smallUserWord} lost to ${convertToWord(computerChoice)}${smallCompWord}. You lost!`
}
function draw(userChoice, computerChoice) {
    userScore_span.innerHTML = userScore;
    computerScore_span.innerHTML = computerScore;
    const smallUserWord = 'user'.fontsize(3).sub();
    const smallCompWord = 'Comp'.fontsize(3).sub();
    document.getElementById(userChoice).classList.add('grey-glow')
    setTimeout(function() {document.getElementById(userChoice).classList.remove('grey-glow')}, 300)
    result_div.innerHTML = `${convertToWord(userChoice)}${smallUserWord} draw against ${convertToWord(computerChoice)}${smallCompWord}. It's a draw.`
}

function game(userChoice) {
    const computerChoice = getComputerChoice();
    switch (userChoice + computerChoice) {
        case 'pr':
        case 'rs':
        case 'sp':
            win(userChoice, computerChoice);
            break;
        case 'ps':
        case 'sr':
        case 'rp':
            lose(userChoice, computerChoice);
            break;
        case 'rr':
        case 'pp':
        case 'ss':
            draw(userChoice, computerChoice);
            break;
    }
}

function main() {
rock_div.addEventListener('click', function() {
    game('r');
})

paper_div.addEventListener('click', function() {
    game('p');
})

scissors_div.addEventListener('click', function() {
    game('s');
})

}

main();






