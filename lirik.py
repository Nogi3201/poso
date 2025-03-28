import time
from threading import Thread
import sys

lyrics = [
    ("Di hahurangan ki", 0.6),
    ("Ai hodo patikkoson au", 0.7),
    ("Molo borngin lasni ari", 0.6),
    ("Ingot do ho tu au", 0.8),
    ("", 0.5),
    ("Mauliate ma inang", 0.6),
    ("Di sude haholongan mi", 0.7),
    ("Inanghu naburju na uli lagu", 0.8),
    ("", 0.5),
    ("Di tangiangmi i inang", 0.6),
    ("Di haholongan mi tu au", 0.7),
    ("Apus ma ilumi inang", 0.6),
    ("Posroham posroham ale inang", 0.9)
]

delays = [0, 5.0, 11.0, 17.0, 20.8, 0, 5.0, 11.0, 17.0, 20.8, 0 , 0 , 0]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]  
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:  
        thread.join()

if __name__ == "__main__":  
    sing_song()
