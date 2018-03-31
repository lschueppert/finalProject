import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://empirenews.net/", memoize_articles=False)
for article in paper.articles:
	file.write("http://empirenews.net/ " + article.url + "\n")