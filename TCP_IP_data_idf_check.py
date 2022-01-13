#!/usr/bin/python
import numpy as np
from data_gen import Dataset
from random import shuffle
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from scipy.cluster import hierarchy
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.cluster import DBSCAN
from mpl_toolkits import mplot3d
from sklearn.feature_extraction.text import TfidfVectorizer

def Preproc(data):
    data_n = []
    for line in data.split(','):
        k = line.replace(".", "")
        data_n.append(k)
    return data_n


def Preproc1(data):
    data_n = []
    for line in data.split(','):
        data_n.append(line)
    return data_n


def Represent(data):
    Count = {"UDP": 0, "ICMP": 0, "TCP": 0}
    for item in data:
        if "UDP" in item:
            Count["UDP"] += 1
        if "ICMP" in item:
            Count["ICMP"] += 1
        if "TCP" in item:
            Count["TCP"] += 1
    return Count


def Create_stop_words(data_dict):
    stop_words = []
    mean = sum(data_dict.values())/len(data_dict)
    delta = mean * 0.6
    for d in data_dict.items():
        if d[1] > mean + 1.3*delta or d[1] < mean - delta:
            stop_words.append(d[0])
    return stop_words


def Remove_edges(data, stopwords):
    Parsed_data = []
    for line in data.split(','):
        line = line.strip()
        line = line.replace("=", " ")
        line = line.lower()
        char_list = ['|']
        # Split the line into words
        words = line.split(" ")
        words = [ele for ele in words if all(ch not in ele for ch in char_list)]
        resultwords = [word for word in words if word not in stopwords]
        resultwords = list(filter(None, resultwords))
        print(resultwords)
        result = ' '.join(resultwords)
        Parsed_data.append(result)
    return Parsed_data


def Create_text_files(data, labels, method):
    result = []
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    total = [result, result1, result2, result3, result4, result5, result6]
    for i in range(len(data)):
        if labels[i] == 0:
            result.append(data[i])
        if labels[i] == 1:
            result1.append(data[i])
        if labels[i] == 2:
            result2.append(data[i])
        if labels[i] == 3:
            result3.append(data[i])
        if labels[i] == 4:
            result4.append(data[i])
        if labels[i] == 5:
            result5.append(data[i])
        if labels[i] == 6:
            result6.append(data[i])
    a = open("output/%s.txt" % method, 'w')
    number = 0
    for cluster in total:
        for element in cluster:
            a.write(element + "\n")
        a.write("=================%i==================\n" %number)
        number = number + 1
    a.close()


MyNetwork = Dataset()
MyNetwork.Simulate_ALL()
print(Represent(MyNetwork.data))
plt.bar(Represent(MyNetwork.data).keys(), Represent(MyNetwork.data).values())
plt.savefig('output/MyChart.png')
######Cant remember wtf is hapenening here but this thing need to be here######
d = dict()
text = repr(MyNetwork.data)
for line in text.split():
    # Remove the leading spaces and newline character
    line = line.strip()
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
    # Remove the punctuation marks from the line
    line = line.replace("=", " ")
    char_list = ['|']
    # Split the line into words
    words = line.split(" ")
    words = [ele for ele in words if all(ch not in ele for ch in char_list)]
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
# Print the contents of dictionary
d = dict(sorted(d.items(), key=lambda item: item[1]))
plt.clf()
plt.bar(d.keys(), d.values())
plt.savefig('output/Word_count.png')
New = Preproc(repr(MyNetwork.data))
Old = Preproc1(repr(MyNetwork.data))
#shuffle(Old)
######################Clusterization process ##################
vectorizer = TfidfVectorizer()
print(type(Old))
vectorizer.fit(Old)
print(vectorizer.vocabulary_)
vector = vectorizer.transform(Old)
print(vector.shape)
print(vector.toarray())
pca = PCA(n_components=4)
vector = pd.DataFrame(vector.toarray())
x_pca = pca.fit_transform(vector)
print("======================")
print(pca.singular_values_)
x_pca = pd.DataFrame(x_pca)
print(x_pca.head())
kmeans = KMeans(n_clusters=7, random_state=0).fit(x_pca)
print(kmeans.labels_)
#X_dist = kmeans.transform(x_pca)**2
print('--------------------')
#print(X_dist)
clustering = DBSCAN(eps=3, min_samples=3).fit(x_pca)
print("======================")
plt.clf()
mergins = hierarchy.linkage(x_pca, method='ward')
hierarchy.dendrogram(mergins)
plt.rcParams["figure.figsize"] = [10,10]
plt.savefig('output/Dendrogram.png')
T = hierarchy.fcluster (mergins, t=7, criterion='maxclust')
#################Print 3d scatter plor #########################
plt.clf()
ax = plt.axes(projection='3d')
pca3 = PCA(n_components=3)
pca3 = pca3.fit_transform(vector)
X = pca3[:, 0]
Y = pca3[:, 1]
Z = pca3[:, 2]
ax.scatter3D(X, Y, Z, c=kmeans.labels_)
plt.savefig('output/3d_vis.png')
plt.clf()
#################Print 2d scatter plor #########################
pca3 = PCA(n_components=2)
pca3 = pca3.fit_transform(vector)
X = pca3[:, 0]
Y = pca3[:, 1]
plt.scatter(X, Y, c=clustering.labels_)
plt.savefig('output/2d_vis.png')
#################Show clusters############################
print(len(Old))
Create_text_files(Old, kmeans.labels_, "Kmean")
Create_text_files(Old, T, "hierarch")
Create_text_files(Old, clustering.labels_, "DBSCAN")
#################SHOW INIT PACKETS########################
b = open("output/Init.txt", 'w')
for cluster in Old:
    b.write(cluster + "\n")
b.close()
#################PCA Test###############################
pca1 = PCA(n_components=1)
pca1 = pca1.fit_transform(vector)
pca1.sort(axis=0)
print(type(pca1))
c = open("output/PCA_Vis.txt", 'w')
for cluster in pca1:
    cluster = str(cluster).replace("[","")
    cluster = cluster.replace("]", "")
    c.write(cluster + ",")
c.close()
