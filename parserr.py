import requests
from bs4 import BeautifulSoup
import urllib
import fake_useragent

headers = {''}#это юзер агент из браузера на вкладке network 
user = fake_useragent.UserAgent().random#это юзер агент из библиотеки fake_useragent. Какой использовать нужно тестить...

HOST = ''
link = r''
session = requests.Session()#сессия...

header = {
	'user-agent': user
}
URL = []
src = ''
count = 10#это цифра по количеству страниц, ее нужно где-то брать
for i in range(1, count+1):
	URL.append(src + str(i))#тут дописать pages и тд



def parse():
	for i in URL:










