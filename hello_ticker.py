

import golly as g


TEXT         = "TUN A TSUB ANNIF"      # word to display has to be backwards to work
ROW_SPACING  = 20           # vertical cells between bitmap rows
COL_SPACING  = 20           # horizontal cells between bitmap columns
CHAR_GAP     = 40           # extra horizontal gap between characters
ORIGIN_X     = 0            # where to start placing ships (right edge)
ORIGIN_Y     = 0            # top of the bitmap


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

EATER = ["0011","0101","0100","1100"]

LWSS_CELLS = [
    
    (1, 0), (4, 0),          # row 0
    (0, 1),                   # row 1
    (0, 2), (5, 2),           # row 2
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),  # row 3
]


def place_lwss(lx, ly):
    """Place a westward LWSS with bounding-box top-left at (lx, ly)."""
    for dx, dy in LWSS_CELLS:
        g.setcell(lx + dx, ly + dy, 1)


def build_ship_positions(text):

    positions = []

    x_cursor = ORIGIN_X

    for char_index, ch in enumerate(text.upper()):
        glyph = FONT.get(ch, FONT[' '])
        num_cols = len(glyph[0])   # always 5

        # Columns: col 0 is leftmost in the glyph.
        # To display left-to-right, col 0 must arrive first ⟹ starts rightmost.
        # So col 0 gets x_cursor, col 1 gets x_cursor - COL_SPACING, etc.
        for col in range(num_cols):
            gx = x_cursor - col * COL_SPACING
            for row in range(7):
                if glyph[row][num_cols-col-1] == '1':
                    gy = ORIGIN_Y + row * ROW_SPACING
                    positions.append((gx, gy))

        # After all columns of this character, advance cursor for next char
        x_cursor -= (num_cols * COL_SPACING) + CHAR_GAP

    return positions

EAT = [
      (2,0), (3,0),
      (1,1), (3,1),
      (1,2),
      (0,3),(1,3)
]
def place_eat():
     
      eatpos = []      

      x_cursor = -((len(TEXT)*5 + ROW_SPACING)*5*5)+4
      y_cursor = 4
      for i in range(7):
            ey = y_cursor + i * ROW_SPACING
            eatpos.append((x_cursor, ey))
      
      for pos in eatpos:
           for dx, dy in EAT:
                g.setcell(pos[0] + dx, pos[1] + dy, 1)
           
     

# ── main ───────────────────────────────────────────────────────────────────────
def main():
      g.new("HELLO Ticker")
      g.setrule("B3/S23")

      g.show("Building HELLO ticker pattern ...")

      positions = build_ship_positions(TEXT)

      for (gx, gy) in positions:
            place_lwss(gx, gy)

      eaterPos = place_eat()
            
      g.fit()
      g.update()

      total_ships = len(positions)
      g.show(
            "Done! Placed %d LWSSs spelling '%s'.  "
            "Press Space or Run to watch them scroll left."
            % (total_ships, TEXT)
      )

main()