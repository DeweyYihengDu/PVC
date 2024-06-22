library(ggtree)
library(ape)
library(ggplot2)

# 读取树文件
tree <- read.tree("./tree/tree/alignment_unique.fasta.treefile")

# 绘制基础系统发育树
p <- ggtree(tree)

# 美化树的外观
p <- p + 
  geom_tiplab(size=3, align=TRUE) +  # 增加标签并对齐
  theme_tree2() +                   # 使用树的主题
  labs(title="Phylogenetic Tree")   # 添加标题

# 打印绘图
print(p)

# 保存绘图为文件
# ggsave("phylogenetic_tree.png", plot=p, width=8, height=6, dpi=300)

dist_matrix <- cophenetic(tree)

# 计算每个样本与其他所有样本的平均距离
mean_distances <- rowMeans(dist_matrix)

# 找出平均距离最大的前三个样本
top3_samples <- names(sort(mean_distances, decreasing = TRUE))[1:9]

cat("差异性最大的前 3 个样本是：", top3_samples, "\n")

# 删除这三个样本
pruned_tree <- drop.tip(tree, top3_samples)

# 绘制新的系统发育树
plot(pruned_tree, main = "Pruned Phylogenetic Tree")

####################
# get the label text

# 获取叶节点的标签
tip_labels <- tree$tip.label

# 获取内部节点的标签（如果有）
node_labels <- tree$node.label

# 输出叶节点的标签
cat("叶节点的标签是：\n")
print(tip_labels)

# 输出内部节点的标签
cat("内部节点的标签是：\n")
print(node_labels)

