$(document).ready(function () {
    let timer;
    let seconds = 0;
    let isPaused = false;

    function updateTimerDisplay() {
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        const remainingSeconds = seconds % 60;

        const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
        $("#timer").text(formattedTime);
    }

    function startTimer() {
        timer = setInterval(function () {
            seconds++;
            updateTimerDisplay();
        }, 1000);
    }

    function pauseTimer() {
        clearInterval(timer);
        isPaused = true;
    }

    function resumeTimer() {
        isPaused = false;
        startTimer();
    }

    function resetTimer() {
        clearInterval(timer);
        seconds = 0;
        isPaused = false;
        updateTimerDisplay();
    }

    $("#start").click(function () {
        if (!isPaused) {
            resetTimer();
        }
        startTimer();
    });

    $("#pause").click(function () {
        pauseTimer();
    });

    $("#resume").click(function () {
        if (isPaused) {
            resumeTimer();
        }
    });

    $("#reset").click(function () {
        resetTimer();
    });
});