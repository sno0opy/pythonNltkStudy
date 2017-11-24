#coding=utf-8
#开头不声明 默认为ascⅡ编码保存 本书为python自然语言处理
#============================================================符号声明
'''
									!					软件和书中版本不同注意点
									表达式：            基本表达式	
'''
#============================================================
from __future__ import division
import nltk
from nltk.book import *				# *太费时间改为text1却发现无用
#----------------------------------------1.1文本和词汇
#五个nltk常用函数
'''
text1.concordance("monstrous")
text1.similar("monstrous")
text1.common_contexts(["monstrous","very"])
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text3.generate() 					#!此函数已失效
'''
#len set sorted函数的用法和函数自定义
'''
sorted(set(text3))
print len(set(text3))
print len(text3)/len(set(text3))

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
vocabulary1=fdist1.most_common()	#!此处注意 我用的是NLTK3版本此处不在使用keys而是most_common	So for NLKT version 3, instead of fdist1.keys()[:50], use fdist1.most_common(50).
print vocabulary1[:50]
print fdist1['whale']
#fdist1.plot(50,cumulative=True)
#print fdist1.hapaxes()				#只出现一次的词   在此处有9000多个
'''
#细粒度的选择词

#特性P 满足时p(w)为真
#表达式： b. {w for w in V if p(w)}		#此集合中所有的w都满足：w是集合V（词汇表）的一个元素且w有特性P
									#产生链表而不是集合 可能有相同元素
'''
V=set(text1)
#long_word={w for w in V if len(w)>15}     				#此处书中为[]但我写为｛｝也能运行
long_word={word for word in V if len(word)>15}
print sorted(long_word)
fdist5=FreqDist(text5)
print sorted(w for w in set(text5) if len(w)>7 and fdist5[w]>7)
'''
#词语搭配和双连词 
'''
print bigrams(['more','is','said','than','done'])		#<generator object bigrams at 0x0284A8F0> 
print list(bigrams(['more','is','said','than','done']))	#!书上会出现上面问题 按照网上添加list（）
text4.collocations()									#出现频率比预期频率更频繁的双联词
'''
#计算其它东西
'''
#print [len(w) for w in text1]
fdist = FreqDist([len(w) for w in text1])
print fdist.most_common()								#text中出现的词的长度排序列表
print fdist.items()										
'''
#----------------------------------------1.4回到python:决策与控制
#sent7=['wangt','minimi','fi','goto','sdf','print','debian','go','home','director','a','as','nonexecutive']
#条件														表达式：[w for w in text if condition]
									#c 
									#not c
									#c1 and c2
									#c1 or c2
									#运算符 < <= == != > >=
'''
print [w for w in sent7 if len(w)>3]					
									#词汇比较运算符
"""
	s.startswith(t)					测试s是否以t开头
	s.endswith(t)
	t in 							测试s中是否包含t
	s.islower()						测试s中所有字符是否都是小写字母
	s.isupper()
	s.isalpha()						s中所有字符是否都是字母
	s.isalnum()						s中所有字符是否都是字母和数字
	s.isdigit()						s中所有字符是否都是数字
	s.istitle()						s中是否首字母大写（s中所有词都首字母大写）
"""
print sorted([w for w in text1 if w.endswith('ableness')])
'''
#对每个元素进行操作											表达式：[f(w) for...]或者[w.f() for...]
'''
print [len(w) for w in sent7]
print [w.upper() for w in sent7]
print len(text1)
print len(set(text1))
print len(set([word.lower() for word in text1]))
print len(set([word.lower() for word in text1 if word.isalpha()]))
print len(set([word for word in text1 if word.isalpha() and word.islower()])) #比上面对于text中没对应小写的词会丢失
'''
#嵌套代码块
'''
word="cat"
if len(word)<5:
	print 'word length is less than 5'
for word in ["me",'cat','sdf','kill','wole','whole']:
	print word
'''
#条件循环
'''
sent1=['a','Call','me','Ishael','.']
for xyzzy in sent1:
	if xyzzy.endswith('l'):
		print xyzzy
for token in sent1:
	if token.islower():
		print token,'is a lowercase word'
	elif token.istitle():
		print token,"is a titlecase word"
	else:
		print token,"is punctuation"
tricky=sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
print tricky
for word in tricky:
	print word,
'''
#----------------------------------------1.5自动理解自然语言
#词意消歧
#指代消解
#自动生成语言
#机器翻译
#babelize_shell()					#!该模块已经不再提供
#人机对话系统
#----------------------------------------1.6小结
#P35
#----------------------------------------1.7深入阅读
#介绍书籍
#----------------------------------------1.8练习

#6
text2.dispersion_plot(['Elinor','Marianne','Edward','Willoughby'])
#7
text5.collocations()
#9
my_string='word miss'
print my_string
print my_string*3					#不会加空格
#10
my_sent=['mu','shit']
print ''.join(my_sent)
print ''.join(my_sent).split('u',1)
#12
print 'monty python'[6:12]
print ['monty','python'][1]
#13
print sent1[2][2]
#15
for word in sorted(set(text5)):
	if word.startswith('b'):
		print word
