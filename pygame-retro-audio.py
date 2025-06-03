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
    for i in range(num_samples):
        yield next(sample)


def build_samples(freq, duration):
    period = int(44100 / freq)
    samples = array("h", [0] * period)
    amplitude = 32767
    for time in range(period):
        if time < period / 2:
            samples[time] = amplitude
        else:
            samples[time] = -amplitude
    return samples


#    def parse_string(self, play_string):
#        tokenized = [f for f in re.findall("([a-z]|[0-9]+|[#+-><])", play_string) if f]
#        myarray = []
#        for j, i in enumerate(tokenized):
#            try:
#                k = tokenized[j+1]
#            except:
#                k = None
#            sharp = 0
#            if i == ">":
#                self.modifier += 12
#            elif i == "<":
#                self.modifier -= 12
#            elif i in ("n", "l"):
#                self.stac = False
#            elif i == "s":
#                self.stac = True
#            elif i == "t":
#                self.tempo = int(k)
#            elif i == "q":
#                if int(k) == 1:
#                    self.env = 1
#                else:
#                    self.env = 0
#            elif i == "v":
#                print(k)
#                self.current_vol = int(k)
#                self.current_volume = int(k) * self.vol_steps
#                print(self.current_volume)
#            elif i == "o":
#                self.modifier = (int(k) - self.octave) * 12
#            elif i == "p":
#                if k:
#                    self.notelen = int(k)
#                    f = 60.0/(self.tempo*(self.notelen/4.0))
#                    print(f)
#                    time.sleep(f)
#            elif i in self.major_notes:
#                if k:
#                    if k == "#" or k == "+":
#                        sharp = 1
#                    elif k == "-":
#                        sharp = -1
#                    elif k.isdigit():
#                        self.notelen = int(k)
#                x = self.play_note(i, sharp)
#                print (i, k)
#                sound = pygame.sndarray.make_sound(x)
#                sound.play()
#                time.sleep(len(x)/(self.sample_rate * 1.0))
#                self.notelen = 4
#
# print(multiplier, num_samples)

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
