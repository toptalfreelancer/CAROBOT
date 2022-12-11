from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton

buttons = [
	'kids', 
	'started', 
	'beginner', 
	'elementary', 
	'pre-intermediate', 
	'interemdiate', 
	'upper-intermadiate',
	'advanced',
	'pre-ielts'
]

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

for i in buttons:
	button = KeyboardButton(i.capitalize())
	keyboard2.add(button)

startbutton = KeyboardButton('/start')
start = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(startbutton)

contact = KeyboardButton('Kontaktni ulashish',request_contact=True)
# location = KeyboardButton('Lokatsiyani ulashish',request_location=True)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

keyboard1.add(contact)