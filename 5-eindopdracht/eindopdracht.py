#%%

#Hier wordt de tijd library van python ingegoegd
import time

#Hier vraag ik welke tijd je wilt beginnen
uur = input("Voer uur in:"); uur = int(uur)
min = input("Voer min in:"); min = int(min)
sec = input("Voer sec in:"); sec = int(sec)

#dit is de function voor de klok
def klok(uur,min,sec):
    #dit er zodat het niet meer dan 24 uur kan worden.
    for u in range(uur, 24):
        #dit er zodat het niet meer dan 60 min kan worden.
        for m in range(min, 60):
            #dit er zodat het niet meer dan 60 sec kan worden.
            for s in range(sec, 60):
                #dit is zodat de uur reset
                if u == 23:
                    uur=0
                #dit is zodat de min reset
                if m == 59:
                    min = 0
                #dit is zodat de sec reset
                if s == 59:
                    sec = 0
                #Hierdoor wordt de tijd op de scherm getoont
                print(str(u).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)) 
                time.sleep(1)   

#Dit is zodat de klok aan gaat  
klok(uur,min,sec)

#Dit is er zodat de klok reset
while True:
    def klok2():
        #dit er zodat het niet meer dan 24 uur kan worden.
        for hh in range(0, 24):
            #dit er zodat het niet meer dan 60 min kan worden.
            for mm in range(0, 60):
                #dit er zodat het niet meer dan 60 sec kan worden.
                for ss in range(0, 60):
                    #Hierdoor wordt de tijd op de scherm getoont
                    print(str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2))
                    time.sleep(1)
    #Dit is zodat de 2e klok aan gaat                  
    klok2()

# %%
