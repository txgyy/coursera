import requests
from time import sleep
import os
from urllib.request import urlretrieve


exc = open('exception.txt','a')
suc = open('success.txt','a')
#第一次注释掉
# with open('exception.txt','r') as exception_url:
#     e = exception_url.readlines()

for i in range(4,5):
    with open('week'+str(i)+'_content_urls.txt','r') as content_urls:
        if not os.path.isdir('week'+str(i)):
            os.mkdir('week'+str(i))
        os.chdir('week'+str(i))
        j=0
        for content in content_urls:
            j+=1
            cont=content.split(' https://')
            name = cont[0]
            if '?' in name:
                name = ' '.join(name.split('?'))
            if '&' in name:
                name = 'and'.join(name.split('&'))
            if ':' in name:
                name = ','.join(name.split(':'))
            if '"' in name:
                name = '`'.join(name.split('"'))
            if '/' in name:
                name = ' '.join(name.split('/'))
            video = 'https://'+cont[1]
            subtitle = 'https://'+cont[2].strip('\n')
            # if name + ' ' + video + ' ' + subtitle+'\n' in e:
            if not os .path.isdir(str(j)+name):
                os.mkdir(str(j)+name)
            os.chdir(str(j)+name)
            try:
                if not os.path.isfile(name+'.mp4'):
                    urlretrieve(video, name+'.mp4')
            except Exception as e:
                exc.write(name + ' ' + video + ' ' + subtitle +' https://'+str(e)+'\n')
            else:
                try:
                    if not os.path.isfile('en' + name + '.vtt'):
                        text = requests.get(subtitle, verify=False).text
                        with open('en' + name + '.vtt', 'w') as vtt:
                            vtt.write(text)
                            suc.write(name + ' ' + video + ' ' + subtitle)
                        sleep(4)
                except Exception as e:
                    exc.write(name + ' ' + video + ' ' + subtitle + ' https://' + str(e) + '\n')

            os.chdir('..')
        os.chdir('..')
