import os
import script
import unittest
class miPrueba(Unittest.testCase)
  def test_summarize_contents(self)
    s = script.summarize_contents(os.path.abspath("data/AF323668.gbk"))
    self.assertDictEqual({""})
    
    s = script.summarize_contents(os.path.abspath("data/ls_orchid.fasta"))
    self.assertDictEqual({""})
    
    s = script.summarize_contents(os.path.abspath("data/ls_orchid.gbk"))
    self.assertDictEqual({""})
    
    s = script.summarize_contents(os.path.abspath("data/m_cold.fasta"))
    self.assertDictEqual({""})
    
    s = script.summarize_contents(os.path.abspath("data/NC_002703.gbk"))
    self.assertDictEqual({""})
    
    s = script.summarize_contents(os.path.abspath("data/opuntia.fasta"))
    self.assertDictEqual({""})
