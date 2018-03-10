import requests
import json
from time import sleep
text = requests.get('https://www.coursera.org/api/opencourse.v1/course/ml-clustering-and-retrieval?showLockedItems=true').text
with open('ml-clustering-and-retrieval.txt','w') as ml_clustering_and_retrieval:
    ml_clustering_and_retrieval.write(text)
url = 'https://www.coursera.org/api/opencourse.v1/video/'
url_r = 'https://www.coursera.org'
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'CSRF3-Token=1489035417.ETkkY7ExVOLRz0BP; __204u=4635864012-1488171417225; __204r=https%3A%2F%2Fwww.coursera.org%2F; _ga=GA1.2.1093683102.1488415191; __utma=158142248.1093683102.1488415191.1488614231.1488614231.1; __utmz=158142248.1488614231.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); CAUTH=Mv2GPxs5x4Jn3QSZN1T1-6PfEAkGT3cugGwz3arx6qN-kubMIXjaDdHlb3f1_9sDUf7ApfQlSyFXDAaB9k_nxA.trVTel4LBdiz9sA5QMvUMQ.tecKYfNi57zHuS6K1f6U_-oVHmnWJmyvNvXW9hIntEouSG3wj0UOPHu07p9PU_3JCNnvfxp4MnSF30GRLqz-TcBPBVbBMCOQaDM7hngpBc7xwbYNuwcvc_Hxv2bJkF6xULcQtNTQHOVW6C57o6gYsTTqNrMyu7vpCAfb2EYDWmY; maestro_login_flag=1; ip_origin=CN; ip_currency=USD; __400v=343fa3fc-ec1b-4a77-97ee-0dd97de4f69e; __400vt=1488761471990',
'Host':'www.coursera.org',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
with open('ml-clustering-and-retrieval.txt','r') as ml_clustering_and_retrieval:
    classification= ml_clustering_and_retrieval.read()
    classification= json.loads(classification)
    index = 0
    for elements in classification['courseMaterial']['elements']:
        index+=1
        with open('week'+str(index)+'_content_urls.txt', 'a') as content_urls:
            for e in elements['elements']:
                for element in e['elements']:
                    name = element['name']
                    if element['content']['definition'].get('videoId'):
                        content = requests.get(url+element['content']['definition']['videoId'],headers=headers)
                        sleep(2)
                        content = json.loads(content.text)
                        subtitle = url_r + content['subtitlesVtt']['en']
                        for video in content['sources']:
                            if video['resolution']=='720p':
                                video = video['formatSources']['video/mp4']
                                content_urls.write(name + ' ' + video + ' ' + subtitle + '\n')
