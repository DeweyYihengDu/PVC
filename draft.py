from Bio import Entrez
import os

Entrez.email = "u7457260@anu.edu.au"  # 请使用您的电子邮件地址
taxonomy_id = "204428"  

# 搜索所有属于拟杆菌门的细菌基因组
genome_search_query = f"txid{taxonomy_id}[Organism:exp] AND genome[filter]"
genome_handle = Entrez.esearch(db="nucleotide", term=genome_search_query, retmax=1000)
genome_records = Entrez.read(genome_handle)
genome_handle.close()

genome_ids = genome_records["IdList"]

# 下载全基因组序列
for genome_id in genome_ids:
    genome_file = f"{genome_id}_genome.fasta"
    if not os.path.isfile(genome_file):
        with Entrez.efetch(db="nucleotide", id=genome_id, rettype="fasta", retmode="text") as handle:
            genome_data = handle.read()
        with open(genome_file, "w") as output_file:
            output_file.write(genome_data)

# 搜索所有属于拟杆菌门的16S基因
rRNA_search_query = f"txid{taxonomy_id}[Organism:exp] AND 16S[filter]"
rRNA_handle = Entrez.esearch(db="nucleotide", term=rRNA_search_query, retmax=1000)
rRNA_records = Entrez.read(rRNA_handle)
rRNA_handle.close()

rRNA_ids = rRNA_records["IdList"]

# 下载16S基因序列
for rRNA_id in rRNA_ids:
    rRNA_file = f"{rRNA_id}_16S.fasta"
    if not os.path.isfile(rRNA_file):
        with Entrez.efetch(db="nucleotide", id=rRNA_id, rettype="fasta", retmode="text") as handle:
            rRNA_data = handle.read()
        with open(rRNA_file, "w") as output_file:
            output_file.write(rRNA_data)

# 搜索所有属于拟杆菌门的蛋白质
protein_search_query = f"txid{taxonomy_id}[Organism:exp]"
protein_handle = Entrez.esearch(db="protein", term=protein_search_query, retmax=1000)
protein_records = Entrez.read(protein_handle)
protein_handle.close()

protein_ids = protein_records["IdList"]

# 下载蛋白质序列
for protein_id in protein_ids:
    protein_file = f"{protein_id}_protein.fasta"
    if not os.path.isfile(protein_file):
        with Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text") as handle:
            protein_data = handle.read()
        with open(protein_file, "w") as output_file:
            output_file.write(protein_data)

