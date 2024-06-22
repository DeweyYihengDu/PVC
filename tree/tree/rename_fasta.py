from Bio import SeqIO

input_file = "alignment.fasta"
output_file = "alignment_unique.fasta"

# 用于记录样本名称的字典
name_dict = {}

# 读取并处理fasta文件
sequences = []
for record in SeqIO.parse(input_file, "fasta"):
    name = record.id
    if name in name_dict:
        # 如果样本名称重复，增加一个编号
        name_dict[name] += 1
        new_name = f"{name}_{name_dict[name]}"
        record.id = new_name
        record.description = new_name
    else:
        name_dict[name] = 0
    sequences.append(record)

# 写入新的fasta文件
SeqIO.write(sequences, output_file, "fasta")
