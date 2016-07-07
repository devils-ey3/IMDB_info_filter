__author__ = "Devils-ey3"

class RTB(object):
    def __init__(self,dataHtml,link):
        self.review = None
        self.totalReview = None
        self.helpFulFound = None
        for i in dataHtml.findAll('div'):
            try:
                if i['id']=='titleUserReviewsTeaser':
                    string = str(i.p)
                    string = string.strip().replace('<br/>','\n')
                    self.review = string[25:len(string)-10:].strip()
                    break
            except:
                pass

            for a in i.findAll('a'):
                try:
                    if 'reviews?ref_=tt_urv' in a['href']:
                        self.totalReview = "Total " + a.string[8::].strip() + " this movie."

                except:
                    pass
        for i in dataHtml.findAll('div'):
            try :
                if 'yn' in i['class']:
                    string = i.text.strip()
                    self.helpFulFound = string[:string.index('.'):].strip()

            except:
                pass

    # def review(self):
    #     return  self.review
    #
    # def totalReview(self):
    #     return self.totalReview
    #
    # def helpFulReview(self):
    #     return self.helpFulFound