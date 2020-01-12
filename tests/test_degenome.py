import sys
import unittest
import glob

sys.path.append('../degenome')
import gtf_to_gen_pos
import dge_to_ideogram


class GtfToGenPosTestCase(unittest.TestCase):

    def test_gtf_to_gen_pos(self):
        args = [
            '--gtf-path',
            '../tests/data/sampled_gencode.vM23.basic.annotation.gtf.gz',
            '--organism',
            'Mus musculus',
            '--output-dir',
            '/tmp/'
        ]
        parsed_args = gtf_to_gen_pos.create_parser().parse_args(args)
        gtf_to_gen_pos.etl(parsed_args)

        with open('/tmp/Mus_musculus.gen_pos.tsv') as f:
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


class DgeToIdeogramTestCase(unittest.TestCase):

    def test_dge_to_ideogram(self):
        args = [
            '--gen-pos-path',
            '../tests/data/Mus_musculus.gen_pos.tsv',
            '--dge-path',
            '../tests/data/sampled_GLDS-21_array_differential_expression.csv',
            '--output-dir',
            'data'
        ]
        parsed_args = dge_to_ideogram.create_parser().parse_args(args)
        gene_pos_path = parsed_args.gen_pos_path
        dge_path = parsed_args.dge_path
        output_dir = parsed_args.output_dir

        dge_to_ideogram.etl(gene_pos_path, dge_path, output_dir)

        output_files = glob.glob("data/*.json")

        self.assertEqual(len(output_files), 5)