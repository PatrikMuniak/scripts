theBoard={'topL': 'X' , 'topM': 'X','topR': 'X',
          'midL': '', 'midM': '', 'midR': '',
          'lowL': '', 'lowM': '', 'lowR': ''}
validMoves=[]

def winner():
    if theBoard['topL' and 'topM' and 'topR'] == 'X':
                #('midL' and 'midM' and 'midR') or
                #('lowL' and 'lowM' and 'lowR')] == 'X':
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
        
winner()
noWinner()
