import newspaper

file = open("articleDatabase.txt", "a")
paper = newspaper.build("http://dcgazette.com", memoize_articles=False)
for article in paper.articles:
	if article.url != "https://dcgazette.com/2018/worlds-powerful-rocket-makes-history-successful-launch/":	
		file.write("http://dcgazette.com/ " + article.url + "\n")