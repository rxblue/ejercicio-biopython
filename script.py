#Ejercicio biopython
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os.path

filename = "/mnt/C/Users/rxblue/ejercicio-biopython/data/ls_orchid.gbk"
def summarize_contents(filename):

    lista = []
    lista = os.path.split(filename)
    records = list(SeqIO.parse(filename, "genbank"))
    cadena = ("file: " + lista[1])
    cadena += ("path" + lista[0])
    cadena += ("num_records = %i records" % len(records))
    for seq_record in SeqIO.parse(filename, "genbank"):
        cadena += ("name: " + str(seq_record.name))
        cadena += ("id: " + str(seq_record.id))
        cadena += ("description: " + str(seq_record.description))
    print(cadena)


from Bio.Seq import Seq

def concatenate_and_get_reverse_of_complement(self):                                                       
    
    concatenated = Seq("")
    for s in list_of_seqs():
        concatenated += s
    concatenated
    my_seq = concatenated
    print(my_seq.reverse_complement())

def print_protein_and_stop_codon_using_standard_table(Diccionario{dnaseq, messenger_rna, prot}):

    messenger_rna = coding_dna.transcribe()
    messenger_rna

    prot = messenger_rna.translate()

    
    

