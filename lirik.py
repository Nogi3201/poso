import time
from threading import Thread
import sys

lyrics = [
    ("Di hahurangan ki", 0.1),
    ("Ai hodo patikkoson au", 0.12),
    ("Molo borngin lasni ari", 0.11),
    ("Ingot do ho tu au", 0.11),
    ("Mauliate ma inang", 0.15),        
]

delays = [0, 3.0, 7.0, 10.0, 13.0, ]

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
