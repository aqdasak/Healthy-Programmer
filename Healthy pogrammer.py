from pygame import mixer
from time import time, sleep
from datetime import datetime

initWater = time()
initEyes = time()
initExercise = time()


def title():
    cls()
    print(":: :: :: HEALTHY PROGRAMMER :: :: ::")


def play_music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=-1)  # loops=-1 => loop indefinitely
    while True:
        a = input().lower()
        if a == stopper:
            mixer.music.stop()
            print("\n::::::::: GREAT :::::::::")
            sleep(0.2)
            title()
            break

        elif a == "hold":
            mixer.music.stop()
            hold()
            break

        elif a == "skip":
            mixer.music.stop()
            reset()
            title()
            break


def hold():
    cls()
    print(":: :: :: HEALTHY PROGRAMMER (on hold) :: :: ::")
    print("Input res to resume")
    while True:
        res = input().lower()
        if res == "res" or res == "resume":
            print("\nResuming...")
            reset()
            sleep(0.2)
            title()
            return 0


def reset():
    global initEyes, initWater, initExercise
    initWater = time()
    initEyes = time()
    initExercise = time()


def log(msg):
    with open("Healthy Programmer.txt", "a") as f:
        f.write(f"{msg}\t: {datetime.now()}\n")


def cls():
    from os import system, name
    # for windows os.name is 'nt'
    system('cls' if name == 'nt' else 'clear')


if __name__ == '__main__':
    cls()
    waterSec = 25 * 60
    eyesSec = 20 * 60
    exerSec = 45 * 60

    print(":: :: :: HEALTHY PROGRAMMER :: :: ::")
    while True:
        sleep(60)
        if (time() - initWater) > waterSec:
            print("Time to drink water. Input 'drank' to stop music or 'hold' to pause the program or 'skip' to skip all.")
            play_music("water.mp3", "drank")
            initWater = time()
            log("Water")
        if (time() - initEyes) > eyesSec:
            print("Time to do eyes exercise. Input 'eyes' to stop music or 'hold' to pause the program or 'skip' to skip all.")
            play_music("eyes.mp3", "eyes")
            initEyes = time()
            log("Eyes")
        if (time() - initExercise) > exerSec:
            print("Time to exercise. Input 'done' to stop music or 'hold' to pause the program or 'skip' to skip all.")
            play_music("exercise.mp3", "done")
            initExercise = time()
            log("Exercise")
