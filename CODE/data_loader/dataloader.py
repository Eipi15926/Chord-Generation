from data_loader.dataset import MidiDataset
# from dataset import MidiDataset
from torch.utils.data import DataLoader


class MidiDataLoader(DataLoader):
    def __init__(self, config):
        data_path = config['data_path']
        batch_size = config['batch_size']
        shuffle = config['shuffle']
        validation_split = config['validation_split']
        num_workers = config['num_workers']
        batch_len = config['batch_len']
        self.batch_len = batch_len
        dataset_config={'data_path': data_path, 'batch_len': batch_len, 'transform': None, 'target_transform': None, 'use_one_hot': False}
        midi_dataset = MidiDataset(dataset_config)
        self.validation_split = validation_split
        self.shuffle = shuffle

        self.batch_idx = 0

        self.init_kwargs = {
            'dataset': midi_dataset,
            'batch_size': batch_size,
            'shuffle': self.shuffle,
            'num_workers': num_workers,
            'drop_last': True
        }
        super(MidiDataLoader, self).__init__(**self.init_kwargs)


if __name__ == '__main__':
    config = {'data_path': 'output.pkl', 'batch_size': 2, 'batch_len': 32, 'shuffle': True, 'validation_split': 0.1, 'num_workers': 0}
    loader = MidiDataLoader(config)
    print(loader.batch_size)
    exit()
    for melody, chord in loader:
        print(melody)
        exit()