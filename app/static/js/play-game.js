/*!
	* Toasts
	* 
	* 
*/

var questionList = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
];

var activeQuestion = 0;
var correctAnswer = 'a-0';
var renewTimer = false;

if (document.readyState == 'loading') 
{
    document.addEventListener('DOMContentLoaded', main)
} 
else 
{
    main()
}

function main() {
    try {$('#passedModal').modal({backdrop: 'static'});}
    catch {}

    let startBut = document.querySelector('#show-question');
    startBut.addEventListener('click', showQuestion);
}

function showQuestion() {
    let startBut = document.querySelector('#show-question');
    let readyMessage = document.querySelector('#ready-msg');
    
    startBut.classList.add('d-none');
    readyMessage.classList.add('d-none');

    if(questionList.length < 1) {
        finishGame();
        return;
    }
    
    let randomIndex = Math.floor(Math.random() * questionList.length);
    let randomQuestion = questionList.splice(randomIndex, 1)[0];

    let qID = '#q-' + randomQuestion;
    let nextId = '#n-' + randomQuestion;
    activeQuestion = randomQuestion;
    correctAnswer = 'a-' + randomQuestion;

    let chosenQuestion = document.querySelector(qID);
    chosenQuestion.classList.remove('d-none');

    let nextQuestion = document.querySelector(nextId);
    nextQuestion.classList.remove('d-none');
    nextQuestion.addEventListener('click', gotoNext);

    let timer = document.querySelector('.timer');
    timer.classList.remove('d-none');
    countDown();

    let answerButs = document.querySelectorAll('.ans-btn');
    for(let i = 0; i < answerButs.length; i++) {
        answerButs[i].addEventListener('click', checkAnswer);
    }
}

function countDown() {
    let startBut = document.querySelector('#show-question');
    let readyMessage = document.querySelector('#ready-msg');
    let qId = '#q-'+ activeQuestion;
    let nextId = '#n-' + activeQuestion;
    let timeId = '#timesup-'+ activeQuestion;
    let question = document.querySelector(qId);
    let nextQuestion = document.querySelector(nextId);
    let timeMessage = document.querySelector(timeId);

    let timerElement = document.querySelector('.timer');
    let timerValue = document.querySelector('#timer-val').value;
    let timeInSeconds = timerValue * 60;
    timerElement.innerHTML = '0' + timerValue + ':00';
    timerElement.classList.remove('text-danger');

    let timer = setInterval(() => {
        // Decrement the time by 1 second
        timeInSeconds--;
      
        // Convert the time to minutes and seconds
        let minutes = Math.floor(timeInSeconds / 60);
        let seconds = timeInSeconds % 60;
      
        // Add leading zeros if necessary
        if (minutes < 10) {
          minutes = '0' + minutes;
        }
        if (seconds < 10) {
          seconds = '0' + seconds;
        }
      
        // Update the timer element
        timerElement.innerHTML = minutes + ':' + seconds;

        if((minutes == 0) && (seconds < 30)) {
            timerElement.classList.add('text-danger');
        }
      
        // Stop the timer when time is up
        if (timeInSeconds == 0) {
            clearInterval(timer);
            timeMessage.classList.remove('d-none');
            question.classList.add('d-none');
            nextQuestion.classList.add('d-none');
            timerElement.classList.add('d-none');
            setTimeout(() => {
                timeMessage.classList.add("d-none");
                startBut.classList.remove('d-none');
                readyMessage.classList.remove('d-none');
              
            }, 2000);
        }

        if(renewTimer) {
            clearInterval(timer);
            renewTimer = false;
            timeInSeconds = timerValue * 60;
        }
    }, 1000);
}

