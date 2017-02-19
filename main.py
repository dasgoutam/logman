import pyxhook.pyxhook as pyxhook
import time

class Stroke:
	def __init__(self, key, mname, time):
		self.key = key
		self.mname = mname
		self.time = time
	
	
# This function is called every time a key is presssed
def kbevent(event):
    global running
    global UpArray, DownArray
    # print key info
    tm = repr(time.time())

    keyEvent = Stroke(event.Key, event.MessageName, tm)
    if keyEvent.mname == "key down":
    	UpArray.append(keyEvent)
    else:
    	DownArray.append(keyEvent)

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 13:
    	if keyEvent.mname == "key up":   		
	        running = False

def printList(array):
	for stroke in array:
		print stroke.key, stroke.mname, stroke.time, "#"
	print "##"

UpArray = []
DownArray = []
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
# file = open('output.txt', 'w')
# Create a loop to keep the application running
running = True
while running:
     time.sleep(0.00001)

# Close the listener when we are done
hookman.cancel()


print "Key Down:\n"
# print printList(UpArray)
for stroke in DownArray:
	print stroke.key, stroke.mname, stroke.time, "#"
print "###"
# print "counter:", counter
print len(UpArray)
print "Key Up:\n"
print printList(DownArray)
print len(DownArray)
# file.close()