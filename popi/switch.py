import time
import wiringpi

class RemoteSwitch(object):
   repeat = 10 # Number of transmissions
   pulselength = 300 # microseconds

   def __init__(self, unit_code, system_code=[1,1,1,1,1], pin=17):
      '''
      devices: A = 1, B = 2, C = 4, D = 8, E = 16
      system_code: according to dipswitches on your Elro receivers
      pin: according to Broadcom pin naming
      '''
      self.pin = pin
      self.system_code = system_code
      self.unit_code = unit_code

   def switchOn(self):
      self._switch(wiringpi.HIGH)

   def switchOff(self):
      self._switch(wiringpi.LOW)

   def _switch(self, switch):
      self.bit = [142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 142, 136, 128, 0, 0, 0]

      for t in range(5):
         if self.system_code[t]:
            self.bit[t]=136
      x=1
      for i in range(1,6):
         if self.unit_code & x > 0:
            self.bit[4+i] = 136
         x = x<<1

      if switch == wiringpi.HIGH:
         self.bit[10] = 136
         self.bit[11] = 142

      bangs = []
      for y in range(16):
         x = 128
         for i in range(1,9):
            b = (self.bit[y] & x > 0) and wiringpi.HIGH or wiringpi.LOW
            bangs.append(b)
            x = x>>1

      wiringpi.wiringPiSetupSys()
      wiringpi.pinMode(self.pin,wiringpi.OUTPUT)
      wiringpi.digitalWrite(self.pin,wiringpi.LOW)
      for z in range(self.repeat):
         for b in bangs:
            wiringpi.digitalWrite(self.pin, b)
            time.sleep(self.pulselength/1000000.)

