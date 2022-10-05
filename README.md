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
funds transfer pricing. Effective behavioral models with good predictive ability allow banks to avoid
both unexpected losses and liquidity gaps and the cost of holding unnecessarily large liquidity
buffers and capital reserves. 

## Data Science Pipeline
The contributing model consists of the following process:
- Data preprocessing with NumPy and Pandas
- Model implementation
    - Oversample data with SMOTE
    - Predict with logistic regression
    - Address imbalance problems with K-fold Cross-Validation

## License
Copyright (c) [2022] [Fang-Yi Kuo]


