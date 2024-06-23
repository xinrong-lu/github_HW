import curses
import random

# Constants
SNAKE_BODY_CHAR = ' '
NORMAL_FOOD_CHAR = 'π'
SPECIAL_FOOD_CHAR = 'X'
OBSTACLE_CHAR = ' '


# Directions
DIRECTIONS = {
    curses.KEY_UP: (-1, 0),
    curses.KEY_DOWN: (1, 0),
    curses.KEY_LEFT: (0, -1),
    curses.KEY_RIGHT: (0, 1)
}

# Game class
class SnakeGame:
    def __init__(self):
        self.window = curses.initscr()
        self.window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.window.timeout(100)

        # Get window dimensions
        self.height, self.width = self.window.getmaxyx()

        # Initialize snake and food        
        self.snake_x = self.width // 4
        self.snake_y = self.height // 2
        self.snake = [
            [snake_y, snake_x],
            [snake_y, snake_x - 1],
            [snake_y, snake_x - 2]
        ]
        self.snake_length = 3
        self.food = [self.height // 2, self.width // 2]
        self.special_food = None

        self.direction = curses.KEY_RIGHT

        # Generate obstacles
        self.obstacles = self.generate_obstacles()

        # Game state
        self.is_paused = False
        self.is_game_over = False
        self.score = {
            'normal_food': 0,
            'special_food': 0
        }


    def generate_food(self):
        while True:
            food_y = random.randint(1, self.height - 2)
            food_x = random.randint(1, self.width - 2)
            if [food_y, food_x] not in self.snake and \
                    [food_y, food_x] not in self.obstacles:
                return [food_y, food_x]

    def generate_obstacles(self):
        num_obstacles = (self.width * self.height) // 150
        obstacles = []
        for _ in range(num_obstacles):
            obstacle_len = random.randint(5, 10)
            obstacle_direction = random.choice(['horizontal', 'vertical'])
            obstacle_y = random.randint(1, self.height - 2)
            obstacle_x = random.randint(1, self.width - 2)

            if obstacle_direction == 'horizontal':
                if obstacle_x + obstacle_len > self.width - 1:
                    obstacle_x = self.width - obstacle_len - 1
                obstacles.extend(
                    [[obstacle_y, obstacle_x + i] for i in range(obstacle_len)]
                )
            else:
                if obstacle_y + obstacle_len > self.height - 1:
                    obstacle_y = self.height - obstacle_len - 1
                obstacles.extend(
                    [[obstacle_y + i, obstacle_x] for i in range(obstacle_len)]
                )
        return obstacles

    def handle_input(self):
        key = self.window.getch()
        if key == ord(' '):
            self.is_paused = not self.is_paused
        elif key in DIRECTIONS and not self.is_paused:
            next_direction = DIRECTIONS[key]
            if (next_direction[0] != -1 * DIRECTIONS[self.direction][0] or
                    next_direction[1] != -1 * DIRECTIONS[self.direction][1]):
                self.direction = key

    def update(self):
        if not self.is_paused:
            # Move snake
            new_head = [self.snake[0][0] + DIRECTIONS[self.direction][0],
                        self.snake[0][1] + DIRECTIONS[self.direction][1]]
            self.snake.insert(0, new_head)

            # Check collision with food
            if self.snake[0] == self.food:
                self.score['normal_food'] += 1
                self.snake_length += 1  # Increment snake length
                self.food = self.generate_food()
            elif self.special_food and self.snake[0] == self.special_food:
                self.score['special_food'] += 1
                if self.snake_length > 1:
                    self.snake.pop()
                self.special_food = None
            else:
                self.snake.pop()  # Remove tail if not growing

            # Check collision with obstacles
            if self.snake[0] in self.obstacles or \
                    self.snake[0][0] in [0, self.height - 1] or \
                    self.snake[0][1] in [0, self.width - 1] or \
                    self.snake[0] in self.snake[1:]:
                self.is_game_over = True

            # Generate special food
            if not self.special_food and random.random() < 0.03:
                self.special_food = self.generate_food()



    def draw(self):
        self.window.clear()
        self.window.border()

        # Draw snake
        for i, (y, x) in enumerate(self.snake):
            if i == 0:
                self.window.addch(y, x, SNAKE_BODY_CHAR, curses.color_pair(2) | curses.A_STANDOUT)
            else:
                self.window.addch(y, x, SNAKE_BODY_CHAR, curses.color_pair(2))

        # Draw food
        self.window.addch(self.food[0], self.food[1], NORMAL_FOOD_CHAR, curses.color_pair(1))

        # Draw special food
        if self.special_food:
            self.window.addch(self.special_food[0], self.special_food[1], SPECIAL_FOOD_CHAR, curses.color_pair(3))

        # Draw obstacles
        for y, x in self.obstacles:
            self.window.addch(y, x, OBSTACLE_CHAR, curses.color_pair(4) | curses.A_REVERSE)

        # Draw score
        score_text = f"Score: Normal Food: {self.score['normal_food']} | " \
                     f"Special Food: {self.score['special_food']}"
        self.window.addstr(0, 2, score_text)

        # Draw game over message
        if self.is_game_over:
            self.window.addstr(
                self.height // 2, (self.width - len("GAME OVER")) // 2,
                "GAME OVER", curses.color_pair(5) | curses.A_BOLD
            )

        # Refresh the window
        self.window.refresh()



    def play(self):
        while not self.is_game_over:
            self.handle_input()
            self.update()
            self.draw()

        # End game
        self.window.getch()
        curses.endwin()
        print(f"Game Over!\nReason: {'Snake collided with obstacles' if self.is_game_over else 'Unknown'}")
        print(f"Normal Food Eaten: {self.score['normal_food']}")
        print(f"Special Food Eaten: {self.score['special_food']}")


def main():
    game = SnakeGame()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal food color
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)  # Snake body color (gray)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Special food color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Obstacles color
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_WHITE)  # Game over message color

    game.play()


if __name__ == "__main__":
    main()
