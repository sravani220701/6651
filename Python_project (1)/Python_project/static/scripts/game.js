// Initialize Canvas
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
document.body.appendChild(canvas);

// Set up canvas size
const WIDTH = 800;
const HEIGHT = 600;
canvas.width = WIDTH;
canvas.height = HEIGHT;
canvas.style.backgroundColor = 'white'; // Set background color

// Define colors
const BLACK = '#000000';
const WHITE = '#FFFFFF';
const GRAY = '#808080';
const GREEN = '#00FF00';
const RED = '#FF0000';

// Load and scale images
const player_image = new Image();
player_image.src = 'path/to/your/player_image.png';
player_image.onload = function() {
    player_image.width /= 2;
    player_image.height /= 2;
};

// Load background image
const background_image = new Image();
background_image.src = 'path/to/your/background_image.png';
background_image.onload = function() {
    ctx.drawImage(background_image, 0, 0, WIDTH, HEIGHT);
};

// Define recyclable and non-recyclable trash images
const recyclable_trash_images = [];
const non_recyclable_trash_images = [];

// Function to load trash images
function loadTrashImages(folderPath, trashArray) {
    // Your code to load images into trashArray
}

loadTrashImages('path/to/your/recyclable_trash', recyclable_trash_images);
loadTrashImages('path/to/your/non_recyclable_trash', non_recyclable_trash_images);

// Initialize and play background music
const background_music = new Audio('path/to/your/background_music.mp3');
background_music.loop = true;
background_music.play();

// Define fonts
const font = '36px Arial';
const game_over_font = '72px Arial';
const button_font = '36px Arial';
const title_font = '72px Arial';
const name_font = '48px Arial';
const points_font = '36px Arial';

// Define player properties
let player_rect = {
    x: WIDTH / 2,
    y: HEIGHT - 10,
    width: player_image.width,
    height: player_image.height
};

// Define trash items
let trash_items = [];
let current_trash = {};

// Function to populate trash items
function populateTrashItems() {
    // Your code to populate trash_items array
}

populateTrashItems();
current_trash = trash_items.shift(); // Pop first item

let trash_rect = {
    x: Math.random() * (WIDTH - 20) + 20,
    y: 0,
    width: current_trash.image.width,
    height: current_trash.image.height
};

// Initialize score, level, and misses
let score = 0;
let level = 1;
let misses = 0;
const max_misses = 3;
const level_targets = [5, 10, 15];

// Initialize recyclable and non-recyclable counts
let recyclable_count = 0;
let non_recyclable_count = 0;

// Points display variables
let points_display_time = 30; // Time to display points on the screen
let points_display_counter = 0;
let points_display_value = 0;

// Initial trash fall speed
let trash_fall_speed = 2;

// Button dimensions
const button_width = 200;
const button_height = 50;
const button_x = WIDTH / 2 - button_width / 2;

// Game states
const GET_NAME = 0;
const START = 1;
const PLAYING = 2;
const GAME_OVER = 3;
let game_state = GET_NAME;

// Player name
let player_name = '';

// Function to draw get name screen
function drawGetNameScreen() {
    ctx.drawImage(background_image, 0, 0);
    ctx.fillStyle = GREEN;
    ctx.font = font;
    ctx.fillText("Let's see how much trash you collect!!", WIDTH / 2 - 200, HEIGHT / 9);

    ctx.fillStyle = GREEN;
    ctx.font = title_font;
    ctx.fillText("Enter Your Name", WIDTH / 2 - 200, HEIGHT * 5 / 6.4);

    ctx.fillStyle = BLACK;
    ctx.font = name_font;
    ctx.fillText(player_name, WIDTH / 2 - 200, HEIGHT * 5 / 5.8);

    ctx.fillStyle = GRAY;
    ctx.font = font;
    ctx.fillText("Press Enter Now", WIDTH / 2 - 200, HEIGHT * 5 / 5.3);
}

// Function to draw start screen
function drawStartScreen() {
    ctx.drawImage(background_image, 0, 0);

    ctx.fillStyle = GREEN;
    ctx.font = title_font;
    ctx.fillText("Litter ", WIDTH / 2 - 200, HEIGHT / 9);

    ctx.fillStyle = RED;
    ctx.font = title_font;
    ctx.fillText("Legends", WIDTH / 2 - 200, HEIGHT / 9);

    ctx.fillStyle = BLACK;
    ctx.font = button_font;
    ctx.fillRect(button_x, HEIGHT / 2 + 120, button_width, button_height);
    ctx.fillStyle = WHITE;
    ctx.fillText("Start Game", button_x + 40, HEIGHT / 2 + 150);

    ctx.fillStyle = GREEN;
    ctx.font = font;
    ctx.fillText(`Recyclable: ${recyclable_count}`, 20, HEIGHT - 100);

    ctx.fillStyle = RED;
    ctx.font = font;
    ctx.fillText(`Non-Recyclable: ${non_recyclable_count}`, 20, HEIGHT - 50);
}

// Function to draw game over screen
function drawGameOverScreen() {
    ctx.drawImage(background_image, 0, 0);

    ctx.fillStyle = BLACK;
    ctx.font = game_over_font;
    ctx.fillText("Great Game! Game Over", WIDTH / 2 - 200, HEIGHT / 2);

    ctx.fillStyle = GRAY;
    ctx.font = font;
    ctx.fillText(`${player_name}'s Score is: ${score}`, WIDTH / 2 - 200, HEIGHT / 10);

    ctx.fillStyle = GREEN;
    ctx.font = font;
    ctx.fillText("Fact: Recycling one ton of plastic saves 5,774 kWh of energy", WIDTH / 2 - 200, HEIGHT / 7);

    ctx.fillStyle = BLACK;
    ctx.font = button_font;
    ctx.fillRect(button_x, HEIGHT / 1.8 + 100, button_width, button_height);
    ctx.fillStyle = WHITE;
    ctx.fillText("New Game?", button_x + 40, HEIGHT / 1.8 + 150);
}

