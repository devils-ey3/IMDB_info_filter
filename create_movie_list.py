import os,os.path
import glob
f = open('movie_list.txt','a')
for i in glob.glob(os.getcwd()+'\\*'):
    name = i
    name = name[len(os.getcwd())+1::].replace('.',' ')
    if 'srt' not in name:
        print(name)
        try:
            f.write(name+'\n')
        except:
            pass
f.close()
