import torch
from torch.utils.data import DataLoader
import joblib

from torchvision import transforms
import torchvision


class Test01Service:
    def getResult(self, inputImage):
        trans = transforms.Compose([transforms.Resize((32, 32)),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                    ])
        imageData = torchvision.datasets.ImageFolder(root="static/uploads", transform=trans)
        testImageloader = DataLoader(imageData,
                                     batch_size=1,
                                     shuffle=False,
                                     num_workers=1)
        dataiter = iter(testImageloader)
        images, labels = dataiter.next()
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
        _, predicted = torch.max(outputs, 1)
        result = (classes[predicted])
        return result


