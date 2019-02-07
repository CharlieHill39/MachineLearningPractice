'''
knn算法实现
numpy科学计算库
'''

from numpy import *
import operator
'''
作用：用于创建训练样本集和类别标签列表
'''
def create_data_set():
	#创建2维数组,训练数据集
	training_data_set = array([[1.0,0.9],[1.0,1.0],[0.1,0.2],[0.0,0.1]])
	#4个样本类别
	labels = ["A","A","B","B"]

	return training_data_set,labels
'''
作用：knn算法实现
参数：
	target_data_set：待分类样本集
	training_data_set：训练样本集
	labels：类别标签列表
	k：k近邻数字
'''
def knn_classify(target_data_set,training_data_set,labels,k):
	#step1:计算待分类样本集与训练样本集每个样本的欧氏距离
	diff = tile(target_data_set,(4,1)) - training_data_set #特征差值数组
	squared_diff = diff ** 2#差值平方
	squared_sum = squared_diff.sum(axis=1) #差值的平方累加求和
	distance = squared_sum ** 0.5 #差值的平方累加和的开发结果

	#step2:按照距离由近到远排序,返回的是脚标
	sorted_distance = distance.argsort()

	#step3：根据排序结果选择k个近邻，并计算k个近邻中，每个样本所属类别出现的次数
	class_count_dict  = {}
	for i in range(k):
		label = labels[sorted_distance[i]]
		class_count_dict[label] = class_count_dict.get(label,0) + 1

	#step4:返回出现次数最多的类别标签
	sorted_class_count = sorted(class_count_dict.items(),key=operator.itemgetter(1),reverse=True)

	#step4:返回出现次数最多的类别
	return sorted_class_count[0][0]

def main():
	training_data_set,labels = create_data_set()
	k = 3
	test1 = array([1.2,1.0])
	output_label = knn_classify(test1,training_data_set,labels,k)
	print("待分类样本：",test1,"通过KNN预测的分类：",output_label)

	test2 = array([0.1, 0.3])
	output_label = knn_classify(test2, training_data_set, labels, k)
	print("待分类样本：", test2, "通过KNN预测的分类：", output_label)

main()









