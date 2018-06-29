import turicreate as tc

# 1. Load the data
data = tc.SFrame('instruments.sframe')

# 2. Split to train and test data
train_data, test_data = data.random_split(0.8)

# 3. Create model
model = tc.image_classifier.create(train_data, target='instrument_name')

# 4. Predictions
predictions = model.predict(test_data)

# 5.  Evaluate the model and save the results into a dictionary
results = model.evaluate(test_data)
print("Accuracy         : %s" % results['accuracy'])
print("Confusion Matrix : \n%s" % results['confusion_matrix'])

# 6. Save the model
model.save('instruments.model')

# 7. Export to CoreML format
model.export_coreml('model/instruments.mlmodel')