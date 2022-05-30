from game import SnakeGame
from turtle import Screen
# Exception-free version


def reset(scr, game):
    scr.clearscreen()
    del game
    main()


def main():
    try:
        screen = Screen()
        snake_game = SnakeGame()
        snake_game.play()

        # Restart game
        screen.onkey(lambda: reset(screen, snake_game), 'Return')  # 'enter' key

        screen.mainloop()

    except Exception as e:
        # print(e)
        pass


if __name__ == '__main__':
    main()
