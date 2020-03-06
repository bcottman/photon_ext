registry = PhotonRegistry(custom_elements_folder=custom_elements_folder)
registry.register(
    photon_name="MyCustomEstimator",
    class_str="custom_estimator.CustomEstimator",
    element_type="Estimator",
)

registry.register(
    photon_name="MyCustomTransformer",
    class_str="custom_transformer.CustomTransformer",
    element_type="Transformer",
)

registry.activate()

registry.list_available_elements()

registry.info("MyCustomEstimator")
registry.info("MyCustomTransformer")