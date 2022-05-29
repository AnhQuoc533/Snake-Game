from game import SnakeGame
from turtle import Screen
# Exception-free version


def reset(game):
    game.reset()
    del game
    main()


def main():
    try:
        scr = Screen()
        game = SnakeGame()

        # Exit game
        scr.onkey(scr.bye, 'Escape')  # 'esc' key
        # Restart game
        scr.onkey(lambda: reset(game), 'Return')  # 'enter' key

        game.play()
        scr.mainloop()

    except Exception:
        pass


if __name__ == '__main__':
    main()
