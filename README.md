# statkit_deep-own-mini-stats-library

A simple Python statistics and visualization library created by **Deep**.  
This package provides descriptive statistics, normality testing, confidence intervals, outlier detection, and visualization tools — all in one class.

---

##  Features
- **Basic Statistics**: sum, count, min, max, range, mean, median, mode  
- **Dispersion Measures**: variance, standard deviation, skewness, kurtosis  
- **Quartiles & Outliers**: Q1, Q3, IQR, whiskers, outlier count  
- **Empirical Rule**: 68-95-99.7 rule check  
- **Normality Test**: Shapiro-Wilk test  
- **Confidence Intervals**: 95%, 97%, 99%  
- **Visualizations**: Histogram, Boxplot, Countplot, Pie chart (auto-detect discrete vs continuous data)  
- **`everything()`** method: Runs all statistics and visualizations at once  

---

##  Installation
Clone the repository:
```bash
git clone https://github.com/your-username/datastats-deep.git
cd datastats-deep

===========================================================================================================================
from datastats_deep import DataStats_Deep

# Example data
data = [3, 24, 31, 5, 3, 24, 30, 44, 13, 69, 24, 1, 30, 2]

# Create object
stats_obj = DataStats_Deep(data)

# Run everything
stats_obj.everything()

# Or call individual methods
stats_obj.average()
stats_obj.visualize()
=============================================================================================================================
Total Sum: 303
Total Count: 14
Maximum Value: 69
Minimum Value: 1
Range: 68
Mean: 21.64
Median: 24.0
Mode: 24
Variance: 346.78
Standard Deviation: 18.62
Skewness: 1.19
Kurtosis: 0.52
...
============================================================================================================================
 Convert into proper pip-installable package

 Add hypothesis testing (t-tests, chi-square, ANOVA)

 Support for DataFrames directly

 Add correlation and regression analysis
