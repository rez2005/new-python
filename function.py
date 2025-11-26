def display_message():
	print('I am coming.')
display_message()
def favorite_book(title):
	print(f"I like {title}")
favorite_book('a')
def make_shirt(size,color='yellow'):
	print(f"The shirt is {size},its color is {color}.")
	if color == 'yellow':
		print('I love it.')
make_shirt('large','red')
make_shirt(color='blue',size='medium')
make_shirt('little')
def describe_city(city='Shanghai',country='China'):
	print(f"{city} is in {country}.")
describe_city()
describe_city('Beijing')
describe_city(country='America')
def make_albums(artist,title,number=None):
	album={'artist':artist,'title':title}
	if number:
		album['number']=number
	return album
album1=make_albums('a','sad')
album2=make_albums('b','happy','9')
print(album1),print(album2)
while True:
	print("(enter 'q' at any time to quit)")
	artist=input("artist:")
	if artist=='q':
		break
	title=input("title:")
	if title=='q':
		break
	album3=make_albums(artist,title)
	print(album3)
messages=['a','b','c']
sent_messages=[]
def show_messages(messages,sent_messages):
	while messages:
		message=messages.pop()
		print(message)
		sent_messages.append(message)
	print(sent_messages)

show_messages(messages[:],sent_messages)
print(messages)
