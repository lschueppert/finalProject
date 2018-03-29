import newspaper

file = open("articleDatabase.txt", "a")
articleList = []
paper = newspaper.build("http://cnn.com/", memoize_articles=False)
for article in paper.articles:
	articleList.append(["http://cnn.com/", article.url])
	file.write("http://cnn.com/ " + article.url + "\n")
