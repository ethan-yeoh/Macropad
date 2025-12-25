import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()



keyboard.col_pins = (board.D0, board.D1, board.D2) # COL0, COL1, COL2
keyboard.row_pins = (board.D3, board.D6)           # ROW0, ROW1
keyboard.diode_orientation = DiodeOrientation.COL2ROW


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D8, board.D7, None, False), # Encoder 1
    (board.D10, board.D9, None, False),# Encoder 2
)


layers = Layers()
keyboard.modules.append(layers)

UNDO = KC.LCTRL(KC.Z)
REDO = KC.LCTRL(KC.Y)

keyboard.keymap = [
    [
        [KC.ESC,    KC.L,    KC.D,
         KC.E,      KC.S,    KC.ENTER]
    ]
]

encoder_handler.map = [
    [
       
        (KC.MW_UP, KC.MW_DOWN),  
        
        (UNDO, REDO),            
    ]
]

if __name__ == '__main__':
    keyboard.go()
