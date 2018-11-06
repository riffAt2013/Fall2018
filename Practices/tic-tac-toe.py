#w/o GUI TTC example
import pprint
board =  {'top-left':' ','top-middle':' ', 'top-right':' ', 
         'mid-left':' ', 'mid-middle':' ', 'mid-right':' ', 
         'bottom-left':' ', 'bottom-middle':' ', 'bottom-right':' '}

def boardPrinted(board):
    print(board['top-left']+ '|'+ board['top-middle']+ '|'+ board['top-right'])
    print('-----')
    print(board['mid-left']+ '|'+ board['mid-middle']+ '|'+ board['mid-right'])
    print('-----')
    print(board['bottom-left']+ '|'+ board['bottom-middle']+ '|'+ board['bottom-right'])

print ('Welcome to my TIC_TAC_TOE game.')
print('Player One choose your weapon: X or O')
choice = input()

if choice == 'X':
    playerOne = 'X'
    playerTwo = 'O'
else:
    playerOne = 'O'
    playerTwo = 'X'

#there can be at most 9 turns since after that the board will be filled. create a for loop ranging 9
count = 0

while True:
    boardPrinted(board)
    print('Turn for '+ playerOne)
    turn1 = input()
    board[turn1] = playerOne
    count += 1    
    if count == 9:
        break
    print ('Turn for '+ playerTwo)
    turn2 = input()
    board[turn2] = playerTwo
    count += 1
    if count == 9:
        break
    
    print('Final Outcome: ')
    boardPrinted(board)
    
    


