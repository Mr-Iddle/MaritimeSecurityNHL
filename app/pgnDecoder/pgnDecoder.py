"""
    PGN Decoder
    Made by Arian Atapour for the AIS/Honeypot project
    NHL Stenden 
"""

# Full PGN message
pgn = input("Enter PGN message: ")

# Splitting the message
# 01:36:27.998 R 11FB1000 00 3E 78 6C 21 50 25 21
pgnSplit = pgn.split(" ")
# print(pgnSplit)

# Checking if received by device
pgnR = None

if pgnSplit[1] == "R":
    pgnR = "Received"
else:
    pgnR = "Not received"


#Decoding PGN from hex to decimal
""" 
h = input('Enter PGN :')
d = int(h, base=16)
print('Decimal :', d)
"""

# Final message
print("--------------DECODED PGN MESSAGE--------------" + "\n" + "Timestamp: " + pgnSplit[
    0] + "\n" + "Status: " + pgnR + "\n" + "--------------END OF DECODED PGN MESSAGE--------------")
