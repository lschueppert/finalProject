import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://www.redstate.com/", memoize_articles=False)
for article in paper.articles:	
	file.write("http://www.redstate.com/ " + article.url + "\n")