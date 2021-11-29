import numpy as np


def find_max_min_on_date(provinces, dates: np.ndarray, data: np.ndarray, date):
    # ไม่อนุญาตให้ใช้คำสั่ง for, while, comprehension, map, reduce, recursive, itertools ในการคำนวณ 
    return {
        'max': [*provinces[np.where(data[:, [np.where(dates==date)[0][0]]]==np.amax(data[:, [np.where(dates==date)[0][0]]], axis=0))[0]]],
        'min': [*provinces[np.where(data[:, [np.where(dates==date)[0][0]]]==np.amin(data[:, [np.where(dates==date)[0][0]]], axis=0))[0]]]
    }
    
def find_max_min_in_province(provinces,dates,data,province):
  # ไม่อนุญาตให้ใช้คำสั่ง for, while, comprehension, map, reduce, recursive, itertools ในการคำนวณ 
    return {
        'max': [*dates[np.where(data[np.where(provinces==province)[0][0]]==np.amax(data[np.where(provinces==province)[0][0]]))]],
        'min': [*dates[np.where(data[np.where(provinces==province)[0][0]]==np.amin(data[np.where(provinces==province)[0][0]]))]]
    }
                             
# def find_average_growth(provinces,data,n):
#   # ไม่อนุญาตให้ใช้คำสั่ง for, while, comprehension, map, reduce, recursive, itertools ในการคำนวณ 
#   # อนุญาตให้ใช้คำสั่ง for เฉพาะใน list comprehension ในบรรทัด return เท่านั้น   
#     pass

# def normalize(data):
#   # ไม่อนุญาตให้ใช้คำสั่ง for, while, comprehension, map, reduce, recursive, itertools ในการคำนวณ 
#     pass


