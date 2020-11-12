import os
import script
import unittest

class miPrueba(unittest.TestCase):
  def test_summarize_contents(self):
    s = script.summarize_contents(os.path.abspath("data/AF323668.gbk"))
    self.assertDictEqual({""})
    print(s)
    s = script.summarize_contents(os.path.abspath("data/ls_orchid.fasta"))
    self.assertDictEqual({""})
    print(s)
    s = script.summarize_contents(os.path.abspath("data/ls_orchid.gbk"))
    self.assertDictEqual({""})
    print(s)
    s = script.summarize_contents(os.path.abspath("data/m_cold.fasta"))
    self.assertDictEqual({""})
    print(s)
    s = script.summarize_contents(os.path.abspath("data/NC_002703.gbk"))
    self.assertDictEqual({""})
    print(s)
    s = script.summarize_contents(os.path.abspath("data/opuntia.fasta"))
    self.assertDictEqual({""})
    print(s)

  def test_concatenate_and_get_reverse_of_complement(self):

    dnaseq = script.concatenate_and_get_reverse_of_complement("acgtcgggtatacggcatgacgta")
    self.assertEqual("gctgcagcagcattattacgcgcg", dnaseq)

    dnaseq = script.concatenate_and_get_reverse_of_complement("gcacgtacgatgcatctgatcact")
    self.assertEqual("cgatcgcctacgattacggaaagc", dnaseq)

    dnaseq = script.concatenate_and_get_reverse_of_complement("gcatggtgaaagcctagcttagcc")
    self.assertEqual("acgtcgggtatacggcatgacgta", dnaseq)

    dnaseq = script.concatenate_and_get_reverse_of_complement("gctgcagcagcattattacgcgcg")
    self.assertEqual("gctgcagcagcattattacgcgcg", dnaseq)

    dnaseq = script.concatenate_and_get_reverse_of_complement("acgtcgggtatacggcatgacgta")
    self.assertEqual("gcatggtgaaagcctagcttagcc", dnaseq)


  def test_print_protein_and_stop_codon_using_standard_table(Diccionario{dnaseq, messenger_rna, prot, }):

    dnaseq = Seq("acgtcgggtatacggcatgacgta")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("gctgcagcagcattattacgcgcg")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("gcatggtgaaagcctagcttagcc")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("cgatcgcctacgattacggaaagc")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("gcacgtacgatgcatctgatcact")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

  def test_proteins_and_codons_using_mitocondrial_yeast_table(Diccionario{dnaseq, messenger_rna, prot, }):


    dnaseq = Seq("acgtcgggtatacggcatgacgta")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("gctgcagcagcattattacgcgcg")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("gcatggtgaaagcctagcttagcc")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("cgatcgcctacgattacggaaagc")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)

    dnaseq = Seq("gcacgtacgatgcatctgatcact")
    self.print_protein_and_stop_codon_using_standard_table(dnaseq)
    