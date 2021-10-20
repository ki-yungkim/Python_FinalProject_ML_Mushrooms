import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import torchvision
from torch.utils.data import DataLoader
import joblib

from torchvision import transforms

class Test01Service:
    def getResult(self, inputImage):
        trans = transforms.Compose([transforms.Resize((32, 32)),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                    ])
        imageData = torchvision.datasets.ImageFolder(root="static/uploads/", transform=trans)
        testImageloader = DataLoader(imageData,
                                     batch_size=1,
                                     shuffle=False,
                                     num_workers=1)
        dataiter = iter(testImageloader)
        images, labels = dataiter.next()

        # Single ImageFile convert to TensorObject
        # inputImg = Image.open(inputImage)
        # resizeImg = inputImg.resize((32,32))
        # tf = transforms.ToTensor()
        # tensorImg = tf(resizeImg)
        # tensorImg = tensorImg.unsqueeze(0)
        # print('tensor1:',tensorImg.shape)
        # normalize = transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        # tensorImg2 = normalize(tensorImg)
        # print('tensor2:',tensorImg2.shape)

        classes = ['Agaricus',
                   'Amanita',
                   'Boletus',
                   'Cortinarius',
                   'Entoloma',
                   'Hygrocybe',
                   'Lactarius',
                   'Russula',
                   'Suillus']
        net = joblib.load("mushroom_test.pkl")
        outputs = net(images)
        # outputs = net(tensorImg2)
        _, predicted = torch.max(outputs, 1)
        result = (classes[predicted])
        return result

    # def getResult(self, inputImage):
    #     inputImg = Image.open(inputImage)
    #     resizeImg = inputImg.resize((32,32))
    #     tf = transforms.ToTensor()
    #     tensorImg = tf(resizeImg)
    #     tensorImg = tensorImg.unsqueeze(0)
    #
    #     fileName = "test00.pkl"
    #
    #     net = Net()
    #     net = joblib.load(fileName)
    #     classes = [
    #         'Agaricus',
    #         'Amanita',
    #         'Boletus',
    #         'Cortinarius',
    #         'Entoloma',
    #         'Hygrocybe',
    #         'Lactarius',
    #         'Russula',
    #         'Suillus'
    #     ]
    #
    #     output = net(tensorImg)
    #     _, predicted = torch.max(output, 1)
    #     res = classes[predicted]
    #
    #     return res
