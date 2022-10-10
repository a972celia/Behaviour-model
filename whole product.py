import numpy as np
import pandas as pd
import datetime as dt
import os


class Product:
    def __init__(self,file_name):
        print("product in initiated")
        print(self.name)
        self.read_file(file_name)
        self.transform()

    def read_file(self,file_name):  # read the dataset
        print("file is read from Product class with file name = {}".format(file_name))
        path = "/Users/Desktop/test/.."
        filename = 'filename'
        df = read.csv(os.path.join(path, filename))
        return df

    def transform(self):  #prepossess 
        print("transform is called from Product class")
        df['MATURDAT'] = df['MATURDAT'].dt.time
        df['OPENDATE'] =  df['OPENDATE'].dt.time
        df['VALUEDAT'] = df['VALUEDAT'].dt.time

        return df

#Real time deposit
class TermDeposit(Product):
    def __init__(self,file_name):
        super().__init__(file_name=file_name)
        self.data = df

    def get_tenor():
        '''
        MATURDAT:Contractual maturity date of the instrument
        VALUEDAT:The date when the instrument is last renewed/rollovered
        TENOR_CAT:The difference between VALUEDAT and MATURDAT
        '''
        # The contractual tenor is obtained by calculating the difference between VALUEDAT and MATURDAT
        self.data['TENOR_CAT'] = self.data['MATURDAT'] - self.data['VALUEDAT']

        one_month_tenor = self.data.TENOR_CAT.isin(range(0,30)) 
        two_months_tenor = self.data.TENOR_CAT.isin.(range(30,60))
        three_months_tenor = self.data.TENOR_CAT.isin(range(60,120))
        six_months_tenor = self.data.TENOR_CAT.isin(range(120,240))
        twelve_months_tenor = self.data.TENOR_CAT.isin(range(240,365))
        
        self.data.loc[one_month_tenor,'TENOR'] = '1M'
        self.data.loc[two_months_tenor,'TENOR'] = '2M'
        self.data.loc[htree_months_tenor,'TENOR'] = '3M'
        self.data.loc[six_months_tenor,'TENOR'] = '6M'
        self.data.loc[twelve_months_tenor,'TENOR'] = '12M'

        return self.data.TENOR

    # convert currency HKD, USD, CNH, and AUD into number
    def currency_to_index(self):     
        '''
        CURRSMBL: Currency of the instrument
        '''
        LIST_CURRSMBL = ['HKD','USD','CNH','AUD','ALL']
        
        currency_list = []
        for index,row in self.data.iterrows():
            for i, cur in enumerate (LIST_CURRSMBL):
                if row['CURRSMBL'] = cur :
                        currency= i
            currency_list.append(currency)            
                else:
                    pass 
        self.data.['CURRENCY'] = currency_list
        
        return self.data.CURRENCY 

    # Once all sample deposits are categorized into the two behaviors 
    # the aggregate balance and the number of accounts of each group is then calculated.
    def check_behavior(self):
        '''
        ANCO:The unique ID number of a customer's particular term deposit account/instrument
        MATURDAT:Contractual maturity date of the instrument
        BATCH_DATE:The date when the records are observed and recorded
        VALUEDAT:The date when the instrument is last renewed/rollovered
        '''
        ObservDate_end = max(self.data['BATCH_DATE'])  
        ObservDate_start = min(self.data['BATCH_DATE']) 
        
        behavior_list = []
        account_list = list(set(self.data['ACNO']))

        for acc in account_list: #by each account 
            temp_df = self.data[self.data['ACNO']== acc]
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
                    
            temp_df = []
            behavior_list.append(behavior)
        self.data.BEHAVIOR = behavior_list
        return self.data.BEHAVIOR


    # Estimation of the early withdrawal rate
    def get_ew_rate (self):
        '''
        PRIN: The outstanding balance of a term deposit account/instrument as of record date
        '''
        self.data.EW_FLAG = np.where(self.data.BEHAVIOR =='EW',1,0) # mark the early withdrawal flag
        
        #Groupby and Aggregate
        grouped_multiple_df = self.data.groupby[['CURRENCY','TENOR','EW_FLAG']].agg({'PRIN':sum})['outstanding_bal']
        grouped_multiple_df = grouped_multiple_df.reset_index()
        
        ew_rate_list = []
        for index, row in grouped_multiple_df.iterrows():
    
            ew_rate = row['EW_FLAG'] * row['outstanding_bal'] / row['outstanding_bal']
            ew_rate_list.append(ew_rate)

        grouped_multiple_df['EW_RATE'] = ew_rate_list
        
        return grouped_multiple_df

    def main():

        df['TENOR'] = get_tenor(df)
        df['CURRENCY'] = currency_to_index(df)
        df['BEHAVIOR'] = check_behavior(df)

        # get retail segment
        df_retail = df[df['TYPE']=='Retail']

        output = get_ew_rate(df_retail)
        final_output = output[['CURRENCY','TENOR','EW_RATE']]

        return final_output

    


class Mortgage(Product):
    def __init__(self,file_name):
        super().__init__(file_name = file_name)


td = TermDeposit(file_name="td.csv")






