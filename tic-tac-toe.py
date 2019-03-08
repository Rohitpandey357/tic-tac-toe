import time

theBoard = {'1':'', '2': '', '3': '',
            '4': '', '5': '', '6': '',
            '7': '', '8': '', '9': ''}
def printBoard(board):
    print('\n\n'+board['1'] + '  | ' + board['2'] + ' | ' + board['3'])
    print('--+--+--')
    print(board['4'] + '  | ' + board['5'] + ' | ' + board['6'])
    print('--+--+--')
    print(board['7'] + '  | ' + board['8'] + ' | ' + board['9'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('\n\nTurn for ' + turn + '. Move on which space? (1-9) \n')
    move = input()
    if (theBoard[move]==''):
        theBoard[move] = turn
    else:
         print('Enter a valid move.')
    
    if move not in theBoard:
        print('Enter a valid move.')
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'  
    if theBoard['1']!='' and theBoard['2']==theBoard['1'] and theBoard['3']==theBoard['2']:
                print(turn+ ' Won!')
                printBoard(theBoard)
                time.sleep(10)
                exit()
    
    if theBoard['4']!='' and theBoard['5']==theBoard['4'] and theBoard['6']==theBoard['5']:
                print(turn+ ' Won!')
                printBoard(theBoard)
                time.sleep(10)
                exit()
    
    if theBoard['7']!='' and theBoard['8']==theBoard['7'] and theBoard['9']==theBoard['8']:
                print(turn+ ' Won!')
                printBoard(theBoard)
                time.sleep(10)
                exit()

    if theBoard['1']!='' and theBoard['4']==theBoard['1'] and theBoard['7']==theBoard['4']:
                print(turn+ ' Won!')
                printBoard(theBoard)
                time.sleep(10)
                exit()   

    if theBoard['2']!='' and theBoard['5']==theBoard['2'] and theBoard['8']==theBoard['5']:
                print(turn+ ' Won!')
                printBoard(theBoard)
                time.sleep(10)
                exit() 

    if theBoard['3']!='' and theBoard['6']==theBoard['3'] and theBoard['9']==theBoard['6']:
                print(turn+ ' Won!')
                printBoard(theBoard)
                time.sleep(10)
                exit()            

    if theBoard['1']!='' and theBoard['5']==theBoard['1'] and theBoard['9']==theBoard['5']:
                    print(turn+ ' Won!')
                    printBoard(theBoard)
                    time.sleep(10)
                    exit()
    if theBoard['3']!='' and theBoard['5']==theBoard['3'] and theBoard['7']==theBoard['5']:
                    print(turn+ ' Won!')
                    printBoard(theBoard)                     
                    time.sleep(10)
                    exit()

