import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Step 1: Create Dataset
data = {
    'Age': ['Young','Young','Middle','Senior','Senior','Senior','Middle','Young',
            'Young','Senior','Young','Middle','Middle','Senior'],
    'Income': ['High','High','High','Medium','Low','Low','Low','Medium',
               'Low','Medium','Medium','Medium','High','Medium'],
    'Student': ['No','No','No','No','Yes','Yes','Yes','No',
                'Yes','Yes','Yes','No','Yes','No'],
    'Credit_Rating': ['Fair','Excellent','Fair','Fair','Fair','Excellent',
                      'Excellent','Fair','Fair','Fair','Excellent','Excellent',
                      'Fair','Excellent'],
    'Buys_Computer': ['No','No','Yes','Yes','Yes','No','Yes','No',
                      'Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

# Step 2: Encode Categorical Data
le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Step 3: Split Data
X = df.drop('Buys_Computer', axis=1)
y = df['Buys_Computer']

# Step 4: Train Decision Tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# Step 5: Classify New Sample
# Example: Age=Young, Income=Medium, Student=Yes, Credit=Fair
new_sample = [[1, 2, 1, 1]]
prediction = model.predict(new_sample)

print("Prediction (1=Yes, 0=No):", prediction)
