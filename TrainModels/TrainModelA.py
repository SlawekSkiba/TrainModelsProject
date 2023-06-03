from abstraction.ITrainModel import ITrainModel


class ModelA(ITrainModel):
    def init(self, parameters_url):
        print("Initializing Model A with parameters:", parameters_url)

    def train(self, continue_training):
        print("Training Model A, continue:", continue_training)

    def evaluate(self, song):
        print("Evaluating song using Model A:", song)

