     
from game_func import display_board, enter_move, draw_move, make_list_of_free_fields

board = [
    [1, 2, 3],
    [4, "X", 6],  # computador começa no centro
    [7, 8, 9]
]


while True:
    display_board(board)

    # Jogador
    enter_move(board)
    if victory_for(board, "O"):
        display_board(board)
        print("Você ganhou!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Empate!")
        break

    # Computador
    draw_move(board)
    if victory_for(board, "X"):
        display_board(board)
        print("Computador ganhou!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Empate!")
        break




