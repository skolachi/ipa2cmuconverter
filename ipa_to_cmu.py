

# define the phone mapping in ipa2cmu.map and read this into a dictionary 
ipa2cmu = dict([tuple(f.strip().split('\t')) for f in open('ipa2cmu.map')]) 

print(ipa2cmu)

def convert(text):
	cmu = []
	for i in range(len(text)):
		if i < len(text) - 1:
			if text[i:i+2] in ipa2cmu.keys():
				cmu.append(ipa2cmu[text[i:i+2]])
			else:
				cmu.append(ipa2cmu[text[i]])
		else:
			cmu.append(ipa2cmu[text[i]])

	return cmu

print(convert('kiwi'))
