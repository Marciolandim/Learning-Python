     
from game_func import display_board, enter_move, draw_move, make_list_of_free_fields

board = [
    [1, 2, 3],
    [4, "X", 6],  # computador começa no centro
    [7, 8, 9]
]


while make_list_of_free_fields(board):
    display_board(board)

    # Jogador
    enter_move(board)
    if not make_list_of_free_fields(board):
        print("Tabuleiro cheio! Empate!")
        break

    # Computador
    draw_move(board)





