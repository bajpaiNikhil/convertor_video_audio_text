

import speech_recognition as sr

import textwrap
# import json
r=sr.Recognizer()

with sr.AudioFile("audioo.wav") as source:
    r.adjust_for_ambient_noise(source, duration=1)
    audio=r.listen(source)
    #print(r.recognize_google(audio,show_all=True))
    try:
        text=r.recognize_google(audio,show_all=True)
        print("stupid")
        file2 = open('myfile3.txt', 'w')
        s=text['alternative'][0]['transcript']
        file2.writelines("\n".join(textwrap.wrap(s,56)))
        # file2.writelines(text['alternative'][0]['transcript'])
        # file2.close()
        # print(text)

        print(text['alternative'][0]['transcript'])
    except:
        print("NOt working")
    # #text=r.recognize_google(audio,key="AIzaSyDRdSN1VaRW27HxA68rZW5FesS2qoPD8", language="fr-FR",show_all=True)
    # sFinalResult = r.recognize_google(audio,language='en',show_all=True)
    # text = json.dumps(sFinalResult, ensure_ascii=False).encode('utf8')
    # print("stupid")
    # print(text)
    #     # print("Not being able to read")