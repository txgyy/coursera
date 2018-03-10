from time import sleep
from selenium import webdriver
import os
import random


browser = webdriver.Chrome()
browser.get('https://translate.google.cn/#auto/zh-CN')
en = browser.find_element_by_id('source')
ch = browser.find_element_by_id('result_box')
click = browser.find_element_by_id('gt-submit')
with open('eroors.txt', 'a') as errors:
    for i in range(3, 7):
        with open('week' + str(i) + '_content_urls.txt', 'r') as content_urls:
            os.chdir('week' + str(i))
            j = 0
            for content in content_urls:
                j += 1
                cont = content.split(' https://')
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
                video = 'https://' + cont[1]
                subtitle = 'https://' + cont[2].strip('\n')
                os.chdir(str(j) + name)
                if not os.path.isfile(name + '.vtt'):
                    with open('en'+name + '.vtt', 'r') as vtt:
                        zimu = []
                        tran = []
                        with open(name + '.vtt', 'a', encoding='utf8') as trans:
                            for line in vtt:
                                if line == '\n' or (line[0].isdigit() and not line[1].isalpha()):
                                    zimu.append(line)
                                else:
                                    zimu.append(1)
                                    tran.append(line)
                            try:
                                t = ''.join(tran)
                                if len(t) < 4800:
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text = ch.text.split('\n')
                                    en.clear()
                                elif len(t)<9600:
                                    index = len(tran)//2
                                    t = ''.join(tran[0:index])
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text1 = ch.text.split('\n')
                                    en.clear()
                                    t = ''.join(tran[index:])
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text2 = ch.text.split('\n')
                                    en.clear()
                                    text = text1 + text2
                                else:
                                    index = len(tran)//4
                                    t = ''.join(tran[0:index])
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text1 = ch.text.split('\n')
                                    en.clear()
                                    t = ''.join(tran[index:index*2])
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text2 = ch.text.split('\n')
                                    en.clear()
                                    t = ''.join(tran[index*2:index*3])
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text3 = ch.text.split('\n')
                                    en.clear()
                                    t = ''.join(tran[index*3:])
                                    en.send_keys(t)
                                    click.click()
                                    st = random.uniform(3, 5)
                                    sleep(st)
                                    text4 = ch.text.split('\n')
                                    en.clear()
                                    text = text1 + text2+text3+text4
                                if not text:
                                    errors.write(os.getcwd() + '\n')
                                else:
                                    for index, item in enumerate(zimu):
                                        if item == 1:
                                            zimu[index] = text.pop(0) + '\n'
                                    for content in zimu:
                                        trans.write(content)
                            except:
                                errors.write(os.getcwd() + '\n')
                os.chdir('..')
            os.chdir('..')

browser.close()
