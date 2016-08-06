
# coding: utf-8

# In[1]:

#Visualizing hundreds of my favourite songs on Spotify.
# A tale of statistics, personal taste and BPMs

#Dimitris Spathis <dispathis@gmail.com>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

df = pd.read_csv('spotify sortyourmusic favorite playlist.csv', sep=';', encoding='cp1252')


# In[3]:

df


# In[4]:

#get the last 4 characters from Date xx/xx/xxxx or xxxx for consistency
df['YEAR'] = df['RELEASE'].str[-4:]


# In[5]:

df['YEAR'] = df['YEAR'].convert_objects(convert_numeric=True)


# In[6]:

# sanity check, we should have 321 samples
#null_data = df[df.isnull().any(axis=1)]
#null_data


# In[7]:

df = df.drop('RELEASE', 1)


# In[8]:

df


# In[9]:

#hack because pandas thinks that our minutes are hours
time = pd.DatetimeIndex(df['LENGTH'])
seconds = time.hour * 60 + time.minute


# In[10]:

(df['Seconds']) = seconds


# In[11]:

df = df.drop('LENGTH', 1)


# In[12]:

df.to_csv('spotify cleaned.csv')


# In[13]:

df


# In[222]:


plt.figure(1, figsize=(20, 10),)

hfont = {'fontname':'Proxima Nova'}

plt.subplot(331)
sns.distplot(df.BPM);
plt.text(10, .010, r'$\mu=\ 121.12$', fontsize=22)
plt.xlabel('Tempo (BMP)', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(332)
sns.distplot(df['POP.']);
plt.text(70, .020, r'$\mu=\ 30.51$', fontsize=22)
plt.xlabel('Popularity', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(333)
sns.distplot(df.ENERGY);
plt.text(85, .010, r'$\mu=\ 52.05$', fontsize=22)
plt.xlabel('Energy', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(334)
sns.distplot(df.LOUD);
plt.text(-30, 0.10, r'$\mu=\ -9.36$', fontsize=22)
plt.xlabel('Loudness  ', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(335)
sns.distplot(df.DANCE);
plt.text(70, 0.02, r'$\mu=\ 47.38$', fontsize=22)
plt.xlabel('Danceability ', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(336)
sns.distplot(df.VALENCE);
plt.text(80, 0.01, r'$\mu=\ 40.68$', fontsize=22)
plt.xlabel('Valence (positive mood)', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(337)
sns.distplot(df.ACOUSTIC);
plt.text(80, 0.02, r'$\mu=\ 40.46$', fontsize=22)
plt.xlabel('Acousticness', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(338)
sns.distplot(df.YEAR);
plt.xlabel('Release Year', fontsize=18, **hfont)
plt.grid(True)

plt.subplot(339)
sns.distplot(df.Seconds);
#this corresponds to YEAR above, but somehow Matplot fucked it up when changing it
plt.text(-1100, 0.002, r'$\mu≈\ 2004$', fontsize=22)

#Seconds 
plt.text(500, 0.002, r'$\mu=\ 262.82$', fontsize=22)
plt.xlabel('Song Duration (sec)', fontsize=18, **hfont)
plt.grid(True)

plt.tight_layout(pad=0.5, w_pad=0.6, h_pad=1.0)


# In[17]:

df.describe(include = 'all')


# In[160]:

plt.rc("legend", fontsize=35)
#sns.jointplot(y=df['ENERGY'], x=df['LOUD'], kind="hex", color="r", size=13).set_axis_labels("Loudness", "Energy", fontsize=35)
#sns.jointplot(y=df['ENERGY'], x=df['ACOUSTIC'], kind="hex", color="r", size=13).set_axis_labels("Acousticness", "Energy", fontsize=35)
#sns.jointplot(y=df['DANCE'], x=df['VALENCE'], kind="hex", color="r", size=13).set_axis_labels("Valence (positive mood)", "Danceability", fontsize=35)
#sns.jointplot(y=df['ACOUSTIC'], x=df['LOUD'], kind="hex", color="r", size=13).set_axis_labels("Loudness", "Acousticness", fontsize=35)
#sns.jointplot(y=df['ENERGY'], x=df['VALENCE'], kind="hex", color="r", size=13).set_axis_labels("Valence (positive mood)", "Energy", fontsize=35)
#sns.jointplot(y=df['POP.'], x=df['ENERGY'], kind="hex", color="r", size=13).set_axis_labels("Energy", "Popularity", fontsize=35)
sns.jointplot(y=df['YEAR'], x=df['LOUD'], kind="hex", color="r", size=13).set_axis_labels("Loudness", "Release Year", fontsize=35)


# In[161]:

df


# In[162]:

x = df.drop(['#', 'TITLE', 'ARTIST'], axis=1)
#y = df['POP.']
x


# In[163]:

from sklearn.manifold import TSNE
X_embedded = TSNE(n_components=2).fit_transform(x)


# In[256]:

from matplotlib.pyplot import *
fig = figure(figsize=(20, 20))
ax = axes(frameon=False)
setp(ax, xticks=(), yticks=())
subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=0.9,
                wspace=0.0, hspace=0.0)
scatter(X_embedded[:, 0], X_embedded[:, 1], s=80,   marker="8")

for row_id in range(0, len(df)):
    #if (df.ARTIST[row_id] in ['The National']):
        target_word = df.TITLE[row_id]
        xx = X_embedded[row_id, 0]
        yy = X_embedded[row_id, 1]
        plt.annotate(target_word, (xx,yy), size=10, xytext=(-90,90), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round4', fc='white', alpha=0.3),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', 
                            color='red'))



# In[220]:

#df.to_pickle('spotify_dataframe.pkl')


# In[78]:

x.corr()
# ENERGY LOUD 0.75
# ENERGY ACOUSTIC -0.72
# DANCE VALENCE 0.58
# ACOUSTIC LOUD -0.52
# ENERGY VALENCE 0.46
# POP ENERGY 0.25
# YEAR LOUD 0.23


# In[257]:

x


# In[258]:

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(x)


# In[259]:

print(pca.explained_variance_ratio_) 


# In[260]:

x_pca = pca.fit_transform(x)


# In[358]:

from sklearn import svm
clf = svm.OneClassSVM(kernel="rbf", gamma=0.001, nu=0.3)
clf.fit(x_pca)


# In[361]:

xx, yy = np.meshgrid(np.linspace(-200, 800, 500), np.linspace(-200,800, 500))

Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(30, 20),)
#plt.title("Novelty Detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.Blues_r)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=5, colors='red')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='orange')

#visualize song titles
'''
for row_id in range(0, len(df)):
    #if (df.ARTIST[row_id] in ['The National']):
        target_word = df.TITLE[row_id]
        xxx = x_pca[row_id, 0]
        yyy = x_pca[row_id, 1]
        plt.annotate(target_word, (xxx,yyy), size=10, xytext=(-90,90), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round4', fc='white', alpha=0.3),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', 
                            color='red'))
'''   

b1 = plt.scatter(x_pca[:, 0], x_pca[:, 1], c='white', s=100)
plt.axis('tight')
plt.xlim((-200, 650))
plt.ylim((-150, 150))

leg = plt.legend([a.collections[0], b1, ],
           ["learned frontier", "training observations"],
           loc="upper left",prop={'size':30}, frameon=True)

plt.show()


# In[271]:

plt.scatter(x_pca[:, 0], x_pca[:, 1], c='white')


# In[ ]:



