import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Flappy Runner", layout="centered")
st.title("🏃‍➡️ Flappy Runner - Streamlit Edition")

components.html(
    """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                overflow: hidden;
                margin: 0;
                padding: 0;
            }
            canvas {
                border: 2px solid black;
                background: linear-gradient(skyblue, lightgreen);
                display: block;
                margin: 0 auto;
            }
            #scoreDisplay {
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 24px;
                font-weight: bold;
                background: rgba(255,255,255,0.7);
                padding: 5px 15px;
                border-radius: 8px;
            }
            #gameOverText {
                position: absolute;
                top: 200px;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(0, 0, 0, 0.75);
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                display: none;
                z-index: 10;
            }
        </style>
    </head>
    <body>
        <canvas id="gameCanvas" width="400" height="600"></canvas>
        <div id="gameOverText">
            <h2>💥 Game Over</h2>
            <p id="finalScoreText"></p>
            <p id="highScoreText"></p>
            <p>Press <strong>Space</strong> to retry</p>
        </div>
        <div id="scoreDisplay">Score: 0 | 🏆 High: 0</div>

        <!-- Sound effects -->
        <audio id="bgMusic" loop>
            <source src="https://voca.ro/19Ip6z4SJIqP" type="audio/mpeg">
        </audio>
        <audio id="scoreSound">
        
            <source src="https://voca.ro/1kjxaGw2XzDX" type="audio/mpeg">
        </audio>
        <audio id="gameOverSound">
            <source src="https://voca.ro/11caoNJkfERM" type="audio/mpeg">
        </audio>

        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");

            let birdY = 250;
            let velocity = 0;
            const gravity = 0.5;
            const flapStrength = -8;
            const birdX = 80;
            const birdSize = 30;

            let pipes = [];
            const pipeWidth = 60;
            const pipeGap = 150;
            let frame = 0;
            let score = 0;
            let highScore = 0;
            let gameRunning = false;

            const scoreDisplay = document.getElementById("scoreDisplay");
            const gameOverText = document.getElementById("gameOverText");
            const finalScoreText = document.getElementById("finalScoreText");
            const highScoreText = document.getElementById("highScoreText");

            const bgMusic = document.getElementById("bgMusic");
            const scoreSound = document.getElementById("scoreSound");
            const gameOverSound = document.getElementById("gameOverSound");

            document.addEventListener("keydown", function(e) {
                if (e.code === "Space") {
                    if (gameRunning) {
                        velocity = flapStrength;
                    } else {
                        startGame();
                    }
                }
            });

            function drawBird() {
                ctx.beginPath();
                ctx.arc(birdX + birdSize / 2, birdY + birdSize / 2, birdSize / 2, 0, 2 * Math.PI);
                ctx.fillStyle = "yellow";
                ctx.fill();
                ctx.stroke();
            }

            function drawPipes() {
                ctx.fillStyle = "green";
                pipes.forEach(pipe => {
                    ctx.fillRect(pipe.x, 0, pipeWidth, pipe.top);
                    ctx.fillRect(pipe.x, pipe.top + pipeGap, pipeWidth, canvas.height - pipe.top - pipeGap);
                });
            }

            function updatePipes() {
                if (frame % 100 === 0) {
                    const top = Math.random() * (canvas.height - pipeGap - 100) + 50;
                    pipes.push({ x: canvas.width, top: top });
                    score++;
                    scoreSound.currentTime = 0;
                    scoreSound.play();
                }

                pipes.forEach(pipe => pipe.x -= 2);
                pipes = pipes.filter(pipe => pipe.x + pipeWidth > 0);
            }

            function checkCollision() {
                const birdTop = birdY;
                const birdBottom = birdY + birdSize;
                const birdLeft = birdX;
                const birdRight = birdX + birdSize;

                for (let pipe of pipes) {
                    const pipeLeft = pipe.x;
                    const pipeRight = pipe.x + pipeWidth;
                    const pipeTopHeight = pipe.top;
                    const pipeBottomY = pipe.top + pipeGap;

                    const hitHorizontal = birdRight > pipeLeft && birdLeft < pipeRight;
                    const hitVertical = birdTop < pipeTopHeight || birdBottom > pipeBottomY;

                    if (hitHorizontal && hitVertical) return true;
                }

                return birdBottom > canvas.height || birdTop < 0;
            }

            function drawScore() {
                scoreDisplay.innerText = "Score: " + score + " | 🏆 High: " + highScore;
            }

            function showGameOver() {
                gameRunning = false;
                gameOverText.style.display = "block";
                finalScoreText.innerText = "You scored " + score + " points!";
                if (score > highScore) highScore = score;
                highScoreText.innerText = "High Score: " + highScore;

                bgMusic.pause();
                gameOverSound.currentTime = 0;
                gameOverSound.play();
            }

            function gameLoop() {
                if (!gameRunning) return;

                ctx.clearRect(0, 0, canvas.width, canvas.height);
                drawBird();
                drawPipes();
                drawScore();

                velocity += gravity;
                birdY += velocity;

                updatePipes();

                if (checkCollision()) {
                    showGameOver();
                    return;
                }

                frame++;
                requestAnimationFrame(gameLoop);
            }

            function startGame() {
                gameOverText.style.display = "none";
                birdY = 250;
                velocity = 0;
                pipes = [];
                frame = 0;
                score = 0;
                gameRunning = true;

                bgMusic.currentTime = 0;
                bgMusic.loop = true;
                bgMusic.play();

                gameLoop();
            }

            startGame();
        </script>
    </body>
    </html>
    """,
    height=700
)
