
import bs4
from bs4 import BeautifulSoup as bs
import re
import requests


url = input()
res = requests.get(url)
print(res.raise_for_status())
soup = bs(res.text, 'lxml')
p = re.compile("^fbd_itm clear", re.MULTILINE)
texts = soup.find_all("div", attrs={"id":" some word "})
user = []
for text in texts:
    t = text.find_all('a', attrs={"href":" some tag "})
    user.append(t)
user_str = str(user)
p = re.compile(">.{2,8}<")
result = p.findall(user_str)
owner = soup.find_all("div", attrs={"class":" some class "})
owner = str(owner)
o = re.compile(">.{2,8}</a")    # some length
writer = o.findall(owner)
writer = str(writer).replace('>', '').replace('</a','')
writer = str(writer)[2:-2]

users = []

for resu in result:
    if resu != ">, <":
        if resu[1:-1] not in users:    
            if resu[1:-1] != writer:
                users.append(str(resu[1:-1]))
                i += 1
           
user_names = []
i = 1
for name in users:
    user_names.append(str(i)+'. '+name)
    i += 1
j = 0    
while j < len(user_names):
    if "</a>, " in user_names[j]:
        user_names[j] = user_names[j].replace("</a>, ", "")
    else: pass
    j += 1





print(user_names)




