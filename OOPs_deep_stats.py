#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import shapiro

class DataStats_Deep:
    def __init__(self, user_data):
        self.data = np.array(user_data)
    
    def total(self):
        print('Total Sum:', sum(self.data))
        
    def count(self):
        print('Total Count:', len(self.data))
        
    def minimum(self):
        print('Minimum Value:', min(self.data))
        
    def maximum(self):
        print('Maximum Value:', max(self.data))
        
    def data_range(self):
        print('Range:', max(self.data) - min(self.data))
        
    def average(self):
        print('Mean:', np.mean(self.data))
        
    def median(self):
        print('Median:', np.median(self.data))
        
    def mode(self):
        try:
            mode_val = stats.mode(self.data, keepdims=True)
            print('Mode:', mode_val.mode[0])
        except:
            print('No mode')
            
    def var(self):
        print('Variance:', np.var(self.data))
        
    def std_var(self):
        print('Standard Deviation:', np.std(self.data))
        
    def skew(self):
        print('Skewness:', stats.skew(self.data))
        
    def kurt(self):
        print('Kurtosis:', stats.kurtosis(self.data))
        
    def q1(self):
        self.quartile1 = np.percentile(self.data, 25)
        print('Q1:', self.quartile1)
        
    def q3(self):
        self.quartile3 = np.percentile(self.data, 75)
        print('Q3:', self.quartile3)
        
    def iqr(self):
        self.iq_range = self.quartile3 - self.quartile1
        print('IQR:', self.iq_range)
        
    def lw(self):
        self.lower = self.quartile1 - self.iq_range * 1.5
        print('Lower Whisker:', self.lower)
        
    def uw(self):
        self.upper = self.quartile3 + self.iq_range * 1.5
        print('Upper Whisker:', self.upper)
        
    def outliers_count(self):
        outliers = len([i for i in self.data if i > self.upper or i < self.lower])
        print('Total Outliers Count:', outliers)
        
    def empirical_rule(self):
        vary = np.var(self.data, ddof=1)
        print('Variance:', vary)
        
        std_dev = vary ** 0.5
        print('Standard Deviation:', std_dev)
        
        for i in range(1, 4):
            lower = np.mean(self.data) - i * std_dev
            upper = np.mean(self.data) + i * std_dev
            perc = ((self.data >= lower) & (self.data <= upper)).sum() / len(self.data)
            print(f'{i} Standard deviation Range:({lower:.2f} to {upper:.2f}) --> {perc*100:.2f}% of data ')
            
    def normality_test(self):
        stat_val, p_val = shapiro(self.data)
        if p_val > 0.05:
            print('Likely Follows Normal Distribution')
        else:
            print('Likely Does Not Follow Normal Distribution')
            
    def confidence_interval(self):
        standard_error = np.std(self.data) / np.sqrt(len(self.data))
        for conf, z in [(95, 1.96), (97, 2.17), (99, 2.576)]:
            moe = standard_error * z
            lower = np.mean(self.data) - moe
            upper = np.mean(self.data) + moe
            print(f'{conf}% Confidence Interval: {lower:.2f}, {upper:.2f}')
            
    def visualize(self):
        if len(set(self.data)) < 7:
            print('Detected Discrete Data')
            plt.figure(figsize=(6, 6))
            sns.countplot(x=self.data)
            plt.show()
            
            plt.figure(figsize=(6, 6))
            data_count = pd.Series(self.data).value_counts()
            plt.pie(data_count, labels=data_count.index, autopct="%0.2f%%")
            plt.show()
        else:
            print('Detected Continuous Data')
            plt.figure(figsize=(6, 6))
            sns.histplot(self.data, kde=True)
            plt.show()
        
            plt.figure(figsize=(6, 6))
            sns.boxplot(x=self.data)
            plt.show()
            
    def everything(self):
        self.total()
        self.count()
        self.maximum()
        self.minimum()
        self.data_range()
        self.average()
        self.median()
        self.mode()
        self.var()
        self.std_var()
        self.skew()
        self.kurt()
        self.q1()
        self.q3()
        self.iqr()
        self.lw()
        self.uw()
        self.outliers_count()
        self.empirical_rule()
        self.confidence_interval()
        self.normality_test()
        self.visualize()


# dummy=[3,24,31,5,3,24,30,44,13,69,24,1,30,2]
# st_obj=DataStats_Deep(dummy)
# st_obj.everything()

