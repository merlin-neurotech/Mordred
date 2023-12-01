import playsound
import random

def find_song(wave_flag):
    # for alpha waves
    if (wave_flag == True):
        playsound()

feelings_to_songs = {
    #Theta waves 
    "Sleepy": ["intermezzo_pietro","rise_lunarskybox","ivory_trxxshed","words_gregoryalan","jetelaisserai_patrickwatson",""],

    "Awake": ["Someone Like You - Adele"],
    #Alpha waves
    "Focused": ["screamsaver_subtronics", "thelastgoodbye_odesza","makeithappen_rufus","thedifference_flume","pianosonatanumber9_mozart"],
    "NotFocused": ["partyintheusa_mileycyrus",],
    #Beta waves
    #Classical
    "Chill": ["Break Stuff - Limp Bizkit"],
    #EDM
    "Pumped": ["Summer of '69 - Bryan Adams"],
    #Gamma waves
    "Transcendant": ["Interstellar - Hans Zimmer?"],
    "Disoriented": ["Creepy Music"]
}

n = random.randint(0, len(feelings_to_songs["Focused"]) - 1)
print (feelings_to_songs["Focused"][n])
playsound.playsound("Focused/"+feelings_to_songs["Focused"][n]+".mp3", True)
# print (feelings_to_songs["Focused"])
# feelings_to_songs["Focused"].pop(0)
# print (feelings_to_songs["Focused"])


