def main():
	fp=open("exp.txt",'wb')
	for i in range(1000):
		fp.write(str(i))
main()