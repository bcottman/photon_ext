tree = PipelineElement('DecisionTreeClassifier',
                       hyperparameters={'criterion': ['gini'],
                                         'min_samples_split': IntegerRange(2, 4)})

svc = PipelineElement('LinearSVC',
                      hyperparameters={'C': FloatRange(0.5, 25)})


my_pipe += Stack('final_stack', [tree, svc], use_probabilities=True)

my_pipe += PipelineElement('LinearSVC')
my_pipe.fit(X, y)