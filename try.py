import SimpleModel
import os

model = SimpleModel.SimpleModel(400, 200, 100, 17, numX = 20, numY = 20)
names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "方块", "黑桃", "红桃", "梅花"]
nums = [i for i in range(17)]
#一些映射
names2nums = dict(zip(names, nums))
nums2names = dict(zip(nums, names))

totalFile = "D:/VSCodeProject/Try/Z_PIC"
fileList = os.listdir(totalFile)
for Times in range(1000):
    for fileName in fileList:
        file = os.listdir(f"{totalFile}/{fileName}")
        for pic in file:
            if (names2nums.get(fileName) == None):
                break;
            dataX, dataY = model.readImage(f"{totalFile}/{fileName}/{pic}", names2nums[fileName])
            model.train(dataX, dataY)
    print(f"--------------------------{Times}--------------------------") 

# model.loadModel("Z_TEMP")
tempList, tempIndex = model.use(model.readImageOnly(f"{totalFile}/10/vlcsnap-2020-02-05-23h22m36s885_outhand_7912318_2.png"))
print(tempList)
print(tempIndex)
print(nums2names[int(tempIndex)])

model.saveModel("Z_TEMP")