__author__ = "Devils-ey3"
from bs4 import BeautifulSoup
import requests
class DW(object):
    def __init__(self,data,link):
        x = data.findAll('div')
        for i in x:
            try:
                if 'Director:' in i.h4.text.strip():
                    self.director = i.span.text.strip()
                    break
            except:
                self.director = "there is an error"
        # for i in x:
        #     try:
        #         if 'Writer:' in i.h4.text.strip():
        #             self.writer = i.span.text.strip()
        #             break
        #     except:
        #         pass

        for i in data.findAll('div'):
            try :
                self.rating = i.div.strong['title']
                break
            except :
                self.rating = "there is an error"
        Full_Cast_Crew = link + 'fullcredits?ref_=tt_ov_st_sm'
        request = requests.get(Full_Cast_Crew)
        soup = BeautifulSoup(request.text,'html.parser')
        self.writerList = []
        self.topActorList=[]
        for i in soup.findAll('a'):
            try:
                if 'ref_=ttfc_fc_wr' in i['href']:
                    self.writerList.append(i.text.strip())
            except :
                pass

        for i in soup.findAll('a'):
            try :
                if 'ref_=ttfc_fc_cl_t' in i['href']:
                    self.topActorList.append(i.text.strip())
            except:
                pass



        # for i in data.findAll('a'):
        #     z = i.get('href')
        #     try :
        #         if isinstance(z,str) and z.startswith('fullcredit') and z.endswith('writers'):
        #             self.link = link + z
        #             print("hello"+self.link)
        #     except:
        #         self.writer = data.find("span",{"class":"itemprop","itemprop":"name"})
        #         self.writer = self.writer.text.strip()
        #         print('hello')
    def get_director(self):
        return self.director
    def get_writers(self):
        return self.writerList
    def get_rating(self):
        return self.rating
    def get_actors(self):
        return self.topActorList

