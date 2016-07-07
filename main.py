__author__ = "Devils-ey3"
import time
try:
    import requests
    from bs4 import BeautifulSoup
except:
    print("You have a problem with request and bs4 module")
    print("Open the picture 'install request and bs4' and install it")
    time.sleep(5)
    exit()
from mod.BackEndPhotoLink import Photo
import re
from mod.DirWriRev import DW
from mod.RevTagBox import RTB
from mod.StoGenPar import SGP
import re

def Main():
    c = """
╦╔╦╗╔╦╗╔╗   ╦┌┐┌┌─┐┌─┐┬─┐┌┬┐┌─┐┌┬┐┬┌─┐┌┐┌
║║║║ ║║╠╩╗  ║│││├┤ │ │├┬┘│││├─┤ │ ││ ││││
╩╩ ╩═╩╝╚═╝  ╩┘└┘└  └─┘┴└─┴ ┴┴ ┴ ┴ ┴└─┘┘└┘
╔═╗┬┬ ┌┬┐┌─┐┬─┐
╠╣ ││  │ ├┤ ├┬┘
╚  ┴┴─┘┴ └─┘┴└─  by Devils-ey3
    """
    print(c)
    fl = open('movie_list.txt')
    movie_list=[]
    for i in fl.readlines():
        movie_list.append(i)
    fl.close()
    print(movie_list)
    for m in movie_list:
        try:
            j = '+'.join(m.split(' '))
            link = "https://www.bing.com/search?q=site:imdb.com+"+j
            sublink = requests.get(link)
            soup = BeautifulSoup(sublink.text,'html.parser')
            for i in soup.findAll('div'):
                try:
                    if "b_attribution" in i['class']:
                        if 'www.imdb.com' in i.cite.get_text():
                            link = i.cite.get_text()
                            break

                except:
                    pass
            link = 'http://'+link
            data = requests.get(link)
            dataHtml = BeautifulSoup(data.text,'html.parser')
            photo_link = Photo(dataHtml)
            print("=========================================================================")
            print(photo_link.movie_name)
            print("=========================================================================")
            print(photo_link.duration)
            print("=========================================================================")
            print(link)
            print("=========================================================================")
            print(photo_link.getLink())  # photo link

            directorAndWrite = DW(dataHtml,link)
            print("=========================================================================")
            print(directorAndWrite.get_director()) # director
            print("=========================================================================")
            print(directorAndWrite.get_writers()) # writer
            print("=========================================================================")
            print(directorAndWrite.get_rating()) # get rating
            print("=========================================================================")
            print(directorAndWrite.get_actors()) #get actors
            reviewTagBox = RTB(dataHtml,link)
            print("=========================================================================")
            print(reviewTagBox.review+"\n"+reviewTagBox.helpFulFound) #get review and helpFulFound
            print("=========================================================================")
            print(reviewTagBox.totalReview) # get total review

            storyGensParentg = SGP(dataHtml,link)
            print("=========================================================================")
            print(storyGensParentg.storyLine) #get story Line
            print("=========================================================================")
            print(storyGensParentg.genres) # get a list of categories
            print("=========================================================================")
            print(storyGensParentg.get_parentGuide()) # parent guide as dict
            print("=========================================================================")
            with open(photo_link.movie_name+'.txt','a') as file:
                file.write("*****************   Movie Name   *****************\n")
                file.write(photo_link.movie_name)
                file.write("\n\n*****************   IMDB link   *****************\n")
                file.write(link)
                file.write("\n\n*****************   Duration   *****************\n")
                file.write(photo_link.duration)
                file.write("\n\n*****************   Photo Link   *****************\n")
                file.write(photo_link.getLink())
                file.write("\n\n*****************   Directors   *****************\n")
                file.write(directorAndWrite.get_director())
                file.write("\n\n*****************   Writers   *****************\n")
                for name in directorAndWrite.get_writers():
                    file.write('--> '+name)
                    file.write('\n')
                file.write("\n*****************   Actors   *****************\n")
                for name in directorAndWrite.get_actors():
                    file.write('--> '+name)
                    file.write('\n')
                file.write("\n*****************   Movie Rating   *****************\n")
                file.write(directorAndWrite.get_rating())
                file.write("\n\n*****************   Most helpful review And Found the review helpful   *****************\n")
                file.write(reviewTagBox.review.strip()+'\n\n'+reviewTagBox.helpFulFound+'\n'+reviewTagBox.totalReview)
                file.write("\n\n*****************   Story Line   *****************\n")
                file.write(storyGensParentg.storyLine)
                file.write("\n\n*****************   Categories   *****************\n")
                for name in storyGensParentg.genres:
                    file.write('--> '+name)
                    file.write('\n')
                file.write("\n*****************   Parents Guide   *****************\n")
                for k,v in storyGensParentg.get_parentGuide().items():
                    file.write('------------  '+k+'  -------------')
                    value = re.match('./10',v)
                    if value:
                        file.write('\n'+v[:4:])
                        file.write('\n')
                        file.write(v[4::]+'\n\n\n')
                    else :
                        file.write('\n'+v+'\n\n\n')

            del directorAndWrite
            del reviewTagBox
            del storyGensParentg
            del photo_link
        except:
            continue
        time.sleep(10)
if __name__ == "__main__":Main()
