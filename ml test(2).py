from matminer.featurizers.composition import ElementFraction
# 使用 feature_labels() 方法
ef = ElementFraction()
element_fraction_labels = ef.feature_labels()
print(element_fraction_labels)
