#%%return unique values
iris_data.unique()

#%%updateData
iris_data.loc[iris_data['class'] == 'versicolor', 'class'] = 'Iris-versicolor'

#so that pandas knows to treat rows with 'NA' as missing values.
iris_data = pd.read_csv('iris.csv', na_values=['NA'])

#summary 
iris_data.describe()

#drop rows by condition
iris_data = iris_data.loc[(iris_data['class'] != 'Iris-setosa') | (iris_data['sepal_width_cm'] >= 2.5)]


#hist graph
iris_data.loc[iris_data['class'] == 'Iris-setosa', 'sepal_width_cm'].hist()

#new way to assign value
iris_data.loc[(iris_data['class'] == 'Iris-versicolor') &
              (iris_data['sepal_length_cm'] < 1.0),
              'sepal_length_cm'] *= 100.0

#to and from csv
iris_data.to_csv('iris-data-clean.csv', index=False)
iris_data_clean = pd.read_csv('iris-data-clean.csv')               

#assert 
#We can quickly test our data using assert statements: 
#We assert that something must be true, 
#if it is, then nothing happens and the notebook continues running. 
#if our assertion is wrong, then the notebook stops running and brings it to our attention. For example:
assert 1 == 2
