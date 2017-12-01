
#开头不声明 默认为ascⅡ编码保存 本书为python自然语言处理 #coding=utf-8由于编码问题使用python3不再需要声明
#============================================================符号声明
'''
									!					软件和书中版本不同注意点
									表达式：            基本表达式	
'''
#============================================================
from __future__ import division
import nltk 
#from nltk.book import *				# *太费时间改为text1却发现无用
#----------------------------------------3.1从网络和硬盘访问文本
#电子书
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')		#此处是由于下面会编码错误  此处为python2时使用的方法 但后面还会出错
'''
from urllib.request import urlopen
'''
url ="http://www.gutenberg.org/files/2554/2554-0.txt"
raw=urlopen(url).read()
print (type(raw))
print (len(raw))
print (raw[:100])
raw=raw.decode('utf-8')					#加这一句是由于我是用python3 将raw有byte转为str
tokens=nltk.word_tokenize(raw)
print (type(tokens))
print (len(tokens))
print (tokens[:10])
text=nltk.Text(tokens)
print (type(text))
print (text[1020:1060])
raw.find('PART Ⅰ')
print(raw.find("End of Project Gutenberg's Crime"))
raw=raw[5303:1157681]
print(raw)
'''
#处理HTML
'''
from bs4 import BeautifulSoup
url="http://i.firefoxchina.cn/"
html=urlopen(url).read()
print(html[:60])
#raw=nltk.clean_html(html)				#clean_html函数已经不再使用 使用beautifulsoup的get_text
soup=BeautifulSoup(html,"html.parser")
raw =soup.get_text()
print(raw[:200])
tokens=nltk.word_tokenize(raw)	
print(tokens)
tokens=tokens[200:500]
text=nltk.Text(tokens)
print(text)
'''
#读取本地文件
'''
f=open('Test.txt','rU')
print(f.read())
raw=f.read()							#第二次read（）赋值给raw会为空
print(raw)
#用户输入
s=input("Enter some text:")							#python3没有raw_input 并入input
print('you typed ',len(nltk.word_tokenize(s)),'words.')
'''
#了解byte-str-link之间的转化
#----------------------------------------3.2字符串：最底层的文本处理
#字符串的基本操作(有加乘无减除)
'''
circus='Monty Python'
print(circus)
circus='Monty Python\'s Flying Circus'
print(circus)
circus="Monty Python's Flying Circus"
print(circus)
couplet='Shall I compare thee ti a Summer day?'\
		'Thou are more lovely and more temperate:'+"you"
print(couplet)
couplet="""Shall I compare thee ti a Summer day?
			thou are more lovely and more temperate:"""
print(couplet)
a=[1,2,3,4,5,6,7,6,5,4,3,2,1]
b=[' '*4*(7-i) + 'very'*i for i in a]
print(b)
'''
#输出字符串
#访问单个字符（下标索引--正负）
'''
sent='colorless green ideas sleep furiously'
for char in sent:
	print(char,end=' ')
for word in sent:
	print(word,end="")
print()
from nltk.corpus import gutenberg
raw=gutenberg.raw("melville-moby_dick.txt")
fdist=nltk.FreqDist([ch.lower() for ch in raw if ch.isalpha()])
print(fdist.most_common())
'''
#访问子字符串
'''
monty='monty python'
print(monty[6:10])						#n:m输出n到m-1
if 'ty' in monty:
	print ('found "ty"')
print (monty.find('python'))
print(monty.rfind('python'))
'''
#更多字符串操作
'''
				s.find(t)              	#返回t第一个索引，没有返回-1
				s.rfind(t)			   	#返回最后一个t的索引，没有-1
				s.index(t)				#与find类似，但没有引起ValueError
				s.rindex(t)
				s.join(text)       		#连接字符串s和text中的词汇
				s.split(t)				#在所有t的位置将s分割为链表
				s.splitelines()			#将s按行分割为字符串链表
				s.lower()
				s.upper()
				s.titlecase()
				s.strip()				#返回一个没有首尾空白的复制
				s.replace(t,u)			#用u替换s中的t
'''
#链表与字符串的差异
'''
query="who knows?"
beatles=["john",'Paul','George','Ringo']
print(query[2])
print(beatles[2])
print(query[:2])
print(beatles[:2])
print(query+"i don't")
#print(beatles+'Brian') 				#会报错
print(beatles+['Brian'])
beatles[0]="john Lennon"
del beatles[-1]
print(beatles)
#query[0]="F"							#会报错因为字符串不可变
'''
#----------------------------------------3.3使用Unicode进行文字处理
'''
path=nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
import codecs
f=codecs.open(path,encoding='latin2')	#将编码文件以unicode读入
for line in f:
	line=line.strip()
	print(line.encode("unicode_escape"))
f=codecs.open(path,'w',encoding="utf-8")#在文件中写入unicode
'''
#----------------------------------------3.4使用正则表达式
import re 
wordlist=[w for w in nltk.corpus.words.words('en') if w.islower()]
print([w for w in wordlist if re.search('ed$',w)])