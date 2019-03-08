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
while theBoard['1']=='' or  theBoard['2']=='' or  theBoard['3']=='' or  theBoard['4']=='' or  theBoard['5']=='' or  theBoard['6']=='' or  theBoard['7']=='' or  theBoard['8']=='' or  theBoard['9']=='' :
    printBoard(theBoard)
    print('\n\nTurn for ' + turn + '. Move on which space? (1-9) \n')
    move = input()
    if move not in theBoard:
        print('\nEnter a valid move.')

    elif (theBoard[move]==''):
        theBoard[move] = turn
        
    else:
         print('\nEnter a valid move.')
    
    
    
    if theBoard['1']!='' and theBoard['2']==theBoard['1'] and theBoard['3']==theBoard['2']:
                printBoard(theBoard)
                print(turn+ ' Won!')
                time.sleep(10)
                exit()
    
    if theBoard['4']!='' and theBoard['5']==theBoard['4'] and theBoard['6']==theBoard['5']:
                printBoard(theBoard)
                print(turn+ ' Won!')
                time.sleep(10)
                exit()
    
    if theBoard['7']!='' and theBoard['8']==theBoard['7'] and theBoard['9']==theBoard['8']:
                printBoard(theBoard)
                print(turn+ ' Won!')
                time.sleep(10)
                exit()

    if theBoard['1']!='' and theBoard['4']==theBoard['1'] and theBoard['7']==theBoard['4']:
                printBoard(theBoard)
                print(turn+ ' Won!')
                time.sleep(10)
                exit()   

    if theBoard['2']!='' and theBoard['5']==theBoard['2'] and theBoard['8']==theBoard['5']:
                printBoard(theBoard)
                print(turn+ ' Won!')
                time.sleep(10)
                exit() 

    if theBoard['3']!='' and theBoard['6']==theBoard['3'] and theBoard['9']==theBoard['6']:
                printBoard(theBoard)
                print(turn+ ' Won!')
                time.sleep(10)
                exit()            

    if theBoard['1']!='' and theBoard['5']==theBoard['1'] and theBoard['9']==theBoard['5']:
                    printBoard(theBoard)
                    print(turn+ ' Won!')
                    time.sleep(10)
                    exit()
    if theBoard['3']!='' and theBoard['5']==theBoard['3'] and theBoard['7']==theBoard['5']:
                    printBoard(theBoard)
                    print(turn+ ' Won!')
                    time.sleep(10)
                    exit()

    if theBoard['1']!='' and  theBoard['2']!='' and  theBoard['3']!='' and  theBoard['4']!='' and  theBoard['5']!='' and  theBoard['6']!='' and  theBoard['7']!='' and  theBoard['8']!='' and  theBoard['9']!='' :
        printBoard(theBoard)
        print('\nMatch Draw!')
        time.sleep(10)
        exit()

    if theBoard[move]==turn:
        if turn == 'X':
                turn = 'O'
        else:
                turn = 'X'     