import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

penguins = pd.read_csv('penguins_cleaned.csv')

df = penguins.copy()
target = 'species'
encode = ['sex', 'island']

# Applying Ordinal feature encoding

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}

def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# Separating features and target
X = df.drop('species', axis=1)
Y = df['species']

# Build random forest model
model = RandomForestClassifier()
model.fit(X, Y)

# Export model
pickle.dump(model, open('penguins_clf.pkl', 'wb'))
