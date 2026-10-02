name = "Siyu"
school = "南京大学"
major = "计算机"
height = 1.75

print(f"姓名：{name}")
print(f"学校：{school}")
print(f"专业: {major}")
print(f"身高：{height :.1f}米")
print(f"身高：{height * 100 :.0f}厘米")


#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print(f"小明成绩提升的百分比为{r:.1f}%")