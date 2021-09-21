import random
SWG=['Snake','Water','Gun']
computer=random.choice(SWG)
pscr=0
cscr=0
i=0
k=10
while i<10:
    print('number of chance chance',k)
    print('snake , water , gun ')
    player=input(str('select the one:'))
    for j in player.split():
        player=player.replace(j,j.capitalize())


    if player==computer:
        print('tie!')
        print('your score', pscr, '\ncomputer score', cscr)
    elif player=='Snake':
        if computer=='Gun':
            print("your lose!",computer,"maar  dia",player,"ko")
            cscr=cscr+1
            pscr=pscr-1
            print('your score',pscr, '\ncomputer score',cscr)
        else:
            print('ypu won ',player,'bhagh gya',computer,'me swim kr ke')
            pscr=pscr+1
            cscr=cscr-1
            print('your score', pscr, '\ncomputer score', cscr)

    elif player=='Water':
        if computer=='Gun':
            print('you won !',computer,'ko duba dia',player,'ne')
            pscr=pscr+1
            cscr=cscr-1
            print('your score', pscr, '\ncomputer score', cscr)

        else:
            print('you loss!',computer,'bhagh gya',player,'me swim kr ke')
            pscr=pscr-1
            cscr=cscr+1
            print('your score', pscr, '\ncomputer score', cscr)

    elif player=='Gun':
        if computer=='Water':
            print('you loss!',computer,'bhogo dia',player,'ko')
            pscr=pscr-1
            cscr=cscr+1
            print('your score', pscr, '\ncomputer score', cscr)
        else:
            print('you won !',computer,'ko maar dia',player,'ne')
            pscr=pscr+1
            cscr=cscr-1
            print('your score', pscr, '\ncomputer score', cscr)

    else:
        print('please check your input')

    i=i+1
    k=k-1

if i==10:
    print("final score\n")
    print('computer score:',cscr)
    print('player score',pscr)
    if pscr==cscr:
        print('tie')
    elif pscr<cscr:
        print('you loss')
    else:
        print('you won')



