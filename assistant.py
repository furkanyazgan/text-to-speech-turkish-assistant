from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os

r = sr.Recognizer()

 # texti sese çevirme türkçe
def speak(audioString):

    tts = gTTS(text=audioString, lang='tr')
    tts.save("audio.mp3")

    playsound("audio.mp3")

    os.remove('audio.mp3')


# soru cevaplama asistanı
def cevapla(text):
    print("Soru :" , text)
    cevap = "seni anlayamadım"


    if(text == "ne haber"):
        cevap = "iyi sen"

    if (text == "neredesin"):
        cevap ="burdayım"

    if (text == "ben geldim"):
        cevap = "hoşgeldin"



    # cevabı sese çevir
    speak(cevap)
    print("Cevap:",cevap)



# sesi texte çevirme
while (1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2,language='tr-tr')

            MyText = MyText.lower()



            cevapla(MyText)


    except sr.RequestError as e:
        print("Sonuçlar istenemedi internet yavaş olabilir; {0}".format(e))

    except sr.UnknownValueError:
        print("Yüksek sesle konuşun lütfen.")








