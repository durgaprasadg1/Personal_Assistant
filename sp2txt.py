import speech_recognition as sr
import txt2sp

def sp2t():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)

        try:
            voice_data = r.recognize_google(audio)
            if voice_data:  
                # print("You said:", voice_data)
                return voice_data
            else:
                # print("Didn't catch that.")
                txt2sp.txt2sp("Please repeat.")
        except sr.UnknownValueError:
            # print("Sorry, I didn't get that.")
            txt2sp.txt2sp("Please repeat.")
        except sr.RequestError:
            # print("Request Error occurred.")
            txt2sp.txt2sp("Please repeat.")
        except Exception as e:
            print("An error occurred:", e)
            txt2sp.txt2sp("Please repeat.")


