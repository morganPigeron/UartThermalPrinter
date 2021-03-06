
class UartThermalPrinter:

    def __init__(self, uart):
        self.uart = uart #share uart object

    #***Control Commands***

    #LF 
    #Print and line feed
    def print(self, text):
        self.uart.write(text) #send text to buffer
        self.uart.write(chr(10)) #LF

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

        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(33)) # !
        self.uart.write(chr(n))  # n

    #ESC - n
    #Turn underline mode on/off
    def underline(self, n = 0): #0 = off, 1 = 1 dot width, 2 = 2 dots width
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(45)) # -
        self.uart.write(chr(n))  # n

    #ESC @
    #Initialize printer
    def initialize(self):
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(64)) # @

    #ESC E n
    #Turn emphasized mode on/off
    def emphasized(self, toggle = False):
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(69)) #E
        self.uart.write(chr(toggle)) #n
    
    #ESC G n
    #Turn double-strike mode on/off
    def doubleStrike(self, toggle = False):
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(71)) #G
        self.uart.write(chr(toggle)) #n    
    
    #ESC M n
    #Select character font
    def font(self, font = 1): #1,2 or 3 (some printer dont have 3)
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(77)) #M
        self.uart.write(chr(n)) #n  

    #ESC a n
    #Select justification
    def justification(self, mode = 'left'): #left , center, right
        if mode == 'left':
            n = 0 #left
        elif mode == 'center':
            n = 1 #center
        else:
            n = 2 #right
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(97)) #a
        self.uart.write(chr(n)) #n         

    #ESC d n
    #Print and feed n lines
    def printNfeed(self, text, line = 1):
        if line > 255:
            line = 255
        elif line < 1:
            line = 1

        self.uart.write(text) #send text to buffer
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(100)) #d
        self.uart.write(chr(line)) #n   
    
    #ESC e n
    #Print and reverse feed n lines
    def printNreverse(self, text, line = 1):
        if line > 255:
            line = 255
        elif line < 1:
            line = 1
        
        self.uart.write(text) #send text to buffer
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(101)) #e
        self.uart.write(chr(line)) #n           

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
        self.uart.write(chr(27)) #ESC
        self.uart.write(chr(101)) #t
        self.uart.write(chr(code)) #code

    #GS B n
    #Turn white/black reverse printing mode on/off
    def reverseColor(self, toggle = False): #0 off, 1 on
        self.uart.write(chr(29)) #GS
        self.uart.write(chr(66)) #B
        self.uart.write(chr(toggle)) #n

    #GS h n
    #Select bar code height
    def barCodeHeight(self, height = 162):
        self.uart.write(chr(29)) #GS
        self.uart.write(chr(104)) #h
        self.uart.write(chr(height)) #n  

    #GS k m d1...dk NUL      