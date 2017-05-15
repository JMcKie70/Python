
import re
def get_matching_words(regex):
	 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", 
	 "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", 
	 "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", 
	 "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", 
	 "tabloid", "unbearable", "union", "videotape"]
	 matches = []
	 for word in words:
	 	if re.search(regex,word):
	 		matches.append(word)
	 return matches

# print get_matching_words("v") #all words that contain a "v"

# print get_matching_words("ss") #all words that contain a double-s

# print get_matching_words("e") #all words that end with an e

# print get_matching_words('b.b') #all words that contain a b, any character, then b

# print get_matching_words('b*.b') #a b, any number of characters, then b

# print get_matching_words(r"a*.e*.i*.o*.u") #all five vowels in order

# print get_matching_words("[regularexpression]") #letters in regular expression

# print get_matching_words(r'(.)\1') #contain double letter