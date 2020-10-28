#Ejercicio biopython
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SecFeature
from Bio.SeqRecord import SeqRecord
import os.path

filename = "/mnt/C/Users/OneDrive/Escritorio/ejercicio-biopython/biopython-notebook/notebooks/data/ls_orchid.gbk"
def summarize_contents(filename):
lista = []
lista = os.path.split(filename)
record = list(SeqIO.parse(filename, "genbank"))
cadena = ("file: " + lista[1])
cadena += ("path" + lista[0])
cadena += ("num_records = %i records" % len(records))
for seq_record in SeqIO.parse(filename, "genbank"):
    cadena += ("name: " + str(seq_record.name))
    cadena += ("id: " + str(seq_record.id))
    cadena += ("description: " + str(seq_record.description))
print(cadena)
