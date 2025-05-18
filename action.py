import txt2sp
import sp2txt
import webbrowser
import os
import pyjokes
import requests
import subprocess
import pywhatkit
import cv2
import datetime
import random

# def randAlphabetgame():
#     n = random.randint(97, 123)
#     guesses = 0
#     txt2sp.txt2sp("Choose an alphabet after a second.")


#     while True:
#         spoken_input = sp2txt.sp2t().strip().lower()

#         if "exit" in spoken_input or "break" in spoken_input:
#             txt2sp.txt2sp("Game exited. Bye!")
#             return

#         if spoken_input.isdigit():
#             txt2sp.txt2sp("Invalid input. Please say an alphabet.")
#             continue

#         a = int(spoken_input)
#         guesses += 1


#         if a > n:
#             txt2sp.txt2sp("Go back")
#         elif a < n:
#             txt2sp.txt2sp("go ahead")
#         else:
#             txt2sp.txt2sp(f"You have guessed the alphabet perfectly in {guesses} guesses!")
#             return




def StonePaperScissor():
    stone_inputs = ["stone", "stone stone"]
    scissors_inputs = ["scissor", "scissors", "caesar"]
    paper_inputs = ["paper"]

    choices = ["stone", "paper", "scissor"]
    
    while True:
        txt2sp.txt2sp("Give your choice after a second.")
        UserChoice = sp2txt.sp2t()
        UserChoice = UserChoice.strip().lower()

        if "exit" in UserChoice or "break" in UserChoice:
            txt2sp.txt2sp("Game exited. Bye!")
            return
        if UserChoice in stone_inputs:
            UserChoice = "stone"
        elif UserChoice in scissors_inputs:
            UserChoice = "scissor"
        elif UserChoice in paper_inputs:
            UserChoice = "paper"
        else:
            txt2sp.txt2sp("Wrong choice. Try again.")
            continue

        AiChoice = random.choice(choices)
        print(f"Computer's Choice: {AiChoice}")
        txt2sp.txt2sp(f"I chose {AiChoice}")

      
        if UserChoice == AiChoice:
            txt2sp.txt2sp("Oops! Same choices. Match Draw.")
            return

        if (UserChoice == "stone" and AiChoice == "scissor") or \
           (UserChoice == "paper" and AiChoice == "stone") or \
           (UserChoice == "scissor" and AiChoice == "paper"):
            txt2sp.txt2sp("You won. I lost.")
        else:
            txt2sp.txt2sp("Oops! You lost. Better luck next time.")

def GuessNo():
    n = random.randint(1, 100)
    guesses = 0
    txt2sp.txt2sp("Choose a number after a second.")

    while True:
        spoken_input = sp2txt.sp2t().strip().lower()

        if "exit" in spoken_input or "break" in spoken_input:
            txt2sp.txt2sp("Game exited. Bye!")
            return

        if not spoken_input.isdigit():
            txt2sp.txt2sp("Invalid input. Please say a number.")
            continue

        a = int(spoken_input)
        guesses += 1

        if a > n:
            txt2sp.txt2sp("Smaller number please.")
        elif a < n:
            txt2sp.txt2sp("Greater number please.")
        else:
            txt2sp.txt2sp(f"You have guessed the number perfectly in {guesses} guesses!")
            return

def tellJoke():
    txt2sp.txt2sp("Here's a joke")
    joke = pyjokes.get_joke()
    txt2sp.txt2sp(joke)
    return joke

def  OpenApp(app):
    txt2sp.txt2sp(f"opening {app}")
    if(app == 'word'):
        app = "win"+app
        os.startfile(f"{app}")
    elif(app == "powerpoint"):
        os.startfile("powerpnt")
    elif ('vs' in app):
        os.startfile("C:\\Users\\HP\\Desktop\\V S Code.lnk")
    else:
        webbrowser.open(f"https://www.{app}.com")

def PlayMusic(userData):
    if("play" in userData ) :
        txt2sp.txt2sp("Playing music for you, Sir.")
        userData  = userData
        song = userData[4:]
        print(song)
        pywhatkit.playonyt(f"https://www.youtube.com/search?q={song}")
        return f"{song} playing"
    elif("stop" in userData):
        txt2sp.txt2sp("Stopping the music, Sir.")
        os.system("taskkill /im chrome.exe /f")
        return "Music Stopped"
    
