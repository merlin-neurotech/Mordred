import playsound
import random

#testing purposes I think -------------------------------------
# def find_song(wave_flag):
#     # for alpha waves
#     if (wave_flag == True):
#         playsound()
# --------------------------------------------------------------

feelings_to_songs = {
    #We are going to look at only alpha waves, deciding between focused or unfocused (compared to baseline)

    #Alpha waves
    # focused songs are pretty hype, and are to be used for a GRIND
    "Focused": ["screamsaver_subtronics", "thelastgoodbye_odesza","makeithappen_rufus","thedifference_flume","pianosonatanumber9_mozart"],
    # not focused songs are much more relaxed, used to take a break and unwind from the grind sesh that was just finished
    "NotFocused": ["16missedcalls_brent", "marvinsroom_drake", "rollinginthedeep_adele", "shotsforme_drake", "words_gregalanisakov"],

    # code we won't use -----------------------------------------------------------------------
    # #Theta waves 
    # "Sleepy": ["intermezzo_pietro","rise_lunarskybox","ivory_trxxshed","words_gregoryalan","jetelaisserai_patrickwatson",""],
    # "Awake": ["Someone Like You - Adele"],
    # #Beta waves
    # #Classical
    # "Chill": ["Break Stuff - Limp Bizkit"],
    # #EDM
    # "Pumped": ["Summer of '69 - Bryan Adams"],
    # #Gamma waves
    # "Transcendant": ["Interstellar - Hans Zimmer?"],
    # "Disoriented": ["Creepy Music"]
    # -------------------------------------------------------------------------------------------
}


arrKey = "NotFocused"

# this is the code we want to loop. If we loop the entire file then the song array will be reinitialized each time
n = random.randint(0, len(feelings_to_songs[arrKey]) - 1)
print (len(feelings_to_songs[arrKey]), "\n")
print (feelings_to_songs[arrKey][n])
playsound.playsound(arrKey+"/"+feelings_to_songs[arrKey][n]+".mp3", True)
print (arrKey+"/"+feelings_to_songs[arrKey][n]+".mp3", "\n")

feelings_to_songs[arrKey].pop(n)
print (feelings_to_songs[arrKey])



