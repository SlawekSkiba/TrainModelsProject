from abstraction.ITrainModel import ITrainModel


class ModelB(ITrainModel):
    def init(self, parameters_url):
        print("Initializing Model B with parameters:", parameters_url)

    def train(self, continue_training):
        print("Training Model B, continue:", continue_training)

    def evaluate(self, song):
        print("Evaluating song using Model B:", song)

