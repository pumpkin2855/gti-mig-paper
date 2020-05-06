#/usr/bin/env python
# -*- coding: utf-8 -*-

from pytrends.request import TrendReq
import csv
import time
import pandas as pd

"""
Return in a DataFrame the GTI of certains keywords
    - kw_list : list of MAXIMUM 5 keywords 
    - country : the country in which we extract the GTI
    - time_frame : the requested span of time for the keywords (see https://github.com/GeneralMills/pytrends 
    for more informations)
    - index : the list of dates (thus the index of the DataFrame) in case of no returned value by Google
"""
def getDataKeyword(kw_list,country,time_frame,index):
    pytrend.build_payload(kw_list, cat=0, timeframe=time_frame, geo=country, gprop='')
    data = pytrend.interest_over_time()
    if len(data.columns)<len(kw_list)+1:
        if len(data.columns) == 0:
            return pd.DataFrame(data=[[0]*len(kw_list)]*len(index),index=index,columns=kw_list)
        print('no returned gti for keywords : ' + str(set(kw_list).symmetric_difference(set(data.columns[:-1]))))
    return data.loc[:,data.columns[:-1]]

'''
This function returns in a DataFrame (and write it in a csv) the unilateral GTI (i.e. "migration keyword" OR "name of the 
destination country")of a country for a specified span of time. The values of the DataFrame are the GTI, the index
are the dates and the columns are the keywords.
    - csv_write_file_name : the name of the csv file to write the GTI
    - country : the ISO code for the country in which we extract the GTI
    - file_keywords : the csv file containing the keywords/names of the destination countries in the different languages
    - time_frame : the requested span of time for the keywords (see https://github.com/GeneralMills/pytrends 
    for more informations), 'today 3-m' = the 3 past months
'''
def get_all_uniGTI(csv_write_file_name,country,file_keywords,language,time_frame='today 3-m',dialect=csv.excel, **kwargs):
    index_language = ['English','French','Spanish'].index(language)
    csv_reader = csv.reader(open(file_keywords, encoding='utf-8'), dialect=dialect, **kwargs)
    next(csv_reader)
    pytrend.build_payload([language], cat=0, timeframe=time_frame, geo=country, gprop='')
    df = pytrend.interest_over_time()
    del df[language]
    del df['isPartial']
    kw_list = []
    for line in csv_reader:
        kw = line[index_language]
        kw_list.append(kw.replace(',',' +'))
        if len(kw_list) == 5:
            data = getDataKeyword(kw_list,country,time_frame,df.index)
            kw_list = []
            df = df.join(data)
    if len(kw_list) > 0:
        data = getDataKeyword(kw_list, country, time_frame,df.index)
        df = df.join(data)
    df.to_csv(csv_write_file_name)
    return df


'''
This function returns in a DataFrame (and write it in a csv) the bilateral GTI (i.e. "migration keyword + name of the 
destination country")of a country for a specified span of time. The values of the DataFrame are the GTI, the index
are the dates and the columns are the complete keywords.
    - csv_write_file_name : the name of the csv file to write the GTI
    - country : the ISO code for the country in which we extract the GTI
    - file_keywords : the csv file containing the keywords in the different languages
    - file_destination-countries : the csv file containing the names of the destination countries in the different languages
    - time_frame : the requested span of time for the keywords (see https://github.com/GeneralMills/pytrends 
    for more informations), 'today 3-m' = the 3 past months
'''
def get_all_biGTI(csv_write_file_name,country,file_keywords,file_destination_countries,language,time_frame='today 3-m',dialect=csv.excel, **kwargs):
    index_language = ['English','French','Spanish'].index(language)
    f_kw = open(file_keywords, encoding='utf-8')
    csv_reader_kw = csv.reader(f_kw, dialect=dialect, **kwargs)
    csv_reader_dest = csv.reader(open(file_destination_countries, encoding='utf-8'), dialect=dialect, **kwargs)
    next(csv_reader_dest)
    pytrend.build_payload([language], cat=0, timeframe=time_frame, geo=country, gprop='')
    df = pytrend.interest_over_time()
    del df[language]
    del df['isPartial']
    kw_list = []
    for dests in csv_reader_dest:
        dest = dests[index_language].split(',')[0]
        f_kw.seek(0)
        next(csv_reader_kw)
        for line in csv_reader_kw:
            kw = line[index_language] + ' ' + dest
            kw_list.append(kw.replace(',', ' '+dest+' +'))
            if len(kw_list) == 5:
                data = getDataKeyword(kw_list, country, time_frame,df.index)
                kw_list = []
                df = df.join(data)
        # Sleep to avoid the Google Trends limit of requests
        print("GTI done for ", dest, " sleep 30 seconds for next")
        time.sleep(30)
    if len(kw_list) > 0:
        data = getDataKeyword(kw_list, country, time_frame,df.index)
        df = df.join(data)
    df.to_csv(csv_write_file_name)
    return df


# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(hl='en-US', tz=360)

# Examples of uses :
# df = get_all_uniGTI('data/countryGTI_Venezuela.csv','VE','data/destination_countries.csv','Spanish')
# df = get_all_biGTI('data/biGTI_Venezuela.csv','VE','data/keywords.csv','data/destination_countries.csv','Spanish')
