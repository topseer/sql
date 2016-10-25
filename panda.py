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
iris_data.loc[iris_data['class'] == 'Iris-setosa', 'sepal_width_cm'].hist()
