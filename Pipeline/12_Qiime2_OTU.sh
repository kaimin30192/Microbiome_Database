#!/bin/sh
# Date : 2021/09/27
# Author : Kaimin
# Description : This is a program to do OTU clustering and taxanomic classification.

echo ">>> Do OTU analysis ..."
# OTU Clustering (Import Data)
qiime tools import \
  --input-path Import.fna \
  --output-path Import.qza \
  --type SampleData[Sequences]

# OTU Clustering (Dereplicate Sequences)
qiime vsearch dereplicate-sequences \
  --i-sequences Import.qza \
  --o-dereplicated-table table.qza \
  --o-dereplicated-sequences rep-Import.qza

# OTU Clustering 
qiime vsearch cluster-features-open-reference \
  --i-table table.qza \
  --i-sequences rep-Import.qza \
  --i-reference-sequences ../../Tools/Reference_GreenGene_97_OTU/GreenGene_97_otu.qza \
  --p-perc-identity 0.97 \
  --p-threads 72 \
  --o-clustered-table table-or-97.qza \
  --o-clustered-sequences rep-seqs-or-97.qza \
  --o-new-reference-sequences new-ref-seqs-or-97.qza

# Feature Classify
qiime feature-classifier classify-sklearn \
  --p-n-jobs -41 \
  --i-classifier ../../Tools/Reference_GreenGene_97_OTU/classifier.qza \
  --i-reads rep-seqs-or-97.qza \
  --o-classification taxonomy.qza

# Visualization
qiime metadata tabulate --m-input-file taxonomy.qza --o-visualization taxonomy.qzv
qiime metadata tabulate --m-input-file table-or-97.qza --o-visualization table-or-97.qzv
exit