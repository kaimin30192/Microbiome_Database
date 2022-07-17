# Alpha diversity

library(mia)
library(ggplot2)
library(patchwork)
library(vegan)
library(ggsignif)
library(scater)

count <- read.table("S_count.csv", row.names = 1, sep="\t", header=T)
taxa <- read.table("S_taxa.csv", row.names = 1, sep="\t", header=T)
sample_info <- read.csv("S_info.csv", row.names = 1)
tse <- TreeSummarizedExperiment(assays = list(counts = count),
       colData = sample_info,
       rowData = taxa)

### calculate the shannon index
tse <- mia::estimateDiversity(tse,
       abund_values = "counts",
       index = "shannon",
       name = "shannon")
df <- as.data.frame(colData(tse)[colData(tse)$Dataset %in%
      c("Group_A", "Group_B"), ])
df$Dataset <- factor(df$Dataset)
comb <- split(t(combn(levels(df$Dataset), 2)),
        seq(nrow(t(combn(levels(df$Dataset), 2)))))
pdf('S_alpha_shannon.pdf')
ggplot(df, aes(x = Dataset, y = shannon)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2) +
  geom_signif(comparisons = comb, map_signif_level = FALSE) +
  theme(text = element_text(size = 20))
dev.off()

### calculate the chao1 index
tse <- mia::estimateRichness(tse,
       abund_values = "counts",
       index = "chao1",
       name="chao1")
df <- as.data.frame(colData(tse)[colData(tse)$Dataset %in%
      c("Group_A", "Group_B"), ])
df$Dataset <- factor(df$Dataset)
comb <- split(t(combn(levels(df$Dataset), 2)),
        seq(nrow(t(combn(levels(df$Dataset), 2)))))
pdf('S_alpha_chao1.pdf')
ggplot(df, aes(x = Dataset, y = chao1)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2) +
  geom_signif(comparisons = comb, map_signif_level = FALSE) +
  theme(text = element_text(size = 20))
dev.off()

### calculate the dissimilarity using the MDS ordination
### based on Bray-Curtis distance
if(1<0){
  tse <- runMDS(tse,
        FUN = vegan::vegdist,
        method = "bray",
        name = "PCoA_BC",
        exprs_values = "counts")
  p <- plotReducedDim(tse, "PCoA_BC", colour_by = "Dataset")
  e <- attr(reducedDim(tse, "PCoA_BC"), "eig");
  rel_eig <- e/sum(e[e>0])
  p <- p + labs(x = paste("PCoA 1 (", round(100 * rel_eig[[1]],1), "%", ")", sep = ""),
                y = paste("PCoA 2 (", round(100 * rel_eig[[2]],1), "%", ")", sep = ""))
  pdf('S_beta.pdf')
  dev.off()
}