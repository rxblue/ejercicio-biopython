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

list_of_seqs = [Seq("acgtcgggtatacggcatgacgta"), Seq("gctgcagcagcattattacgcgcg")]
def concatenate_and_get_reverse_of_complement():                                                       
    concatenated = Seq("")
    for s in list_of_seqs():
        concatenated += s
    concatenated
    concatenated = my_seq
    print(my_seq.reverse_complement())