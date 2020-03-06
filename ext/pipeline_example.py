my_pipe = Hyperpipe('name_of_pipe',
                    ...)
my_pipe.add(PipelineElement('pre-processer_transformer_name'))
my_pipe += PipelineElement('estimator_name',
                           hyperparameters={'hp_1':
                                             ...})
my_pipe.fit(X, y)