import numpy as np


class RepeatDataset(object):

    def __init__(self, dataset, times):
        self.dataset = dataset
        self.times = times
        if hasattr(self.dataset, 'flag'):
            self.flag = np.tile(self.dataset.flag, times)
        self._original_length = len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx % self._original_length]

    def __len__(self):
        return self.times * self._original_length
