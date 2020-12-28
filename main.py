from life import LifeBoard

if __name__ == "__main__":
    size = int(input("Size of board: "))
    board = LifeBoard(size)
    filled = False
    print("Type in co-ordinates to fill spaces. Type -1 to finish.")
    while not filled:
        print(board)
        x = int(input("X: "))
        y = int(input("Y: "))
        if x == -1 or y == -1:
            filled = True
        else:
            board.switch(x, y)
    print(board)
    print("Done. Press any key to step through the game.")
    while True:
        input()
        board.step()
        print(board)