def whatsApp():
    try:
        txt2sp.txt2sp("Opened the whatsapp in Backside now. ")
        txt2sp.txt2sp("Tell me the contact number after a second ")
        numInput  = sp2txt.sp2t()
        number = str("+91" + numInput)
        txt2sp.txt2sp("Repeating the contact number. Please Check.");
        for i in range (3,len(number)):
            txt2sp.txt2sp(number[i])
        txt2sp.txt2sp("is it correct");
        check = sp2txt.sp2t()
        check = check.lower()
        try:
            if(check in ["yeah","yeah yeah","yeah yeah yeah" "yep","yes yes" , 'yes' , "yeah brother"]):
                txt2sp.txt2sp("OK, Tell me the message to send after a second ")
                msgInput = sp2txt.sp2t()
                message = str(msgInput)
                if (message == "break"):
                    exit()
                elif(message != ''):
                    txt2sp.txt2sp("Sending the message.")
                    pywhatkit.sendwhatmsg_instantly(number, message)
                    return "Msg sent."
                else:
                    return "Msg not sent"   
            elif(check in ['no','no no','no no no','naah','naa','nope' 'na na']):
                txt2sp.txt2sp("Okay! Opening again.")
                whatsApp()
        except Exception as err:
            txt2sp.txt2sp("An error occured!")
    except Exception as err: 
        txt2sp.txt2sp("An error occured!")
def clearNotes():
    txt2sp.txt2sp("Clearing all notes, wait a second")
    data =''' '''
    with open("C:\\Users\\HP\\Desktop\\Note\\note.txt",'w') as file:
        file.write(f"\n{data}")
    file.close()
    txt2sp.txt2sp("Cleared all notes successfully. You can check now")
    
def takeNote():
    data =''' '''
    txt2sp.txt2sp("Taking Note, start speaking after a second.")
    data = sp2txt.sp2t()
    with open("C:\\Users\\HP\\Desktop\\Note\\note.txt",'a') as file:
        file.write(f"\n{data}")
    file.close()
    txt2sp.txt2sp("Noted down successfully")
    
def getCurrentTime():
    now = datetime.datetime.now()
    actual_Time = str(now.time()).split('.')[0]
    txt2sp.txt2sp(f"The time is {actual_Time}")  
    return actual_Time

def talkingTom():
    try:
        text = sp2txt.sp2t()
        if "break" in text or "stop" in text or "break up" in text :
            txt2sp.txt2sp("Okay Stopping.")
            exit()
        else: 
            txt2sp.txt2sp(text)
            talkingTom()
    except Exception as err:
        if err:
            txt2sp.txt2sp("I didn't got it. Please Repeat")
            talkingTom()

def BMI():
    txt2sp.txt2sp("Whats the height in centimetres")
    heightinput = sp2txt.sp2t()
    if(heightinput == "break"):
        exit()

    try: 
        height = float(heightinput)
    except:
        txt2sp.txt2sp("Sorry, I couldn't understand the height. Lets try again")
        return BMI()
    try: 
        txt2sp.txt2sp("Whats the weight in KG.")
        weightInput = sp2txt.sp2t()
        weight  = float(weightInput)
        if(weightInput == "break"):
            exit()  
    except: 
        txt2sp.txt2sp("Unable to catch the weight.  Lets try again")
        return BMI()
    bmi = weight / (((height)/100) ** 2)
    
    return bmi

def get_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = response.json()
    txt2sp.txt2sp(data['text'])
    text = sp2txt.sp2t()
    if "one more" in text or "once more" in text :
        get_random_fact()
    elif "ok" in text or "break" in text or "stop" in text or text not in ["one more" , "once more"]:
        return 
 
