#!/usr/bin/python
import random, time
timestorun = 10
string = ""
stringlength = 0

thing = ["Coffee","Doctor Who","Football","Sports","Baseball","Cigar","Tabletop Gaming",
"Settlers of Catan","Video Games","Video Poker","Blackjack","Gambling","True Detective",
"Breaking Bad","Mens Rights","Pizza","Caffeine","Craft Beer","Eczema","Anti-Vaccine",
"Conservative","Constitution","Bible","Christ","Gun Rights","Pro-Life","Bodybuilding",
"Oxycodone","Xanax","Wine","Whiskey","Liquor","Anime","Miyazaki","Bukowski","Hitler",
"Hunting","White Nationalist","Bugchaser","Weird Twitter","Marijuana","Dog","Cat",
"JRPGs","Arson","Libertarian","Dawkins","Married","Steampunk","Veteran","Egalitarian",
"Politics"]

modifier = ["Fan","CEO","Guy","Dad","Liker","Enjoyer","Appreciator","Fanatic","Lover",
"Guru","Fetishist","Obsessive","Blogger","Writer","Parent","Man","Dude","Junkie",
"Addict","Snob","Aficionado","Nerd","Geek"]

disclaimers = ["I am very random","RTs are not endorsements","Opinions are my own",
"Opinions do not reflect those of my employer"]

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
		if random.randint(0,10) > 5:
			print "#" + thing[random.randint(0,len(thing))-1],
		if random.randint(0,10) > 5:
			print "#" + thing[random.randint(0,len(thing))-1],
		exit()
		
	timestorun = timestorun - 1
