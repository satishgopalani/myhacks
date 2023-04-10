#
# Author: Satish Gopalani 
# Date: March 27th, 2023
# Version: 1.0

import sys
import speech_recognition as sr
import math
import time
import openai
import os
from gtts import gTTS

#from playsound import playsound
#import pygame
#import serial
#from espeak import espeak

#model_to_use="text-davinci-003" # most capable
#model_to_use="text-curie-001"
#model_to_use="text-babbage-001"
model_to_use="text-ada-001" # lowest token cost

# Load your API key from an environment variable or secret management service
openai.api_key="### INSERT YOUR OPENAI API KEY ###"

def chatGPT(query):
	response = openai.Completion.create(
		model=model_to_use,
		prompt=query,
		temperature=0.3, # Controls how much random or specific you want response (higher to lower)
		max_tokens=1000 # max response size
		)
	return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']


# main program
def main():
	print("Ctrl+C for exit")
	r = sr.Recognizer()
	try:
		while True:
			with sr.Microphone() as source:
				try:
					r.adjust_for_ambient_noise(source)
					print("Say Something!")
					audio=r.listen(source,20,5)
					print("Recognizing now...")
					command=str(r.recognize_google(audio))
					print("Google speech Recognitiion thinks you said: " + command)
					query=command
					(res,usage) = chatGPT(query)
					print("Response: " + res)
					#os.system("espeak " + res)
		
					tts=gTTS(text=res, lang='en')
					tts.save("good.mp3")
					os.system("mpg123 -q good.mp3")

				except KeyboardInterrupt as kir :
					raise kir
				except :
					pass
	except KeyboardInterrupt:
		pass

if __name__ == '__main__':
	main()

