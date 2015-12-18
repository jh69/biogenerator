#!/usr/bin/python
import random, time
timestorun = 20
string = ""
stringlength = 0

thing = ["Coffee","Doctor Who","Football","Sports","Baseball","Cigar",
"Tabletop Gaming", "Settlers of Catan","Video Games","Video Poker",
"Blackjack","Gambling","True Detective","Breaking Bad",
"Mens Rights","Pizza","Caffeine","Craft Beer","Eczema","Anti-Vaccine",
"Conservative","Constitution","Bible","Christ","Gun Rights","Pro-Life",
"Bodybuilding","Oxycodone","Xanax","Wine","Whiskey","Liquor","Anime",
"Miyazaki","Bukowski","Hitler","Hunting","White Nationalist","Bugchaser",
"Weird Twitter","Marijuana","Dog","Cat","JRPG","Arson","Libertarian","Dawkins",
"Poly","Steampunk","Veteran","Egalitarian","Politics","SJW","Gamergate",
"Star Wars","Bernie Sanders","Hillary Clinton","Donald Trump","Craft Whiskey",
"Brunch","NASCAR","America","Ferret","Rat","Open Source","Ruby","Netflix",
"Gout","Chagas","Horse","Comedy","Favstar","420","2A","Open Carry","Marketing",
"Social Media","LinkedIn","Networking","Travel"]

modifier = ["Fan","CEO","Guy","Dad","Liker","Enjoyer","Appreciator","Fanatic","Lover",
"Guru","Fetishist","Obsessive","Blogger","Writer","Parent","Man","Dude",
"Junkie","Addict","Snob","Aficionado","Nerd","Geek","Freak","Enthusiast","Admirer","Fiend","Hound","Expert","Critic","Nut","Maven","Savant","Zealot",
"Follower","Influencer","Evangelist"]

disclaimers = ["I am very random","RTs are not endorsements",
"Opinions are my own","Opinions do not reflect those of my employer",
"Just here to talk " + thing[random.randint(0,len(thing))-1],
"Business inquiries? DM me."]

while timestorun > 0:
	if random.randint(0,10) > 7:
		string = thing[random.randint(0,len(thing))-1] + " " + modifier[random.randint(0,len(modifier))-1] + "."
		print string,
	else:
		string = thing[random.randint(0,len(thing))-1] + "."
		print string,
	stringlength = stringlength + len(string)
	if stringlength > 70:
		if random.randint(0,10) > 8:
			string = disclaimers[random.randint(0,len(disclaimers))-1] + "."
			print string,
	if stringlength > 100:
		print "#" + thing[random.randint(0,len(thing))-1],
		exit()
		
	timestorun = timestorun - 1
