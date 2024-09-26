print('''
      
                  ___________
           / |       | |
        ,' ,'         \/',_    __
     ,'__/             |    ',|  "'-,,,,,,,
   ,/  _|',            |                |   
   |  |   |',           \               |    
   |__|   |  ',          ',             |     
  /       |     ',        ,_"""""---'-_,'______
 /        |        ',,_-'"    |        |        ',
|_________|         |         /        |        / ',,'""""|
|__  |        ,____/         |        _|       /    |___  /
'\___|      ,'_,'|_,-,_______|         |       /      , '/
  \,' _', _/  ,, ,',|        |          \       |   '" ,'
   \ / |_ ,  |  \||||       ,' |      ,'|    _""    |,'
    ' ,'  ', |  ||||| __ ,'   _|_ ,'    |    |""---/
       ' ,"""','"""""" |     /           \"""|    /
                      |_____|_      __''"    \   |
                     |  |  /  """"""   |      \ /
                      \ / |            |       /
                       \--'            |      /
                       |   \__        _|__    |
                       |      |__     |   ',,,|
                       |         |____|   /   |
                       /         _|    ,,'_   |
                      |__________|___,'  ,,' /
                       \      ---'    \,/  ,'
                        \     |    ,,,' \_/
                         |    |_,''      |/
                         |    |       []_|
                          \___'        /
                           \       __,'
                            \_____/                        
                                                              ''' )

print("Wellcome to treasure Magic land")
print("your misson is to find the treasure")
choise1=input('You are crossroad , where you want to go ? type "left" or "right" ').lower()

if choise1=="right":
    choise1_2=input('you have come to a love lake . there is an land in the middle of the lake .type "wite" to wait for boat. Type "swim" swim acrose.').lower()   
    if choise1_2 == "wite":
        choise1_3=input("enter a password.(it coud be the name name of lake or land)").lower()
        if choise1_3=="magic":
            choise1_4=input("correct answer.please prove that you are human:)  \n555+5= ")
            if choise1_4=="560":
                choise1_5=input("Which door you want to go. BLACK,RED ,BLUE, OR YELLO ").lower()
                if choise1_5=="black":
                    choise1_5_1=input('where you want to go ? type "left" or "right" ').lower()
                    if choise1=="left":
                        print("game over") 
                    else:
                        print("game over")    
                elif choise1_5=="red":
                     print("Welcome to the rollercoster")
                     height=int(input("What is your height in cm ?\n"))
                     if height>=100:
                         print("sorry,game over")
                     else:
                         print("sorry,game over")                     
                elif choise1_5=="blue":
                    print("yess you you got the treasure") 
                else:
                    print("game over")
            else:
                print("game over")
    else:
        print("game over")
elif choise1=="left":
    print("you fell into a hole")
else:
    print("game over. better luck in next time ")


    
         








