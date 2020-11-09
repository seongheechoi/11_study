# lec16_3_tm.R
# Crawling
# textmining

## modify and use the code right below only if there is a problem with 'rjava'
#Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151')

# install packages
#install.packages("xml2") # to read html
#install.packages("rvest") # to use 'html_nodes'
#install.packages("KoNLP") # korean natural language processing
#install.packages("tm") # corpus, term-document matrix, etc.
#install.packages("stringr") # to use 'str_match'
#install.packages("wordcloud") # word cloud
# install.packages("qgraph") # qgraph of co-occurence matrix

# use packages
#library(xml2)
#library(rvest)
#library(KoNLP)
#library(tm)
#library(stringr)

# crawling base URL
url_base <- 'http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=51786&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='

# make a vector to contain comments
reviews <- c()

# start crawling
for(page in 1:10){
  url <- paste(url_base, page, sep='') # from page 1 to 70
  htxt <- read_html(url)
  comment <- html_nodes(htxt, 'div')%>%html_nodes('div.input_netizen')%>%
    html_nodes('div.score_result')%>%html_nodes('ul')%>%html_nodes('li')%>%
    html_nodes('div.score_reple')%>%html_nodes('p') # exact location of comments
  review <- html_text(comment) # extract only texts from comments
  review <- repair_encoding(review, from = 'utf-8') # repair faulty encoding
  review <- str_trim(review) # trim whitespace from start and end of string
  reviews <- c(reviews, review) # save results
}

# extract nouns(N) and predicates(P)
ext_func <- function(doc){
  doc_char <- as.character(doc)
  ext1 <- paste(SimplePos09(doc_char))
  ext2 <- str_match(ext1, '([A-Z가-힣]+)/[NP]')
  keyword <- ext2[,2]
  keyword[!is.na(keyword)]
}

# 1. term-document matrix
corp <- Corpus(VectorSource(reviews)) # generate a corpus

tdm <- TermDocumentMatrix(corp, # generate a term-document matrix
                          control=list(
                            tokenize=ext_func,
                            removePunctuation=T,
                            removeNumbers=T,
                            wordLengths=c(4,8)))

tdm_matrix <- as.matrix(tdm) # save as a matrix
Encoding(rownames(tdm_matrix)) <- "UTF-8" # encoding

word_count <- rowSums(tdm_matrix) # sum of term frequencies of each word
word_order <- word_count[order(word_count, decreasing=T)] # sort in descending order

doc <- as.data.frame(word_order) # save as a data frame

# 2. word cloud
library(wordcloud)

windowsFonts(font=windowsFont("맑은 고딕")) # set font
set.seed(1234)
wordcloud(words=rownames(doc), freq=doc$word_order, min.freq=2,
          max.words=100, random.order=FALSE, scale=c(5,1), rot.per=0.35,
          family="font", colors=brewer.pal(8,"Dark2"))

# 3. co-occurrence matrix
#word_order2 <- order(word_count, decreasing=T) # sort in descending order
#top_word <- tdm_matrix[word_order2[1:20],] # Top 20 most used words
#co_occur_matrix <- top_word %*% t(top_word)

