import speech_recognition
import pyttsx
import webbrowser
import wikipedia
import winsound

speech_engine = pyttsx.init('sapi5')         
speech_engine.setProperty('rate', 150)
r = speech_recognition.Recognizer()                                                                         #starting the speech_recognition recognizer                                                                     #it works with 1.2 as well
freq=500
dur=700
recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold=400


def speak(text):
   speech_engine.say(text)
   speech_engine.runAndWait()

def listen():
    with speech_recognition.Microphone() as source:
        
        audio = recognizer.listen(source,timeout=None)
        
    try: 
        #return str(recognizer.recognize_google(audio)) #returneaza string
        return str(recognizer.recognize_google(audio, key = None, language = "en-US", show_all = False))
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""




def listen_string():
    winsound.Beep(freq,dur)
    with speech_recognition.Microphone() as source:
        
        audio = recognizer.listen(source,timeout=None)
        
    try: 
        #return str(recognizer.recognize_google(audio)) #returneaza string
        return str(recognizer.recognize_google(audio, key = None, language = "en-US", show_all = False))
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

def print_keywords():
   print("Keywords:\n 'list'-prints list of keywords again\n 'wikipedia'-search on wikipedia about \n 'search'-search for what are you saying\n  'video'-opens youtube video \n'bye'-stop program\n")
   speak("Keywords:\n 'list'-prints list of keywords again\n 'wikipedia'-search on wikipedia about \n 'search'-search for what are you saying\n  'video'-opens youtube video \n 'bye'-stop program\n")
   speak("I am waiting for a keyword")
   



def search_for():
      speak("What am I searching for?")
      search=listen_string()
      words=search.split()
      del words[0:2]
      st=' '.join(words)
      speak("I am searching for "+str(st))
      url='http://google.ro/search?q='+str(st)
      webbrowser.open(url)
      speak('Google results for:'+ str(st))
def wikipedia_search():
   wikipedia.set_lang("en")
   speak("What am I searching for on wikipedia?")
   search=listen_string()
   words=search.split()
   del words[0:2]
   st=' '.join(words)
   speak("I am searching for "+str(st))
   wksum=wikipedia.summary(st, sentences=3)
   speak(wksum)
def video_for():
   speak("what am i searching for?")
   search=listen_string()
   #words=search.split
   #st=''.join(words)
   print('Vidoe results for' +search)
   url='https://www.youtube.com/results?search_query='+search
   webbrowser.open(url)
   speak('Video results for' +search)

def commands(): 
   speak("hello, please speak after the beep. what is your name?")
   user=listen_string()
   print("user is:"+user)
   speak("Hello " +user+" we are friends now")
   print_keywords()

   while(True):

      kw="list"
      ex="bye"
      sc="search"
      wp="Wikipedia"
      vd="video"
      speak("How can I help you?")
      command=listen_string()
      print("you said " + command)
         
      if kw in command:
         print_keywords()
      elif vd in command:
         video_for()
      elif sc in command:
         search_for()
      elif wp in command:
         wikipedia_search()
      elif ex in command:
         speak("bye"+user)
         break

while(True):
   tr="start"
   command=listen()
   if tr in command:
      commands()
   
   
