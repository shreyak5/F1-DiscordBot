import bs4 as bs
import requests
import json

url = "https://www.welovequizzes.com/formula-1-quiz-questions-and-answers/"
source = requests.get(url).text
soup = bs.BeautifulSoup(source, 'lxml')

data = []

# All questions are in <h3> tags
for h3 in soup.find_all('h3'):
    # only one of <h3> tags in the source code is NOT a question, therefore we ignore it
    if("Popular Posts" in h3.text):
        continue
    empty = {"question": "", "options" : [], "answer" : ""}  
    empty['question'] = (h3.text)[3:].strip()
    data.append(empty)

# All answers in a <div> tag with class = "su-spoiler-content"
# The answers are in the format "Answer: A. <answer>"
# We extract only the option, i.e A / B / C
i = 0
for ans in soup.find_all('div', class_ = "su-spoiler-content"):
    data[i]['answer'] = ans.text[7:9].strip()
    i = i + 1

i = 0
# All questions have 3 options each 
# Each option is present inside a plain <p> tag
for options in soup.find_all('p', class_ = None):
    if(i == len(data)):
        break
    if("A. " in options.text):
        data[i]['options'].append(options.text)
    elif("B. " in options.text):
        data[i]['options'].append(options.text)
    elif("C. " in options.text):
        data[i]['options'].append(options.text)
        i = i + 1

# Storing dictionary data in a json file    
with open("data\questions.json", "w") as f:
    json.dump(data, f, indent = 2)

# Sources:
# - https://www.welovequizzes.com/formula-1-quiz-questions-and-answers/