guests=['a','b','c']
guests[0]='d'
message0=f"Could you do me a favor to come to my party,{guests[0]},{guests[1]} and {guests[2]}."
message1="Sorry,I suddenly got a news that a coundn't make it to our party"
print(message1)
print(message0)
print("Now,three more people will be invited.")
guests.insert(0,"e")
guests.insert(2,"f")
guests.append("g")
print(f"Could you do me a favor to come to my party,{guests[0]},{guests[1]},{guests[2]},{guests[3]},{guests[4]} and {guests[5]}")
print("Unfortunately,only two people can be invited.")
qwq=guests.pop(0)
print(f"Sorry,{qwq},you aren't invited!")
qwq=guests.pop(0)
print(f"Sorry,{qwq},you aren't invited!")
qwq=guests.pop(0)
print(f"Sorry,{qwq},you aren't invited!")
qwq=guests.pop(0)
print(f"Sorry,{qwq},you aren't invited!")
print(f"Congratulations,{guests[0]},{guests[1]},you are invited.")
print(len(guests))
del guests[0]
del guests[0]
print(guests)