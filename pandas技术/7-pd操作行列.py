import pandas as pd

# 再pandas中一行一列都是一个序列，类似于字典一样，可以将字典转成序列，索引index就是键
dat = {"a": 10, "b": 20, "c": 30}
s1 = pd.Series(dat, index=dat.keys(), name="A")
print(s1.index)

# 还可以使用指定索引的创建方法
l1 = ['a', 'b', 'c', 'd']
l2 = [100, 200, 300, 400]
s2 = pd.Series(l2, index=l1, name="B")
print(s2.index)

# 将序列加入到dataFrame中，才能算一行或一列, 以字典形式加的话，就是列
data = pd.DataFrame({s1.name: s1, s2.name: s2})
print(data)

# 会把序列的名字当做行号，把索引当做列号
data2 = pd.DataFrame([s1, s2])
print(data2)

# 如果两个序列中，有的格有交集，有的没有交集，那就将有交集的填上，没有交接的就赋值NaN,也就是没有一个值
