from game import SnakeGame
from turtle import Screen


def reset(scr):
    scr.clearscreen()
    main()


def main():
    screen = Screen()
    SnakeGame().play()

    # Restart game
    screen.onkey(lambda: reset(screen), 'Return')  # 'enter' key
    screen.mainloop()


if __name__ == '__main__':
    main()
