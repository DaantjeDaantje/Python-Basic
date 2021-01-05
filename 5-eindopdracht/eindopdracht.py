#%%

#Hier vraag ik welke tijd je wilt beginnen
uur = input("Voer uur in:"); uur = int(uur)
min = input("Voer min in:"); min = int(min)
sec = input("Voer sec in:"); sec = int(sec)

#Hier wordt de tijd library van python ingegoegd
import time
#Zolang de loop True is wordt de klok uitgevoerd
while True:
    #Hierdoor wordt de tijd op de scherm getoont
    print(str(uur).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2))
    sec = sec + 1
    time.sleep(1)
    #Hier wordt gecheckt of er totaal 60 sec is en dan reset de sec en gaat er 1 min bij.
    if sec == 60:
        sec = 0
        min = min + 1
    #Hier wordt gecheckt of er totaal 60 min is en dan reset de min en gaat er 1 uur bij.
    if min == 60:
        min = 0
        uur = uur + 1
    #Hier wordt gecheckt of er totaal 24 uur is en dan reset de de tijd en dan start er een nieuwe dag
    if uur == 24:
        uur = 0 
        min = 0
        sec = 0
# %%
