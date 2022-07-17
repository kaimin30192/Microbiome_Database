# Alpha diversity

library(mia)
library(ggplot2)
library(patchwork)
library(ggsignif)

count <- read.table("count_species.csv", row.names = 1, sep="\t", header=T)
taxa <- read.table("taxa_species.csv", row.names = 1, sep="\t", header=T)
sample_info <- read.csv("metadata_of_Dataset_A+B.csv", row.names = 1)
tse <- TreeSummarizedExperiment(assays = list(counts = count),
       colData = sample_info,
       rowData = taxa)

### calculate the chao1 index
tse <- mia::estimateRichness(tse,
       abund_values = "counts",
       index = "chao1",
       name="chao1")
df <- as.data.frame(colData(tse)[colData(tse)$SampleType %in%
      c("Group_A", "Group_B"), ])
df$SampleType <- factor(df$SampleType)
comb <- split(t(combn(levels(df$SampleType), 2)),
        seq(nrow(t(combn(levels(df$SampleType), 2)))))
pdf('alpha_diversity_chao1.pdf')
ggplot(df, aes(x = SampleType, y = chao1)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2) +
  geom_signif(comparisons = comb, map_signif_level = FALSE) +
  theme(text = element_text(size = 20))
dev.off()
