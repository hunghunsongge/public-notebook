import numpy as np 
a=(0.4714/74.67)**2+(0.3580/1.17283)**2+(1/8.093)**2
b=(a**0.5)*14.38
print(b)

def phsaver(a):
	m = len(a)
	aver = []
	for i in range(m):
		sum = 0
		for num in a[i]:
			sum = sum + num
		aver.append(sum/len(a[i]))
	return aver
#physics undecided 求A类不确定度
def phsunde(a):
	m = len(a)
	ud = []
	for i in range(m):
		ud.append(0)
	for j in range(m):
		ave = phsaver(a)[j]
		sum = 0
		dim = len(a[j])
		for num in a[j]:
			sum = sum + (num - ave)**2
		unde = (sum/(dim*(dim - 1)))**0.5
		print ("第",j+1,"行的平均值为：",ave)
		print ("第",j+1,"行的A类不确定度为：",unde)
	return ud
if __name__ == "__main__":
	a = input('请输入要计算的表格，同行用,(英文逗号）分隔，换行用;(英文分号）分隔：\n')
	a = a.split(";")
	s = len(a)
	for i in range(s):
		a[i] = a[i].split(',')
		n = len(a[i])
		for j in range(n):
			a[i][j] = eval(a[i][j])
	phsunde(a)
