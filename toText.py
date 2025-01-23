import easyocr
from PIL import Image
from packaging import version
import sys
path1 = r'C:\pythonFile\\'
#img=Image.open(path1 + '应.jpg')
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
#result = reader.readtext(path1 + img)
result = reader.readtext(r'C:\pythonFile\\result.jpg')
#print(result)
char = '佣'


xYList = []#格式为，最后一项为该项目的index([[0, 3228], [200, 3228], [200, 3302], [0, 3302]], '[字形]甲', 0.8371180902348793, 45)
lineIndex = 0
matchedIndexList = [] #匹配有“查询字”的项目的index
for line in result:    
    print("line:  " + str(line))
    if char  in line[1]:
        matchedIndexList.append(lineIndex)
    lineIndex += 1

#给每一个字的解释，找分割处的坐标，如果后续出现识别率问题，需要再优化
lineIndex2 = 0
for line in result:
    if '字形' in line[1]:
        line = line + (lineIndex2,)
        xYList.append(line)
        print('xYList的每一项' + str(line))
    lineIndex2 += 1

#result.jpg为两页合并而成的竖版图片
from PIL import Image, ImageEnhance
image1 = Image.open(r'C:\pythonFile\\result.jpg')
# image2 = Image.open(path1 + '伯_454.jpg')
w,h = image1.size
#box对背景图进行上下分割。
#比哪个解释出现得最多
objectIndex = 0
countIndex = 0
topIndexList = []
for index in xYList:
    topIndex = 0 #每一项出现“查询字”的次数，最多的那个就是目标解释内容
    if countIndex < len(xYList) - 1:
        everyIndexArr = [xYList[countIndex][-1], xYList[countIndex + 1][-1]]
        for index1 in matchedIndexList:
            if  everyIndexArr[0]  < index1 < everyIndexArr[1]:
                topIndex += 1
        topIndexList.append(topIndex)
        countIndex += 1

#取得最大值得index
value = max(topIndexList)  # 最大值
idx = topIndexList.index(value)  # 最大值索引
objectIndex = idx
#直接根据目标来切割目标解释
b1 = xYList[objectIndex][0][1][1]
b2 = xYList[objectIndex + 1][0][1][1]
#print('b1: ' + str(b1))
#print('b2: ' + str(b2))
a1 = 0 
b1 = int(b1) - 150
a2 = 920 + 10
b2 = int(b2) - 150
box1 = (a1, b1, a2, b2)
im1 = image1.crop(box1)
flag = Image.new('RGB',(a2 - a1, b2 - b1))
flag.paste(im1, (0,0))
flag.show()
flag.save(r'C:\pythonFile\\RR.jpg',quality=40)
sys.exit()



# b1 = 0
# b2 = 0
# xYIndex = 0
# for line in xYList:
#     print('222:  ' + str(matchedIndexList))
#     for objectIndex in matchedIndexList:
#         if xYList[xYIndex][-1] < objectIndex <  xYList[xYIndex + 1][-1]:
#             b1 = xYList[xYIndex][0][1][1]
#             b2 = xYList[xYIndex + 1][0][1][1]
#             #print('b1: ' + str(b1))
#             #print('b2: ' + str(b2))
#             a1 = 0 
#             b1 = int(b1) - 150
#             a2 = 920 + 10
#             b2 = int(b2) - 150
#             box1 = (a1, b1, a2, b2)
#             im1 = image1.crop(box1)
#             flag = Image.new('RGB',(a2 - a1, b2 - b1))
#             flag.paste(im1, (0,0))
#             flag.show()
#             flag.save(r'C:\pythonFile\\RR.jpg',quality=40)
#             sys.exit()
              
#     xYIndex += 1
sys.exit()
# c1 = a2
# d1 = b1
# c2 = 2040 + 10
# d2 = b2
#a1,a2为x轴坐标，b1,b2为y轴坐标，形成一个四边形
# box1 = (a1, b1, a2, b2)
# box2 = (c1,d1,c2,d2)
#im1是上半部分
#im2是下半部分
# im1 = image1.crop(box1)
# im2 = image1.crop(box2)

#第二张图，相同操作
# box3 = (a1 + 20, b1, a2 + 20, b2)
# box4 = (c1+ 20,d1,c2+ 20,d2)
# im3 = image2.crop(box3)
# im4 = image2.crop(box4)




#新建画布
# flag = Image.new('RGB',(a2 - a1, b2 - b1))
#lag = Image.new('RGB',(int(w/2),int(h*2)))
# #对图片上半部分进行明暗处理，对下半部分进行对比度处理
# im1 = ImageEnhance.Brightness(im1).enhance(0.5)
# im2 = ImageEnhance.Contrast(im2).enhance(2.0)
# flag.paste(im1, (0,0))
# flag.paste(im2, (0,int(h - 420 - 50)))
# flag.paste(im3, (0,int((h - 420 - 50))*2))
# flag.paste(im4, (0,int((h - 420 - 50))*3))
# flag.save(path1 + 'result.jpg',quality=100)
# flag.show()




        

# with open('E:\pythonFile\\result.json', 'w', encoding='UTF-8') as f:
#     for line in result:
        
#         f.write(line)
#         if '字形' in line[4]:
#             print(line)