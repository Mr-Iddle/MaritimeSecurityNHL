"""
    PGN Decoder
    Made by Arian Atapour for the AIS/Honeypot project
    NHL Stenden 
"""

"""
    Changelog:
        v0.1: Decoding timestam, received status, PGN number and device sent from
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
pgnHSplitH = pgnSplit[2][1:-2]
#print(pgnHSplit)
pgnDConv = int(pgnHSplitH, base=16)
#print(pgnDConv);


# Final message
print("--------------DECODED PGN MESSAGE--------------" + "\n" + "Timestamp: " + pgnSplit[
    0] + "\n" + "Status: " + pgnR + "\n" + "PGN Number: " + str(pgnDConv) + "\n"
       + "COM sevice sent from: " + pgnSplit[3] + "\n" + "--------------END OF DECODED PGN MESSAGE--------------")
