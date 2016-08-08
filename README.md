##spotifav
#### Relevant blog post: [medium.com/p/fe50c94b8af3](https://medium.com/p/fe50c94b8af3)
The idea is simple. After I found out that I have access to some interesting features (danceability, loudness etc) on my Spotify playlists, I decided to crunch some numbers in order to discover some patterns of my favorite songs. For reality check, I compared my songs with the [Today's Top Hits](https://open.spotify.com/user/spotify/playlist/5FJXhjdILmRA2z5bvz4nzf) playlist, leading to some fun observations. You can get the aforementioned features for your playlists by this clever [Echonest app](http://static.echonest.com/SortYourMusic/).

This repository contains the necessary code, data, and Jupyter Notebooks to estimate histograms, correlation heatmaps, dimensionality reduction and visualization with t-SNE and outlier detection with One-Class SVM visualized in contour plots. 

To run you should set up the usual sci-Python gang: Matplotlib, Numpy, Pandas, Seaborn and Sklearn. 

###Histograms & Correlations

| Histograms of my playlist's features | Compared to the most popular Spotify playlist |
| ------------- | ------------- |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/histograms.png)  | ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/histograms%20comparison.png)  |

|   |   | 
| ------------- | ------------- |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/Acousticness%20Loudness%20Corr.png)  | ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/Danceability%20Valence%20Corr.png)  |

|   |   | 
| ------------- | ------------- |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/Energy%20Acousticness%20Corr.png)  | ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/Energy%20Loudness%20Correlation.png)  |

|   |   | 
| ------------- | ------------- | 
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/Energy%20Valence%20Corr.png)  | ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/Popularity%20Energy%20Corr.png)  |

###t-SNE Dimensionality Reduction

| Arcade Fire songs | Belle & Sebastian songs |
| ------------- | ------------- |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/tsne%20arcade%20fire.png)  | ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/tsne%20belle%20sebastian.png)  |

###Outlier Detection 

| Contour plot of fitted one-class SVM  |
| -------------  |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/one%20class%20plot.png)  |
