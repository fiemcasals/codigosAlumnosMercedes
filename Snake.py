import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root, width=400, height=400, size=20):
        self.root = root
        self.width = width
        self.height = height
        self.size = size
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.snake = [(width//2, height//2)]
        self.food = self.place_food()
        self.canvas = tk.Canvas(root, width=width, height=height, bg='black')
        self.canvas.pack()
        self.root.bind('<Key>', self.change_direction)
        self.update()

    def place_food(self):
        while True:
            x = random.randrange(0, self.width, self.size)
            y = random.randrange(0, self.height, self.size)
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if key in ['Up', 'Down', 'Left', 'Right'] and opposites.get(key) != self.direction:
            self.direction = key

    def move(self):
        x, y = self.snake[0]
        if self.direction == 'Up':
            y -= self.size
        elif self.direction == 'Down':
            y += self.size
        elif self.direction == 'Left':
            x -= self.size
        elif self.direction == 'Right':
            x += self.size
        new_head = (x, y)
        # Check collisions
        if (
            x < 0 or x >= self.width or
            y < 0 or y >= self.height or
            new_head in self.snake
        ):
            self.running = False
            return
        self.snake = [new_head] + self.snake
        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete('all')
        # Draw food
        x, y = self.food
        self.canvas.create_rectangle(x, y, x+self.size, y+self.size, fill='red', outline='')
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = 'green' if i == 0 else 'lightgreen'
            self.canvas.create_rectangle(x, y, x+self.size, y+self.size, fill=color, outline='')
        self.canvas.create_text(50, 10, text=f'Score: {self.score}', fill='white', font=('Arial', 12))

    def update(self):
        if self.running:
            self.move()
            self.draw()
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(self.width//2, self.height//2, text='¡Perdiste!', fill='white', font=('Arial', 24))
            self.canvas.create_text(self.width//2, self.height//2+30, text=f'Puntaje: {self.score}', fill='white', font=('Arial', 16))

def main():
    root = tk.Tk()
    root.title('Snake en Tkinter')
    game = SnakeGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

