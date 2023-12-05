import torch
import torchvision.transforms as transforms
import torchvision.io as io
import torch.nn as nn

class SimpleModel:
    def __init__(self, *nums, numX : int, numY : int):
        paramater = list()
        for i in range(len(nums) - 2):
            paramater.append(nn.Linear(nums[i], nums[i + 1]))
            paramater.append(nn.ReLU())
        paramater.append(nn.Linear(nums[-2], nums[-1]))
        self.model = nn.Sequential(*paramater)
        self.criterion = nn.CrossEntropyLoss()  #选择交叉熵损失函数，适用于分类问题
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01) #梯度下降
        self.preProcess = transforms.Compose([  #图片处理
            transforms.ToPILImage(),
            transforms.CenterCrop((numX, numY)),
            transforms.Resize((numX, numY)),
            transforms.Grayscale(num_output_channels=1),
            transforms.ToTensor()
        ])

    def train(self, dataX, dataY):
        self.optimizer.zero_grad()
        loss = self.criterion(self.model(dataX), dataY)
        loss.backward()
        self.optimizer.step()

    def use(self, dataX) ->tuple:
        # 使用训练好的模型进行预测
        with torch.no_grad():  # 在推断时不需要计算梯度
            outputs = self.model(dataX)
        return outputs, torch.argmax(outputs)
    
    def readImage(self, fileName : str, y : int) -> tuple:
        img = io.read_image(fileName)
        img = self.preProcess(img)
        return img.view(1, -1), torch.LongTensor([y])
    
    def readImageOnly(self, fileName : str):
        img = io.read_image(fileName)
        img = self.preProcess(img)
        return img.view(1, -1)
    
    def loadModel(self, fileName : str):
        self.model = torch.load(fileName + ".pth")
        self.model.train()
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01) #梯度下降
        # self.model.eval()

    def saveModel(self, fileName : str):
        self.model = torch.save(self.model, fileName + ".pth")