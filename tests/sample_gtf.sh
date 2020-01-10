#!/usr/bin/env bash

# Samples first 500 lines of chromosomes 1, 2, 10, 19, 20, X and Y in mouse GTF
# Output is used as reference for testing
#
# PREREQUISITES
# Download and decompress mouse GENCODE GTF:
# curl -s ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M23/gencode.vM23.basic.annotation.gtf.gz | gunzip -c > gencode.vM23.basic.annotation.gtf
#
# EXAMPLE:
# cd tests/data
# ./../sample_gtf.sh
#
# Possible TODOs: 
# - Convert to Python
# - Use variables!
# - Read entire file once, not once for each chromosomes

head -n 1 gencode.vM23.basic.annotation.gtf  > sampled_gencode.vM23.basic.annotation.gtf
grep -E "chr1\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
grep -E "chr2\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
grep -E "chr10\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
grep -E "chr19\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
grep -E "chr20\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
grep -E "chrX\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
grep -E "chrY\t" gencode.vM23.basic.annotation.gtf | head -n 500 >> sampled_gencode.vM23.basic.annotation.gtf
gzip -f sampled_gencode.vM23.basic.annotation.gtf
tput bel
