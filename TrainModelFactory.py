import inspect
import importlib
import pkgutil

from abstraction.ITrainModel import ITrainModel


class TrainModelFactory:
    def __init__(self):
        self.registered_models = {}

    def register_model(self, name, model_class):
        self.registered_models[name] = model_class

    def create_model(self, name):
        model_class = self.registered_models.get(name)
        if model_class:
            return model_class()
        else:
            raise ValueError("Model not found: " + name)


    def register_models_from_module(self, module_name):
        module_prefix = module_name + "."
        module_path = module_name
        for loader, name, is_pkg in pkgutil.iter_modules():
            if name == module_name:
                module_path = loader.path
                break

        if module_path:
            for loader, name, is_pkg in pkgutil.iter_modules([module_path]):
                full_module_name = module_prefix + name
                module = importlib.import_module(full_module_name)
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if inspect.isclass(attr) and issubclass(attr, ITrainModel) and attr != ITrainModel:
                        self.register_model(attr_name, attr)
        else:
            raise ValueError("Module not found: " + module_name)

    def print_registered_modules(self):
        print("Registered modules:")
        for name in self.registered_models:
            print(name)