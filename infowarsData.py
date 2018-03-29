import newspaper

file = open("articleDatabase.txt", "a")
articleList = []
paper = newspaper.build("http://www.infowars.com/", memoize_articles=False)
for article in paper.articles:
	if article.url != "http://infowars.com":	
		articleList.append(["http://www.infowars.com/", article.url])
		file.write("http://www.infowars.com/ " + article.url + "\n")
