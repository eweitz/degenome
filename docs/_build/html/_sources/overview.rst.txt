DEGenome – Differential expression across the genome
====================================================
|Build| |Coverage| |PyPI|


DEGenome_ transforms differential gene expression (DGE) data to Ideogram_ JSON.

Written in Python, the DEGenome pipeline takes in genome annotations and DGE
matrices, and outputs Ideogram.js JSON annotation files.

You can then upload Ideogram JSON to the cloud, and explore it in an
interactive genome visualization at
https://eweitz.github.io/ideogram/differential-expression.

For a walk-through example, see the `DEGenome tutorial on Terra
<https://app.terra.bio/#workspaces/degenome/degenome/notebooks/launch/degenome-tutorial.ipynb>`_.

.. _DEGenome: https://github.com/eweitz/degenome

.. _Ideogram: https://github.com/eweitz/ideogram

.. |Build| image:: https://img.shields.io/circleci/build/github/eweitz/degenome.svg
  :target: https://circleci.com/gh/eweitz/degenome

.. |Coverage| image:: https://codecov.io/gh/eweitz/degenome/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/eweitz/degenome

.. |PyPI| image:: https://img.shields.io/pypi/v/degenome.svg
  :target: https://pypi.org/project/degenome

.. image:: images/explore_differential_expression_across_the_genome.png
  :width: 690
  :alt: Explore differential expression across the genome