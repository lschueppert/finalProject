f = open("articleText.txt", "r")
lines = f.readlines()
f.close()

while true:
	f = open("articleText.txt", "w")
	lineNum = input("Line : ")
	lineNum--
	counter = 0
	for line in lines:
		if counter == lineNum:
			text = input("Text: ").strip()
			f.write(text)
			f.close()
