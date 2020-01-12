DEGenome – Differential expression across the genome
====================================================

DEGenome is a pipeline that transforms differential gene expression (DGE) data
to Ideogram.js_ annotations.  Written in Python, it takes in genome annotations
and DGE matrices, and outputs Ideogram JSON files.  You can then upload Ideogram
JSON to your server, and explore it in an interative genome visualization at
https://eweitz.github.io/ideogram/differential-expression.

.. image:: docs/images/explore_differential_expression_across_the_genome.png
  :width: 600
  :alt: Explore differential expression across the genome

.. _Ideogram.js: https://github.com/eweitz/ideogram