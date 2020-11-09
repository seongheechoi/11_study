# lec5_4.R

# maps : world map
install.packages("maps")
library(maps)

# mapdata : more world map 
install.packages("mapdata")
library(mapdata)

# mapdata : latitude and longitude
install.packages("mapproj")
library(mapproj)

# Korea using map package
par(mfrow = c(1, 2), mar=c(2,2,2,2))
map(database = 'world', region = c('South Korea', 'North Korea'))
title("Korea : maps packages")

# Korea using mapdata package
map(database = 'worldHires', region = c('South Korea', 'North Korea'))
title("Korea : mapdata packages")

# China with large city
par(mfrow = c(1, 1), mar=c(2,2,2,2))
map("worldHires", "China")
map.cities(country = "China", capitals = 3, minpop = 3500000, maxpop = 5000000)
title("capitals=3, minpop=3500000, maxpop=5000000")

# Using mapdata package
# Korea, Japan, China (Textbook : R Visualization)
par(mfrow = c(1, 1), mar=c(2,2,2,2))
map('worldHires', region=c('South Korea', 'North Korea', 'Japan', 'China'))
map('worldHires', region=c('South Korea'), col = 'blue', add = TRUE, fill = TRUE)
map('worldHires', region=c('North Korea'), col = 'coral', add = TRUE, fill = TRUE)
map('worldHires', region=c('Japan'), col = 'grey',add = TRUE, fill = TRUE)
map('worldHires', region=c('China'), col = 'yellow',add = TRUE, fill = TRUE)


# Dokdo map using mapproj package
library(mapproj)

# for reading Korean : encoding to UTF-8 
# file menu: Tools_global options_code_saving
map('worldHires', proj = 'azequalarea', orient = c(37.24223, 131.8643, 0))
map.grid(col = 2)
points(mapproject(list(y = 37.24223, x = 131.8643)), col = "blue", pch = "x", cex = 2)
title("독도")

# Assault in US (1973)
par(mfrow = c(1, 1), mar=c(1,1,1,1))
# library(maps)
# excluding Alaska, Hawaii 
sub.usa <- subset(USArrests,!rownames(USArrests) %in% c("Alaska", "Hawaii"))
# data with State name, Assult count
usa.data <- data.frame(states = rownames(sub.usa), Assault = sub.usa$Assault)
# legend
col.level <- cut(sub.usa[, 2], c(0, 100, 150, 200, 250, 300, 350))
legends <- levels(col.level)
# displaying color for the size  
levels(col.level) <- sort(heat.colors(6), decreasing = TRUE)
usa.data <- data.frame(usa.data, col.level = col.level)
# Map 
map('state', region = usa.data$states, fill = TRUE, col = as.character(usa.data$col.level))
title("USA Assault map")
legend(-77, 34, legends, fill = sort(heat.colors(6), decreasing = TRUE), cex = 0.7)

help(USArrests)
head(USArrests)

## extra practice : Italy
op <- par(no.readonly=TRUE)
par(mfrow=c(2, 2), mar=c(0, 0, 1, 0))
map("italy")
title("databse=\"italy\"")
map("italy", fill=TRUE, col=2:4)
title("fill=T, col=2:4")
map("italy", resolution=5)
title("resolution=5")
map("italy")
map("italy", "a", exact=FALSE, fill=TRUE, col="red", add=TRUE, lwd=3)
title("exact=F, add=T, lwd=5")
par(op)


######################################################
# color
# 1 black   2 red   3 green   4 blue   5 cyan   6 magenta   7 yellow   8 gray
####################################################
par(mfrow=c(1, 1))
barplot(rep(1,8), yaxt="n", col=1:10)
# see all color (657 colors)
colors()
# see rgb values for 657 colors
col2rgb(colors()) 
# make table of colors and the corresponding RGB
cc1<-cbind(colors(), t(col2rgb(colors()))) 

# select colors including "cyan" 
colors()[grep("cyan", colors())]

colors()[grep("sky", colors())]
