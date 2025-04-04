 import os
from click import command
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def commands():
        r=sr.Recognizer()
        with sr.Microphone()as source:
            print("Listening......")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
        try:
            print("wait for few moments......")
            query = r.recognize_google(audio,language='en-in')
            print(f"you just said: {query}\n")
        except Exception as e:
            print(e)
            speak("please tell me again")
            query="none"
        return query 
def wakeUpCommands():
     r=sr.Recognizer()
     with sr.Microphone()as source:
          print("Sleeping!....")
          r.pause_threshold = 1
          r.adjust_for_ambient_noise(source,duration=1)
          audio=r.listen(source)
     try:
          query = r.recognize_google(audio,language='en-in')
          print(f"you just said: {query}\n")
     except Exception as e:
          query="none"
     return query 
def wishings():
     hour = int(datetime.datetime.now().hour)
     if hour >=0 and hour<12:
          print("  GOOD MORNING SIR,HAVE A NICE DAY")
          speak("  GOOD MORNING SIR,HAVE A NICE DAY")
     elif hour>=12 and hour<17:
          print("  GOOD AFTERNOON SIR")
          speak("  GOOD AFTERNOON SIR")
     elif hour>=17 and hour<19:
          print("  GOOD EVENING SIR")
          speak("  GOOD EVENING SIR")
     else:
          print(" WELCOME TO NIGHTSHIFT SIR")
          speak(" WELCOME TO NIGHTSHIFT SIR")      
if __name__ == "__main__":
     while True:
          query=wakeUpCommands().lower()
          if 'activate command mode' in query:
               print("Activating Command Mode Sir!.....")
               speak("Activating command mode sir!.....")
               wishings()
               print("Yes Sir What Can I Do For You!...")
               speak("Yes Sir What Can I Do For You!...")
               while True:          
                    query = commands().lower()
                    if'time' in query:
                         strTime = datetime.datetime.now().strftime("%H:%M:%S")
                         speak("Sir, Now The Time Is: " + strTime)
                         print(strTime)
                    if'mute'in query:
                         speak("I'm Muting Sir!....")
                         break
                    if'exit program'in query:
                         print("I'm Leaving Sir,Byeee!.....Don,t Forgot To Take Your Meal Sir!...")
                         speak("I'm Leaving Sir,Byeee!.....Don,t Forgot To Take Your Meal Sir!...")
                         quit()
                    if 'open chrome'in query:
                         speak("Opening Chrome Sir ")
                         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                         while True:
                              chromeQuery=commands().lower()
                              if "search" in chromeQuery:
                                   youtubeQuery=chromeQuery
                                   youtubeQuery=youtubeQuery.replace('search',"")
                                   pyautogui.write(youtubeQuery)
                                   pyautogui.press('enter')
                                   speak('searching!....')
                              elif 'close chrome' in query:
                                   pyautogui.hotkey('ctrl','w')
                                   speak("closing the chrome sir!...")
                                   break
                    if 'lets begin the work'in query or 'open ardunio' in query:
                         speak("Optimising Sir!...")
                         speak("please wait!...")
                         speak("opening Arduino Sir!...")
                         os.startfile("C:Users\\karthikeyen\\AppData\\Local\\Programs\\Arduino IDE\\Arduino IDE.exe")
                    if 'open media player' in query:
                         speak("Opening vlc media player Sir ")
                         os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
                    if 'open file manager' in query:
                         speak("Opening file manager Sir ")
                         os.startfile("C:\\Users\\karthikeyen\\OneDrive\\Desktop\\This PC - Shortcut.lnk")
                    if'play music' in query or 'play song' in query or 'play a song' in query:
                         speak("playing song sir")
                         os.startfile("C:\\Users\\karthikeyen\\OneDrive\\Music\\Playlists\\new.wpl")
                    if 'next song' in query:
                         speak("Next Song Sir!...")
                         pyautogui.hotkey('ctrl','f')
                    if 'previous song' in query:
                         speak("Previous song Sir!...")
                         pyautogui.hotkey('ctrl','b')
                         pyautogui.hotkey('ctrl','b')
                    if 'shuffle' in query:
                         speak("shuffling Song Sir!...")
                         pyautogui.hotkey('ctrl','h')
                    if 'volume up'in query or 'increase volume' in query:
                         speak("increasing volume sir!....")
                         pyautogui.press('f3')
                    if 'continue'in query or 'resume' in query or 'stop' in query or 'pause' in query:
                         speak("Ok sir!....")
                         pyautogui.press('space')
                    if 'wikipedia' in  query:
                         speak("searching in wikipedia")
                         try:
                              query=query.replace("wikipedia",'')
                              results = wikipedia.summary(query, sentences=2)
                              print(results)
                              speak("according to wikipedia..")
                              speak(results)
                         except:
                              print("No Results Found..")
                              speak("No Results Found..")
                    if 'youtube' in query :
                         playquery=query.replace("youtube",'')
                         playquery=query.replace("play",'')
                         speak("playing"+playquery)
                         pywhatkit.playonyt(playquery)
                    if 'write' in query:
                         speak("Please tell me what  should I write")
                         while True:
                              typequery = commands()
                              if typequery=="exit typing": 
                                   print("Done Sir")
                                   speak("Done Sir")
                                   break 
                              else:
                                   pyautogui.write(typequery)
                    if'minimize the window'in query or 'minimise ' in query or 'minimize' in query :
                         pyautogui.hotkey('win','down','down')
                         speak('minimizing sir!...')
                    if'maximize the window'in query or 'maximise ' in query :
                         pyautogui.hotkey('win','up','up')
                         speak('maximizing sir!....')
                    if'close'in query or 'close the window' in query :
                         pyautogui.hotkey('ctrl','w')
                    if'open control panel'in query or 'control ' in query :
                         pyautogui.moveTo(1733,1050)
                         pyautogui.leftClick()
                    if'screenshot'in query:
                         speak('taking screenshot sir')
                         pyautogui.press('prtsc')
                    if 'open our channel'in query or 'go to our channel'in query or 'our channel' in query or 'youtube channel' in query:
                         speak("Opening Our Channel sir!....")
                         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                         while True:
                              pyautogui.write('https://www.youtube.com/channel/UCZpzgFrQrpkn1pB6uuiUxDA')
                              pyautogui.press('enter')
                              break                     
                    if 'open canva'in query:
                         speak("Opening canva Sir ")
                         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                         while True:
                              pyautogui.write('https://www.canva.com/')
                              pyautogui.press('enter')
                              break                
