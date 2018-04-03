from newspaper import Article
import newspaper
f = open("articleDatabase.txt", "r")
lines = f.readlines()
f.close()

f = open("articleText.txt", "w")
for line in lines:
	try:
		article = Article(line.split(' ')[1].strip())
		article.download()
		article.parse()
		f.write(article.text.replace("\n", " ") + "\n")
	except: 
		f.write("0\n")
f.close()
