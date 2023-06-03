# This is a sample Python script.
from Tests.TrainModelFactoryTests import test_train_model_factory
from TrainModelFactory import TrainModelFactory


def run_model(model_name):
    factory = TrainModelFactory()

    # Automatically register models from a module
    factory.register_models_from_module("TrainModels")
    factory.print_registered_modules()

    # Create and use models
    model = factory.create_model(model_name)
    model.init("parameters_url")
    model.train(True)
    model.evaluate("song")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_train_model_factory()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
