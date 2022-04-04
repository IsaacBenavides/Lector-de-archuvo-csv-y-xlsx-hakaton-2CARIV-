import csv
import openpyxl
import pandas as pd
import datetime


class Utils:
    def read_csv(path):
        data = []
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

    def read_excel(path):
        df = pd.read_excel(io=path)
        return df

    def month_to_number(month):
        dict_month = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12,
        }
        return dict_month[month.lower()]

    def formate_date(date):
        try:
            if(type(date) == datetime.datetime):
                date_formated = date
            else:
                ds = date.split("/")
                date_formated = datetime.datetime(
                    int(ds[2]), int(ds[0]), int(ds[1]))
        except:
            date_formated = datetime.datetime.now()
        return date_formated
