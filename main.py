from __future__ import print_function

import pyxhook.pyxhook as pyxhook
import time
import csv


class KeyStroke:
	def __init__(self, key, mname, time):
		self.key = key
		self.mname = mname
		self.time = time

	
class StrokesLine:
	def __init__(self, UpArray, DownArray):
		self.UpArray = UpArray
		self.DownArray = DownArray
		self.line = ""
	
	def writeFirstLine(self):
		space = "    "
		with open("output.txt", "w") as output:
			for i in range(len(self.UpArray) - 1):
				output.write("H." + self.UpArray[i].key + space)
				output.write("DD." + self.DownArray[i].key + "." + self.DownArray[i+1].key + space)
				output.write("UD." + self.UpArray[i].key + "." + self.DownArray[i+1].key + space)
			output.write("H." + self.UpArray[i+1].key + "\n")

	def writeLine(self):
		space = "    "
		with open("output.txt", "a") as output:
			for i in range(len(self.UpArray) - 1):
				holdTime = self.UpArray[i].time - self.DownArray[i].time
				downDownTime = float(self.DownArray[i+1].time) - float(self.DownArray[i].time)
				upDownTime = float(self.DownArray[i+1].time) - float(self.UpArray[i].time)

				output.write(str(holdTime) + space)
				output.write(str(downDownTime) + space)
				output.write(str(upDownTime) + space)
				
			holdTime = self.UpArray[i+1].time - self.DownArray[i+1].time
			output.write(str(holdTime) + "\n")

	def wirteFirstCSV(self):
		firstLine = []
		for i in range(len(self.UpArray) - 1):
			firstLine.append("H." + self.UpArray[i].key)
			firstLine.append("DD." + self.DownArray[i].key + "." + self.DownArray[i+1].key)
			firstLine.append("UD." + self.UpArray[i].key + "." + self.DownArray[i+1].key)
		firstLine.append("H." + self.UpArray[i+1].key)

		writer = csv.writer(open("output.csv", 'w'))
		writer.writerow(firstLine)

	def writeCSV(self):
		line = []
		for i in range(len(self.UpArray) - 1):
			holdTime = self.UpArray[i].time - self.DownArray[i].time
			downDownTime = float(self.DownArray[i+1].time) - float(self.DownArray[i].time)
			upDownTime = float(self.DownArray[i+1].time) - float(self.UpArray[i].time)
			line.append(str(holdTime))
			line.append(str(downDownTime))
			line.append(str(upDownTime))
		line.append(str(self.UpArray[i+1].time - self.DownArray[i+1].time))

		writer = csv.writer(open("output.csv", 'a'))
		writer.writerow(line)


	
# This function is called every time a key is presssed
def kbevent(event):
    global running
    global UpArray, DownArray
    # print key info
    # tm = repr(time.time())
    tm = time.time()

    keyEvent = KeyStroke(event.Key, event.MessageName, tm)
    if keyEvent.mname == "key down":
    	DownArray.append(keyEvent)
    else:
    	UpArray.append(keyEvent)

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 13:
    	if keyEvent.mname == "key up":   		
	        running = False

def printList(array):
	for stroke in array:
		print(stroke.key, stroke.mname, stroke.time, "#")
	# print "##"

UpArray = []
DownArray = []
# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
hookman.KeyUp = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()
# Create a loop to keep the application running
running = True
while running:
     time.sleep(0.00001)

# Close the listener when we are done
hookman.cancel()

a = StrokesLine(UpArray, DownArray)
a.writeFirstLine()
a.writeLine()
a.wirteFirstCSV()
a.writeCSV()


# print("Key Down:\n")
# # print printList(UpArray)
# for stroke in DownArray:
# 	print(stroke.key, stroke.mname, stroke.time, "#")
# # print "###"
# # print "counter:", counter
# print(len(UpArray))
# print("Key Up:\n")
# print(printList(UpArray))
# print(len(DownArray))
# # file.close()