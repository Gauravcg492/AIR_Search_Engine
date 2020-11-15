from read_inv_index import get_index, is_file_exists, write_index
from kgram import Kgram
import json

class Index:
    def __init__(self, inv_ind_path, kgram_path):
        self.__inv_ind = get_index(inv_ind_path)
        # check is kgram index already exists
        if(is_file_exists(kgram_path)):
            kgram_ind = get_index(kgram_path)
            self.__kgram = Kgram(self.__inv_ind, kgram_ind)
        else:
            self.__kgram = Kgram(self.__inv_ind)
            write_index(kgram_path, self.__kgram.get_kgram_index())
    
    def get_inv_index(self):
        return self.__inv_ind
    
    def get_kgram_obj(self):
        return self.__kgram