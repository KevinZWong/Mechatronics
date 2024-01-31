import time
import board
import neopixel

def transition(pixels, start_RGB, end_RGB, length):
    # Calculate the time to wait before changing each color component
    time_RGB = [length / max(1, abs(end - start)) for start, end in zip(start_RGB, end_RGB)]
    current_times_RGB = [time.time()] * 3
    direction = [1 if end > start else -1 for start, end in zip(start_RGB, end_RGB)]

    while start_RGB != end_RGB:
        for i in range(3):
            if time.time() - current_times_RGB[i] > time_RGB[i]:
                # Update the color component
                start_RGB[i] += direction[i]
                current_times_RGB[i] = time.time()
                pixels.fill(tuple(start_RGB))
                print(start_RGB)
                time.sleep(0.01)  # Add a small delay to see the transition

def main():
    print("Starting Color Transition")

    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
    start_color = [0, 0, 0]  # Starting color 
    end_color = [255, 200, 100]  # Ending color 
    transition_length = 10  # Transition length in seconds

    transition(pixels, start_color, end_color, transition_length)

    print("Ending Color Transition")

main()
