import speech_recognition as sr
import random
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import serial

# Declare robot name (Wake-Up word)
robot_name = 'jarvis'

# random words list
hi_words = ['hi', 'hello', 'hy bhai']
bye_words = ['bye', 'tata']
r_u_there = ['are you there', 'you there']

# initilize things
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
listener = sr.Recognizer()

# connect with NiNi motor driver board over serial communication
try:
    port = serial.Serial("COM4", 9600)
    print("Phycial body, connected.")
except:
     print("Unable to connect to my physical body")


def listen():
	""" listen to what user says"""
	try:
		with sr.Microphone() as source:
			print("Talk>>")
			listener.pause_threshold = 1
			voice = listener.listen(source)
			command = listener.recognize_google(voice).lower()
			# all words lowercase- so that we can process easily
			command = command.lower()
			print(command)

			# look for wake up word in the beginning
			if (command.split(' ')[0] == robot_name):
				# if wake up word found....
				print("[wake-up word found]")
				process(command)
	except:
		pass

def process(words):
	""" process what user says and take actions """
	print(words) # check if it received any command

	# break words in
	word_list = words.split(' ')[1:]   # split by space and ignore the wake-up word

	if (len(word_list)==1):
		if (word_list[0] == robot_name):
			talk("How Can I help you?")
			return

	if word_list[0] == 'play':
		"""if command for playing things, play from youtube"""
		talk("Okay boss, playing")
		extension = ' '.join(word_list[1:])                    # search without the command word
		port.write(b'V')
		pywhatkit.playonyt(extension)
		port.write(b'v')
		return

	elif word_list[0] == 'search':
		"""if command for google search"""
		port.write(b'V')
		talk("Okay boss, searching")
		port.write(b'v')
		extension = ' '.join(word_list[1:])
		pywhatkit.search(extension)
		return

	if (word_list[0] == 'get') and (word_list[1] == 'info'):
		"""if command for getting info"""
		port.write(b'V')
		talk("Okay, I am right on it")
		port.write(b'v')
		extension = ' '.join(word_list[2:])                    # search without the command words
		inf = pywhatkit.info(extension)
		talk(inf)                                              # read from result
		return

	elif word_list[0] == 'open':
		"""if command for opening URLs"""
		port.write(b'V')
		talk("Opening, sir")
		url = f"http://{''.join(word_list[1:])}"   # make the URL
		webbrowser.open(url)
		return
	elif word_list[0] == 'handshake':
		port.write(b'v')

	elif word_list[0] == 'go forward':
		port.write(b'F')

	elif word_list[0] == 'go back':
		port.write(b'B')

	elif word_list[0] == 'turn left':
		port.write(b'L')

	elif word_list[0] == 'turn right':
		port.write(b'R')

	elif word_list[0] == 'dance':
		port.write(b'U')

	elif word_list[0] == 'stand':
		port.write(b'X')

	elif word_list[0] == 'sit':
		port.write(b'x')

	elif word_list[0] == 'hand wave':
		port.write(b'W')

    # now check for matches
	for word in word_list:
		if word in hi_words:
			""" if user says hi/hello greet him accordingly"""
			port.write(b'V')               # send command to wave hand
			talk(random.choice(hi_words))

		elif word in bye_words:
			""" if user says bye etc"""
			port.write(b'w')
			talk(random.choice(bye_words))


def talk(sentence):
	""" talk / respond to the user """
	engine.say(sentence)
	engine.runAndWait()

# run the app
while True:
    listen()  # runs listen one time