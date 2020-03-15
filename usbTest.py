import serial
import time

uart = serial.Serial('COM4',9600, timeout=0)
"""
class UartThermalPrinter:

    def __init__(self, uart):
        self.uart = uart #share uart object

    #***Control Commands***

    #LF 
    #Print and line feed
    def print(self, text):
        self.uart.write(text.encode(encoding='utf-8', errors='strict')) #send text to buffer
        self.uart.write(chr(10).encode(encoding='utf-8', errors='strict')) #LF

    #ESC ! n
    #Select print mode(s)
    def printMode(
        self,
        font         = 'A', # or B
        emphasized   = False,
        doubleHeight = False,
        doubleWidth  = False,
        underline    = False):

        #     b7 b6 b5 b4 b3 b2 b1 b0
        # n =  0  0  0  0  0  0  0  0
        n = 0

        if font != 'A': # so its B
            n |= 1 #b0

        if emphasized:
            n |= 1 << 3 #b3

        if doubleHeight:
            n |= 1 << 4 #b4

        if doubleWidth:
            n |= 1 << 5 #b5

        if underline:
            n |= 1 << 7 #b7

        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(33).encode(encoding='utf-8', errors='strict')) # !
        self.uart.write(chr(n).encode(encoding='utf-8', errors='strict'))  # n

    #ESC - n
    #Turn underline mode on/off
    def underline(self, n = 0): #0 = off, 1 = 1 dot width, 2 = 2 dots width
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(45).encode(encoding='utf-8', errors='strict')) # -
        self.uart.write(chr(n).encode(encoding='utf-8', errors='strict'))  # n

    #ESC @
    #Initialize printer
    def initialize(self):
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(64).encode(encoding='utf-8', errors='strict')) # @

    #ESC E n
    #Turn emphasized mode on/off
    def emphasized(self, toggle = False):
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(69).encode(encoding='utf-8', errors='strict')) #E
        self.uart.write(chr(toggle).encode(encoding='utf-8', errors='strict')) #n
    
    #ESC G n
    #Turn double-strike mode on/off
    def doubleStrike(self, toggle = False):
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(71).encode(encoding='utf-8', errors='strict')) #G
        self.uart.write(chr(toggle).encode(encoding='utf-8', errors='strict')) #n    
    
    #ESC M n
    #Select character font
    def font(self, font = 1): #1,2 or 3 (some printer dont have 3)
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(77).encode(encoding='utf-8', errors='strict')) #M
        self.uart.write(chr(n).encode(encoding='utf-8', errors='strict')) #n  

    #ESC a n
    #Select justification
    def justification(self, mode = 'left'): #left , center, right
        if mode == 'left':
            n = 0 #left
        elif mode == 'center':
            n = 1 #center
        else:
            n = 2 #right
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(97).encode(encoding='utf-8', errors='strict')) #a
        self.uart.write(chr(n).encode(encoding='utf-8', errors='strict')) #n         

    #ESC d n
    #Print and feed n lines
    def printNfeed(self, text, line = 1):
        if line > 255:
            line = 255
        elif line < 1:
            line = 1

        self.uart.write(text.encode(encoding='utf-8', errors='strict')) #send text to buffer
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(100).encode(encoding='utf-8', errors='strict')) #d
        self.uart.write(chr(line).encode(encoding='utf-8', errors='strict')) #n   
    
    #ESC e n
    #Print and reverse feed n lines
    def printNreverse(self, text, line = 1):
        if line > 255:
            line = 255
        elif line < 1:
            line = 1
        
        self.uart.write(text.encode(encoding='utf-8', errors='strict')) #send text to buffer
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(101).encode(encoding='utf-8', errors='strict')) #e
        self.uart.write(chr(line).encode(encoding='utf-8', errors='strict')) #n           

    #ESC t n
    #Select character code table
    def characterCode(self, code = 0):
        #code : 0 PC437 (USA: Standard Europe)
        #code : 1 Katakana
        #code : 2 PC850 (Multilingual)
        #code : 3 PC860 (Portuguese)
        #code : 4 PC863 (Canadian-French)
        #code : 5 PC865 (Nordic)
        #code : 16 WPC1252
        #code : 17 PC866 (Cyrillic #2)
        #code : 18 PC852 (Latin 2)
        #code : 19 PC858 (Euro)
        self.uart.write(chr(27).encode(encoding='utf-8', errors='strict')) #ESC
        self.uart.write(chr(101).encode(encoding='utf-8', errors='strict')) #t
        self.uart.write(chr(code).encode(encoding='utf-8', errors='strict')) #code

    #GS B n
    #Turn white/black reverse printing mode on/off
    def reverseColor(self, toggle = False): #0 off, 1 on
        self.uart.write(chr(29).encode(encoding='utf-8', errors='strict')) #GS
        self.uart.write(chr(66).encode(encoding='utf-8', errors='strict')) #B
        self.uart.write(chr(toggle).encode(encoding='utf-8', errors='strict')) #n

    #GS h n
    #Select bar code height
    def barCodeHeight(self, height = 162):
        self.uart.write(chr(29).encode(encoding='utf-8', errors='strict')) #GS
        self.uart.write(chr(104).encode(encoding='utf-8', errors='strict')) #h
        self.uart.write(chr(height).encode(encoding='utf-8', errors='strict')) #n  

    #GS k m d1...dk NUL      
"""
imprimante = UartThermalPrinter(uart)

imprimante.initialize()
imprimante.printNfeed("Liste de course",1)
imprimante.printNfeed("-----------------",3)
imprimante.printNfeed("- Riz",1)
imprimante.printNfeed("- Serviette",1)
imprimante.printNfeed("- Tomate",1)
imprimante.printNfeed("- sac poubelle",1)
imprimante.printNfeed("- liquide vaisselle",1)
imprimante.printNfeed("- CocaCola",1)
imprimante.printNfeed("- Oeufs",1)
imprimante.printNfeed("- Poivron",1)
imprimante.printNfeed("- Yaourt",1)
imprimante.printNfeed("- Beurre",1)
imprimante.printNfeed("- Pizza",1)