## Come back to the video when you have little better understanding with the Models

Data Science-Crash Course [video link](https://www.youtube.com/watch?v=XU5pw3QRYjQ)

Overview
- What is data science?
- Setup
- Linear Regression
- Logistic Regression
- LDA and QDA
- Resampling
- Regularization
- Decision trees
- Support Vector Machines
- Unsupervised learning

**What is data science?**
- A field that uses scientific methods to extract knowledge and insights from data

It comprise of all three below
- Machine learning scientist: develop algorithms
- Data Analyst: answers business quentions
- Data Engineer: build the software to gather data from different sources

**Linear Regression**
```python
reg = LinearRegression()
reg.fit(X, y)

intercept = reg.intercept_[0]
coef = reg.coef_[0][0]
```

Null hypothesis
```python
exog = sm.add_constant(X)
est = sm.OLS(y, exog).fit()

print(est.summary())
```

Multiple Linear Regression
```python
reg = LinearRegression()
reg.fit(X, y)

beta_0 = reg.intercept_[0]

beta_1 = reg.intercept_[0][0]
beta_2 = reg.intercept_[0][1]
beta_3 = reg.intercept_[0][2]
```

**Classification**
- Simple classifiction: binary classification eg. spam or not spam
- Classify in more than 2 classes eg. eye color(blue, green, brown)

Regression vs Classification
- Regression: response variable is quantitative
- Classification: response variable is categorical or qualitative

**Logistic Regression**

Probability
- Determine the probability of an observation to be aprt of a class or not
- Output between 0 and 1 (1 meas very likely)

Sigmoid fucntion

LDA in Python
```python
lda = LinearDiscriminantAnalysis()

lda.fit(X_train, y_train.rabel())

y_prob_lda = lda.predict_proba(X_test)[:,1]
y_pred_lda = np.where(y_prob_lda>0.5, 1, 0)
```

