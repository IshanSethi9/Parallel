#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3 
import comtypes.gen
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
from PIL import Image 
import pyautogui
import sys
import tkinter
import random
import PyPDF2
from yahoo_fin import stock_info as si
import numpy as np
from googletrans import Translator


# In[2]:


engine = pyttsx3.init() #'sapi5' is optional
engine.say("Hello")
engine.runAndWait()

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
  
for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) 

# Initialize the Speech Engine
engine = pyttsx3.init('sapi5') #sapi5 is optional
# Get the voice objects and print them. (This is just to see, if you have more than one voice.)
voices = engine.getProperty('voices')
#print(voices)
# Set the voice to the second voice. (voices[0].id would be the first voice)
engine.setProperty('voice', voices[1].id)
#voice id 1 is female, id 0 is male
# Set the words per minute rate of the Speech engine
engine.setProperty('rate', 105)
# Tell the engine what you want it to say.
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
# Tell the engine to start saying what you wanted it to and stop when it reaches the end of the queued sayings.
engine.runAndWait()
# In[3]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("hello")


# In[4]:


def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

#time()


# In[5]:


def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

#date()


# In[6]:


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    sever.starttls()
    server.login('abcd@gmail.com','1234')
    server.sendmail('abcd@gmail.com',to,content)
    server.close()


# In[7]:


def screenshot():
    img=pyautogui.screenshot()
    img.save()


# In[8]:


def wishme():
    speak("welcome to my world!")
    time() #Speak the time
    date() #Speak the date
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    elif hour>=18 and hour<=24:
        speak("Good evening!")
    else:
        speak("Good night!")
        
    speak("what can i do for you?")
    
#wishme()


# In[9]:


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(query)
        
    except Exception as e:
        print(e)
        speak("Pardon me, can you please say that again...")
        return takeCommand()
    
    return query

#takeCommand()


# In[10]:


#tic-tac-toe: human vs human

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []


def gameBoard():
    print('7'+'|'+'8'+'|'+'9')
    print('-+-+-')
    print('4'+'|'+'5'+'|'+'6')
    print('-+-+-')
    print('1'+'|'+'2'+'|'+'3')
    print()
#gameBoard()

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def inp_move():
    #move1 = input()
    move1 = takeCommand()
    if move1.isdigit():
        if int(move1) > 0 and int(move1) < 10:
            return move1
        else:
            print('Please enter a number within range')
            speak('Please enter a number within range')
            tst = inp_move()
            return tst
    else:
        print('please enter a number')
        speak('please enter a number')
        tmp = inp_move()
        return tmp


def humanGame():
    
    gameBoard()

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        speak("It's your turn,"+turn+".Move to which place?")

        move = inp_move()


        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            speak("That place is already filled. Move to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                speak("Game Over")
                print(" **** " +turn + " won. ****")
                speak(turn+"won")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            speak("Game Over")
            print("It's a Tie!!")
            speak("Aah! It's a tie")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    #restart = input("Do want to play Again?(y/n)")
    speak("Do you want to play again?")
    restart = takeCommand().lower()
    if restart == "yes":
        for key in board_keys:
            theBoard[key] = " "

        humanGame() #this is to restart if the user wants to...


# In[11]:


#tic-tac-toe: human vs computer

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def basicBoard():
    print("1 | 2 | 3")
    print("-+-+-+-+-")
    print("4 | 5 | 6 ")
    print("-+-+-+-+-")
    print("7 | 8 | 9")
#basicBoard()

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-+-+-+-+-+-')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-+-+-+-+-+-')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)
    
