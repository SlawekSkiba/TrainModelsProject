from TrainModelFactory import TrainModelFactory
from TrainModels.TrainModelA import ModelA
from TrainModels.TrainModelB import ModelB
from TrainModels.TrainModelC import ModelC


def test_train_model_factory():
    factory = TrainModelFactory()

    # Register models
    factory.register_model("ModelA", ModelA)
    factory.register_model("ModelB", ModelB)
    factory.register_model("ModelC", ModelC)

    # Test ModelA
    model_name = "ModelA"
    model = factory.create_model(model_name)
    assert isinstance(model, ModelA)
    model.init("parameters_url")
    model.train(True)
    model.evaluate("song")

    # Test ModelB
    model_name = "ModelB"
    model = factory.create_model(model_name)
    assert isinstance(model, ModelB)
    model.init("parameters_url")
    model.train(False)
    model.evaluate("song")

    # Test ModelC
    model_name = "ModelC"
    model = factory.create_model(model_name)
    assert isinstance(model, ModelC)
    model.init("parameters_url")
    model.train(True)
    model.evaluate("song")

    # Test non-existent model
    model_name = "ModelD"
    try:
        model = factory.create_model(model_name)
    except ValueError as e:
        assert str(e) == "Model not found: ModelD"
    else:
        assert False, "Expected ValueError for non-existent model"


# Run the tests
test_train_model_factory()