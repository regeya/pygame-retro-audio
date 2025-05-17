import pygame
import random
import array
import time

# Initialize Pygame
pygame.mixer.pre_init(channels=1, allowedchanges=0)
pygame.init()
pygame.mixer.init()

# Define audio parameters
frequency = 440  # A4 note
amplitude = 0.5  # Volume (0.0 to 1.0)
sample_rate = 44100
duration = 0.5  # seconds

num_samples = int(sample_rate * duration)
wave_data = array.array("h")


def return_noise_samples(multiplier):
    while True:
        random_num = random.randint(-128, 128) << 8
        if random_num == 32768:
            random_num = 32767
        for i in range(multiplier):
            yield random_num


def generate_noise(multiplier, num_samples):
    sample = return_noise_samples(multiplier)
    print(sample)
    for i in range(num_samples):
        yield next(sample)

#    def build_samples(self):
#        period = int(round(get_init()[0] / self.frequency))
#        samples = array("h", [0] * period)
#        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
#        for time in range(period):
#            if time < period / 2:
#                samples[time] = amplitude
#            else:
#                samples[time] = -amplitude
#        return samples

print(multiplier, num_samples)

for multiplier in (4, 8, 16):
    wave_data = array.array("h")
    for sample in generate_noise(multiplier, num_samples):
        wave_data.append(sample)

    sound = pygame.mixer.Sound(buffer=wave_data)
    # Play the sound
    sound.play()
    time.sleep(1)

# Keep the program running until the sound finishes or the user quits
running = True
while running and pygame.mixer.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.mixer.quit()
pygame.quit()
