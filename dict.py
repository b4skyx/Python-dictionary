import json
from difflib import SequenceMatcher as seqm
from difflib import get_close_matches as getmatch


data=json.load(open("dict_data.json"))
def translate(w):
	w=w.lower()
	if(w in data.keys()):
		return data[w][0]
	elif( len(getmatch(w,data.keys())) > 0 ):
		print("Did you mean one of these words?")
		t=getmatch(w,data.keys())

		for i in range(0,len(t)-1):
			print((i+1)," : ",t[i])
		while True:
			index=int(input("Enter the index number, Enter 0 if not shown:  "))
			if index==0:
				return "The searched word does not exists in the dictionary...\nWait for the next update <3"
			elif index >= len(t):
				print("Invalid Index. Please Try Again...")
			else:
				return data[t[index-1]][0]


searchword=str(input("Enter the word to be searched in the dictionary: "))
print(translate(searchword))