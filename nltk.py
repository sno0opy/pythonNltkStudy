#coding=utf-8
#开头不声明 默认为ascⅡ编码保存
from __future__ import division
from nltk.book import *
#----------------------------------------1.1
#五个nltk常用函数
#text1.concordance("monstrous")
#text1.similar("monstrous")
#text1.common_contexts(["monstrous","very"])
#text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
#text3.generate() 此函数已失效

#len set 函数的用法和函数自定义
##sorted(set(text3))
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
#----------------------------------------1.2
#文本即为链表，可由索引找到单词
sent1=['call','me','Ishmeal','.']
print sent1.append("momo")
print sent1
print sent1[0] 
#m:n选中的是索引为m...n-1,当省略时前者默认为链表首，后者为链表尾
print sent1[1:4]
#单词在文本中的第一个索引
print sent1.index("me")
sent1[0]='funk'