def action(data):
    userData = data.lower()
    if "what is your name" in userData or "name" in userData:
        txt2sp.txt2sp("My name is virtual assistant.")
        return "My name is virtual assistant."
    elif "hello" in userData or "hey" in userData or "hye" in userData or "hii" in userData :
        txt2sp.txt2sp("Hey Sir , How can I help you ?")
        return "Hey Sir , How can I help you ?"
    elif "good morning" in userData: 
        txt2sp.txt2sp("Good Morning, what can I help with?")
        return "Good Morning, what can I help with?"
  
    elif "good afternoon" in userData:
        txt2sp.txt2sp("Good Afternoon! How can I assist you today?")
        return "Good Afternoon! How can I assist you today?"
    elif "good evening" in userData:
        txt2sp.txt2sp("Good Evening! How may I help you?")
        return "Good Evening! How may I help you?"
    elif "good night" in userData:
        txt2sp.txt2sp("Good Night Sir! Take care.")
        return "Good Night Sir! Take care."
    elif "how are you" in userData or "how r u" in userData:
        txt2sp.txt2sp("I'm great, Sir! Thanks for asking. How about you?")
        return "I'm great, Sir! Thanks for asking. How about you?"
    elif "i am fine" in userData or "i'm fine" in userData:
        txt2sp.txt2sp("Glad to hear that, Sir!")
        return "Glad to hear that, Sir!"
    elif "thank you" in userData or "thanks" in userData:
        txt2sp.txt2sp("You're most welcome, Sir!")
        return "You're most welcome, Sir!"
    elif "who are you" in userData or "hu r u" in userData:
        txt2sp.txt2sp("I am your personal assistant, always here to help you.")
        return "I am your personal assistant, always here to help you."
    elif "bye" in userData or "goodbye" in userData:
        txt2sp.txt2sp("Goodbye Sir! Have a great day ahead!")
        return "Goodbye Sir! Have a great day ahead!"
    elif "see you" in userData or  "c u" in userData:
        txt2sp.txt2sp("See you soon, Sir!")
        return "See you soon, Sir!"
    elif "take care" in userData:
        txt2sp.txt2sp("Thank you, Sir! You too take care!")
        return "Thank you, Sir! You too take care!"
    elif "nice to meet" in userData:
        txt2sp.txt2sp("Nice to meet you too, Sir!")
        return "Nice to meet you too, Sir"
    elif "what's up" in userData or "whats up" in userData:
        txt2sp.txt2sp("All good here, Sir! How about you?")
        return "All good here, Sir! How about you?"
    elif "how's your day" in userData or "how is your day" in userData:
        txt2sp.txt2sp("My day is going great, Sir! Always ready to assist you.")
        return "My day is going great, Sir! Always ready to assist you."
    elif "are you there" in userData:
        txt2sp.txt2sp("Yes Sir, I am always here for you.")
        return "Yes Sir, I am always here for you."
    elif "can you help me" in userData or "i need help" in userData:
        txt2sp.txt2sp("Of course Sir! I'm here to help. Please tell me what you need.")
        return "Of course Sir! I'm here to help. Please tell me what you need."
    elif "what can you do" in userData:
        txt2sp.txt2sp("I can assist you with many tasks like opening applications, searching information, playing music, and much more!")
        return "I can assist you with many tasks like opening applications, searching information, playing music, and much more!"
    elif "you are good" in userData or "you are awesome" in userData:
        txt2sp.txt2sp("Thank you so much, Sir! I'm glad you think so.")
        return "Thank you so much, Sir! I'm glad you think so."
    elif "you are bad" in userData:
        txt2sp.txt2sp("I'm sorry to hear that, Sir. I'll try to improve!")
        return "I'm sorry to hear that, Sir. I'll try to improve!"
    elif "i am bored" in userData or "i m bored" in userData:
        txt2sp.txt2sp("Let’s do something fun, Sir! I can tell you a joke")
        joke = tellJoke()
        return joke
    elif "good job" in userData or "well done" in userData:
        txt2sp.txt2sp("Thank you so much, Sir! It means a lot!")
        return "Thank you so much, Sir! It means a lot!"
    elif "i am happy" in userData:
        txt2sp.txt2sp("That's wonderful to hear, Sir! Stay happy and positive.")
        return "That's wonderful to hear, Sir! Stay happy and positive."
    elif "i am sad" in userData:
        txt2sp.txt2sp("I'm sorry to hear that, Sir. I'm here for you. Hope you feel better soon.")
        return "I'm sorry to hear that, Sir. I'm here for you. Hope you feel better soon."
    elif "i am tired" in userData:
        txt2sp.txt2sp("You should take some rest, Sir. Health comes first!")
        return "You should take some rest, Sir. Health comes first!"
    elif "motivate me" in userData:
        txt2sp.txt2sp("Sure Sir! Remember, every day is a new beginning. Believe in yourself, and you can achieve anything!")
        return "Sure Sir! Remember, every day is a new beginning. Believe in yourself, and you can achieve anything!"

    elif "open calculator" in userData:
        txt2sp.txt2sp("Opening Calculator for you.")
        subprocess.Popen("calc")
        return "Calculator Opened"
    
    elif "open notepad" in userData:
        txt2sp.txt2sp("Opening Notepad, Sir.")
        subprocess.Popen("notepad", shell=True)
        return "Notepad Opened"

    elif "play" in userData or "song" in userData:
        PlayMusic(userData)

    elif "stop music" in userData or "stop the music" in userData or "stop the song" in userData:
        PlayMusic(userData)

    elif "search" in userData :
        txt2sp.txt2sp("Opened Google to search")
        searching= userData[7:]
        webbrowser.open(f"https://www.google.com/search?q={searching}")
        return "done"
    
    elif "what is" in userData or "how is" in userData:
        txt2sp.txt2sp("Lets search it")
        searching = userData[7:]
        webbrowser.open(f"https://www.chatgpt.com/search?q={searching}")
        return "Ai is opened for you"

    elif "bmi" in userData or "Tell me my bmi" in userData:
        result = BMI()
        bmi= float(result)
        if(result < 18.5):
            txt2sp.txt2sp("You may be too thin and lack proper nutrition. Your category is Underweight.")
        elif(result>18.5 and result<24.9):
            txt2sp.txt2sp("You have a healthy body weight. Your category is Normal.")
        elif(result>25 and result<29.9):
            txt2sp.txt2sp("You may be carrying excess weight. Your category is Overweight.")
        else:
            txt2sp.txt2sp("You  have a High risk of health problems. Your category is Obese.")
        return result
    
    elif "what is" in userData or "how is" in userData:
        txt2sp.txt2sp("Lets search it")
        searching = userData[7:]
        webbrowser.open(f"https://www.google.com/search?q={searching}")
        return "google is opened for you"
    
    elif "tell me a joke" in userData or "tel mi a joke" in userData:
       tellJoke()
    
    elif "whatsapp" in userData or "message" in userData or "WhatsApp" in userData or "open whatsapp" in userData:
       whatsApp()

    elif "tell me a fact" in userData or "fact" in userData or "tel mi a fact" in userData :
        txt2sp.txt2sp("Here's a fact")
        fact = get_random_fact()        
        return f"{fact}"
    elif userData in ["choose a random number", "give me a random number" ,"tell me a random number"]:
        num = random.randint(1,100) 
        txt2sp.txt2sp(f"here's your number, {str(num)}")
        return num
    elif "time" in userData or "tell me the time" in userData:
        txt2sp.txt2sp("Let me check the time for you.")       
        response = f"The time is {getCurrentTime()}"
        txt2sp.txt2sp(response)
        return response
    
    elif "repeat" in userData or "repeat after me" in userData or "talking tom" in userData:
        txt2sp.txt2sp("Okay! I am your talking tom now. Start speaking after a second.")
        talkingTom()

    elif "whether" in userData or "tell me the weather" in userData:
        txt2sp.txt2sp("Let me check the whether for you.")
        webbrowser.open("https://www.google.com/search?q=weather")
        return "Whether is served for you."
    
    elif userData in ["stone paper scissor" , "stone" , "paper" , "scissor", "stone paper sizzer"] :
        txt2sp.txt2sp("Lets play Stone Paper Scissor")
        StonePaperScissor()
        txt2sp.txt2sp("Wanna Play Again ?")
        userChoice = sp2txt.sp2t()
        if(userChoice in ["yeah","yeah yeah","yeah yeah yeah" "yep","yes yes" , 'yes' , "yeah brother"]): 
            StonePaperScissor()
        else:
            txt2sp.txt2sp("Call me Whenever want to play.")
            return "played Stone Paper Scissor"
        
    elif userData in ["guess number game" , "guess number" , "random number game" , "number game"]:
        GuessNo()
    
    elif "open" in userData:
        app = userData[5:]
        OpenApp(app)
        return f"{app} opened."
   
    elif userData in ["click my picture", "take my photo" , "click my image","my picture"]:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            txt2sp.txt2sp("Cannot open the camera")
            exit()
        else :
            ret,frame = cap.read()
            if ret :
                txt2sp.txt2sp("Clicking picture. Say cheeeeeeeese !.")                       
                folder ="C:\\Users\\HP\\Desktop\\coding\\PythonFiles\\intermediate_Prjct\\Personalised\\Images\\_"
                random_id =  datetime.datetime.now().strftime("%H%M%S%f")
                cv2.imwrite(f"{folder}_{random_id}.png" , frame)
                return "Image captured Successfully. Saved at    Images folder."
            else :
                txt2sp.txt2sp("Failed To Capture your picture" )
                return "Failed To Capture your picture" 

        cap.release()
        cv2.destroyAllWindows()
    
    elif userData in [ "take a note", "take note", "please note" ,"write the note"]:
        takeNote()
        return "Notes taken Successfully"
    elif userData in [ "clear notes", "clear all note" , "clean notes" ,"clear note"]:
        clearNotes()
        return "Notes Cleared Successfully"

    elif "shutdown" in userData:
        txt2sp.txt2sp("Sutting down")
        os.system("shutdown /s /t 5")

        return "ok sir"

    elif "restart the system" in userData:
        txt2sp.txt2sp("Restarting the system.")
        os.system("shutdown /r /t 5")
        return "Restarting the system."
    
    elif "sleep" in userData:
        txt2sp.txt2sp("Sleeping")
        os.system('powershell -command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Application]::SetSuspendState(\'Suspend\', $false, $false)"')
        return "System is going to sleep."
    elif  userData in ["close","close close", "lose" , "shut up"]:
        exit()
    else:
        txt2sp.txt2sp("Sorry Sir, I didn't understand that. Can you please repeat?")
        return "Sorry Sir, I didn't understand that. Can you please repeat?"