# MIQ
# Language: Python
# Input: CSV
# Output: TSV 
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy_1.16

PluMA plugin that accepts a CSV file of taxa and abundances (rows are samples, columns are taxa).

It performs interquartile analysis, associating with each sample and taxon (i, j) the interquartile (1,2,3,or 4) of taxon j in sample i

It then returns a TSV file of two columns, one row for each taxon.  Each row contains the taxon, and its median interquartile value across all samples.  The purpose is really to give an idea of how highly abundant a taxon is relative to others in the sample.


