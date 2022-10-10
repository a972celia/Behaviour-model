# Real time deposit 
import numpy as np
import pandas as pd
import datetime as dt
import os 


def __init__(self,data):
    self.datadata = data
    



# def tenor_to_timeslot(self):
#     # The contractual tenor is obtained by calculating the difference between VALUEDAT and MATURDAT

#     df['TENOR_CAT'] = df['MATURDAT'] - df['OPENDATE']
#     tenor_list = []
#     for index,row in df.iterrows():
#         if row['TENOR_CAT'] < 30 :
#             tenor = '1M'
#         elif row['TENOR_CAT'] >= 30 and row['TENOR_CAT'] < 60:
#             tenor = '2M'
#         elif row['TENOR_CAT'] >= 60 and row['TENOR_CAT'] < 120 :
#             tenor = '3M'
#         elif row['TENOR_CAT'] >= 120 and row['TENOR_CAT'] < 240:
#             tenor = '6M'
#         elif row['TENOR_CAT'] >= 240 and row['TENOR_CAT'] < 365:
#             tenor= '12M'
#         tenor_list.append(tenor)
#     df['TENOR'] = tenor_list  
#     return df['TENOR']

def get_tenor(self):
    '''
    MATURDAT:Contractual maturity date of the instrument
    VALUEDAT:The date when the instrument is last renewed/rollovered
    TENOR_CAT:The difference between VALUEDAT and MATURDAT
    '''
    # The contractual tenor is obtained by calculating the difference between VALUEDAT and MATURDAT
    df['TENOR_CAT'] = df['MATURDAT'] - df['VALUEDAT']

    one_month_tenor = df.TENOR_CAT.isin(range(0,30)) 
    two_months_tenor = df.TENOR_CAT.isin.(range(30,60))
    three_months_tenor = df.TENOR_CAT.isin(range(60,120))
    six_months_tenor = df.TENOR_CAT.isin(range(120,240))
    twelve_months_tenor = df.TENOR_CAT.isin(range(240,365))
    
    df.loc[one_month_tenor,'TENOR'] = '1M'
    df.loc[two_months_tenor,'TENOR'] = '2M'
    df.loc[htree_months_tenor,'TENOR'] = '3M'
    df.loc[six_months_tenor,'TENOR'] = '6M'
    df.loc[twelve_months_tenor,'TENOR'] = '12M'

    return df.TENOR

# convert currency HKD, USD, CNH, and AUD into number
def currency_to_index(df):     
    '''
    CURRSMBL: Currency of the instrument
    '''
    LIST_CURRSMBL = ['HKD','USD','CNH','AUD','ALL']
    
    
    currency_list = []
    for index,row in df.iterrows():
        for i, cur in enumerate (LIST_CURRSMBL):
            if row['CURRSMBL'] = cur :
                    currency= i
        currency_list.append(currency)            
            else:
                pass 
    df['CURRENCY'] = currency_list
    
    return df['CURRENCY'] 
    
      
# Once all sample deposits are categorized into the two behaviors 
# the aggregate balance and the number of accounts of each group is then calculated.
def check_behavior(df):
    '''
    ANCO:The unique ID number of a customer's particular term deposit account/instrument
    MATURDAT:Contractual maturity date of the instrument
    BATCH_DATE:The date when the records are observed and recorded
    VALUEDAT:The date when the instrument is last renewed/rollovered
    '''
    ObservDate_end = max(df.BATCH_DATE)  
    ObservDate_start = min(df.BATCH_DATE) 
    
    behavior_list = []
    account_list = list(set(df.ACNO))

    for acc in account_list: #by each account 
        temp_df = df[df['ACNO']== acc]
        for i ,(index, row) in enumerate(tem_df.iterrows()) :  #by each account's deposit 
            if  i == len(tem_df)-1:   # last traction of that deposit 
                if (row['BATCH_DATE'] != ObservDate_end): 
                    if (row['MATURDAT'] - row['BATCH_DATE']<=30): 
                    # "Withdrawal at maturity” if the account is closed or rolled over at the contractual maturity date.   
                            behavior = 'W'                               
                    else (row['MATURDAT'] - row['BATCH_DATE'] >30):
                    # “Early Withdrawal” if the account is closed before the contractual maturity date.
                            behavior = 'EW'  
            else:
                behavior = ''
                # else if !(is.nan(row['BATCH_DATE'])):
                #     if (row['MATURDAT']==row['VALUEDAT']):
                #         behavior = 'R'   #if not last tranction should be rollover
                # else if is.nan(row['BATCH_DATE']):
                #     behavior = 'NA'
        temp_df = []
        behavior_list.append(behavior)
    df.BEHAVIOR = behavior_list
    return df.BEHAVIOR


# Estimation of the early withdrawal rate
def get_ew_rate (df):
    '''
    PRIN: The outstanding balance of a term deposit account/instrument as of record date
    '''
    df['EW_FLAG'] = np.where(df['BEHAVIOR']=='EW',1,0) # mark the early withdrawal flag
    
    #Groupby and Aggregate
    grouped_multiple_df = df.groupby[['CURRENCY','TENOR','EW_FLAG']].agg({'PRIN':sum})['outstanding_bal']
    grouped_multiple_df = grouped_multiple_df.reset_index()
    
    ew_rate_list = []
    for index, row in grouped_multiple_df.iterrows():
 
        ew_rate = row['EW_FLAG'] * row['outstanding_bal'] / row['outstanding_bal']
        ew_rate_list.append(ew_rate)

    grouped_multiple_df.EW_RATE = ew_rate_list
    
    return grouped_multiple_df


def main():
    #excute the process
    path = "/Users/Desktop/test/.."
    filename = 'filename'
    df = read.csv(os.path.join(path, filename))  # read the dataset

    #prepossess 
    df['MATURDAT'] = df['MATURDAT'].dt.time
    df['OPENDATE'] =  df['OPENDATE'].dt.time
    df['VALUEDAT'] = df['VALUEDAT'].dt.time
    df['TENOR'] = get_tenor(df)
    df['CURRENCY'] = currency_to_index(df)
    df['BEHAVIOR'] = check_behavior(df)

    # get retail segment
    df_retail = df[df['TYPE']=='Retail']

    output = get_ew_rate(df_retail)
    final_output = output[['CURRENCY','TENOR','EW_RATE']]

    return final_output

 if __name__ == "__main__":
     main()

