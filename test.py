from sklearn import tree
import graphviz

X = [[1,1], [2,1], [1,2], [2,2]]    #输入参数
y = [0,1,1,1]  #目标参数
clf = tree.DecisionTreeClassifier()
clf.fit(X,y)
dot_data = tree.export_graphviz(clf,filled=True)
graph = graphviz.Source(dot_data)
graph
