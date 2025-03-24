# -*- coding: utf-8 -*-
"""Analysis_airlines_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10JQqhvDfol5ublmGoZeg12uKsS1nfy0M
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import dateutil
from scipy.stats import mode
import importlib

#Airlines dataset

#df = pd.read_csv("/content/drive/MyDrive/data/Asiana Airlines_Data.csv")
#df = pd.read_excel("/content/drive/MyDrive/data/Emirates_Airline_Data_Final.xlsx")
#df = pd.read_csv("/content/drive/MyDrive/data/Lufthansa Airlines_Data.csv")
df = pd.read_excel("/content/drive/MyDrive/data/Qatar_Airways_Data_Final.xlsx")
#df1 = pd.read_excel("/content/drive/MyDrive/data/IndiGo Airlines_Data_Final.xlsx")
#df = pd.read_excel("/content/drive/MyDrive/data/Vueling Airlines_Data_Final.xlsx")
df1 = pd.read_excel("/content/drive/MyDrive/data/Sun Country Airlines_Data_Final.xlsx")

#upsampeled and downsampled data
#df = pd.read_csv("/content/drive/MyDrive/data/downsampled_dataset.csv")   #Asiana airline
#df = pd.read_csv("/content/drive/MyDrive/data/upsampled_dataset.csv")

#df = pd.read_csv("/content/drive/MyDrive/data/Sampled_dataset/Lufthansa_downsampled_dataset.csv")
#df = pd.read_csv("/content/drive/MyDrive/data/Sampled_dataset/Lufthansa_upsampled_dataset.csv")
#df = pd.read_csv("/content/drive/MyDrive/data/Sampled_dataset/Qatar_downsampled_dataset.csv")
#df = pd.read_csv("/content/drive/MyDrive/data/Sampled_dataset/Qatar_upsampled_dataset.csv")
#df = pd.read_csv("/content/drive/MyDrive/data/Sampled_dataset/IndiGo_downsampled_dataset.csv")
#df = pd.read_csv("/content/drive/MyDrive/data/Sampled_dataset/IndiGo_upsampled_dataset.csv")

df.head()

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

df.shape

cols = df.columns.to_list()
print('Columns in the dataset:')
print(cols)

n_reviews = df.shape[0]
print('Number of customer reviews in the dataset: {:d}'.format(n_reviews))

df['Overall_rating'].unique()

df['Overall_rating'].describe()

unique_values = df['Recommended'].value_counts()
print(unique_values)

df['Recommended'] = df['Recommended'].map({'yes': True, 'no': False})

df.head(5)

df.describe()

columns_with_nan = ['Overall_rating', 'Seating_comfort','Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']

for col in columns_with_nan:
    mode_value = df[col].mode().iloc[0]
    print(f"Mode value for {col}: {mode_value}")

df.isnull().sum()



df1.head()

rating_counts = df1['Overall_rating'].value_counts().sort_index()

# Print the counts for each rating
for rating, count in rating_counts.items():
    print(f'Rating {rating}: {count} occurrences')

for col in columns_with_nan:
    mode_value = df1[col].mode().iloc[0]
    df1[col].fillna(mode_value, inplace=True)

df1.isnull().sum()

# df1['Recommended'] = df['Recommended'].map({'yes': True, 'no': False})

df1['Recommended'].head()

# df1['Recommended'] = df['Recommended'].map({'yes': 1, 'no': 0})

mapping = {'yes': 1, 'no': 0}
df1['Recommended'] = df1['Recommended'].map(mapping)

print(df1['Recommended'].unique())

rating_counts = df['Overall_rating'].value_counts().sort_index()

# Print the counts for each rating
for rating, count in rating_counts.items():
    print(f'Rating {rating}: {count} occurrences')

for col in columns_with_nan:
    mode_value = df[col].mode().iloc[0]
    df[col].fillna(mode_value, inplace=True)

df.isnull().sum()

rating_counts = df['Overall_rating'].value_counts().sort_index()

# Print the counts for each rating
for rating, count in rating_counts.items():
    print(f'Rating {rating}: {count} occurrences')

print(df)

df.columns[df.isnull().any()]

df['Overall_rating'].plot(kind='hist', bins=20)
plt.ylabel('Number of Ratings')
plt.xlabel('Overall Rating')
# plt.title('My Title');

#df3=pd.read_csv("/content/drive/MyDrive/data/oversampled_dataset.csv")
#df3

#df3['Overall_rating'].plot(kind='hist', bins=20)
#plt.ylabel('Number of Ratings')
#plt.xlabel('Overall Rating')
#plt.title('My Title');



#Linear Regression

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# Extract the independent variables (X) and the dependent variable (Y)
X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']]
Y = df['Overall_rating']

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, Y_train)

# Predict using the test data
Y_pred = model.predict(X_test)

# Calculate the Mean Squared Error and R-squared score
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

Y_pred

#test for unseen dataset

# Create the linear regression model and fit it on the training data
model = LinearRegression()
model.fit(X_train, Y_train)

# Extract the independent variables (X) and the dependent variable (Y) for df1
X_test_df1 = df1[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']]
Y_test_df1 = df1['Overall_rating']

# Use the pre-trained model to predict on the test data from df1
Y_pred_df1 = model.predict(X_test_df1)

# Evaluate the model's performance on df1
mse_df1 = mean_squared_error(Y_test_df1, Y_pred_df1)
r2_df1 = r2_score(Y_test_df1, Y_pred_df1)

print("Mean Squared Error on df1:", mse_df1)
print("R-squared on df1:", r2_df1)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Create the Random Forest regressor
rf_regressor = RandomForestRegressor(random_state=42)

# Fit the Random Forest model on the training data
rf_regressor.fit(X_train, Y_train)

# Use the Random Forest model to predict on the test data from df1
Y_pred_rf_df1 = rf_regressor.predict(X_test_df1)

# Evaluate the Random Forest model's performance on df1
mse_rf_df1 = mean_squared_error(Y_test_df1, Y_pred_rf_df1)
r2_rf_df1 = r2_score(Y_test_df1, Y_pred_rf_df1)

print("Performance of Random Forest Regressor on df1:")
print(f"Mean Squared Error: {mse_rf_df1}")
print(f"R-squared: {r2_rf_df1}")

import xgboost as xgb

# Create the XGBoost regressor
xgb_regressor = xgb.XGBRegressor(random_state=42)

# Fit the XGBoost model on the training data
xgb_regressor.fit(X_train, Y_train)

# Use the XGBoost model to predict on the test data from df1
Y_pred_xgb_df1 = xgb_regressor.predict(X_test_df1)

# Evaluate the XGBoost model's performance on df1
mse_xgb_df1 = mean_squared_error(Y_test_df1, Y_pred_xgb_df1)
r2_xgb_df1 = r2_score(Y_test_df1, Y_pred_xgb_df1)

print("Performance of XGBoost Regressor on df1:")
print(f"Mean Squared Error: {mse_xgb_df1}")
print(f"R-squared: {r2_xgb_df1}")



#Logistic Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print(df['Recommended'].unique())

df['Recommended'] = df['Recommended'].astype('int')
print(df['Recommended'].unique())

df['Recommended'].value_counts()

counts = df['Recommended'].value_counts()
plt.pie(counts, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Recommended')
plt.show()

# Extract the independent variables (X) and the dependent variable (Y)
X1 = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']]
Y1 = df['Recommended']

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train, X_test, Y_train, Y_test = train_test_split(X1, Y1, test_size=0.2, random_state=42)

Y1

# Create the logistic regression model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)
classification_rep = classification_report(Y_test, Y_pred)

print(f"Accuracy: {accuracy}")
print("\n")
print("Confusion Matrix:")
print(conf_matrix)
print("\n")
print("Classification Report:")
print(classification_rep)

#test for unseen dataset

# Extract the independent variables (X) and the dependent variable (Y) for df1
X_test_df1 = df1[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']]
Y_test_df1 = df1['Recommended']

# Use the pre-trained model to predict on the test data from df1
Y_pred_df1 = model.predict(X_test_df1)

# Evaluate the model's performance on df1
accuracy_df1 = accuracy_score(Y_test_df1, Y_pred_df1)
conf_matrix_df1 = confusion_matrix(Y_test_df1, Y_pred_df1)
classification_rep_df1 = classification_report(Y_test_df1, Y_pred_df1)

print(f"Accuracy: {accuracy_df1}")
print("Confusion Matrix:")
print(conf_matrix_df1)
print("Classification Report:")
print(classification_rep_df1)

from sklearn.ensemble import RandomForestClassifier

# Create the Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# Fit the Random Forest model on the training data
rf_model.fit(X_train, Y_train)

# Use the Random Forest model to predict on the test data from df1
Y_pred_rf_df1 = rf_model.predict(X_test_df1)

# Evaluate the Random Forest model's performance on df1
accuracy_rf_df1 = accuracy_score(Y_test_df1, Y_pred_rf_df1)
conf_matrix_rf_df1 = confusion_matrix(Y_test_df1, Y_pred_rf_df1)
classification_rep_rf_df1 = classification_report(Y_test_df1, Y_pred_rf_df1)

print("Performance of Random Forest on df1:")
print(f"Accuracy: {accuracy_rf_df1}")
print("Confusion Matrix:")
print(conf_matrix_rf_df1)
print("Classification Report:")
print(classification_rep_rf_df1)





from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from textblob import TextBlob
from wordcloud import WordCloud
from nltk.stem import WordNetLemmatizer
from string import digits
import requests
import pandas as pd
import nltk
import string
import seaborn as sns
import re
nltk.download("stopwords")
stop_words = set(stopwords.words('english'))
nltk.download('punkt')

df['Review'] = df['Review'].str.replace('[^\w\s]','')
print(df['Review'])

print(df.iloc[1,1])
df['Review'] = df.apply(lambda row: nltk.word_tokenize(row['Review']), axis=1)
print(df.iloc[0,1])

df['Review'] = df['Review'].apply(lambda x: ' '.join([word for word in x if word not in (stop_words)]))
print(df['Review'])

def polarity_calc(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None


def tag_cal(num):
    if num<0:
        return 'Negative'
    elif num>0:
        return 'Positive'
    else:
        return 'Neutral'


df['polarity'] = df['Review'].apply(polarity_calc)
df['tag'] = df['polarity'].apply(tag_cal)
print(df)

(df.groupby('tag').size()/df['tag'].count())*100

text = " "
for ind in df.index:
    if df['tag'][ind] == "Positive":
        text = text + df['Review'][ind]
wordcloud_positive = WordCloud().generate(text)
# Display the generated image:
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.axis("off")
plt.show()

text2= " "
for ind in df.index:
    if df['tag'][ind] == "Negative":
        text2 = text2 + df['Review'][ind]
wordcloud_negative = WordCloud().generate(text2)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.axis("off")
plt.show()

df['tag'].value_counts().plot(kind='bar')
sns.set(font_scale=1.4)
df['tag'].value_counts().plot(kind='bar', figsize=(7, 6), rot=0)
plt.xlabel("Sentiment", labelpad=14)
plt.ylabel("No of reviews", labelpad=14)
plt.title("Sentiment counts", y=1.02);

def sentiment_clean_text(text):
    if '|' in text:
        text = text.split('|')[1]
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Preprocessing function for emotion analysis
def emotion_clean_text(text):
    text = word_tokenize(text, "english")
    stop_words = set(stopwords.words('english'))

    text_list = [word for word in text if word not in stop_words]
    return text_list

# Apply sentiment_clean_text function to the 'Review' column
df['Cleaned_Sentiment_Review'] = df['Review'].apply(sentiment_clean_text)

# Apply emotion_clean_text function to the 'Review' column
df['Cleaned_Emotion_Review'] = df['Review'].apply(emotion_clean_text)

print(df.head())

def emotion_maping (file,di):

    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        di[word] = emotion

    return di

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# function to carry out the
def sentiment_analyze(text):

    scores = SentimentIntensityAnalyzer().polarity_scores(text) # return dictionary of scores

    if (scores['neg'] > scores['pos']):

        return 0

    else:
        return 1

# define needed data structures
cleaned_text = ""
temp_emotion_list = []
score = 0
emotion_dict = {}
words_score_dict = {}
moods_list_st = []
moods_list_tp = []

cols = df.columns.to_list()
print('Columns in the dataset:')
print(cols)

airline_main_categories = ['flight','service','seat','food','crew','time','good','class','cabin','seats','staff','business']
temp_category_list = []

#!pip install kaggle

#from google.colab import files
#files.upload()

# Read and process the emotions file
emotions_dict = {}
with open('/content/drive/MyDrive/data/emotion.txt', 'r') as emotions_file:
    for line in emotions_file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        emotions_dict[word] = emotion

# Print the emotions dictionary
print(emotions_dict)

# Remove leading spaces from emotion values
emotions_dict = {word: emotion.strip() for word, emotion in emotions_dict.items()}

print("Emotion Dictionary:", emotion_dict)

all_emotions = []

for i in range(len(df)):

    # get the review of index i
    text = str(df['Review'][i])

    # step 1: let's clean the text and assign cleaned list to dataFrame
    cleaned_text= sentiment_clean_text(text)

import nltk
nltk.download('vader_lexicon')

#Step 2: sentiment Analysis
score = sentiment_analyze(cleaned_text)
moods_list_st.append(score)

from collections import Counter

# Step 3: advanced clean for emotions
cleaned_text_list = emotion_clean_text(cleaned_text)
#df['Review'][i] = cleaned_text_list
df['Review'][i] = " ".join(cleaned_text_list)  # Join the list back into a string


# Step 4: emotion list builder
temp_emotion_list = []
for word in emotions_dict.keys():
    if word in cleaned_text_list:
        temp_emotion_list.append(emotions_dict[word])

all_emotions.extend(temp_emotion_list)  # Append emotions to the all_emotions list

# Create a Counter dictionary to count the frequencies of each emotion
emotion_summary = dict(Counter(all_emotions))

# Step 5: category list builder
for cat in airline_main_categories:
    if cat in cleaned_text_list:
        temp_category_list.append(cat)

for i in range(len(df)):
    # get the review of index i
  text = str(df['Review'][i])
    # Step 1: Clean the text for sentiment analysis
  cleaned_text = sentiment_clean_text(text)

    # Step 2: Sentiment Analysis
  score = sentiment_analyze(cleaned_text)
  moods_list_tp.append(score)

    # Step 3: Clean text for emotion analysis
  cleaned_text_list = emotion_clean_text(cleaned_text)
  df['Review'][i] = cleaned_text_list

    # Step 4: Build emotion list
for word in emotion_dict.keys():
    if word in cleaned_text_list:
        temp_emotion_list.append(emotion_dict[word])

    # Step 5: Build category list
for cat in airline_main_categories:
    if cat in cleaned_text_list:
        temp_category_list.append(cat)

print("Cleaned Text List:", cleaned_text_list)

df['mood'] = moods_list_tp

from collections import Counter

# Step 5: plot sentiment and emotions
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# get summary dictionary for sentiment
moods_list_all = moods_list_st + moods_list_tp
mood_summary = dict(Counter(moods_list_all))

# rename dictionary keys before ploting
mood_summary['positive'] = mood_summary.pop(1)
mood_summary['negative'] = mood_summary.pop(0)
fig, ax = plt.subplots()
#ax.bar(mmod_summary.keys(), mmod_summary.values())
ax.pie( mood_summary.values(), labels = mood_summary.keys(), autopct='%.6f%%')

# change the width and length of plot
fig.set_figwidth(5)
fig.set_figheight(5)

# label the plot
plt.xlabel('Sentiments')
plt.ylabel('Frequency')
#plt.savefig('Sentiments.png')
plt.show()

from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Create an empty list to store all emotions
all_emotions = []

for i in range(len(df)):
    text = str(df['Review'][i])
    cleaned_text = sentiment_clean_text(text)

    # Step 2: sentiment Analysis
    score = sentiment_analyze(cleaned_text)
    moods_list_tp.append(score)

    # Step 3: advanced clean for emotions
    cleaned_text_list = emotion_clean_text(cleaned_text)

    # Step 4: emotion list builder
    temp_emotion_list = []
    for word in emotions_dict.keys():
        if word in cleaned_text_list:
            temp_emotion_list.append(emotions_dict[word])

    all_emotions.extend(temp_emotion_list)  # Append emotions to the all_emotions list

# Create a Counter dictionary to count the frequencies of each emotion
emotion_summary = dict(Counter(all_emotions))

# Create a bar plot for emotions
fig, ax = plt.subplots()
ax.bar(emotion_summary.keys(), emotion_summary.values())

# Customize the plot if needed
fig.set_figwidth(10)
fig.set_figheight(5)
plt.xlabel('Emotions')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility

plt.show()



pip install NRCLex

from nrclex import NRCLex

# sentiments = []

# for review_list in df['Cleaned_Emotion_Review']:
#     for review_text in review_list:
#         nrc = NRCLex(review_text)
#         sentiment = nrc.affect_frequencies
#         sentiments.append(sentiment)

# # Convert the sentiments list to a DataFrame and concatenate it with the original DataFrame
# sentiments_df = pd.DataFrame(sentiments)
# result_df = pd.concat([df, sentiments_df], axis=1)
# #result_df.to_csv('result_dataset.csv', index=False)

df.head(3)

#result_df.head(15)

emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']
emotion_counts = {emotion: 0 for emotion in emotions}

for review_list in df['Review']:
#for review_list in df['Cleaned_Emotion_Review']:
#for review_list in df['Cleaned_Sentiment_Review']:

    for review_text in review_list:
        nrc = NRCLex(review_text)
        sentiment = nrc.affect_frequencies
        for emotion in emotions:
            if emotion in sentiment:
                emotion_counts[emotion] += sentiment[emotion]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(emotion_counts.keys(), emotion_counts.values())
plt.xlabel('Emotion')
plt.ylabel('Frequency')
plt.title('Emotion Distribution in Reviews')
plt.xticks(rotation=45)
plt.show()

for emotion in emotions:
    df[emotion] = 0

# Calculate and update emotion counts for each review
#for i, review_list in enumerate(df['Cleaned_Emotion_Review']):
for i, review_list in enumerate(df['Review']):
    for review_text in review_list:
        nrc = NRCLex(review_text)
        sentiment = nrc.affect_frequencies
        for emotion in emotions:
            if emotion in sentiment:
                df.at[i, emotion] += sentiment[emotion]

#df.to_csv("updated_dataset.csv", index=False)

df.head()



pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

sentiment_scores = []

for review_text in df['Cleaned_Sentiment_Review']:
    sentiment = analyzer.polarity_scores(review_text)
    sentiment_scores.append(sentiment)

# Convert the sentiment scores list to a DataFrame and concatenate it with the original DataFrame
sentiment_scores_df = pd.DataFrame(sentiment_scores)
result_df1 = pd.concat([df, sentiment_scores_df], axis=1)

result_df1.head()

plt.figure(figsize=(10, 6))
result_df1['compound'].hist(bins=20, alpha=0.7)
plt.xlabel('Sentiment Compound Score')
plt.ylabel('Frequency')
plt.title('Sentiment Score Distribution')
plt.show()

sentiment_categories = []

for review_text in df['Cleaned_Sentiment_Review']:
    sentiment = analyzer.polarity_scores(review_text)
    compound_score = sentiment['compound']

    if compound_score >= 0.05:
        sentiment_category = 'positive'
    elif compound_score <= -0.05:
        sentiment_category = 'negative'
    else:
        sentiment_category = 'neutral'

    sentiment_categories.append(sentiment_category)

# Add the sentiment categories to the DataFrame
df['Sentiment_Category'] = sentiment_categories

# Count the occurrences of each sentiment category
sentiment_counts = df['Sentiment_Category'].value_counts()

# Create a bar plot
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.xlabel('Sentiment Category')
plt.ylabel('Count')
plt.title('Sentiment Category Distribution')
plt.xticks(rotation=0)
plt.show()

df=result_df1

df.head(2)

# #   downsampling of sentiment analysed data
# from sklearn.utils import resample

# #   Count the occurrences of each sentiment category
# sentiment_counts = df['Sentiment_Category'].value_counts()

# #   Find the maximum count among the sentiment categories
# max_count = max(sentiment_counts)

# #   Oversample the minority class (negative or neutral reviews)
# oversampled_samples = []

# for sentiment in sentiment_counts.index:
#     samples = df[df['Sentiment_Category'] == sentiment]
#     oversampled_samples.append(resample(samples, n_samples=max_count, replace=True, random_state=42))

# oversampled_df = pd.concat(oversampled_samples, ignore_index=True)

# #   Shuffle the DataFrame
# oversampled_df = oversampled_df.sample(frac=1, random_state=42)

# #oversampled_df.to_csv('oversampled_dataset.csv', index=False)



#classification model for low rating(1-5) and high rating(6-10) classes

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Convert Overall_rating to binary classes
df['Rating_Class'] = df['Overall_rating'].apply(lambda x: 0 if x <= 5 else 1)

# Define features and target
#X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']]
X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']]
y = df['Rating_Class']
# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)
# Predict on the test set
y_pred = clf.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:\n", classification_rep)

df['Rating_Class']

df.head(1)



#Linear regression after adding emotions columns

# Extract the independent variables (X) and the dependent variable (Y)
#X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']]
X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']]
#X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money', 'neg', 'pos', 'neu']]
#X = df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust', 'neg', 'neu', 'pos']]
Y = df['Overall_rating']

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train1, Y_train1)

# Predict using the test data
Y_pred1 = model.predict(X_test1)
#Y_pred1

# Calculate the Mean Squared Error and R-squared score
mse = mean_squared_error(Y_test1, Y_pred1)
r2 = r2_score(Y_test1, Y_pred1)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Random forest regressor

from sklearn.ensemble import RandomForestRegressor

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Create and train the Random Forest Regressor
random_forest_regressor = RandomForestRegressor(random_state=42)
random_forest_regressor.fit(X_train, Y_train)

# Predict on the test set
Y_pred_rf_reg = random_forest_regressor.predict(X_test)

# Model evaluation
mse_rf_reg = mean_squared_error(Y_test, Y_pred_rf_reg)
r2_rf_reg = r2_score(Y_test, Y_pred_rf_reg)
print("Random Forest Regressor - Mean Squared Error:", mse_rf_reg)
print("Random Forest Regressor - R2 Score:", r2_rf_reg)

#count regression models - Poison & Negative binomial model

import statsmodels.api as sm
from sklearn.model_selection import train_test_split

# Create the Poisson regression model
poisson_model = sm.GLM(Y_train, sm.add_constant(X_train), family=sm.families.Poisson())
poisson_result = poisson_model.fit()

# Print Poisson regression summary
print("Poisson Regression Summary:")
print(poisson_result.summary())

# Negative Binomial regression model
neg_binomial_model = sm.GLM(Y_train, sm.add_constant(X_train), family=sm.families.NegativeBinomial())
neg_binomial_result = neg_binomial_model.fit()

# Print Negative Binomial regression summary
print("\nNegative Binomial Regression Summary:")
print(neg_binomial_result.summary())



#Logistic regression

# Extract the independent variables (X) and the dependent variable (Y)
Y1 = df['Recommended']
#Y1 = df['Rating_Class']

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y1, test_size=0.2, random_state=42)

# Create the logistic regression model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)
classification_rep = classification_report(Y_test, Y_pred)

print(f"Accuracy: {accuracy}")
print("\n")
print("Confusion Matrix:")
print(conf_matrix)
print("\n")
print("Classification Report:")
print(classification_rep)

# Naive Bayes classifier

# clf = MultinomialNB()
# clf.fit(X_train, Y_train)

# # Predict on the test set
# y_pred = clf.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(Y_test, y_pred)
# classification_rep = classification_report(Y_test, y_pred)

# print("Accuracy:", accuracy)
# print("Classification Report:\n", classification_rep)

# Random forest classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create and train the Random Forest Classifier
random_forest_classifier = RandomForestClassifier(random_state=42)
random_forest_classifier.fit(X_train, Y_train)

# Predict on the test set
Y_pred_rf = random_forest_classifier.predict(X_test)

# Model evaluation
accuracy_rf = accuracy_score(Y_test, Y_pred_rf)
print("Random Forest Classifier - Accuracy:", accuracy_rf)
print("Classification Report:\n", classification_report(Y_test, Y_pred_rf))

feature_importances = random_forest_classifier.feature_importances_
# Get the feature names
feature_names = X_train.columns
# Sort feature importances in descending order
indices = feature_importances.argsort()[::-1]
# Plot
plt.figure(figsize=(15, 6))
plt.title('Feature Importance')
plt.bar(range(X_train.shape[1]), feature_importances[indices], align='center')
plt.xticks(range(X_train.shape[1]), [feature_names[i] for i in indices], rotation=45)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.show()

# Decision Tree classifier

from sklearn.tree import DecisionTreeClassifier

# Create and train the Decision Tree Classifier
decision_tree_classifier = DecisionTreeClassifier(random_state=42)
decision_tree_classifier.fit(X_train, Y_train)

# Predict on the test set
Y_pred_dt = decision_tree_classifier.predict(X_test)

# Model evaluation
accuracy_dt = accuracy_score(Y_test, Y_pred_dt)
print("Decision Tree Classifier - Accuracy:", accuracy_dt)
print("Classification Report:\n", classification_report(Y_test, Y_pred_dt))

# Support Vector Machine Classifier

# from sklearn.svm import SVC

# # Create and train the Support Vector Machine (SVM) Classifier
# svm_classifier = SVC(kernel='linear', random_state=42)  # Linear kernel, change as needed
# svm_classifier.fit(X_train, Y_train)

# # Predict on the test set
# Y_pred_svm = svm_classifier.predict(X_test)

# # Model evaluation
# accuracy_svm = accuracy_score(Y_test, Y_pred_svm)
# print("SVM Classifier - Accuracy:", accuracy_svm)
# print("Classification Report:\n", classification_report(Y_test, Y_pred_svm))

# KNN Classifier

from sklearn.neighbors import KNeighborsClassifier

# Create and train the K-Nearest Neighbors (KNN) Classifier
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X_train, Y_train)

# Predict on the test set
Y_pred_knn = knn_classifier.predict(X_test)

# Model evaluation
accuracy_knn = accuracy_score(Y_test, Y_pred_knn)
print("K-Nearest Neighbors (KNN) - Accuracy:", accuracy_knn)
print("Classification Report:\n", classification_report(Y_test, Y_pred_knn))



from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Assuming X is your feature matrix
features_for_clustering = ['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money']
X_cluster = df[features_for_clustering]

# Standardize the data (important for K-Means)
scaler = StandardScaler()
X_cluster_scaled = scaler.fit_transform(X_cluster)

# Choose the number of clusters (you need to decide this based on your data)
num_clusters = 3

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_cluster_scaled)

# Visualize the clusters (you can adjust this based on the number of features)
plt.scatter(df['Seating_comfort'], df['Value_for_money'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Seating Comfort')
plt.ylabel('Value for Money')
plt.title('K-Means Clustering')
plt.show()

# Explore the characteristics of each cluster
cluster_means = df.groupby('Cluster')[features_for_clustering].mean()
print(cluster_means)

selected_features = ['Overall_rating', 'Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment']

# Select relevant features and handle missing values
df_cluster = df[selected_features].dropna()

# Normalize/Standardize data
scaler = StandardScaler()
X = scaler.fit_transform(df_cluster)

# Choose the number of clusters
num_clusters = 5

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Explore the characteristics of each cluster
cluster_means = df.groupby('Cluster')[selected_features].mean()
print(cluster_means)

df['Route']

df

unique_countries = df['Country'].unique()
print(unique_countries)

from sklearn.preprocessing import LabelEncoder

# Define geographical regions
asia_regions = {
    'East Asia': ['China', 'Japan', 'South Korea', 'North Korea', 'Mongolia'],
    'Southeast Asia': ['Vietnam', 'Thailand', 'Indonesia', 'Malaysia', 'Singapore', 'Philippines', 'Myanmar'],
    'South Asia': ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Bhutan', 'Maldives'],
    'Central Asia': ['Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan'],
    'Western Asia': ['Turkey', 'Iran', 'Iraq', 'Syria', 'Lebanon', 'Jordan', 'Israel', 'Saudi Arabia', 'Yemen', 'Oman', 'United Arab Emirates', 'Qatar', 'Bahrain', 'Kuwait']
}

# Map country to region
def map_country_to_region(country):
    for region, countries in asia_regions.items():
        if country in countries:
            return region
    return 'Other'

# Create 'Region' column
df['Region'] = df['Country'].apply(map_country_to_region)

# Encode 'Region' column
label_encoder = LabelEncoder()
df['Region_Encoded'] = label_encoder.fit_transform(df['Region'])

# Choose features for clustering
features_to_cluster =df[['Seating_comfort', 'Staff_service', 'Food_quality', 'Entertainment', 'Wifi', 'Ground_service', 'Value_for_money', 'anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']]

# Choose the number of clusters
num_clusters = 5

# Apply K-Means
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df['Geographical_Cluster'] = kmeans.fit_predict(features_to_cluster)

# Display the resulting DataFrame
print(df[['Country', 'Region', 'Geographical_Cluster']])

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame
# Choose two features for visualization
feature1 = 'Overall_rating'
feature2 = 'Region'

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df[feature1], y=df[feature2], hue=df['Geographical_Cluster'], palette='viridis', s=80)
plt.title('Scatter Plot of Clusters based on {} and {}'.format(feature1, feature2))
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.legend(title='Geographical Cluster')
plt.show()



