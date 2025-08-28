from random import randrange
global board
global XorO
XorO = "XO"




def display_board(board):
     # A função aceita um parâmetro contendo o status atual da placa
     # e o imprime no console.
    
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|", end=" ")
        
        for cell in row:
            print(" ", str(cell), end="   | ") 

        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")




def enter_move(board):
 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    while True:
        try:

            move = int(input("Digite seu movimento no intervalode 1-9: "))
            if move < 1 or move > 9:
                print("Movimento inválido! Escolha os movimentos entre 1 e 9 :)")
                continue

            row = (move - 1) // 3 
            col = (move - 1) % 3

            if str(board[row][col]) not in XorO:
                board[row][col] = "O"
                break
            else:
                print("Célula ocupada! Altera o seu movimento!")
        except ValueError:
            print("Número de movimento inválido :(")




def make_list_of_free_fields(board):
 # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
 # l - linhas e c - colunas 
    free = []
    for l in range(3):
        for c in range(3):
            if str(board[l][c]) not in XorO:
                free.append((l,c))
    return free




def draw_move(board):
     # A função desenha o movimento do computador e atualiza o tabuleiro.
    free = make_list_of_free_fields(board)
    if free:
        r, c = free[randrange(len(free))]
        board[r][c] = "X"




def victory_for(board, sign):
    # A função analisa o estado da placa a fim de verificar se 
     # o jogador usando 'O's ou 'X's ganhou o jogo


    # Verifica linhas
    for row in board:
        win = True
        for cell in row:
            if cell != sign:
                win = False
                break
        if win:
            return True

    # Verifica colunas
    for c in range(3):
        win = True
        for r in range(3):
            if board[r][c] != sign:
                win = False
                break
        if win:
            return True

    # Verifica diagonal principal
    win = True
    for i in range(3):
        if board[i][i] != sign:
            win = False
            break
    if win:
        return True

    # Verifica diagonal secundária
    win = True
    for i in range(3):
        if board[i][2 - i] != sign:
            win = False
            break
    if win:
        return True

    return False
