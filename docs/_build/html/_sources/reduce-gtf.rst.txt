Reduce GTF
==========
Each organism processed by DEGenome will need a reduced GTF, i.e. a "gen_pos.tsv" file.

The `gtf_to_gen_pos.py` CLI module converts a GTF genome annotation file from
GENCODE, Ensembl, or NCBI into a smaller, simpler, and more metadata-rich TSV
gene position ("gen_pos") file.  The purpose is to speed up, simplify, and
enrich downstream pipelines that require only data on genes, and not e.g.
transcripts or exons.

Example GTF files
^^^^^^^^^^^^^^^^^
* `Human (Homo sapiens), from GENCODE <ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_32/gencode.v32.basic.annotation.gtf.gz>`_
* `Mouse (Mus musculus), from GENCODE <ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M23/gencode.vM23.basic.annotation.gtf.gz>`_
* `Thale cress (Arabidopsis thaliana), from Ensembl <ftp://ftp.ensemblgenomes.org/pub/release-45/plants/gtf/arabidopsis_thaliana/Arabidopsis_thaliana.TAIR10.45.gtf.gz>`_
* `Worm (Caenorhabditis elegans), from Ensembl <ftp://ftp.ensemblgenomes.org/pub/release-45/metazoa/gtf/caenorhabditis_elegans/Caenorhabditis_elegans.WBcel235.45.gtf.gz>`_
* `Rat (Rattus norvegicus), from Ensembl <ftp://ftp.ensembl.org/pub/release-98/gtf/rattus_norvegicus/Rattus_norvegicus.Rnor_6.0.98.chr.gtf.gz>`_