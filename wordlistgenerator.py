#BMC tests
#kharbachat 00:00
fichier=open('wordlist.txt','w')
fichier=open('wordlist.txt','r')
fichier=open('wordlist.txt','w')
test=open('test.txt','r')
s=''
characters=test.readlines()
for ch1 in characters:
	for ch2 in characters:
		for ch3 in characters:
			for ch4 in characters:
				for ch5 in characters:
					for ch6 in characters:
						for ch7 in characters:
							for ch8 in characters:
								s= ch1 + ch2 + ch3 + ch4 + ch5 + ch6 + ch7 + ch8
								fichier.write(s)
								fichier.write('\n')
test.close()
fichier.close()	