function checkAnswer(e) {
    let startBut = document.querySelector('#show-question');
    let readyMessage = document.querySelector('#ready-msg');
    let qId = '#q-'+ activeQuestion;
    let nextId = '#n-' + activeQuestion;
    let passId = '#pass-'+ activeQuestion;
    let failedId = '#failed-'+ activeQuestion;
    let question = document.querySelector(qId);
    let nextQuestion = document.querySelector(nextId);
    let passMessage = document.querySelector(passId);
    let failedMessage = document.querySelector(failedId);
    let timer = document.querySelector('.timer');

    let answer = e.target;
    if(answer.id === correctAnswer) {
        answer.classList.remove('btn-outline-primary');
        answer.classList.add('btn-success');
        answer.disabled = true;

        passMessage.classList.remove('d-none');
        question.classList.add('d-none');
        nextQuestion.classList.add('d-none');
        timer.classList.add('d-none');
        setTimeout(() => {
            passMessage.classList.add("d-none");
            startBut.classList.remove('d-none');
            readyMessage.classList.remove('d-none');
            renewTimer = true;
          
        }, 2000);
    }
    else {
        failedMessage.classList.remove('d-none');
        question.classList.add('d-none');
        nextQuestion.classList.add('d-none');
        timer.classList.add('d-none');
        setTimeout(() => {
            failedMessage.classList.add("d-none");
            startBut.classList.remove('d-none');
            readyMessage.classList.remove('d-none');
            renewTimer = true;
          
        }, 2000);
    }
}

function gotoNext(e) {
    let startBut = document.querySelector('#show-question');
    let readyMessage = document.querySelector('#ready-msg');
    let qId = '#q-'+ activeQuestion;
    let nextId = '#n-' + activeQuestion;
    let question = document.querySelector(qId);
    let nextQuestion = document.querySelector(nextId);
    let timer = document.querySelector('.timer');

    question.classList.add('d-none');
    nextQuestion.classList.add('d-none');
    timer.classList.add('d-none');

    startBut.classList.remove('d-none');
    readyMessage.classList.remove('d-none');

    renewTimer = true;
}

function finishGame() {
    let quizId = document.querySelector('#quiz-id').value;
    let endMessage = document.querySelector('#end-msg');
    let starMessage = document.querySelector('#star-msg');
    let backHomeBut = document.querySelector('#back-home');
    let answerButs = document.querySelectorAll('.ans-btn');
    let star = 0;
    let totalCorrect = 0;
    let correcIds = []
    let winState = [
        ['a-1', 'a-4', 'a-6', 'a-7', 'a-8'],
        ['a-1', 'a-2', 'a-3', 'a-5', 'a-8'],
        ['a-3', 'a-5', 'a-8', 'a-7', 'a-6'],
        ['a-1', 'a-2', 'a-3', 'a-4', 'a-6']
    ]

    for(let i = 0; i < answerButs.length; i++) {
        if(answerButs[i].classList.contains('btn-success')) {
            totalCorrect++;
            correcIds.push(answerButs[i].id)
        }
        answerButs[i].removeEventListener('click', checkAnswer);
    }

    if((totalCorrect >= 7) || ((totalCorrect == 5) && (winState.some(arr => JSON.stringify(arr) === JSON.stringify(correcIds))))) {
        console.log('you win++++')
        star = 3;
    }
    else if(totalCorrect == 6) {
        let tempArr = [...correcIds];
        for(let i = 0; i < tempArr.length; i++) {
            tempArr.splice(i, 1);
            if(winState.some(arr => JSON.stringify(arr) === JSON.stringify(tempArr))) {
                star = 3;
                break;
            }
            else {
                tempArr = [...correcIds];
            }
        }
        if(star != 3) {
            star = 2;
        }

    }
    else if((totalCorrect <= 5) && (totalCorrect > 0)) {
        if(totalCorrect > 3) {
            star = 2;
        }
        else {
            star = 1;
        }
    }
    else {
        star = 0;
    }

    endMessage.classList.remove('d-none');
    starMessage.classList.remove('d-none');
    let endText = '';
    switch(star) {
        case 3:
            endText = 'کارت عالی بود موفق شدی ' + star.toString() + ' ستاره بدست بیاری';
            break;
        case 2:
            endText = 'کارت خوب بود موفق شدی ' + star.toString() + ' ستاره بدست بیاری';
            break;
        case 1:
            endText = 'میتونستی بهتر باشی ولی اشکال نداره بازم تونستی ' + star.toString() + ' ستاره بدست بیاری';
            break;
        default:
            endText = 'هیچ ستاره ای بدست نیاوردی، اشکال نداره. با تلاش و پشتکار تمرینای بیشتری حل کن';
    }
    starMessage.innerHTML = endText;
    backHomeBut.classList.remove('d-none');

    let pigeon = {
        qid: quizId,
        star: star
    }

    $.ajax({
        type: "POST",
        url: "/api/get-result",
        async: false,
        data: JSON.stringify(pigeon),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
            console.log(result)
        }
    });
}
