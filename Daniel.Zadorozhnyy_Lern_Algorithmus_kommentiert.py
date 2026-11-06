import json # Das eingebaute JSON-Modul wird geladen. JSON ist ein Textformat, um Daten zu speichern. 
import difflib # Das Modul difflib wird geladen. Dieses Modul ermöglicht einen Vergleich zwischen Sequenzen, welche z.B. Texte sind oder Listen mit bestimmten Zeichenabfolgen.
import random # Das Modul random wird geladen. Es ermöglicht das Generieren von Zufallszahlen und die zufällige Auswahl von Elementen aus einer Sequenz, die z.B. eine Liste sein könnte.


DATEI_NAME = "wissen.final.json" # Variable speichert einen String

def wissen_laden(): # Nebenfunktion wird definiert
    try:
       
        with open(DATEI_NAME, 'r', encoding='utf-8') as datei: # Die Datei mit dem Namen wissen.json.neu wird geöffnet. Das r steht für Lesemodus, bei welchem die Datei zum Auslesen geöffent wird.
            # Das utf-8 sorgt für eine Umwandlung von Zahlen zu Zeichen, da der Computer nur Zahlen speichern kann. Dabei steht die 8 für 8 Bits, was ein Byte ist.
            # Schriftzeichen werden in Bytes ugewandelt (1-4 Bytes pro Zeichen).
            return json.load(datei) # Die Datei wird ausgelesen und von einer JSON-Datei in eine Python-Dictionary umgewandelt. 
    except FileNotFoundError: # Wenn die Datei nicht gefunden wird, dann wird folgender Inhalt zurückgegeben:
       
        return {
            "bot_wissen": {
    "hallo": ["Hi!", "Moin!", "Hallo, wie gehts?", "Guten Tag!"],
    "wie viele planeten hat unser sonnensystem?": ["8.", "Unser Sonnensystem hat 8 Planeten.", "Insgesamt hat unser Sonnensystem 8 Planeten."],
    "aus welchem gas besteht die luft größtenteils?": ["Aus Stickstoff.", "Aus Stickstoff, welcher ca. 78% der Luft ausmacht.", "Das am meisten vorkommende Gas ist Stickstoff."]
},
            "menge": [0]
}

def wissen_speichern(das_wissen): # Nebenfunktion wird definiert
 
    with open(DATEI_NAME, 'w', encoding='utf-8') as datei: # Das W steht für den Schreibmodus, bei dem eine neue Datei erstellt wird oder komplett überschrieben wird, wenn sie schon existiert.
        json.dump(das_wissen, datei, indent=4) # indent sorgt für schöne Formatierung und die 4 steht für 4 Leerzeichen, mit denen Codeblöcke eingerückt werden.
        #Json.dump() sorgt dafür, dass die Python-Daten wie z.B. eine Dictionary in einen JSON-Text umgewandelt werden.
        # Das_wissen ist ein Parameter, der für die Daten steht, welche umgewandelt und gespeichert werden sollten. In der Variable datei wird die geöffnete Datei gespeichert.
        

daten = {"bot_wissen": { # Hier wird eine Dictionary definiert, welche eine weitere Dicitonary enthält und eine Liste. Die Speicherung in dieser Form ermöglicht es, nur mit einer JSON-Datei zu arbeiten. 
    "hallo": ["Hi!", "Moin!", "Hallo, wie gehts?", "Guten Tag!"],
    "wie viele planeten hat unser sonnensystem?": ["8.", "Unser Sonnensystem hat 8 Planeten.", "Insgesamt hat unser Sonnensystem 8 Planeten."],
    "aus welchem gas besteht die luft größtenteils?": ["Aus Stickstoff.", "Aus Stickstoff, welcher ca. 78% der Luft ausmacht.", "Das am meisten vorkommende Gas ist Stickstoff."]
},
            "menge": [0]
}

