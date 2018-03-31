import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://www.exopolitics.org/", memoize_articles=False)
for article in paper.articles:
	if article.url != "https://exopolitics.org/media/archive/":	
		file.write("http://www.exopolitics.org/ " + article.url + "\n")