from abstraction.ITrainModel import ITrainModel


class ModelC(ITrainModel):
    def init(self, parameters_url):
        print("Initializing Model C with parameters:", parameters_url)

    def train(self, continue_training):
        print("Training Model C, continue:", continue_training)

    def evaluate(self, song):
        print("Evaluating song using Model C:", song)
