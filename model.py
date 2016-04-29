import pickle


class Model:
    def __init__(self, filepath):
        self.model = pickle.load(open(filepath, 'rb'), protocol=pickle.HIGHEST_PROTOCOL)

    def predict(self, array):
        return self.model.predict(array)
