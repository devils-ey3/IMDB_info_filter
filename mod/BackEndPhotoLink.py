__author__ = "Devils-ey3"

class Photo(object):
    def __init__(self,data):
        self.movie_name = data.find("h1",{"itemprop":"name","class":""}).text.strip()
        try:
            self.duration = data.find("time",{"itemprop":"duration"}).text.strip()
        except:
            self.duration = "There is an error"
        for link in data.findAll(itemprop="image"):
            try :
                self.z =  link.get('src')
                break
            except :
                self.z = "There is an error"
    def getLink(self):
        return self.z