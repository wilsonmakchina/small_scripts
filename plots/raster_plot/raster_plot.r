# author: wilson
library(pheatmap)

args <- commandArgs(trailingOnly = TRUE)

if (length(args)==0) {
    stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
    # default output file
    args[2] = "raster_plot.pdf"
}

# input data format: 0-> no events, 1-> events occurs
dat <- read.csv(args[1], head = 1, row.names = 1)
dat <- t(dat)

colors = colorRampPalette(
    c("gray","#003377","#AA0000"))(3)

pheatmap(dat, cluster_rows = F, cluster_cols = F,
         show_colnames = F, 
         col = colors, filename = args[2])
