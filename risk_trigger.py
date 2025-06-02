import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv('loan_data.csv')

# Convert date columns to datetime
df['loan_disbursal_date'] = pd.to_datetime(df['loan_disbursal_date'])
df['loan_closure_date'] = pd.to_datetime(df['loan_closure_date'])

# Calculate Months on Book (MOB) and tenure (days)
df['mob_at_closure'] = ((df['loan_closure_date'] - df['loan_disbursal_date']) / pd.Timedelta(days=30)).astype(int)
df['tenure'] = (df['loan_closure_date'] - df['loan_disbursal_date']).dt.days

# Create label: 1 if early_closure, else 0
df['early_closure'] = df['closure_reason'].apply(lambda x: 1 if x == 'early_closure' else 0)

# Prepare features and labels
features = pd.get_dummies(df[['loan_type', 'branch_state', 'interest_rate', 'credit_score', 'ltv_ratio', 'mob_at_closure', 'tenure']], drop_first=True)
labels = df['early_closure']

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


