__author__ = "Devils-ey3"
import re
import requests
from bs4 import BeautifulSoup

class SGP(object):

    def __init__(self,dataHtml,link):
        self.storyLine = self.parentGuide = None
        self.divValue = None
        self.genres = []
        self.parentGuide = dict()
        for i in dataHtml.findAll('div'):
            try:
                if "titleStoryLine" in i['id']:
                    self.divValue = i
                    string = i.p
                    s = ' '.join(string.split())
                    if '<em class' in string:
                        string = re.findall('<p> (.*)? <em class.+',string)
                        self.storyLine = string[0]
                    else:
                        string = re.findall('<p>(.*)</p>',string)
                        self.storyLine = string[0]
            except:
                pass

        string = str(string)
        string = ' '.join(string.split())
        try:
            if '<em class' in string:
                    string = re.findall('<p> (.*)? <em class.+',string)
                    self.storyLine = string[0]
            else:
                    string = re.findall('<p>(.*)</p>',string)
                    self.storyLine = string[0]
        except:
            self.storyLine = "there is an Error"

        for a in self.divValue.findAll('a'):
            try:
                if 'genre' in a.get('href'):
                    try:
                        self.genres.append(a.string)
                    except:
                        pass
            except:
                pass

        parentLink = link + "parentalguide?ref_=tt_stry_pg"
        data = requests.get(parentLink)
        soup = BeautifulSoup(data.text,'html.parser')
        lst = set()
        # for div in soup.findAll('div'):
        #     try:
        #         for p in div.findAll('p'):
        #             try:
        #                 lst.add(p.attrs['id'])
        #             except:
        #                 pass
        #
        #     except:
        #         pass
        # print(lst)
        # for p in soup.findAll('p'):
        #     try:
        #         for i in lst:
        #             if i in p['id']:
        #                 print('*****  '+p.contents[0].strip()+'  *****')
        #                 print(p.text.replace(str(p.contents[0]),''))
        #                 key = '*****  '+p.contents[0].strip()+'  *****'
        #                 value = p.text.replace(str(p.contents[0]),'')
        #                 self.parentGuide[key] = value
        #                 print("*************************")
        #                 print(p.get_text())
        #     except:
        #         pass

        for i in soup.findAll('div'):
            try:
                for p in i.findAll('p'):
                    try :
                        if 'swiki.2.1.1' in i.p['id']:
                            # Sex & Nudity
                            self.parentGuide['--> Sex & Nudity'] = i.p.get_text().strip()
                            #print(i.p.get_text().strip())
                    except:
                        pass
                    try :
                        if 'swiki.2.2.1' in i.p['id']:
                            # Violence & Gore
                            self.parentGuide['--> Violence & Gore'] = i.p.get_text().strip()
                            #print(i.p.get_text().strip())
                    except:
                        pass
                    try :
                        if 'swiki.2.3.1' in i.p['id']:
                            # Profanity
                            self.parentGuide['--> Profanity'] = i.p.get_text().strip()
                            #print(i.p.get_text().strip())
                    except:
                        pass
                    try :
                        if 'swiki.2.4.1' in i.p['id']:
                            # Alcohol/Drugs/Smoking
                            self.parentGuide['--> Alcohol/Drugs/Smoking'] = i.p.get_text().strip()
                            #print(i.p.get_text().strip())
                    except:
                        pass
                    try :
                        if 'swiki.2.5.1' in i.p['id']:
                            # Frightening/Intense Scenes
                            self.parentGuide['Frightening/Intense Scenes'] = i.p.get_text().strip()
                            #print(i.p.get_text().strip())
                    except:
                        pass
            except:
                pass

    def get_parentGuide(self):
        return self.parentGuide