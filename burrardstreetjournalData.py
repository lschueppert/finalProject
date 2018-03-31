import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://www.burrardstreetjournal.com/", memoize_articles=False)
for article in paper.articles:
	file.write("http://www.burrardstreetjournal.com/ " + article.url + "\n")