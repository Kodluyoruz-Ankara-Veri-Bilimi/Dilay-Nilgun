import pandas as pd
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt

class Information():
    def __init__(self,file_name):
        self.data = pd.read_csv("file_name")
    def Information(self):
        print(self.data.head())
        print(self.data.isnull())
        print(self.data.describe())
        print(self.data.info())

class Visualize():
    def __init__(self):
    def histogram(self):
    def boxplot(self):
    def scatterplot(self):
    def heatmeap(self):
    def barplot(self):

class PreProcessing():
    def __init__(self):
    def cleaning(self):
    def fillna(self):
    def dropna (self):
    def label_encoder(self):
    def one_hot_encoder(self):
