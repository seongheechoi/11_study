# lec3_1.r
# Working directory
# Data import, frequency, histogram, 
# attach, detach

# set working directory
# change working directory 
setwd("D:/tempstore/moocr")

# check the current working directory
getwd()

# 1. Read csv file : brain weight data
brain<-read.csv("brain2210.csv")
head(brain)
dim(brain)

# 2.Read txt file with variable name

car<-read.table(file="autompg.txt", na=" ", header=TRUE)
head(car)
dim(car)

# 3. example for using 'attach'

# to get frequency of male and female (brain data)
table(brain$sex)

# using the command 'attach'
attach(brain)

# get frequency of male and female
table(sex)

# histogram of brain weight
# hist(brain$brainwt)
hist(wt)

detach(brain)


