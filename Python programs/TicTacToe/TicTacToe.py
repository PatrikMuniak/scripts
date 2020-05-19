theBoard={'topL': '' , 'topM': '','topR': '',
          'midL': '', 'midM': '', 'midR': '',
          'lowL': '', 'lowM': '', 'lowR': ''}
validMoves=['topL','topM','topR', 'midL', 'midM', 'midR', 'lowL', 'lowM', 'lowR']
print(validMoves)
def turnX():
    print('X is your turn')
    move=input()
    if move in validMoves:
      theBoard[move]='X'
      net()
      validMoves.remove(move)
      winner()
      turnO()
    else:
        print('Invalid move. Type again.')
        turnX()
    

def turnO():
    print('O is your turn. What is your move?')
    move=input()
    if move in validMoves:
      theBoard[move]='O'
      net()
      validMoves.remove(move)
      turnX()
     
      
    else:
        print('Invalid move. Type again.')
        turnO()

def net():
    print('   '+str(theBoard['topL'])+'|'+'  '+str(theBoard['topM'])+' '+'|'+str(theBoard['topR']))
    print('---+---+---')
    print('   '+str(theBoard['midL'])+'|'+'  '+str(theBoard['midM'])+' '+'|'+str(theBoard['midR']))
    print('---+---+---')
    print('   '+str(theBoard['lowL'])+'|'+'  '+str(theBoard['lowM'])+' '+'|'+str(theBoard['lowR']))

def winner():
    if theBoard['topL' and 'topM' and 'topR'] == 'X':
        print('X won')
        gameFinished()
def noWinner():
    if validMoves==[]:
        gameFinished()
        
def gameFinished():
    print('Game finished.')
    print('What\'s next? New game/Exit')
    action=input()
        
    if action=='New game':
        theBoard['topL']=''
        theBoard['topM']=''
        theBoard['topR']=''
        theBoard['midL']=''
        theBoard['midM']=''
        theBoard['midR']=''
        theBoard['lowL']=''
        theBoard['lowM']=''
        theBoard['lowR']=''
        net()
        turnX()
        turnO()
    if action=='Exit':
        import sys
        sys.exit()
    else:
        print('Invalid Option. type again.')
        gameFinished()
                
net()
winner()
noWinner()
turnX()
turnO()




