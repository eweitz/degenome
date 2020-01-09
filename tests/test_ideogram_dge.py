import sys
import unittest

sys.path.append('../ideogram_dge')
from gtf_to_gen_pos import create_parser, etl


class GtfToGenPosTestCase(unittest.TestCase):

    def test_gtf_to_gen_pos(self):
        args = [
            '--gtf-path',
            '../tests/data/sampled_gencode.vM23.basic.annotation.gtf.gz',
            '--organism',
            'Mus musculus'
        ]
        parsed_args = create_parser().parse_args(args)
        etl(parsed_args)

        with open('Mus_musculus.gen_pos.tsv') as f:
            gen_pos = f.readlines()

        self.assertEqual(len(gen_pos), 50)

        expected_first_line = (
            '# Organism: Mus musculus; ' +
            'assembly: GRCm38; ' + 
            'annotation: GENCODE sampled_gencode.vM23.basic.annotation.gtf.gz'
        )
        self.assertEqual(gen_pos[0].strip(), expected_first_line)
        
        expected_last_line = (
            'ENSMUSG00000053211.10\t' + 
            'Zfy1\t' + 
            'Y\t' + 
            '725128\t' + 
            '797409\t' + 
            'protein_coding'
        )
        self.assertEqual(gen_pos[-1].strip(), expected_last_line)
