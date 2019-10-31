library(ggplot2)

sequence.data <- read.csv(file="venezuela.csv")

p1 <- ggplot() + 
    geom_line(aes(y = GCpercentage, x = id), data = sequence.data) + 
    theme(text=element_text(family="Tahoma"))