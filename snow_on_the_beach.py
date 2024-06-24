import sys
from time import sleep

def print_lyrics():
    lines = [
       
        ("One night a few moons ago I saw flecks of what could've been lights", 0.13), #1
       
        ("But it might just have been you passing by unbeknownst to me", 0.13), #2
       
        ("Life is emotionally abusive and time can't stop me quite like you did", 0.12), #3
       
        ("And my flight was awful, thanks for asking I'm unglued, thanks to you", 0.10), #4 
       
        ("And it's like snow at the beach, weird but fucking beautiful Flying in a dream, stars by the pocketful", 0.10), #5
       
        ("You wanted me tonight, feels impossible But it's coming down, no sound, it's all around", 0.10), #6
       
        ("Like snow on the beach x4", 0.10), #7
       
        ("This scene feels like what I once saw on a screen I searched for aurora borealis green", 0.12),
       
        ("I've never seen someone lit from within Blurring out my periphery", 0.10) #8
    ]

    delays = [1, #1
              0.10, #2
              0.10, #3
              1, #4
              0.10, #5
              0.10, #6
              15, #7
              0.10, #8
              0.10]  #9                   
    
    print("[Music]")
    sys.stdout.flush()
    sleep(17)

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()
