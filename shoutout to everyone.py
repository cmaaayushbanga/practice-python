import pyttsx3

def pronounce_names(name_list):
    engine = pyttsx3.init()

    for name in name_list:
        shoutout = f"Shoutout to {name}"
        engine.say(shoutout)
        print(shoutout)

    engine.runAndWait()

if __name__ == "__main__":
    l = ["Nikhil", "Nishant Kumar", "Aayush Banga"]
    pronounce_names(l)
