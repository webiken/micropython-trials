leds = [pyb.LED(i) for i in range(1,5)]
for l in leds:
    l.off()

n = 0
intensity = 0
blue = 4
try:
   while True:
      n = (n + 1) % 4
      if n == blue:
        ntensity = (intensity + 1) % 255
        leds[blue].intensity(intensity)
        pyb.delay(20)
      leds[n].toggle()
      pyb.delay(50)
finally:
    for l in leds:
        l.off()