#!/usr/bin/python

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

	def writeFirstCSV(self):
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


# This function is called at each iteration to check if the password entered is correct
def checkPass(array):
	global authPass
	typedPass = ""
	for i in range(len(array)):
		typedPass += array[i].key

	if authPass == typedPass:
		return True
	else:
		return False
		
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

def passevent(event):
	global running, authPass
	authPass += event.Key
	if event.Ascii == 13:
		running = False

def printList(array):
	for stroke in array:
		print(stroke.key, stroke.mname, stroke.time, "#")


print("Enter the password you want to log: ")
authPass = ""
hookman = pyxhook.HookManager()
hookman.KeyDown = passevent
hookman.HookKeyboard()
hookman.start()
running = True
while running:
	time.sleep(0.00001)
hookman.cancel()

# iterations = raw_input("Enter the number of times you want to type the password: ")
iterations = 5
print("Nice! You may begin\n")

i = 1
while i <= iterations:
	print("\nAttempt " + str(i) + ":")
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


	if checkPass(UpArray):
		writer = StrokesLine(UpArray, DownArray)
		if i == 1:
			writer.writeFirstLine()
			writer.writeFirstCSV()
		writer.writeLine()
		writer.writeCSV()
		i += 1
	else:
		print("Sorry. Password does not match. Please try again")
