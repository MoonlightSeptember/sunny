import jieba

seg_list = jieba.cut("当中国人都是傻子吗？", cut_all=True)
# join是split的逆操作
# 即使用一个拼接符将一个列表拼成字符串
print("/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("老是发表声明谴责有什么用", cut_all=False)
print("/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("#菲军舰恶意撞击#中国人的尊严何在？")  # 默认是精确模式
print("/ ".join(seg_list))

seg_list = jieba.cut_for_search("老是发表声明谴责有什么用")  # 搜索引擎模式
print("/ ".join(seg_list))
