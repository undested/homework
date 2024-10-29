import random

NoPython = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'] * 2
random.shuffle(NoPython)

board_matrix = []
current_card = 0

for i in range(4):
    row = []
    for j in range(4):
        row.append(NoPython[current_card])
        current_card += 1
    board_matrix.append(row)


revealed = []
for i in range(4):
    revealed.append([False] * 4)

def print_board():
    for row in range(4):
        for col in range(4):
            if revealed[row][col]:
                print(board_matrix[row][col], end=' ')
            else:
                print('X', end=' ')
        print()

while True:
    print_board()


    row1, col1 = map(int, input("Вибери першу карту (рядок стовпчик): ").split())
    row1 -= 1
    col1 -= 1
    revealed[row1][col1] = True
    print_board()


    row2, col2 = map(int, input("Вибери другу карту (рядок стовпчик): ").split())
    row2 -= 1
    col2 -= 1
    revealed[row2][col2] = True
    print_board()

    if board_matrix[row1][col1] != board_matrix[row2][col2]:
        revealed[row1][col1] = False
        revealed[row2][col2] = False

    if all(all(row) for row in revealed):
        print("Ви виграли!")  # Побєда, урааааа, сюдааа
        break
