## spotifav
#### Relevant blog post: [medium.com/p/fe50c94b8af3](https://medium.com/p/fe50c94b8af3)
After I found out that I have access to some interesting features (danceability, loudness etc) on my Spotify playlists, I decided to crunch some numbers in order to discover patterns on my favorite songs. For reality check, I compared my songs with the [Today's Top Hits](https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M) playlist, leading to some fun observations. You can get the aforementioned features for your playlists by this clever [Echonest app](http://sortyourmusic.playlistmachinery.com/).

This repository contains the necessary code, data, and Jupyter Notebooks to estimate histograms, correlation heatmaps, dimensionality reduction and visualization with t-SNE and outlier detection with One-Class SVM visualized in contour plots. 

To run you should set up the usual sci-Python gang: Matplotlib, Numpy, Pandas, Seaborn and Sklearn. 

### Steps
1. Log in to [Echonest app](http://sortyourmusic.playlistmachinery.com/) and choose your playlist.
2. Copy the table to a spreadsheet.
3. Save it as csv.
4. Run ``spotify_favorites.py`` to find correlations and estimate t-SNE and SVM
5. Run ``today_top_hits.py`` to compare step's 4. data with today top hits.

To replicate the artist-level projections as seen in my essay, please comment out [line 196](https://github.com/sdimi/spotifav/blob/master/spotify_favorites.py#L196).

As an alternative to the Echonest app, you can query your playlists directly through the [Spotify API](https://developer.spotify.com/web-api/get-audio-features/), getting access to even more features. Let me know how it went!

### Histograms & Correlations

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

### t-SNE Dimensionality Reduction

| Arcade Fire songs | Belle & Sebastian songs |
| ------------- | ------------- |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/tsne%20arcade%20fire.png)  | ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/tsne%20belle%20sebastian.png)  |

### Outlier Detection 

| Contour plot of fitted one-class SVM  |
| -------------  |
| ![PICTURE](https://github.com/sdimi/spotifav/blob/master/Figures/one%20class%20plot.png)  |
