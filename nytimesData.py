import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://www.nytimes.com/", memoize_articles=False)
for article in paper.articles:	
	file.write("http://www.nytimes.com/ " + article.url + "\n")