def eingabe_vorhanden(): # Nebenfunktion wird definiert.
    antworten = bot_wissen[user_eingabe] # Der Inhalt der Dictonary an dem Key, welcher eingegeben wurde, wird in der Variable antworten gespeichert.
    if len(antworten) == 0: # Falls in dem Key kein Inhalt vorhanden ist, wird folgendes geprintet:
        print("Bot: Darauf habe ich keine Antwort.")
    else: # Wenn es doch Inhalt in dem Key gibt, wird ein gespeichertes Element per Zufall geprintet. 
        print("Bot:", random.choice(antworten))
        
    menge[schluessel.index(user_eingabe)] = menge[schluessel.index(user_eingabe)] + 1 # Der Zahl in der Liste Menge, an der Stelle von der Liste schluessel, welche nur die Keys der Dictionary bot_wissen
    # enthält, wird der Wert 1 dazuaddiert. Dies zeigt wie oft ein Key aus der Dictionary geschrieben wurde. Die beiden Listen sind demnach analog zueinander.
    daten["menge"] = menge # Die Liste menge mit dem neuen Inhalt wird in der Dictionary daten an dem Key menge gespeichert. Somit enthält die große Dictionary nun das neue "Wissen".
    wissen_speichern(daten) # Siehe oben.
    
    if antworten_hinzufuegen == True: # Falls antworten_hinzufuegen True ist, wird diese If-Bedingung ausgeführt.
        print("Bot: Möchtest du, dass ich eine neue Antwort auf diese Frage lerne?")
        zusatz_antwort = input("Deine neue Antwort (oder 'skip'): ") # In dieser Variable wird der Input gespeichert.
        if zusatz_antwort != "skip": # Wenn die Antwort nicht skip ist, wird die Antwort der Dictionary unter dem Key, welcher vorher eingegeben wurde, hinzugefügt. Dies macht der Befehl .append().
            bot_wissen[user_eingabe].append(zusatz_antwort) 
            print("Bot: Danke! Ich habe es mir gemerkt.")
        daten["bot_wissen"] = bot_wissen # Die Dictionary bot_wissen wird in der Dictionary daten an dem Key bot_wissen gespeichert. 
        wissen_speichern(daten) # Siehe oben.
        if zusatz_antwort == "skip":
            print("Bot: Oh, okay.")


daten = wissen_laden() # In der Variable daten werden entweder die JSON-Daten gespeichert oder falls diese nicht vorhanden sind, wird das zurückgegeben, was in der Nebenfunktion steht. 

bot_wissen = daten["bot_wissen"] # In der Variable bot_wissen wird der Inhalt des Keys bot_wissen von der Dictionary daten gespeichert. 

menge = daten["menge"] # In der Variable menge wird der Inhalt des Keys menge von der Dictionary daten gespeichert.

schluessel = list(bot_wissen.keys()) # In der Variable schluessel werden die Keys von der Dictionary bot_wissen als Liste gespeichert.

if len(menge) == 1:
    menge = [0] * len(schluessel) # Falls menge nicht die JSON-Daten bekommt, muss Anzahl der Indizes an schluessel angepasst werden. Wenn man das nicht machen würde, würde eine Funktion weiter unten
    # im Code nicht richtig funktionieren.
    
liste = [] # Das ist eine leere Liste. Die Funktion von ihr wird weiter unten im Code nochmal erklärt. 

befehle = ["/help", "/delete", "/statistics"] # Diese Liste bekommt folgende Elemente. Ich habe diese Liste gemacht, weil sonst eine if-Bedingung weiter unten im Code recht lang geworden wäre
# (Siehe Zeile 176).


print("--- Willkommen beim Chatbot (Beenden mit 'exit' und für Hilfe '/help') ---") # Das, was alles innerhalb den äußersten Klammern steht wird geprintet.

modus = input("Möchtest du neue Antworten hinzufügen können?: ").lower().strip() # Die Eingabe vom Benutzer wird durch den Befehl .lower() in Kleinbuchstaben geschrieben und der Befehl .strip() bewirkt,
# dass Leerzeichen vor einem Wort oder einem Satz und nach einem Wort oder einem Satz komplett weggemacht werden. Diese Befehle sorgen dafür, dass Eingaben auch mit falscher Schreibweise
# und versehentlichen Leerezeichen trotzdem erkannt werden.
if modus == "ja": # Wenn die Eingabe ja war dann bekommt die Variable den Wert True.
    antworten_hinzufuegen = True
else: # Falls die Eingabe nicht ja war, bekommt die Variable den Wert False.
    antworten_hinzufuegen = False

