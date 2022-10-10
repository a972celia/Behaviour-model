# Behavior model for mortgages



loan_df 

# Calculate the contractual tenor in the unit of year
def get_tenor(df):
    '''
    LN_AGE :The number of years passed since the origination of the mortgage
    TIME_TO_MAT : The number of years remaining for the mortgage loan
    TENOR_M: # The contractual tenor in the unit of year and convert the unit to month
    '''
    df.TENOR = df.LN_AGE + df.TIME_TO_MAT
    df.TENOR_M = round((df.TENOR))*12,0)


    return df.Tenor_M

def behavior_tenor():
    pass


def prepossess(): # Remove the accounts that only have 1 or 2 data rows
    pass


# Calculate the prepayment amount
def get_prepayment():
   
    '''
    MAJOR_CINO : Account number
    PREPAY_AMT :  prepayment amount
    BAL_LCE : Local Currency Equivalent Outstanding Balance of the Loan The outstanding balance of 
            the mortgage loan in local currency
    INST_AMT: The scheduled payment for the mortgage loan
    BATCH_DATE:Record Date The date when the records are observed and recorded
    MAT_DATE:Date of the Loan the date of maturity for the mortgage loan
    '''
    latest_observation = max(df.BATCH_DATE)
    
    account_number = list(set(df.BANK_NO))
    for acc in account_number:
        temp_df = df[df['MAJOR_CINO']== acc]
        for i ,(index, row) in enumerate(tem_df.iterrows()) : #enumerate into each acc
            if i == len(tem_df)-1:    # if it belongs to the last tranction of that account
                if row['BATCH_DATE'] == latest_observation: 
                    if row['BAL_LCE'] != 0:
                        df.loc[index,'PREPAY_AMT'] = np.nan
                    elif (row['MAT_DATE']-row['BATCH_DATE']) > 0:
                        df.loc[index,'PREPAY_AMT'] = max((df.loc[index,'BAL_LCE']- df.loc[index-1,'BAL_LCE'])*(-1) - df.loc[index,'INST_AMT'],0)
                    else:
                        df.loc[index,'PREPAY_AMT'] == 0
                else : 
                    if row['BAL_LCE'] != 0:
                        df.loc[index,'PREPAY_AMT'] = df.loc[index-1,'BAL_LCE']
                    elif row['MAT_DATE']- row['BATCH_DATE'] <= 0 :
                        df.loc[index,'PREPAY_AMT'] == 0
                    else:
                        df.loc[index,'PREPAY_AMT'] = max((df.loc[index,'BAL_LCE']- df.loc[index-1,'BAL_LCE'])*(-1) - df.loc[index,'INST_AMT'],0)

            else:    
                if row == 1:
                    pass
                elif :
                    df.loc[index,'PREPAY_AMT'] = max((df.loc[index,'BAL_LCE']- df.loc[index-1,'BAL_LCE'])*(-1) - df.loc[index,'INST_AMT'],0)
        temp_df = []
        
    
    
    return df.PREPAY_AMT

# Calculate the PREPAY_RATE trade by trade
def get_prepay_rate():

    prepay_ratio_list = []
    account_number = list(set(df.BANK_NO))
    for acc in account_number:
        temp_df = df[df['MAJOR_CINO']== acc]
        #for index, row in temp_df.iloc[1:].iterrows():
        for index, row in temp_df.iterrows():
            if row == 0 :
                continue
            PREPAY_RATIO = row['PREPAY_AMOUNT'] / (row-1)['BAL_LCE']
        temp_df = []
        prepay_ratio_list.append(PREPAY_RATIO)
    df.PREPAY_RATIO = prepay_ratio_list

    return df.PREPAY_RATIO



