import random
import sys
import time

SCRAMBLE_WORDS = "ABCDEF@HIJ_LM%OPQR^WX#YZa#b+cdefgh*iqrxyz0123456789"
#ticking rate
SCRAMBLE_SPEED_MS = 50
#seconds on how the scramble before revealing
SCRAMBLE_TIME = 0.5
#revealing left to right characters
REVEAL_TIME = 1.5

def scramble_reveal(text, scramble_time=SCRAMBLE_TIME, reveal_time=REVEAL_TIME, ticking_ms=SCRAMBLE_SPEED_MS):
    # we are going to use time.monotonic() for measuring elapsed time
    start = time.monotonic()

    while True:
        #subtracting to get the exact value
        elapsed = time.monotonic() - start

        #Checking if it is still on the scramble mode
        if elapsed < scramble_time:

            out = "".join(random.choice(SCRAMBLE_WORDS) for _ in text)
            done = False
        else:
            #the elapsed - scramble_time -> get rid of the 0.5
            #dividing it to the reveal time
            progress = min((elapsed - scramble_time) / reveal_time, 1.0)
            #then we times the progress and length of the text
            #Example: 7 is the length and progress is 0.5 then which we times them and gives us the result 3.5 -> 3
            # 3 characters revealed but the others aren't until it comes to their turn
            reveal_count = int(progress * len(text))

            #Is the reveal count bigger than the current index? then if it is, put the actual char not if not then stays at randomize
            out = "".join(text[i] if i < reveal_count else random.choice(SCRAMBLE_WORDS) for i in range(len(text)))
            done = progress >= 1.0

        frame = f"{out}"
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()

        if done:
            break
        time.sleep(ticking_ms / 1000)

    print()


def main():
    prescripts = [
        "Sinner # 1 | YI SANG",
        "Sinner # 2 | FAUST",
        "Sinner # 3 | DON QUIXOTE",
        "Sinner # 4 | RYOSHU",
        "Sinner # 5 | MEURSAULT",
        "Sinner # 6 | HONG LU",
        "Sinner # 7 | HEATHCLIFF",
        "Sinner # 8 | ISHMAEL",
        "Sinner # 9 | SINCLAIR",
        "Sinner # 11 | RODION",
        "Sinner # 12 | OUTIS",
        "Sinner # 13 | GREGOR",
        # "_CLEAR._"
    ]

    print("Dante, can you please introduce your sinners?\n")
    for text in prescripts:
        input("press [ENTER] to continue")
        scramble_reveal(text)
    scramble_reveal("_CLEAR._")
if __name__ == "__main__":
    main()

