from collections import defaultdict
import pickle
import time
import numpy as np

class StatsManager:
    def __init__(self, name="stats"):
        self.name = name
        self.map = defaultdict(list)
    
    def add(self, key, value):
        if value is not None:

            self.map[key].append(value)
    
    def get(self, key=None):
        if key == None:
            return self.map
        return self.map[key]
    
    def load(self, file_name):
        try:
            f = open(file_name, "rb")
            object = pickle.load(f)
            self.map = object
            self.name = file_name.split("-")[0]
            print("stats loaded successfully")
            return self
        except Exception as E:
            print(f"Error Loading File :{E}")
            raise E

    def save(self):
        try:
            save_name = self.name+"-"+"".join([str(i)+"-" for i in list(time.localtime())][:6])[:-1]+".pkl"
            f = open(save_name, "wb")
            pickle.dump(self.map, f)
            print("saved as: "+save_name)
            return save_name
        except Exception as E:
            print(f"Error saving stats: {E}")
            raise E
        
    def get_smoothed(self, key, window_size = 10):
        try:
            data = self.map[key]
            return [ np.mean(data[i:i+window_size])  for i,item in enumerate(data[:-window_size]) ]
        except Exception as E:
            print(f"Error while trying to get moving average : {E}")
