from read_inv_index import get_inv_index
from kgram import Kgram
class Index:
    def __init__(self):
        self.inv_ind = get_inv_index()
        # pass inv_ind to kgram
        self.kgram = Kgram(self.inv_ind)