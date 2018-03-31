f = open("articleDatabase.txt", "r")
lines = f.readlines()
f.close()

f = open("articleDatabase.txt", "w")
for line in lines:
	if line.find("crossword") == -1 and line.find("video") == -1 and line.find("slideshow") == -1:
		f.write(line)
f.close()
		
