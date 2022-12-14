# Behavioral cash flow projection model
## Executive summary
The overall goals of the Project are to enhance the existing liquidity risk
management framework to comply with the Sound Principles and Basel III global requirements and
to meet the Bank’s internal management requirements, especially in the following areas:

- Cash flow projection
Develop and implement cash flow projection methodologies, by taking into account estimated
cash flows due to both contractual terms and customer behaviors.
- Liquidity stress testing
Define liquidity stress scenarios and embed their impacts into the cash flow projection and
thereby propose early warning indicators (“EWI”) in the contingent funding plan (“CFP”).

## Objectives
A large percentage of most bank’s assets and liabilities are without a contractual maturity (e.g.
customer sight deposits or overdrafts) or contain embedded options. These products often form
the basis for majority of profit generation for certain business areas within banking organizations.
To estimate future repricing and rollover of on demand positions and the exercise of embedded
options, banks implement behavioral models.

Modeled cash flows serve as an important input for different aspects of a successful ALM and
balance sheet management, such as liquidity risk management, interest rate risk management and
funds transfer pricing. Effective behavioral models with good predictive ability allow banks to avoid both unexpected losses and liquidity gaps and the cost of holding unnecessarily large liquidity buffers and capital reserves. 

## Liquidity behavioralization
Liquidity behavioralization needs to be applied to reflect the assessment of the expected period to have access to liabilities under severe liquidity stress scenarios, and the expected period to fund assets. Behavioralization is applied when the contractual terms do not reflect the expected behavior of market participants and customer under stress scenario.


- Term deposit : For unpledged term deposit with specific contractual tenor, the early withdrawn amount in the horizon of stress scenario or BAU scenario equals to the contractual cash outflow. The early withdrawal for this rollover amount will consider independent of the previous rollover event (if any). The rollover amount, which is the outstanding balance of the deposit in dollar amount that has rolled over, will be subject to the consideration for early withdrawal until the rollover amount has been reduced to 10% of the original outstanding balance. 
 - Loan: For unvalued call loan from banks, it is assumed that the Bank would like to receive the principal and repay the principal amount with interest,according to the value date and maturity date respectively. A prepayment model estimates the level of early payoffs on a loan or group of loans in a set period of time given possible changes in interest rates.

## Data Preprocessing and Feature Engineering
1. Removed some of the features that have practically no impact of predicting if a burrower will pay back a loan.
2. Removed some null values that are very few in numbers(less than 0.5% of our data)
3. Created dummy variables for some data categories.
4. Did some Feature engineering on categorical data(loan_age,tenor).

## Model Building
### 1. Removing Correlated Features
The main issue of <b>RFE</b> is that it can be expensive to run — so you should do anything you can to reduce the number of features beforehand. Removing correlated features is a great way to do so because as you probably know, you don’t want highly correlated features in your dataset because they provide the same information — one is enough.

###  2. Initialise with Scaler
 It transforms the data in such a manner that it has mean as 0 and standard deviation as 1. In short, it standardizes the data. Standardization is useful for data which has negative values. It arranges the data in a standard normal distribution. It is more useful in classification than regression.

### 3. Oversample data with SMOTE
Oversampling is used when the quantity of data is insufficient. It tries to balance dataset by increasing the size of rare samples. Rather than getting rid of abundant samples, new rare samples are generated by using e.g. repetition, bootstrapping or SMOTE (Synthetic Minority Over-Sampling Technique) 

### 4. Predict with logistic regression
Logistic regression in one of the most common techniques to solve classiﬁcation problems. In our speciﬁc case, we are going to see whether a mortgage will prepay (Yi = 1) or not (Yi = 0) and $p=P(Y=1|X1,X2,…,Xt)$ is the probability of prepayment conditional on explanatory factors $X1,X2,…,Xt$.

## Evaluating Logistic Models 

The <b>Area Under Curve (AUC)</b> is the area under the ROC curve and serves as a single number performance summary of the classifier. AUC is often used as evaluation metric in imbalanced class problems, therefore it makes sense to directly optimize it in the training process.

<b>F1 Score</b> might be a better measure to use if we need to seek a balance between Precision and Recall AND there is an uneven class distribution (large number of Actual Negatives). F1 score reaches its best value at 1 (perfect precision and recall) and worst at 0.


## License
Copyright (c) [2022] [Fang-Yi Kuo]


