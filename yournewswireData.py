import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://yournewswire.com/", memoize_articles=False)
for article in paper.articles:	
	file.write("http://yournewswire.com/ " + article.url + "\n")