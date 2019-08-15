import numpy as np 
import pandas as pd 
from sklearn import svm, model_selection, preprocessing
from sklearn.cluster import KMeans
from sklearn.externals import joblib

df = pd.read_csv("/home/it/TY12/mykdd.csv")
df = df.sample(frac=1)
df = df[:int(len(df)*0.2)]

print(len(df))
# print(len(df.columns.values))
# print(df.head())

set_potocols = set(df['protocol_type'])
set_service = set(df['service'])
set_flag = set(df['flag'])
set_attack = set(df['attack'])

# print(set_potocols)
# print(set_service)
print(set_flag)
print(len(set_attack)) 

columns = df.columns.values
for c in columns:
    df[c] = pd.to_numeric(df[c], errors='ignore')
# df.convert_objects(convert_numeric = True)
df.fillna(0, inplace=True)


converted_columns = {}

def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}

        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            print(column)
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1

            df[column] = list(map(convert_to_int, df[column]))

            converted_columns[column] = text_digit_vals 

    return df

df = handle_non_numerical_data(df)
# print(df.head())

# def to_kdd_pre():
#     return converted_columns

column_keep = ['protocol_type','service','flag','src_bytes','dst_bytes','urgent','num_failed_logins','logged_in','root_shell','is_host_login','is_guest_login','num_shells','count','srv_count']

# 98% without shuffling['protocol_type','service','flag','src_bytes','dst_bytes','wrong_fragment','urgent','num_failed_logins','logged_in','root_shell','su_attempted','is_host_login','is_guest_login']
# 97.8% without shuffling ['protocol_type','service','src_bytes','dst_bytes','wrong_fragment','urgent','num_failed_logins','logged_in','root_shell','su_attempted']
# 97.9% without shuffling ['protocol_type','service','src_bytes','dst_bytes','urgent','num_failed_logins','logged_in','root_shell','su_attempted']
# 96.7% with shuffle ['protocol_type','service','src_bytes','dst_bytes','urgent','num_failed_logins','logged_in','root_shell','su_attempted']

X = np.array(df[column_keep])
y = np.array(df['attack'])


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

joblib.dump(converted_columns,"con_col.pkl")
joblib.dump(X_test,"X_test_data.pkl")
joblib.dump(y_test,"y_test_data.pkl")
clf = svm.SVC()
clf.fit(X_train, y_train)
joblib.dump(clf,"test_kdd_pickle.pkl")
# accuracy = clf.score(X_test, y_test)
# print(accuracy)

# clf = KMeans(n_clusters = len(set_attack))
# clf.fit(X)

# correct = 0
# for i in range(len(X)):
# 	predict_me = np.array(X[i].astype(float))
# 	predict_me = predict_me.reshape(-1, len(predict_me))
# 	prediction = clf.predict(predict_me)
# 	if prediction == y[i]:
# 		correct +=1

# print(correct/len(X))
