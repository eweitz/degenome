import sys
import unittest
import glob

sys.path.append('../ideogram_dge')
import gtf_to_gen_pos


class GtfToGenPosTestCase(unittest.TestCase):

    def test_gtf_to_gen_pos(self):
        args = [
            '--gtf-path',
            '../tests/data/sampled_gencode.vM23.basic.annotation.gtf.gz',
            '--organism',
            'Mus musculus'
        ]
        parsed_args = gtf_to_gen_pos.create_parser().parse_args(args)
        gtf_to_gen_pos.etl(parsed_args)

        with open('Mus_musculus.gen_pos.tsv') as f:
            gen_pos = f.readlines()

        self.assertEqual(len(gen_pos), 188)

        expected_first_line = (
            '# Organism: Mus musculus; ' +
            'assembly: GRCm38; ' + 
            'annotation: GENCODE sampled_gencode.vM23.basic.annotation.gtf.gz'
        )
        self.assertEqual(gen_pos[0].strip(), expected_first_line)

        expected_last_line = (
            'ENSMUSG00000068457.14\t' +
            'Uty\t' +
            'Y\t' +
            '1096861\t' +
            '1245759\t' +
            'protein_coding'
        )
        self.assertEqual(gen_pos[-1].strip(), expected_last_line)
