#coding=utf-8
#开头不声明 默认为ascⅡ编码保存 本书为python自然语言处理
from __future__ import division
import nltk
# *太费时间改为text1无用
from nltk.book import *
#----------------------------------------1.1文本和词汇
#五个nltk常用函数
#text1.concordance("monstrous")
#text1.similar("monstrous")
#text1.common_contexts(["monstrous","very"])
#text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
#text3.generate() 					#此函数已失效

#len set 函数的用法和函数自定义
#sorted(set(text3))
#print len(set(text3))
#print len(text3)/len(set(text3))
'''
print 100*text4.count("a")/len(text4)
def lexical_diversity(text):
	return len(text)/len(set(text))
def percentage(count,total):
	return 100*count/total
print lexical_diversity(text4)
print percentage(text4.count("a"),len(text4))
'''
#----------------------------------------1.2将文本当作词链表
#文本即为链表，可由索引找到单词
'''
sent1=['call','me','Ishmeal','.']
print sent1.append("momo") 			#无法输出
print sent1
print sent1[0] 
print sent1[1:4]					#m:n选中的是索引为m...n-1,当省略时前者默认为链表首，后者为链表尾
print sent1.index("me")				#单词在文本中的第一个索引
sent1[0]='funk'
'''
#变量赋值/变量名以字母开头，可以包含数字字母下划线
'''
my_sent=["Bravely",'bord',"sir",'Robin',',','rode','forth','from','camelot']
print my_sent
noun_phrase=my_sent[1:4]
print noun_phrase
my_word=sorted(noun_phrase)			#排序表大写在小写之前
print my_word
'''
#一些访问链表方式也能用在字符串上
'''
name='qunima'
print name[0]
print name[:4]
print name*2 						#可执行乘法和加法
print name+'!'
print ''.join(['monty','python'])	#连接两个string
print 'monty python'.split()
'''
#复习本节
'''
say=['After','all','is','said','and','done','more','is','said','than','done']
tokens=set(say)
print tokens
tokens=sorted(tokens)
print tokens
print tokens[-2:]
'''
#----------------------------------------1.3计算语言简单的统计
#频率分布 
'''
fdist1 =FreqDist(text1)				#一开始需要输入nltk.book import *
print fdist1
print len(text1)
print len(set(text1))
vocabulary1=fdist1.keys()
print vocabulary1[:50]
print fdist1['whale']
fdist1.plot(50,cumulative=True)
print fdist1.hapaxes()				#只出现一次的词   在此处有9000多个
'''
#细粒度的选择词

#特性P 满足时p(w)为真
#b. {w for w in V if p(w)}			#此集合中所有的w都满足：w是集合V（词汇表）的一个元素且w有特性P
									#产生链表而不是集合 可能有相同元素
'''
V=set(text1)
#long_word={w for w in V if len(w)>15}
long_word={word for word in V if len(word)>15}
print sorted(long_word)
fdist5=FreqDist(text5)
print sorted(w for w in set(text5) if len(w)>7 and fdist5[w]>7)
'''
#词语搭配和双连词 
print bigrams(['more','is','said','than','done'])		#<generator object bigrams at 0x0284A8F0> 
print list(bigrams(['more','is','said','than','done']))	#书上会出现上面问题 按照网上添加list（）
text4.collocations()