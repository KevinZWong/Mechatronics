import time
import board
import neopixel

def main():
    print("Starting Blinking Red Light")

    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
    pixels.fill((0, 0, 0)) 

    while True:
        pixels.fill((255, 0, 0))
        time.sleep(1) 

        pixels.fill((0, 0, 0))
        time.sleep(1) 

    print("Ending Blinking Red Light")

main()
