from Bio import Entrez
import os

def fetch_taxonomy_id(taxonomy_name):
    Entrez.email = "u7457260@anu.edu.au"
    search_handle = Entrez.esearch(db="taxonomy", term=taxonomy_name)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    taxonomy_id = search_results["IdList"][0]
    return taxonomy_id

def fetch_data_and_write_to_file(db, search_query, output_filename, retmax=1000):
    handle = Entrez.esearch(db=db, term=search_query, retmax=retmax)
    records = Entrez.read(handle)
    handle.close()

    ids = records["IdList"]

    with open(output_filename, "w") as output_file:
        for record_id in ids:
            with Entrez.efetch(db=db, id=record_id, rettype="fasta", retmode="text") as handle:
                data = handle.read()
            output_file.write(data)

taxonomy_name = "Planctomycetales"
taxonomy_id = fetch_taxonomy_id(taxonomy_name)

# 下载全基因组序列
genome_search_query = f"txid{taxonomy_id}[Organism:exp] AND latest_refseq[filter] AND all[filter] NOT anomalous[filter]"
fetch_data_and_write_to_file("assembly", genome_search_query, "genomes.fasta")

# 下载16S基因序列
rRNA_search_query = f"txid{taxonomy_id}[Organism:exp] AND 16S[filter] AND bacteria[filter]"
fetch_data_and_write_to_file("nucleotide", rRNA_search_query, "16S_rRNA.fasta")

# 下载蛋白质序列
protein_search_query = f"txid{taxonomy_id}[Organism:exp]"
fetch_data_and_write_to_file("protein", protein_search_query, "proteins.fasta")
