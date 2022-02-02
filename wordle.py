import random
import sys
import nltk
nltk.download('words')

from nltk.corpus import words

common_words = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis", "Beach", "Birth", "Block", "Blood", "Board", "Brain", "Bread", "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest", "Chief", "Child", "China", "Claim", "Class", "Clock", "Coach", "Coast", "Court", "Cover", "Cream", "Crime", "Cross", "Crowd", "Crown", "Cycle", "Dance", "Death", "Depth", "Doubt", "Draft", "Drama", "Dream", "Dress", "Drink", "Drive", "Earth", "Enemy", "Entry", "Error", "Event", "Faith", "Fault", "Field", "Fight", "Final", "Floor", "Focus", "Force", "Frame", "Frank", "Front", "Fruit", "Glass", "Grant", "Grass", "Green", "Group", "Guide", "Heart", "Henry", "Horse", "Hotel", "House", "Image", "Index", "Input", "Issue", "Japan", "Jones", "Judge", "Knife", "Laura", "Layer", "Level", "Lewis", "Light", "Limit", "Lunch", "Major", "March", "Match", "Metal", "Model", "Money", "Month", "Motor", "Mouth", "Music", "Night", "Noise", "North", "Novel", "Nurse", "Offer", "Order", "Other", "Owner", "Panel", "Paper", "Party", "Peace", "Peter", "Phase", "Phone", "Piece", "Pilot", "Pitch", "Place", "Plane", "Plant", "Plate", "Point", "Pound", "Power", "Press", "Price", "Pride", "Prize", "Proof", "Queen", "Radio", "Range", "Ratio", "Reply", "Right", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Scope", "Score", "Sense", "Shape", "Share", "Sheep", "Sheet", "Shift", "Shirt", "Shock", "Sight", "Simon", "Skill", "Sleep", "Smile", "Smith", "Smoke", "Sound", "South", "Space", "Speed", "Spite", "Sport", "Squad", "Staff", "Stage", "Start", "State", "Steam", "Steel", "Stock", "Stone", "Store", "Study", "Stuff", "Style", "Sugar", "Table", "Taste", "Terry", "Theme", "Thing", "Title", "Total", "Touch", "Tower", "Track", "Trade", "Train", "Trend", "Trial", "Trust", "Truth", "Uncle", "Union", "Unity", "Value", "Video", "Visit", "Voice", "Waste", "Watch", "Water", "While", "White", "Whole", "Woman", "World", "Youth"]

TOTAL_HINTS_ALLOWED = 6

def pick_word_of_day():
	return common_words[random.randrange(0, len(common_words))]

def evaluate(guess, word_of_day):
	if len(guess) != len(word_of_day):
		raise ValueError("needs to be "+ str(len(word_of_day)) +" letters!")
	elif guess not in words.words():
		raise ValueError(guess + " not a valid word!")
	else:
		hint = ''
		letters_matched = 0
		for idx, guess_char in enumerate(guess):
			if word_of_day[idx] == guess_char:
				hint += '🟩'
				letters_matched += 1
			elif guess_char in word_of_day:
				hint += '🟨'
			else:
				hint += '⬛'
		return hint, letters_matched

def guess_count(hints_remaining):
	return str(TOTAL_HINTS_ALLOWED - hints_remaining) + "/" + str(TOTAL_HINTS_ALLOWED)

def wordle():
	hints_remaining = TOTAL_HINTS_ALLOWED
	total_guess = ''
	word_of_day = pick_word_of_day().lower()
	print("Start typing guesses. Length of guess: " + str(len(word_of_day)))
	while hints_remaining > 0:
		next_guess = input('')
		try:
			next_hint, letters_matched = evaluate(next_guess.strip().lower(), word_of_day)
		except ValueError as e:
			print(e)
			continue
		hints_remaining -= 1
		total_guess += '\n' + next_hint
		if letters_matched == len(word_of_day):
			print("Found!! " + word_of_day.upper())
			print(guess_count(hints_remaining))
			print(total_guess)
			sys.exit(0)
		else:
			print(guess_count(hints_remaining) + ": " + next_hint)

	print("Out of guesses! Word of the day was: " + word_of_day)

wordle()
