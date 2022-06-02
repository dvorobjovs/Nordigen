import pandas as pd
import random
from datetime import timedelta, datetime

num_of_transactions = 20

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta) 
    return start + timedelta(seconds=random_second)

def create_trans_dataset(num_of_transactions):
    merchants = ['Google','Ebay','Lidl','Amazon','Etsy','Tesco','Morrisons','AO','ASOS','H&M']
    description = ['office supplies','electronics','diy','clothing']
    output=[
            {"trans_description": random.choice(merchants) + '-' + random.choice(description),
             "trans_amount": round(random.randint(1, 1000) * random.random(), 2),
             "trans_date": ''
           }
            for x in range(num_of_transactions)
          ]
    return output

d1 = datetime.strptime('1/5/2022 00:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('30/5/2022 00:00:00', '%d/%m/%Y %H:%M:%S')
trans_dataset = pd.DataFrame(create_trans_dataset(20))
date_lst = [random_date(d1,d2) for t in range(num_of_transactions)]
date_lst.sort()                                                   #need to sort random dates
trans_dataset['trans_date'] = pd.Series(date_lst)
trans_dataset