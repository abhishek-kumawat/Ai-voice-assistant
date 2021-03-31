engine = pyttsx3.init()
wolframalpha_app_id = 'api'  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
  

def wishes():
    speak("welcome back Sir Hope you are well I am your  Assistant")
    time_()
    date_()

    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning  sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon hope you are fine")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir have a wonderful day")     

    speak("at your service sir how can i help you")    

def take_comand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("go ahead listning.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("please say that again i didn't understand")
        return "None"
    return query 

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()   

    server.login('kumawatsaab4646@gmail.com','password')
    server.sendmail('sender@gmail.com',to,content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('Cpu is at'+usage)

    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishes()
    while True:
        query = take_comand().lower()

        if 'time' in query:     #tells time 
            time_()
            
        elif 'date' in query:
            date_()   

        elif 'wikipedia' in query:
            speak("searching..")
            query=query.replace("wikipedia",'')
            result=wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)              


        elif 'send email' in query:
            try:
                speak("what should I say ?")
                content=take_comand()

                speak("who is the reciever ? ")
                reciever=input("enter reciever's email id")

                to = reciever
                sendEmail(to,content) 
                speak(content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send email")    

        elif 'search in chorme' in query:
            speak('what should i search ?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            #chrome location 

            search = take_comand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')   #only .com allowd

        elif 'search in google' in query:
            speak("what should i search ?")
            search_term = take_comand().lower()
            speak('searching....')
            wb.open('https://www.google.com/search?q='+search_term)


        elif 'cpu' in query:
            cpu()


        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going offline sir ')
            quit()

        elif 'word' in query:
            speak("opening MS word..") 
            ms_word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk'
            os.startfile(ms_word) 

        elif "write a note" in query:
            speak("what to write sir..")
            notes = take_comand()
            file = open('notes.txt','w')
            speak("Sir should i include date and time?")
            ans = take_comand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('done taking notes sir')
            else:
                file.write(notes)    


        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())



        elif 'play music' in query:  
            songs_dir = 'E:\\Musics2021'
            music = os.listdir(songs_dir)
            speak('what should i play ?')
            speak('select a number...')        #random songs use this 
            ans = take_comand().lower()
            while('number' not in ans and ans != 'random' and ans !='you choose' and ans !='your choice'):
                speak('i could not understand sir please try again..')
                ans = take_comand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' or 'your choice' in ans:
                no = random.randint(1,21)

            os.startfile(os.path.join(songs_dir,music[no]))



        elif 'news' in query:
            try:
                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=in&apiKey=00e52e7e085747c3aa84f83357dada85')
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headlines from entertainment industry')
                print('*************TOP HEADLINES*****************')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                    print(str(e))    



        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)   



        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res =client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")    




