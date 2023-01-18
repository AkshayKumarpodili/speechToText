import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.3)
        
        print('speak Now')
        
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            print("speaker:", text)
            if text == 'quit':
                break
        except:
            print('Pls Speak again !!')
            

