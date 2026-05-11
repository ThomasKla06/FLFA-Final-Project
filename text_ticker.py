
import golly as g
import time as t

TEXT            = " HELLO"   # word to loop 
ROW_SPACING     = 20        # vertical cells between pixel rows 
COL_SPACING     = 20        # horizontal cells between pixel columns of a letter

CHAR_GAP_CELLS  = 40        # extra cells of clearance between letters
SPAWN_X         = 0         # x grid column where new letters are injected
ORIGIN_Y        = 0         # y grid row of the top pixel row


FONT = {
    'A': ["01110",
          "10001",
          "10001",
          "11111",
          "10001",
          "10001",
          "10001"],

    'B': ["11110",
          "10001",
          "10001",
          "11110",
          "10001",
          "10001",
          "11110"],

    'C': ["01111",
          "10000",
          "10000",
          "10000",
          "10000",
          "10000",
          "01111"],

    'D': ["11110",
          "10001",
          "10001",
          "10001",
          "10001",
          "10001",
          "11110"],

    'E': ["11111",
          "10000",
          "10000",
          "11110",
          "10000",
          "10000",
          "11111"],

    'F': ["11111",
          "10000",
          "10000",
          "11110",
          "10000",
          "10000",
          "10000"],

    'G': ["01111",
          "10000",
          "10000",
          "10111",
          "10001",
          "10001",
          "01111"],

    'H': ["10001",
          "10001",
          "10001",
          "11111",
          "10001",
          "10001",
          "10001"],

    'I': ["11111",
          "00100",
          "00100",
          "00100",
          "00100",
          "00100",
          "11111"],

    'J': ["11111",
          "00010",
          "00010",
          "00010",
          "00010",
          "10010",
          "01100"],

    'K': ["10001",
          "10010",
          "10100",
          "11000",
          "10100",
          "10010",
          "10001"],

    'L': ["10000",
          "10000",
          "10000",
          "10000",
          "10000",
          "10000",
          "11111"],

    'M': ["10001",
          "11011",
          "10101",
          "10001",
          "10001",
          "10001",
          "10001"],

    'N': ["10001",
          "11001",
          "10101",
          "10011",
          "10001",
          "10001",
          "10001"],

    'O': ["01110",
          "10001",
          "10001",
          "10001",
          "10001",
          "10001",
          "01110"],

    'P': ["11110",
          "10001",
          "10001",
          "11110",
          "10000",
          "10000",
          "10000"],

    'Q': ["01110",
          "10001",
          "10001",
          "10001",
          "10101",
          "10010",
          "01101"],

    'R': ["11110",
          "10001",
          "10001",
          "11110",
          "10100",
          "10010",
          "10001"],

    'S': ["01111",
          "10000",
          "10000",
          "01110",
          "00001",
          "00001",
          "11110"],

    'T': ["11111",
          "00100",
          "00100",
          "00100",
          "00100",
          "00100",
          "00100"],

    'U': ["10001",
          "10001",
          "10001",
          "10001",
          "10001",
          "10001",
          "01110"],

    'V': ["10001",
          "10001",
          "10001",
          "10001",
          "10001",
          "01010",
          "00100"],

    'W': ["10001",
          "10001",
          "10001",
          "10001",
          "10101",
          "11011",
          "10001"],

    'X': ["10001",
          "01010",
          "00100",
          "00100",
          "00100",
          "01010",
          "10001"],

    'Y': ["10001",
          "10001",
          "01010",
          "00100",
          "00100",
          "00100",
          "00100"],

    'Z': ["11111",
          "00001",
          "00010",
          "00100",
          "01000",
          "10000",
          "11111"],

    ' ': ["00000",
          "00000",
          "00000",
          "00000",
          "00000",
          "00000",
          "00000"],
}



LWSS_CELLS = [
   
    (1, 0), (4, 0),          # row 0
    (0, 1),                   # row 1
    (0, 2), (5, 2),           # row 2
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),  # row 3
]
LWSS_CELLS_FLIP = [
    
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (5, 1), 
    (0, 2), 
    (1, 3), (4, 3),        
]

def place_lwss(lx, ly):
    """Place a westward LWSS with bounding-box top-left at (lx, ly)."""
    for dx, dy in LWSS_CELLS:
        g.setcell(lx + dx, ly + dy, 1)

def place_lwss_flip(lx, ly):
    """Place a westward LWSS with bounding-box top-left at (lx, ly)."""
    for dx, dy in LWSS_CELLS_FLIP:
        g.setcell(lx + dx, ly + dy, 1)

def spawn_letter(ch):

    glyph = FONT.get(ch.upper(), FONT[' '])
    for col in range(5):
        gx = SPAWN_X - col * COL_SPACING
        for row in range(7):
            if glyph[row][5-1-col] == '1':
                gy = ORIGIN_Y + row * ROW_SPACING
                if col % 2 == 0:
                  place_lwss(gx, gy)
                else:
                    place_lwss_flip(gx, gy)



def main():
    g.new("HELLO Ticker (looping)")
    g.setrule("B3/S23")
    g.autoupdate(True)      


    LETTER_WIDTH_CELLS = 4 * COL_SPACING + CHAR_GAP_CELLS
    GENS_PER_LETTER    = LETTER_WIDTH_CELLS * 2   # cells * 2 gens/cell

    STEP = 4  

    letter_index = 0

    g.show("Spawning '%s' on loop -- close the script window to stop." % TEXT)

    while True:
        gen = g.getgen()
        if int(gen) % 240 == 0:
            ch = TEXT[letter_index % len(TEXT)]
            spawn_letter(ch)
            g.fit()

            
            gens_run = 0
            while gens_run < GENS_PER_LETTER:
                  g.run(STEP)
                  gens_run += STEP
                  g.show(
                  "Letter %d/%d ('%s') -- generation %d -- running..."
                  % (letter_index % len(TEXT) + 1, len(TEXT), ch, gens_run)
                  )

            letter_index += 1
       

main()