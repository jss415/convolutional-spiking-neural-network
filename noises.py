import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import torchvision.transforms.functional as F
from torch.utils.data import DataLoader, sampler
import torch.optim as optim
import os
import time
import pickle
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


class AddGaussianNoise(object):
    def __init__(self, mean=0., std=1.):
        self.std = std
        self.mean = mean
        
    def __call__(self, tensor):
        return tensor + torch.randn(tensor.size()) * self.std + self.mean
    
    def __repr__(self):
        return self.__class__.__name__ + '(mean={0}, std={1})'.format(self.mean, self.std)

class AddSaltAndPepperNoise(object):
    def __init__(self, prob=0.1):
        self.prob = prob
        
    def __call__(self, tensor):
        return tensor + torch.rand(tensor.size()) * self.prob * 2 - self.prob

    def __repr__(self):
        return self.__class__.__name__ + '(prob={0})'.format(self.prob)


class AddSpeckleNoise(object):
    def __init__(self, prob=0.1):
        self.prob = prob
        
    def __call__(self, tensor):
        return tensor + torch.rand(tensor.size()) * self.prob * 2 - self.prob

    def __repr__(self):
        return self.__class__.__name__ + '(prob={0})'.format(self.prob)

class AddGaussianBlur(object):
    def __init__(self, kernel_size, sigma):
        self.sigma = sigma
        self.kernel_size = kernel_size

    def __call__(self, img):
         sigma = self.sigma
         return F.gaussian_blur(img, self.kernel_size, sigma)