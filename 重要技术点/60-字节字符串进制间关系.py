data = b'Z\x01\x00\x01\x00\x00\x00u*\xfc\x03\xec\x00\x00\x00\x00'
data2 = b'{"angle":3.1395,"confidence":0.8978,"current_station":"AP4"}'

"""
一个字节由8位二进制组成，例如：\x01，是由0000 0001组成，

"""
print("-----------------------")
# 截取到一个字节数组，显示成了ascii码Z，标示90
print(data[0:1])

# 获取截取到的元素，是一个十进制90
print(data[0:1][0])
print("-----------------------")
print(data[1:2])
print(data[1:2][0])
print("-----------------------")

print("字节类型转成字符串：")
print(str(data2, encoding="ascii"))
print("----------------------")

print("字符串转成字节类型：")
strdate = "我是中国人"
print(strdate.encode("utf-8"))