while True:

    user_eingabe = input("Du: ").lower().strip() # Die Eingabe vom Benutzer wird durch den Befehl .lower() in Kleinbuchstaben geschrieben und der Befehl .strip() bewirkt, dass Leerzeichen vor einem
    # Wort oder einem Satz und nach einem Wort oder einem Satz komplett weggemacht werden. Diese Befehle sorgen dafür, dass Eingaben auch mit falscher Schreibweise und versehentlichen Leerezeichen
    # trotzdem erkannt werden.

    if user_eingabe == "exit":
        daten["bot_wissen"] = bot_wissen # Der Inhalt von bot_wissen wird in der Dictionary daten in dem Key bot_wissen gespeichert.
        daten["menge"] = menge # Der Inhalt von menge wird in der Dictionary daten in dem Key menge gespeichert.
        wissen_speichern(daten) # Siehe oben.
        print("Wissen gespeichert. Tschüss!")
        break # Mit diesem Befehl werden While- und For-Schleifen komplett beendet.
    
    if user_eingabe == "/delete":

        while True:
    
            e = True 
            while e == True: # Diese While-Schleife wird erst beendet, wenn die Variabel e den Wert False hat. Dies geschieht, wenn das Passwort richtig gewählt wurde oder man skip eingetippt hat.
                passwort = input("Passwort (oder 'skip'): ")
                if passwort == "keks":
                    e = False
                if passwort == "skip":
                    break
        
                while e == False: # Diese While-Schleife wird erst ausgeführt, wenn man das richtige Passwort eingetippt hat und somit die Variable e den Wert False hat.
                    loeschen = input("Welcher Eintrag soll gelöscht werden?: ").lower().strip()
                    if loeschen in bot_wissen: 
                        liste = bot_wissen[loeschen] # In der Variable liste wird der Inhalt des Keys, welcher eingetippt wurde, gespeichert. 
                        print(liste)
                        
                        while True:
                            index = input("Index, welcher gelöscht werden soll: ") # Hier wird der Index gespeichert, welcher gelöscht werden soll.
                        
                            try: # Erstmal wird dieser Block ausgeführt.    
                                index = int(index) # Wenn der Index eine Zahl ist, dann kann er auch als Integer gespeichert werden. Er muss als Integer gespeichert werden damit der Befehl liste[index]
                                # ausgeführt werden kann.
                                if index <= len(liste) - 1: # Wenn der Index kleiner als die Länge der Liste -1 ist, dann kann diese If-Bedingung ausgeführt werden. Len(liste) muss mit 1 subtrahiert
                                    # werden, weil wenn beispielsweise eine Liste 3 Elemente besitzt, sie die Länge 3 haben wird, jedoch wird ja mit dem Index 0 angefangen zu zählen. Würde man jetzt das
                                    # Subtrahieren weglassen, so könnte es sein, dass man liste[3] hätte, was zu einem Fehler führen würde, da es diesen Index nicht gibt. das letzte Element hätte in
                                    # diesem Beispiel den Index 2.
                                    del liste[index] # Mit dem Befehl del wird hier der Inhalt der Liste an dem eingetippten Index komplett gelöscht.
                                    break
                                else:
                                    print("Bot: Dieser Index existiert nicht.") # Falls der Index nicht existiert, wird folgendes geprintet. Danach wird die While-Schleife von neu ausgeführt.
                                
                            except ValueError: # Falls das, was man in die Variable Index reingeschrieben hat keine Zahl ist, wird dies ausgeführt, da nur Zahlen als Integer gespeichert werden können.
                                print("Bot: Das ist keine Zahl.")
                        
                        bot_wissen[loeschen] = liste # Die Dictionary bot_wissen an dem Key loeschen, welcher vorher eingetippt wurde, bekommt den Inhalt der Liste, in welchem ein Teil gelöscht wurde.
                        daten["bot_wissen"] = bot_wissen # In der Dictionary daten an dem Key bot_wissen wird die Dictionary bot_wissen mit dem veränderten Inhalt gespeichert.
                        wissen_speichern(daten) # Siehe oben.
                        print(liste)  
                        break
                    else: # Falls es den Key nicht gibt, welchen man reingeschrieben hat, wird dies ausgeführt.
                        print("Bot: Diesen Eintrag gibt es nicht.")
                       
            break
 
    if user_eingabe == "/statistics": # In dieser If-Bedingung wird nacheinander die Liste schluessel und die Liste menge mit dem selben Index geprintet bis die kompletten Listen geprintet wurden.
        for i in range (len(schluessel)):
            print(schluessel[i], ": ", menge[i])
 
 
    if user_eingabe in bot_wissen: # Falls die Eingabe vom Benutzer in der Dictionary vorhanden ist, wird diese If-Bedingung ausgeführt.
        eingabe_vorhanden() # Siehe oben.


    if user_eingabe.isspace() or user_eingabe == "": # Der Befehl .isspace() prüft, ob ein String ausschließlich aus Leerzeichen besteht und "" steht für komplett leere Eingaben. Diese If-Bedingung dient
        # dazu um leere Eingaben zu erkennen.
        print("Bot: Bitte gib keine leeren Eingaben ein.")


    if user_eingabe == "/help": # Wenn /help eingetippt wurde, wird diese If-Bedingung ausgeführt. 
        print("---Befehle--- \nEintrag aus Dictionary löschen: /delete \nAnzahl aller eingegebenen Fragen, etc.: /statistics \n-------------") # Das \n wird benuttzt, um einen Zeilenumbruch zu machen.


    if "/" in user_eingabe and not user_eingabe in befehle: # Diese If-Bedingung wird ausgeführt, wenn in der Eingabe ein / enthalten ist und wenn die Eingabe nicht in der Liste befehle vorhanden ist.
        # Somit werden unbekannte Befehle erkannt.
        print("Bot: Diesen Befehl gibt es nicht.")
     
     
    if user_eingabe not in bot_wissen and not user_eingabe in befehle and not user_eingabe.isspace() and not user_eingabe == "" and not "/" in user_eingabe:
        # Die If-Bedingung wird ausgeführt, wenn die Eingabe nicht in der Dicitonary bot_wissen und nicht in der Liste befehle vorhanden ist und wenn die Eingabe keine leere Eingabe ist und kein /
        # enthält. 
        wort_vorhanden = False # Diese Variable bekommt den Wert False
        alte_eingabe = user_eingabe # Die user_eingabe wird in diese Variable gespeichert.
        for i in range(len(schluessel)):# Die For-Schleife geht genauso lange wie die Länge der Liste schluessel ist.
            user_eingabe = user_eingabe.replace(" ","") # Der Befehl replace sorgt hier in diesem Fall, dass alle Leerzeichen entfernt werden, da die Leereichen mit "" ersetzt werden. 
            ratio = difflib.SequenceMatcher(None, user_eingabe, schluessel[i].replace(" ","")).ratio() # In der Variable ratio wird folgendes gespeichert. SequenceMatcher ist eine Klasse
            #aus dem Modul difflib, welche zwei Strings miteinander auf Ähnlichkeit vergleicht. An der Stelle von None kommt eigentlich eine Funktion hin, welche erkennen soll, ob ein Symbol ignoriert
            # und sozusagen als "Müll" angesehen werden kann. Das None bewirkt, dass es keine Funktion gibt, welche solchen "Müll" erkennt. Somit werden alle Zeichen bei diesem Vergleich berücksichtig.
            # Die zu vergleichenden Strings sind in diesem Fall user_eingabe und schluessel and dem Index i, bei welchem auch alle Leerzeichen entfernt wurden. Das .ratio() berechnet die Ähnlichkeit
            # zwischen den beiden Strings und gibt dabei einen Wert zwischen 0.0 und 1.0 aus, wobei 1.0 für 100% steht.
            if ratio >= 0.5: # Die If-Bedingung wird ausgeführt, wenn ratio einen Wert von 0.5 oder größer hat.
               print("Bot: Meintest du", schluessel[i], "?")
               eingabe = input("Du: ").lower().strip() # Der Input wird komplett kleingeschrieben und die Leerzeichen am Anfang und am Ende werden entfernt.
       
               if eingabe == "ja": # Die If-Bedingung wird ausgeführt, wenn man ja geschrieben hat.
                   user_eingabe = schluessel[i] # User_eingabe speichert den Inhalt von der Liste schluessel am Index i.
                   eingabe_vorhanden() # Siehe oben.
                   wort_vorhanden = True # Die Variable bekommt den Wert True.
                   break
                   
        
        if wort_vorhanden == False: # Diese If-Bedingung wird nur ausgeführt, wenn die Variable wort_vorhanden den Wert False hat.
            
            user_eingabe = alte_eingabe # Jetzt bekommt die user_eingabe den Inhalt von alte_eingabe. Das muss geschehen, weil sonst der Inhalt von user_eingabe gar keine Leerzeichen mehr hätte.
        
            print("Bot: Das weiß ich leider noch nicht.")
            print("Bot: Was soll ich darauf antworten?")
        
            neue_antwort = input("Deine Antwort (oder 'skip'): ") # Die Variabel speichert den Input.
        
            if neue_antwort != "skip": # Wenn die Eingabe nicht skip ist, wird die If-Bedingung ausgeführt.
                bot_wissen[user_eingabe] = [neue_antwort]
                print("Bot: Danke! Ich habe es mir gemerkt.")
            
                daten["bot_wissen"] = bot_wissen # In der Dictionary daten an dem Key bot_wissen wird der Inhalt bot_wissen gespeichert.
                wissen_speichern(daten) # Siehe oben.
            
                schluessel = list(bot_wissen.keys()) # Die Liste schluessel muss hier nochmal definiert werden, weil 
                menge.append(1) # Die Liste menge wid um einen weiteren Wert, welcher hier 1 ist, erweitert. Somit hat die Liste einen weiteren Index.
            
                daten["menge"] = menge # In der Dictionary daten in dem Key menge wird der Inhalt der Liste menge gespeichert.
                wissen_speichern(daten) # Siehe oben.