# lec8_3.R
# Install package NLP, tm, wordcloud

# set working directory
setwd("D:/tempstore/moocr")

# Natural language processing
install.packages('NLP')
# text mining package
install.packages('tm')
# visualizing
install.packages('wordcloud')
# color displaying
install.packages('RColorBrewer')

# set library (set in order)
library(NLP)
library(tm)
library(RColorBrewer)
library(wordcloud)

# 20 new articles from Reuter- 21578 data set
data(crude)
# To know abour crude data
help(crude)

# remove punctuation in documnet
crude<-tm_map(crude, removePunctuation)
# remove stopwords
crude<-tm_map(crude, removeNumbers)
crude<-tm_map(crude, function(x) removeWords(x,stopwords()))
stopwords()

# from frequency counts
tdm<-TermDocumentMatrix(crude)
m<-as.matrix(tdm)
v<-sort(rowSums(m), decreasing=TRUE)
d<-data.frame(word=names(v), freq=v)

# plot a word cloud
# to see detail help(wordcloud) 
par(mfrow=c(1, 1))
wordcloud(d$word, d$freq, random.order=FALSE)

