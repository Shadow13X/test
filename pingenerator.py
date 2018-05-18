#BMC tests
#kharbachat 00:00
fichier=open('pinlist.txt','w')
fichier=open('pinlist.txt','r')
fichier=open('pinlist.txt','w')
for i in range(10):
	for j in range(10):
		for k in range(10):
			for l in range(10):
				for m in range(10):
					for n in range(10):
						for o in range(10):
							for p in range(10):
								i=str(i)
								j=str(j)
								k=str(k)
								l=str(l)
								m=str(m)
								n=str(n)
								o=str(o)
								p=str(p)
								s= i + j + k + l + m + n + o + p
								fichier.write(s)
								fichier.write('\n')
								i=int(i)
								j=int(j)
								k=int(k)
								l=int(l)
								m=int(m)
								n=int(n)
								o=int(o)
								p=int(p)
fichier.close()	