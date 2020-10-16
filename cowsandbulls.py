import random,string, time
o="Hi! Welcome to Cows and Bulls Game. "
for i in o:
        speed=time.sleep(0.2)
        print(i,end="")
speed=time.sleep(1)
print("The game can be played in two modes: number and letter. The player guesses either digits or letters.")
print()
print("MAKE A CHOICE!")

print('\nMode 1 - Number Mode \nMode 2 - Letter Mode')
m=int(input("Enter the playing mode(1/2):"))
p=int(input("Enter the number of players(1/2):"))
c=14
if (m==1) and (p==1):
        c=13
        print("Let's play a game of Cowbull!") #explanation 
        print("I will generate a number, and you have to guess the numbers one digit at a time.") 
        print("For every number in the wrong place, you get a bull. For every number in the right place, you get a cow.") 
        print("The game ends when you get 4 cows!You have a maximum of 13 guesses.")
        prompt="Get set go!"
        for i in prompt:
                speed=time.sleep(0.1)
                print(i,end=" ")
        speed=time.sleep(1)
        s=list(random.sample(range(0,10),4))
        print("The computer has stored a 4 digit value. \nStart guessing player!")
        for i in range(1,15):
                cow=0
                bull=0
                num=input("Make a guess:")
                new=[int(x) for x in str(num)]
                if s==new:
                        print("you win!")
                        print("Number of guesses:",i)
                        print("Your score is",c)
                        break;
                for ele in s:
                        if ele in new:
                                if s.index(ele)==new.index(ele):
                                        cow+=1
                                else:
                                        bull+=1
                print(cow,"Cows",bull,"Bulls")     
                print("Number of guesses:",i)
                c-=1
                if new!=s and i==13:
                        print("Sorry!You loose!")
                        print("The answer is:",s)
                        break;
elif m==1 and p==2:
    print("Let's play a game of Cowbull!") #explanation 
    print("Player 2 will keep a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a bull. For every number in the right place, you get a cow.")
    print("The game ends when you get 4 cows!")
    prompt="Get set go!"
    for i in prompt:
                speed=time.sleep(0.1)
                print(i,end=" ")
    speed=time.sleep(1)
    num=input("player 2 keep a number:")
    n=[int(x) for x in num]
    m=len(n)
    #[1,2,3,4]
    for i in range(1,14):
        cow=0
        bull=0
        k=input("Player 1 enter a {} digit number:".format(m))
        h=[int(x) for x in k]
        print("Number of guesses:",i)
        if n==h:
            print("You win!")
            print("Your score is",c)
            break;
        #[3,4,5]
        for w in n:
            for j in h:
                if w==j:
                    if n.index(w)==n.index(j):
                        cow+=1
                    else:
                        bull+=1
                        
        print(cow,"Cows",bull,"bulls")
        if h!=n and i==13:
            print("Sorry you lose!")
            print("The answer is:",num)
        c-=1
elif m==2 and p==1:
    print("Let's play a game of Cowbull!") #explanation 
    print("I will generate a word, and you have to guess the word one letter at a time.") 
    print("For every letter in the wrong place, you get a bull. For every letter in the right place, you get a cow.") 
    print("The game ends when you get 4 cows!")
    prompt="Get set go!"
    for i in prompt:
                speed=time.sleep(0.1)
                print(i,end=" ")
    speed=time.sleep(1)
    alpha=string.ascii_lowercase
    h=[random.choice(alpha) for i in range(4)]
    #print(h)
    for i in range(1,21):
        cow=0
        bull=0
        x=input("Guess a 4 letter word:")
        g=list(str(x))
        #print(g)
        if g==h:
            print("You win!!")
            print("Your score is",c)
            break;
        for j in h:
                if j in g:
                    z=h.index(j)
                    y=g.index(j)
                    if z!=y:
                        bull+=1
                    elif z==y:
                        cow+=1
        print(cow,"Cows",bull,"Bulls")          
        print("Number of guesses:",i)
        c-=1
        if g!=h and i==20:
            print("You lose")
            print("The answer is:",h)
            break;

elif (m==2 and p==2):
        print("Let's play a game of Cowbull!") #explanation 
        print("Player2 will generate a word, and you have to guess the word one letter at a time.") 
        print("For every letter in the wrong place, you get a bull. For every one in the right place, you get a cow.") 
        print("The game ends when you get 4 cows!")
        prompt="Get set go!"
        for i in prompt:
                speed=time.sleep(0.1)
                print(i,end=" ")
        speed=time.sleep(1)
        n=input("P2 keep a word:")
        a=len(n)
        h=list(str(n))
        
        for i in range(1,14):
                cow=0
                bull=0
                x=input("Guess a {} letter word:".format(a))
                g=list(str(x))
                #print(g)
                if g==h:
                        print("You win!!")
                        print("Your score is",c)
                        break;
                for j in h:
                        if j in g:
                                z=h.index(j)
                                y=g.index(j)
                                if z!=y:
                                        bull+=1
                                elif z==y:
                                        cow+=1
                                else:
                                        print("Not present")
                print(cow,"cows",bull,"bulls")
                print("Number of guesses:",i)
                c-=1
                
                if g!=h and i==13:
                        print("You lose")
                        print("The answer is:",n)
else:
        print("Invalid input")

                            
        
        
    
