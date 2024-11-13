# #10 --A) Classify the email using the binary classification method. --emails.csv



import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv("emails.csv")
df.drop(columns=['Email No.'], inplace=True, errors='ignore')

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.25, random_state=42)

svc = SVC(C=1.0, kernel='rbf', gamma='auto')
svc.fit(train_x, train_y)

y_pred = svc.predict(test_x)
print("Accuracy Score on test data:", accuracy_score(test_y, y_pred))

vectorizer = CountVectorizer(vocabulary=X.columns)

def predict_message(message):
    message_vector = vectorizer.transform([message.lower()])
    message_df = pd.DataFrame(message_vector.toarray(), columns=X.columns)
    prediction = svc.predict(message_df)
    if prediction[0] == 1:
        print("The message is classified as Spam.")
    else:
        print("The message is classified as Not Spam.")

new_message = "You are the lucky winner of our $5,000 cash giveaway! Just reply to claim your prize now."
predict_message(new_message)


