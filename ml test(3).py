from pymatgen import Composition
# 按照生成特征的顺序来  查看标签
fe2o3 = Composition("Fe2O3")

# 作为一个简单的例子，我们将使用element分数特征化器获得元素分数。
from matminer.featurizers.composition import ElementFraction

ef = ElementFraction()
# 现在我们可以把我们的结果具体化了。
element_fractions = ef.featurize(fe2o3)

element_fraction_labels = ef.feature_labels()
print(element_fraction_labels[7], element_fractions[7])
print(element_fraction_labels[25], element_fractions[25])
