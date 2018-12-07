import requests
import expanddouban
from bs4 import BeautifulSoup
import csv
import codecs

"""
任务1：获取每个地区、每个类型页面的URL
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category,location)
    # https://movie.douban.com/tag/#/: 豆瓣电影分类页面
    # sort=S: 按评分排序
    # range=9,10: 评分范围 9 ~ 10
    # tags=电影: 标签为电影
    return url

"""
任务2：获取电影页面 HTML
return a HTML page of douban movie lists given category and location.
"""
def getMovieHtml(category, location):
    url = getMovieUrl(category, location)
    html = expanddouban.getHtml(url, loadmore=True)
    return html

"""
任务3：定义电影类
define a class of movies including name, rate, location, category, info_link, and cover_link.
"""
class Movie():
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

"""
任务4：获得豆瓣电影的信息
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
    target_movies_list = []
    html = getMovieHtml(category, location)
    soup = BeautifulSoup(html, 'html.parser')
    movies_list = soup.find(class_="list-wp")
    names = movies_list.find_all(class_="title")
    rates =	movies_list.find_all(class_="rate")
    info_links = movies_list.find_all(class_="item")
    cover_links = movies_list.find_all(class_="cover-wp")
    list_size = len(movies_list)
    # 此任务有参考网上资源
    for _ in range(list_size):
    		movie = Movie(names[_].string,rates[_].string,location,category,info_links[_]['href'],cover_links[_].img['src'])
    		target_movies_list.append(movie)
    return target_movies_list

"""
任务5：构造电影信息数据表
output a .csv file of a list which includes all movies information of your favorite three types.
"""
favorite_tags = ['恐怖','文艺','动作']
areas = ['大陆','美国','香港','台湾','日本','韩国','英国','法国','德国','意大利','西班牙','印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦']
target_list = []
for area in areas:
    for tag in favorite_tags:
        target_list += getMovies(tag, area)

# 此任务有参考网上资源
with codecs.open('movies.csv', 'w', 'utf_8_sig') as csvfile:
    fieldnames = ['name', 'rate', 'category', 'location', 'info_link', 'cover_link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for element in target_list:
        writer.writerow({'name':element.name, 'rate':element.rate,'category':element.category,'location':element.location,'info_link':element.info_link,'cover_link':element.cover_link})


"""
任务6：统计电影数据
output a .txt file to determine from all types of movies you choosed before, which areas are top three in number of movies, and the percentage.
"""
Horror_movies=[]
Literary_movies=[]
Action_movies=[]

for element in target_list:
    if element.category == '恐怖':
        Horror_movies.append(element.location)
    elif element.category == '文艺':
        Literary_movies.append(element.location)
    else:
        Action_movies.append(element.location)

Horror_movie_dict = {}

for location in Horror_movies:
	if Horror_movie_dict.get(location):
	   Horror_movie_dict[location] += 1
	else:
	   Horror_movie_dict[location] = 1

Literary_movie_dict = {}

for location in Literary_movies:
	if Literary_movie_dict.get(location):
	   Literary_movie_dict[location] += 1
	else:
	   Literary_movie_dict[location] = 1
        
Action_movie_dict = {}

for location in Action_movies:
	if Action_movie_dict.get(location):
	   Action_movie_dict[location] += 1
	else:
	   Action_movie_dict[location] = 1
       
Horror_movie_total = sum(Horror_movie_dict.values())
Horror_movie_top3 = sorted(Horror_movie_dict,key=lambda x:Horror_movie_dict[x],reverse=True)[:3]
Horror_movie_top3_percentage = "{:.2%}".format(Horror_movie_dict[Horror_movie_top3[0]]*1.0 / Horror_movie_total), "{:.2%}".format(Horror_movie_dict[Horror_movie_top3[1]]*1.0 / Horror_movie_total), "{:.2%}".format(Horror_movie_dict[Horror_movie_top3[2]]*1.0 / Horror_movie_total)

Literary_movie_total = sum(Literary_movie_dict.values())
Literary_movie_top3 = sorted(Literary_movie_dict,key=lambda x:Literary_movie_dict[x],reverse=True)[:3]
Literary_movie_top3_percentage = "{:.2%}".format(Literary_movie_dict[Literary_movie_top3[0]]*1.0 / Literary_movie_total), "{:.2%}".format(Literary_movie_dict[Literary_movie_top3[1]]*1.0 / Literary_movie_total), "{:.2%}".format(Literary_movie_dict[Literary_movie_top3[2]]*1.0 / Literary_movie_total)

Action_movie_total = sum(Action_movie_dict.values())
Action_movie_top3 = sorted(Action_movie_dict,key=lambda x:Action_movie_dict[x],reverse=True)[:3]
Action_movie_top3_percentage = "{:.2%}".format(Action_movie_dict[Action_movie_top3[0]]*1.0 / Action_movie_total), "{:.2%}".format(Action_movie_dict[Action_movie_top3[1]]*1.0 / Action_movie_total), "{:.2%}".format(Action_movie_dict[Action_movie_top3[2]]*1.0 / Action_movie_total)

with open("output.txt","w", encoding = 'utf-8') as f:
		f.write("在恐怖电影中，数量排名前三的地区{}，分别占此类别电影总数的百分比为{}".format(Horror_movie_top3,Horror_movie_top3_percentage))
		f.write("在文艺电影中，数量排名前三的地区{}，分别占此类别电影总数的百分比为{}".format(Literary_movie_top3,Literary_movie_top3_percentage))
		f.write("在动作电影中，数量排名前三的地区{}，分别占此类别电影总数的百分比为{}".format(Action_movie_top3,Action_movie_top3_percentage))