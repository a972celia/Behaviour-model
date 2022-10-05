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

## Liquidity behavioralization
Liquidity behavioralization needs to be applied to reflect the assessment of the expected period to
have access to liabilities under severe liquidity stress scenarios, and the expected period to fund
assets. Behavioralization is applied when the contractual terms do not reflect the expected
behavior of market participants and customer under stress scenario.


- Term deposit : For unpledged term deposit with specific contractual tenor, the early withdrawn amount in the
horizon of stress scenario or BAU scenario equals to the contractual cash outflow. The early withdrawal for this
rollover amount will consider independent of the previous rollover event (if any). The rollover amount,
which is the outstanding balance of the deposit in dollar amount that has rolled over, will
be subject to the consideration for early withdrawal until the rollover amount has been reduced to 10% of the 
original outstanding balance. 
 - Loan: For unvalued call loan from banks, it is assumed that the Bank would like to receive the principal
and repay the principal amount with interest,  subject to certain haircut,according to the value date and 
maturity date respectively. For market-wide scenario, a few counterparty banks shall be partially performing and 
the inflow amount shall be subject to a haircut as it is assumed that a portion of call loan will not be able to be
placed at value date as a few counterparties do not have sufficient liquidity to honor their obligation.


## Data Science Pipeline
The contributing model consists of the following process:
- Data preprocessing with NumPy and Pandas
- Model implementation
    - Oversample data with SMOTE
    - Predict with logistic regression model
    - Address imbalance problems with K-fold Cross-Validation

## License
Copyright (c) [2022] [Fang-Yi Kuo]


