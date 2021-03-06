from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import KFold

from photonai.base import Hyperpipe, PipelineElement, Preprocessing, OutputSettings
from photonai.investigator import Investigator
from photonai.optimization import FloatRange, Categorical, IntegerRange


# WE USE THE BREAST CANCER SET FROM SKLEARN
X, y = load_breast_cancer(True)


my_pipe = Hyperpipe(
    "basic_svm_pipe",
    inner_cv=KFold(n_splits=5),
    outer_cv=KFold(n_splits=3),
    optimizer="sk_opt",
    optimizer_params={"n_configurations": 25},
    metrics=["accuracy", "precision", "recall", "balanced_accuracy"],
    best_config_metric="accuracy",
)

my_pipe.add(PipelineElement("StandardScaler"))

my_pipe += PipelineElement(
    "PCA", hyperparameters={"n_components": IntegerRange(10, 50)}, test_disabled=True
)

my_pipe += PipelineElement(
    "SVC",
    hyperparameters={"kernel": Categorical(["rbf", "linear"]), "C": FloatRange(1, 6)},
    gamma="scale",
)

my_pipe.fit(X, y)

Investigator.show(my_pipe)