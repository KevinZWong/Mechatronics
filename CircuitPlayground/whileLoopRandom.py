import time
import board
import neopixel
from random import randint

def main():
    print("Starting Code Challenge")

    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
    pixels.fill((0, 0, 0))

    while True:
        try:
            user_input = int(input("Enter an integer number from 1 to 10: "))
        except ValueError as e:
            print("Invalid input. Please enter a valid integer.")
            continue

        if 1 <= user_input <= 10:
            print(f"Your number {user_input} is a valid integer from 1 to 10. Thanks")
            pixels[user_input - 1] = (0, 255, 0) 
            counter = 0
            guessed = False

            while counter < 5:
                if randint(1, 10) == user_input:
                    pixels[user_input - 1] = (0, 0, 255) 
                    guessed = True
                    break
                else:
                    pixels[user_input - 1] = (255, 0, 0) 
                counter += 1
                time.sleep(0.5) 

            if guessed:
                print(f'I Win, I guessed your number in {counter + 1} tries')
            else:
                print(f'You Win, I did not guess your number in {counter} tries')
        else:
            print(f"Your number {user_input} is not a valid integer from 1 to 10.")

    print("Ending Code Challenge")

main()