def playerMove():
    run = True
    while run:
        #move = input('Please select a position to place an \'X\' (1-9): ')
        speak("Please select a position to place an X from 1 to 9")
        move=takeCommand()
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
                    speak('Sorry this space is occupied!')
            else:
                print('Please type a number within the range!')
                speak('Please type a number within the range!')
        except:
            print('Please type a number!')
            speak('Please type a number!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def computerGame(board):
    
    basicBoard()
    
    print('Welcome to Tic Tac Toe!')
    speak("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            speak("Sorry, Computer won")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print()
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                speak("Computer placed an O in position"+str(move))
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            speak("X won this time! Good Job!")
            break

    if isBoardFull(board):
        print('Tie Game!')
        Speak("Tie Game!")

    #answer = input('Do you want to play ? (Y/N)')
    speak("Do you want to play the game?")
    answer=takeCommand().lower()
    if answer == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        computerGame(board)


# In[12]:


if __name__=='__main__':
    wishme()
    button_pressed=False


# In[13]:


top = tkinter.Tk()
def giveCommand():
    button_pressed=True
    while button_pressed==True:
        query=takeCommand().lower()
        
        if 'time' in query: #time 
            time()
        
        elif 'date' in query: #date
            date()
            
        elif 'wikipedia' in query: #search on wikipedia
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)
            
        elif 'human game' in query: #tic-tac-toe: human vs human
            speak("The human versus human game has begun")
            humanGame()
            
        elif 'computer game' in query: #tic-tac-toe: human vs computer
            speak("The human versus computer game has begun")
            computerGame(board)
        
        elif 'sum' in query: #add the given numbers
            speak("Please enter the first number")
            a=float(takeCommand())
            if a<0:
                a=0
            speak("The first number is"+str(a))
            speak("Please enter the second number")
            b=float(takeCommand())
            if b<0:
                b=0
            speak("The second number is"+str(b))
            sum=float(a)+float(b)
            speak(sum)
            print("Sum:"+str(sum))
            
        elif 'subtract' in query: #subtract
            speak("Please enter the first number")
            c=float(takeCommand())
            if c<0:
                c=0
            speak("The first number is"+str(c))
            speak("Please enter the second number")
            d=float(takeCommand())
            if d<0:
                d=0
            speak("The second number is"+str(d))
            if c>d:
                sub=float(c)-float(d)
            else:
                sub=float(d)-float(c)
            speak(sub)
            print("Subtract:"+str(sub))
            
        elif 'multiply' in query: #product
            speak("Please enter the first number")
            e=float(takeCommand())
            speak("The first number is"+str(e))
            speak("Please enter the second number")
            f=float(takeCommand())
            speak("The second number is"+str(f))
            product=float(e)*float(f)
            speak(product)
            print("Product:"+str(product))
            
        elif 'divide' in query: #divide
            speak("Please enter the first number")
            g=float(takeCommand())
            speak("The first number is"+str(g))
            speak("Please enter the second number")
            h=float(takeCommand())
            speak("The second number is"+str(h))
            divide1=float(g)/float(h)
            divide2=float(h)/float(g)
            speak(str(g)+"by"+str(h)+"is equal to"+divide1)
            print("Division:"+str(divide1))
            speak(str(h)+"by"+str(g)+"is equal to"+divide2)
            print("Division:"+str(divide2))
            
        elif 'power' in query: #power
            speak("Please enter the base number")
            i=float(takeCommand())
            speak("The base number is"+str(i))
            speak("Please enter the power")
            j=float(takeCommand())
            speak("The power is"+str(j))
            pow=float(i)**float(j)
            speak(pow)
            print("Power:"+str(pow))
            
        elif 'send email' in query: #send mail
            try:
                speak("What do you want to send?")
                content=takeCommand()
                speak(content)
                to='xyz@gmail.com'
                sendEmail(to,content)
                speak("Email sent")
            
            except Exception as e:
                print(e)
                speak("Some problem occured while sending the mail, please try again")
                
        elif 'search' in query: #google 
            speak("What do you want to search?")
            chromepath='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search= takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            
        elif 'logout' in query: #logout
            os.system('shutdown -1')
        
        elif 'shutdown' in query: #shutdown
            os.system('shutdown /s /t 1')
            
        elif 'restart' in query: #restart
            os.system('shutdown /r /t 1')
            
        elif 'play song' in query: #play song
            songs="D:\\Music_Path"  #song directory needs to be updated
            song=os.listdir(songs)
            os.startfile(os.path.join(songs,song[0]))
            
        elif 'pdf text extractor' in query: #pdf text extractor & reader
            pdf=open('C:/Users/Ishan/Downloads/Introduction_to.pdf','rb')
            #pdftext=takeCommand()
            #pdf=open('C:/Ishan/PDF/'+pdftext+'.pdf','rb')
            reader=PyPDF2.PdfFileReader(pdf)
            reader.numPages
            x=int(input())
            #x=int(takeCommand())
            page=reader.getPage(x)
            text=page.extractText()
            text=text.replace("\n"," ")
            print(text)
            speak(text)
        
        elif 'remember' in query: #notes to remember
            speak("What do you want to remember?")
            data=takeCommand()
            speak("You said me to remember" + data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'know anything' in query: #read remember notes
            remember=open('data.txt','r')
            speak("You said to remember that"+remember.read())
            
        elif 'open photo' in query: #pics
            im = Image.open(r"C:Picture.png/.jpg") #picture directory need to be updated
            im.show()  
            
        elif 'take screenshot' in query: #screenshot
            screenshot()
            speak("Screenshot taken")
        
        elif 'motivate me' in query: #motivational quotes
            genQuotes=["The Way Get Started Is To Quit Talking And Begin Doing.","The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.","Don’t Let Yesterday Take Up Too Much Of Today.","You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.","It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.","If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.","People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.","Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.","Entrepreneurs Are Great At Dealing With Uncertainty And Also Very Good At Minimizing Risk. That’s The Classic Entrepreneur.","We May Encounter Many Defeats But We Must Not Be Defeated","Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do.","Imagine Your Life Is Perfect In Every Respect; What Would It Look Like?","We Generate Fears While We Sit. We Overcome Them By Action.","Whether You Think You Can Or Think You Can’t, You’re Right.","Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.","The Man Who Has Confidence In Himself Gains The Confidence Of Others.","“The Only Limit To Our Realization Of Tomorrow Will Be Our Doubts Of Today.","Creativity Is Intelligence Having Fun.","What You Lack In Talent Can Be Made Up With Desire, Hustle And Giving 110% All The Time.","Do What You Can With All You Have, Wherever You Are.","You Are Never Too Old To Set Another Goal Or To Dream A New Dream.","To See What Is Right And Not Do It Is A Lack Of Courage.","Reading Is To The Mind, As Exercise Is To The Body.","Fake It Until You Make It! Act As If You Had All The Confidence You Require Until It Becomes Your Reality.","The Future Belongs To The Competent. Get Good, Get Better, Be The Best!","For Every Reason It’s Not Possible, There Are Hundreds Of People Who Have Faced The Same Circumstances And Succeeded.","Things Work Out Best For Those Who Make The Best Of How Things Work Out.","A Room Without Books Is Like A Body Without A Soul.","I Think Goals Should Never Be Easy, They Should Force You To Work, Even If They Are Uncomfortable At The Time.","One Of The Lessons That I Grew Up With Was To Always Stay True To Yourself And Never Let What Somebody Else Says Distract You From Your Goals.","Today’s Accomplishments Were Yesterday’s Impossibilities.","The Only Way To Do Great Work Is To Love What You Do. If You Haven’t Found It Yet, Keep Looking. Don’t Settle.","You Don’t Have To Be Great To Start, But You Have To Start To Be Great.","A Clear Vision, Backed By Definite Plans, Gives You A Tremendous Feeling Of Confidence And Personal Power.","There Are No Limits To What You Can Accomplish, Except The Limits You Place On Your Own Thinking.","Integrity Is The Most Valuable And Respected Quality Of Leadership. Always Keep Your Word.","Leadership Is The Ability To Get Extraordinary Achievement From Ordinary People","Leaders Set High Standards. Refuse To Tolerate Mediocrity Or Poor Performance","Clarity Is The Key To Effective Leadership. What Are Your Goals?","The Best Leaders Have A High Consideration Factor. They Really Care About Their People","Leaders Think And Talk About The Solutions. Followers Think And Talk About The Problems.","The Key Responsibility Of Leadership Is To Think About The Future. No One Else Can Do It For You.","The Effective Leader Recognizes That They Are More Dependent On Their People Than They Are On Them. Walk Softly.","Leaders Never Use The Word Failure. They Look Upon Setbacks As Learning Experiences.","Practice Golden Rule Management In Everything You Do. Manage Others The Way You Would Like To Be Managed.","Leaders Are Anticipatory Thinkers. They Consider All Consequences Of Their Behaviors Before They Act.","The True Test Of Leadership Is How Well You Function In A Crisis.","Leaders Concentrate Single-Mindedly On One Thing– The Most Important Thing, And They Stay At It Until It’s Complete.","The Three ‘C’s’ Of Leadership Are Consideration, Caring, And Courtesy. Be Polite To Everyone.","Respect Is The Key Determinant Of High-Performance Leadership. How Much People Respect You Determines How Well They Perform."]
            x=random.randint(0,49)
            print(x)
            print(genQuotes[x])
            speak(genQuotes[x])
            
        elif 'drive me crazy' in query: #joker quotes
            jokerQuotes=["The only sensible way to live in this world is without rules.","Smile, because it confuses people. Smile, because it’s easier than explaining what is killing you inside.","What doesn’t kill you, simply makes you stranger!","April sweet is coming in, let the feast of fools begin!","They need you right now, but when they don’t, they’ll cast you out like a leper!","As you know, madness is like gravity…all it takes is a little push.","Let’s put a smile on that face!","We stopped checking for monsters under our bed, when we realized they were inside us.","If you’re good at something, never do it for free.","When the chips are down, these civilized people, they’ll eat each other.","Very poor choice of words.","Why don’t we cut you up into little pieces and feed you to your pooches? Hm? And then we’ll see how loyal a hungry dog really is.","You have nothing, nothing to threaten me with. Nothing to do with all your strength.","Introduce a little anarchy. Upset the established order, and everything becomes chaos. I’m an agent of chaos…","I like you, but I want to kill you.","Do I really look like a guy with a plan? You know what I am? I’m a dog chasing cars. I wouldn’t know what to do with one if I caught it! You know, I just… *do* things.","Why so serious?","Is it just me or is it getting crazier out there","And I won’t kill you because you’re just too much fun. I think you and I are destined to do this forever.","Those mob fools want you gone. So they can get back to the way things were. But I know the truth, there’s no going back. You’ve changed things…forever.","You can’t rely on anyone these days, you gotta do everything yourself, don’t we? That’s ok, I came prepared, it’s a funny world we live in. Speaking of which, you know how I got these scars?","As though we were made for each other… Beauty and the Beast. Of course, if anyone else calls you beast, I’ll rip their lungs out.","See, this is how crazy Batman’s made Gotham! If you want order in Gotham, Batman must take off his mask and turn himself in. Oh, and every day he doesn’t, people will die, starting tonight. I’m a man of my word.","See I’m a man of simple taste. I like things such as gunpowder…dynamite and…gasoline!","Until their spirit breaks completely. Until they get a good look at the real Harvey Dent, and all the heroic things he’s done.","This city deserves a better class of criminal. And I’m gonna give it to them!","And he didn’t die all at once. It was hours before the screaming stopped. I almost didn’t get to sleep that night. That was the last time I’d used crushed glass","All I have are negative thoughts.","I’m only laughing on the outside. My smile is just skin deep. If you could see inside, I’m really crying. You might join me for a weep.","I’ve been using it as a journal, but also as a joke diary, if I have any thoughts or frustrations. I think I told you, I’m pursuing a career in standup comedy.","I am not someone who is loved. I’m an idea. A state of mind.","It’s not about the money, it’s about sending a message. Everything burns!","Nobody panics when things go according to plan, even if the plan is horrifying!","The real joke is your stubborn, bone deep conviction that somehow, somewhere, all of this makes sense! That’s what cracks me up each time!","I used to think that my life was a tragedy. But now I realize, it’s a comedy.","It’s funny, when I was a little boy, and told people I was going to be a comedian, everyone laughed at me. Well, no one’s laughing now.","I’ll tell you what you get! You get what you f**king deserve!","The strongest hearts have the most scars!","Their morals, their code; it’s a bad joke. Dropped at the first sign of trouble. They’re only as good as the world allows them to be. You’ll see- I’ll show you. When the chips are down these, uh, civilized people? They’ll eat each other. See I’m not a monster, I’m just ahead of the curve.","Don’t test the monster in me!","You’re my friend, too.","I got you a kitty.","I’ll never understand why Superman wears the same outfits every day.","Why can’t a girl be nice to a guy without the mook trying to murder her?","My love for my Joker was stronger than their mad house walls","Look…I’m only doing this to help you. Let’s try this again. Acceptance.","They’ve got Hello Kitty on them. They’re fashionable.","Every woman has a crazy side that only the right man can bring out.","In case ya ain’t figured it out, today’s the Joker’s big homecoming, and you’re the guest of honor.","If I get mad at you that means I still care. Worry when I don’t get mad.","You got the look. And a lotta nerve. What you don’t have is the right. Joker was a hero. You’re not fit to lick his boutonniere!","Now you feel like you’ve someone by your side-to share the journey with you.","I love him not for the way he silenced my demons, but for the way his demons dances with mine.","You didn’t like my show? Well, try this one. It’s called ‘Animals Attack People I Hate.’ It’s a comedy.","What’s wrong with you, B-man? You come into Mista J’s home and just start smashing it to pieces! Don’t you know he’s sick?","I promised you some entertainment, right, boys?","Ladies and jerks! There’s been a slight change in tonight’s show. Insteada the opera robbin’ you for somethin’ like a thousand bucks a seat — we’re gonna rob you! Believe me folks, I’ve seen it already. I’m doin’ ya a big favor!","Let me get you outta here girl. We can team up again. Drive all the boys crazy. Ya know? Like the old days…","Nice work,butterfingers, why didn’tcha just turn the batsignal on while you were at it!","I sleep where I want, when I want, with who I want.","I dunno about ‘genius,’ but I do got a PhD.","Oh buckets full, honey. I was tryin’ too hard to impress the wrong guy. Kinda like you with Superman.","You really put the ‘fun’ in funeral"]
            y=random.randint(0,62)
            print(y)
            print(jokerQuotes[y])
            speak(jokerQuotes[y])
            
        elif 'stocks' in query: #stock rate
            x=si.get_live_price('NSE')
            print("$",x)
            speak("$",str(x))
            
        elif 'toss a coin' in query: #toss coin
            n=1
            p=0.5
            x=np.random.binomial(n,p)
            print(x)
            speak(x)
            if(x==1):
                print("Heads")
                speak("Heads")
            else:
                print("Tails")
                speak("Tails")
        
        elif 'abilities' in query: #abilities
            abilities=["I can go offline","I can open your favourite pictures","I can log you out from the system, restart the system & even shutdown the system on your command","I can extract text from pdf & can speak the extracted text","I can play your favourite songs","I can tell you the time & date","I can search for a particular topic on Wikipedia","I can google for you","I can perform basic maths operations like add,subtract, multiply, divide & deal with powers","I can beat you in Tic Tac Toe game","I can help you play Tic Tac Toe game with your friend","I can send a mail for you","I can remember things you want me to remember","I can take Screenshots"]
            z=random.randint(0,4)
            y=random.randint(5,9)
            x=random.randint(10,13)
            speak(abilities[x])
            print(abilities[x])
            speak(abilities[y])
            print(abilities[y])
            speak(abilities[z])
            print(abilities[z])
            
        elif 'future abilities' in query: #what to do next
            speak("Alarm")
            speak("Stopwatch")
            speak("Predict weather")
            speak("Current weather conditions")
            speak("Pykemon")
            speak("Handwritten data extraction & reading")
            print("Alarm")
            print("Stopwatch")
            print("Predict weather")
            print("Current weather conditions")
            print("Pykemon")
            print("Handwritten data extraction & reading")
            
        elif 'translate to spanish' in query: #translate into spanish language
            translator=Translator()
            translations=translator.translate(input(),dest='es')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
            
        elif 'translate to french' in query: #translate into french language
            translator=Translator()
            translations=translator.translate(input(),dest='fr')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
        
        elif 'translate to french' in query: #translate into japanese language
            translator=Translator()
            translations=translator.translate(input(),dest='ja')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
        
        elif 'translate to tamil' in query: #translate into tamil language
            translator=Translator()
            translations=translator.translate(input(),dest='ta')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
            
        elif 'translate to punjabi' in query: #translate into punjabi language
            translator=Translator()
            translations=translator.translate(input(),dest='pa')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
        
        elif 'translate to russian' in query: #translate into russian language
            translator=Translator()
            translations=translator.translate(input(),dest='ru')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
        
        elif 'translate to german' in query: #translate into german language
            translator=Translator()
            translations=translator.translate(input(),dest='de')
            print(translations.origin, '-->', translations.text)
            print(translations.text)
            speak(translations.text)
            
        elif 'offline' in query: #quit
            break     #or use this "button_pressed=False"
    
def quit():
    top.destroy()  #quit/exit
    
B1 = tkinter.Button(top, text ="Give Command", command = giveCommand)
B2 = tkinter.Button(top, text="Quit", command = quit)

B1.pack()
B2.pack()
top.mainloop()

