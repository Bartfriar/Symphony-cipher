#!/bin/python
from flask import Flask, render_template, request

import re
# This dictionary maps the alphanumeric characters to different musical notes playing on different pitch frequncies
note_mapping = {
	'C3' : '0',
	'C#3' : '1',
	'D3' : '2',
	'D#3' : '3',
	'E3' : '4',
	'E#3' : '5',
	'F3' : '6',
	'F#3' : '7',
	'G3' : '8',
	'G#3' : '9',
	'A3' : 'A',
	'A#3' : 'B',
	'B3' : 'C',
	'C4' : 'D',
	'C#4' : 'E',
	'D4' : 'F',
	'D#4' : 'G',
	'E4' : 'H',
	'E#4' : 'I',
	'F4' : 'J',
	'F#4' : 'K',
	'G4' : 'L',
	'G#4' : 'M',
	'A4' : 'N',
	'A#4' : 'O',
	'B4' : 'P',
	'C5' : 'Q',
	'C#5' : 'R',
	'D5' : 'S',
	'D#5' : 'T',
	'E5' : 'U',
	'E#5' : 'V',
	'F5' : 'W',
	'F#5' : 'X',
	'G5' : 'Y',
	'G#5' : 'Z',
	'M2' : ' ',
}

message_mapping = {
	'0': 'C3',
	'1': 'C#3',
	'2': 'D3',
	'3': 'D#3',
	'4': 'E3',
	'5': 'E#3',
	'6': 'F3',
	'7': 'F#3',
	'8': 'G3',
	'9': 'G#3',
	'A': 'A3',
	'B': 'A#3',
	'C': 'B3',
	'D': 'C4',
	'E': 'C#4',
	'F': 'D4',
	'G': 'D#4',
	'H': 'E4',
	'I': 'E#4',
	'J': 'F4',
	'K': 'F#4',
	'L': 'G4',
	'M': 'G#4',
	'N': 'A4',
	'O': 'A#4',
	'P': 'B4',
	'Q': 'C5',
	'R': 'C#5',
	'S': 'D5',
	'T': 'D#5',
	'U': 'E5',
	'V': 'E#5',
	'W': 'F5',
	'X': 'F#5',
	'Y': 'G5',
	'Z': 'G#5',
	' ': 'M2',
}



# Encipher functions


# Function to get the note for a given alphanumeric character.
def get_note(char):
    return message_mapping.get(char.upper(), '')

#Function to convert user text to a musical note

def text_to_notes(text):
	notes = []
	for char in text:
		note = get_note(char)
		if note:
			notes.append(note)
		else:
			notes.append()
	return notes


#Decipher Functions


# Function to seprate the sequence in the cipher
def separate_cipher(cipher):
	separated_array = re.findall(r'[a-zA-Z#]+(?:\d+)?', cipher)
	return separated_array

# Function to Convert the cipher into plaintext


def cipher_to_text(secret):
	sentence = []
	for sec in secret:
		sec = sec.upper()
		if sec in note_mapping:
			sentence.append(note_mapping[sec])
		else:
			sentence.append(sec)
	return sentence


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

  
@app.route('/section2',  methods=['POST'])
def section2():
	if request.method == 'POST':
		message_input = request.form['message']
		notes = text_to_notes(message_input)
		notes_output = (" - ".join([" ".join(notes[i:i+4]) for i in range(0, len(notes), 4)]))
		return notes_output


@app.route('/section3',  methods=['POST'])
def section3():
	if request.method == 'POST':
		notes_input = request.form['notes']
		result_array = separate_cipher(notes_input)
		plaintext_output = cipher_to_text(result_array)
		plaintext = ("".join(plaintext_output))
		return plaintext
		#print("".join(plaintext_output))

# def main():
# 	sequence = input("Enter cipher: ")
# 	result_array = separate_cipher(sequence)
# 	checked_array = cipher_to_text(result_array)
# 	print("".join(checked_array))


if __name__ == "__main__":
	app.run(debug=True)



#def separate(trial):
#    res = separate_cipher(trial)
#    mess = cipher_to_text(res)
#    return mess

#user_input = input("Enter cipher: ")

#message = separate(user_input)

#print(message)


# Function to convert notes into plaintext
# def notes_to_text(notes):
# 	notes = notes.lower().strip()

# 	plaintext = ""

# 	i = 0
# 	while i < len(notes):
# 		if notes[i].isalpha() or notes[i] == '#':
# 			note = notes[i]

# 			i += 1
# 			while i < len(notes) and notes[i].isdigit():

# 				note += notes[i]
# 				i += 1
# 			plaintext += note_mapping.get(note.upper(), '')

# 		i += 1

# 	return plaintext


#notes_input = input("enter notes: ")
#output = notes_to_text(notes_input)
#print("Your message: ", output)