// Function to display level up message
function displayLevelUpMessage(new_level) {
    ctx.fillStyle = BLACK;
    ctx.font = font;
    ctx.fillText(`Level increased to ${new_level}!`, WIDTH / 2 - 200, HEIGHT / 3);
}

// Function to check level up
function checkLevelUp() {
    if (level <= level_targets.length && score >= level_targets[level - 1]) {
        const previous_level = level;
        level++;
        trash_fall_speed++;
        displayLevelUpMessage(level);
    }
}

// Function to reset game
function resetGame() {
    score = 0;
    level = 1;
    trash_fall_speed = 3;
    misses = 0;
    recyclable_count = 0;
    non_recyclable_count = 0;
    populateTrashItems();
    current_trash = trash_items.shift(); // Pop first item
    trash_rect = {
        x: Math.random() * (WIDTH - 20) + 20,
        y: 0,
        width: current_trash.image.width,
        height: current_trash.image.height
    };
}

// Game loop
let running = true;
function gameLoop() {
    requestAnimationFrame(gameLoop);

    if (game_state === GET_NAME) {
        drawGetNameScreen();
    } else if (game_state === START) {
        drawStartScreen();
    } else if (game_state === PLAYING) {
        // Move the trash
        trash_rect.y += trash_fall_speed;
        if (trash_rect.y > HEIGHT) {
            misses++;
            if (misses >= max_misses) {
                game_state = GAME_OVER;
            } else {
                if (trash_items.length === 0) {
                    populateTrashItems();
                }
                current_trash = trash_items.shift();
                trash_rect = {
                    x: Math.random() * (WIDTH - 20) + 20,
                    y: 0,
                    width: current_trash.image.width,
                    height: current_trash.image.height
                };
            }
        }

        // Check for collision
        if (player_rect.x < trash_rect.x + trash_rect.width &&
            player_rect.x + player_rect.width > trash_rect.x &&
            player_rect.y < trash_rect.y + trash_rect.height &&
            player_rect.y + player_rect.height > trash_rect.y) {
            if (current_trash.type === 'recyclable') {
                score += 2;
                points_display_value = 2;
                points_color = GREEN;
            } else {
                score += 3;
                points_display_value = 3;
                points_color = RED;
            }

            points_display_counter = points_display_time;

            if (current_trash.type === 'recyclable') {
                recyclable_count++;
            } else {
                non_recyclable_count++;
            }

            if (trash_items.length === 0) {
                populateTrashItems();
            }
            current_trash = trash_items.shift();
            trash_rect = {
                x: Math.random() * (WIDTH - 20) + 20,
                y: 0,
                width: current_trash.image.width,
                height: current_trash.image.height
            };
            checkLevelUp();
        }

        // Clear canvas
        ctx.clearRect(0, 0, WIDTH, HEIGHT);

        // Draw player
        ctx.drawImage(player_image, player_rect.x, player_rect.y, player_rect.width, player_rect.height);

        // Draw trash
        ctx.drawImage(current_trash.image, trash_rect.x, trash_rect.y, trash_rect.width, trash_rect.height);

        // Draw score, level, and misses
        ctx.fillStyle = BLACK;
        ctx.font = font;
        ctx.fillText(`Score: ${score}`, 10, 10);
        ctx.fillText(`Level: ${level}`, WIDTH - 150, 10);
        ctx.fillText(`Misses: ${misses}/${max_misses}`, WIDTH / 2 - 75, 10);

        // Draw recyclable and non-recyclable counts
        ctx.fillStyle = GREEN;
        ctx.font = font;
        ctx.fillText(`Recyclable: ${recyclable_count}`, 10, 50);

        ctx.fillStyle = RED;
        ctx.font = font;
        ctx.fillText(`Non-Recyclable: ${non_recyclable_count}`, 10, 90);

        // Display points on catching an item
        if (points_display_counter > 0) {
            ctx.fillStyle = points_color;
            ctx.font = points_font;
            ctx.fillText(`+${points_display_value}`, player_rect.x + player_rect.width / 2 - 10, player_rect.y - 30);
            points_display_counter--;
        }
    } else if (game_state === GAME_OVER) {
        drawGameOverScreen();
    }
}

gameLoop();

// Event listeners for keyboard and mouse input
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        if (game_state === GET_NAME) {
            game_state = START;
        } else if (game_state === GAME_OVER) {
            player_name = '';
            resetGame();
            game_state = GET_NAME;
        }
    } else if (event.key === 'Backspace') {
        if (game_state === GET_NAME) {
            player_name = player_name.slice(0, -1);
        }
    } else {
        if (game_state === GET_NAME) {
            player_name += event.key;
        }
    }
});

document.addEventListener('mousedown', function(event) {
    const mouse_x = event.clientX - canvas.getBoundingClientRect().left;
    const mouse_y = event.clientY - canvas.getBoundingClientRect().top;

    if (game_state === START) {
        if (mouse_x >= button_x && mouse_x <= button_x + button_width &&
            mouse_y >= HEIGHT / 2 + 120 && mouse_y <= HEIGHT / 2 + 120 + button_height) {
            game_state = PLAYING;
        }
    } else if (game_state === GAME_OVER) {
        if (mouse_x >= button_x && mouse_x <= button_x + button_width &&
            mouse_y >= HEIGHT / 2 + 150 && mouse_y <= HEIGHT / 2 + 150 + button_height) {
            player_name = '';
            resetGame();
            game_state = GET_NAME;
        }
    }
});
