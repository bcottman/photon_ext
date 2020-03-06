verbose, epochs, batch_size = 1, 10, 32
n_timesteps, n_features, n_outputs = X.shape[1], X.shape[2], 6
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps, n_features)))
model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
model.add(Dropout(0.5))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(n_outputs, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

my_pipe = Hyperpipe('cnn_keras_multiclass_pipe',
                    optimizer='grid_search',
                    optimizer_params={},
                    metrics=['accuracy'],
                    best_config_metric='accuracy',
                    outer_cv=KFold(n_splits=3),
                    inner_cv=KFold(n_splits=2),
                    verbosity=1,
                    output_settings=settings)

my_pipe += PipelineElement('KerasBaseClassifier',
                           hyperparameters={'epochs': Categorical([10, 20])},
                           verbosity=1,
                           model=model)

# NOW TRAIN YOUR PIPELINE
my_pipe.fit(X, y)