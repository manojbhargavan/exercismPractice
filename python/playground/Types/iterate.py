from urllib.request import urlopen
story = urlopen("http://sixty-north.com/c/t.txt")
story_words = []

for line in story:
    for word in line.split():
        story_words.append(word.decode("utf-8"))
    
story.close()
print(story_words)

for word in story_words:
    print(word)
