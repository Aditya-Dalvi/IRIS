import pyttsx3 #pip install pyttsx3 #text to speech
import speech_recognition as sr #pip install speechRecognition
import datetime #shows date and time
import wikipedia #pip install wikipedia
import webbrowser #will open the default web browser
import os #connects the os with the code so can easily direct the files from the os
import smtplib #module that allows sending mails to any machine that uses SMTP protocol #protocol that helps transfering of files
import string #Shows the microphone output as text
import random #gives probability 

engine = pyttsx3.init('sapi5') #assigning voice to the engine(IRIS)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) #voice[1] for female voice
a = string.printable[:-5]

def speak(audio): #speak function that sends output through microphone
    engine.say(audio)
    engine.runAndWait()


def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Iris. Please tell me how may I help you")   

def generate_password():
    # Get all the ASCII characters that are printable
    a = string.printable[:-5]    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Didn't get you :'O say that again please...")
        speak('I did not get you')  
        return "None"
    return query

def sendEmail(to, content): #need to turn of the security option for the email option to work
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adityadalvi2016@gmail.com', '//gamil password')
    server.sendmail('adityadalvi2016@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('Opening stack over flow')
            webbrowser.open("stackoverflow.com")   
        
        elif 'smash carts' in query:
            speak('Opening smash carts')
            webbrowser.open("smashkarts.io")

        elif 'open scribble' in query:
            speak('Opening scribble')
            webbrowser.open("skribbl.io")
        
        elif 'open crazy games' in query:
            speak('Opening crazy games')
            webbrowser.open("crazygames.com")

        elif 'open minecraft server' in query:
            speak('Opening your minecraft server')
            webbrowser.open("aternos.org/go/")

        elif 'open college' in query:
            speak('Opening files')
            collegepath = 'D:\\College work\\DJ SANGHVI'
            os.startfile(collegepath)

        elif 'play music' in query:
            speak('playing music')
            music_dir = 'D:\\College work\\PROJECTS\\Python Projects\\JARVIS\\Music file'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\VS CODE\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adityadalvi2016@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email") 

        elif 'epic games' in query:
            speak('Opening files')
            epicgames = 'C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe'
            os.startfile(epicgames)

        elif 'minecraft' in query:
            speak('Opening files')
            mine = 'C:\\Users\\Aditya\\AppData\\Roaming\\.minecraft\\TLauncher.exe'
            os.startfile(mine)

        elif 'how are you' in query:
            speak("I am fine sir,hope you are well too!")

        elif 'joke' in query:
            speak('why does a banana wants to live alone? Because he is a kela.')
            speak('Sorry for this bad joke')
        
        elif 'password' in query:
            speak('how many digit password you want?')
            number = int(takeCommand())
            # Generate a random password
            password = ''.join(random.choice(a) for i in range(number))
            speak('here is your 8 digit password')
            print(password)

        elif 'bye' in query:
            speak('sayonara sir , have a good day!')
            exit()
        
        elif 'goodbye' in query:
            speak('sayonara sir , have a good day!')
            exit()
        