class TinySuffixArray():

    def __init__(self):
        self.suffixes = []
        self.positions = []

    def index(self, text):
        self.positions = [5, 3, 1, 0, 4, 2]

    def _get_suffixes_of(self, text):
        for i in range(len(text)):
            self.suffixes.append(text[i:])
            self.positions.append(i)

    def _sort_suffixes_between(self, i, j):
        p_suffix = self.suffixes[i]  # pivot suffix
        p_position = self.positions[i]  # pivot position
        l_suffixes = []  # left suffixes
        r_suffixes = []  # right suffixes
        l_positions = []  # left positions
        r_positions = []  # right positions
        for x in range(i + 1, j + 1):
            if self.suffixes[x] <= p_suffix:
                l_suffixes.append(self.suffixes[x])
                l_positions.append(self.positions[x])
            else:
                r_suffixes.append(self.suffixes[x])
                r_positions.append(self.positions[x])
        self.suffixes[i:j+1] = l_suffixes + [p_suffix] + r_suffixes
        self.positions[i:j+1] = l_positions + [p_position] + r_positions
        if len(l_suffixes) > 1:
            self._sort_suffixes_between(i, len(l_suffixes) - 1)
        if len(r_suffixes) > 1:
            self._sort_suffixes_between(len(l_suffixes) + 1, j)