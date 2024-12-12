from ldc import LiverDiseaseTools

path = './data/HepatitisCdata.csv'

data_set = LiverDiseaseTools.load(
    data_set_path=path,
    target_column='Category',
    columns_to_drop=None
)

trained_model = data_set.train_model(tag_of_model=6)

print(trained_model.metrics())

# data without the category, sex and crea
feed_data = [32,"m",42.2,41.9,35.8,31.1,16.1,5.82,4.6,109,21.5,67.1]

result = trained_model.predict(input_list=feed_data)

print(result)

print('Done')