#Ejercicio biopython
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SecFeature
from Bio.SeqRecord import SeqRecord
import os.path
def summarize_contents(filename):
record=SEqIO.read(filename, "genbank")
print("Name: ",record.name)
print("Path: ",os.path.dirname(filename))
record=list(SeqIO.parse(filename,"genbank"))
print("Num_records:"%len(records))
for seq_recors in SeqIO.parse(filename,"genbank"):
print ("ID: ",record.id)
print ("Name: ",record.name)
print("Descriprion: ",record.description)
