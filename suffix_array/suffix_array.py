class SuffixArray():

    def __init__(self):
        self.suffixes = []
        self.starting_positions = []

    def index(self, text):
        self.starting_positions = [5, 3, 1, 0, 4, 2]

    def _get_suffxies_of(self, text):
        for i in range(len(text)):
            self.suffixes.append(text[i:])

