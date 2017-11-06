import requests 


r = requests.get("https://en.wikipedia.org/wiki/Git")
count = 0 
for line in r.text.split("\n"):
    git_occurences = [ w for w in line.split(" ") if w.lower().find("git") == 0 ]
    count = count +  len(git_occurences) 


assert count ==  113 
