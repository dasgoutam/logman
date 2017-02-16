import pyxhook.pyxhook as pyxhook
import time


# This function is called every time a key is presssed
def kbevent(event):
    global running
    # print key info
    tm = repr(time.time())
    info = event.Key + "\t" + event.MessageName + "\t" + repr(time.time()) + "\n"
    file.write(info)

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 13:
        running = False


# def kb1event(event):
# 	global running
# 	info = event.Key + "(up):" + str(time.time()) + " "
# 	file.write(info)

# Create hookmanager
hookman = pyxhook.HookManager()
# print time.time()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
hookman.KeyUp = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()
file = open('output.txt', 'w')
# Create a loop to keep the application running
running = True
while running:
     time.sleep(0.00001)

# Close the listener when we are done
hookman.cancel()
file.close()