from pymatgen import Composition
# Composition 在pymatgen 21年版本，且需要编辑py文件中from sklearn.neighbors.unsupervised import NearestNeighbors语句中删除.unsupervised
fe2o3 = Composition("Fe2O3")
print("fe2o3:",fe2o3)
# 作为一个简单的例子，我们将使用element分数特征化器获得元素分数。
from matminer.featurizers.composition import ElementFraction

ef = ElementFraction()
# 现在我们可以把我们的结果具体化了。
element_fractions = ef.featurize(fe2o3)

print(element_fractions)

