a=input("enter the name of the movie --  ")
for bb in range(100):
    print("DON'T LOOK UP \t DON'T LOOK UP")
oo=0
ll=len(a)//2
for cc in range(len(a) +ll,0,-1):
    print("you have ",cc," chances left  be careful")
    kk = input("NOW ENTER THE LETTER --  ")
    
    if kk == 'rachit the gahhfuudhfuhusdhdfuyshuhsfugfhusfusugusghuyuehjbeuyeuhuehuiyhuhdhihhidhffiihisfssffu':
        for tt in range(100):
            print("you won")
        break

    
    elif kk in a:
        print("\t CORRECT")
        oo+=1
        if oo == len(a):
            print('ALL LETTERS HAVE BEEN GUESSED , NOW GUESS THE NAME OF THE MOVIE ')
            break
         
        elif oo!=len(a) and cc==1:
            print("\t \t \t \t GAME OVER YOU LOST")

        
    elif oo!=len(a) and cc==1:
        print("\t \t \t \t GAME OVER YOU LOST")
        
    else :
        print("\t WRONG")

