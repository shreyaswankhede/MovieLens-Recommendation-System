# MovieLens-Recommendation-System
The objective of this task is to recommend new movies based on the similarity of users, using collaborative filtering.

![alt text](https://github.com/shreyaswankhede/MovieLens-Recommendation-System/blob/master/03.PNG
 "Correlation between features")

***

# Recommendation-System:

* The objective of a Recommendation-System is to recommend relevant items for users, based on their preference. Preference and relevance are subjective, and they are generally inferred by items users have consumed previously.
Different Types of Systems:

1. Collaborative Filtering: For each user, recommender systems recommend items based on how similar users liked the item. 
2. Content-Based Filtering: This method uses only information about the description and attributes of the items users has previously consumed to model user's preferences.
3. Hybrid methods: Recent research has demonstrated that a hybrid approach, combining collaborative filtering and content-based filtering could be more effective than pure approaches in some cases

# Collaborative Filtering vs Content-Based Filtering:

![alt text](https://github.com/shreyaswankhede/MovieLens-Recommendation-System/blob/master/01.png
 "Correlation between features")


****

# Dataset:

MovieLens 100K movie ratings. Stable benchmark dataset. 100,000 ratings from 1000 users on 1700 movies. Released 4/1998.

* Source: https://grouplens.org/datasets/movielens/

***

# Workflow:

* Using Surprise library, a Python library for simple recommendation systems.
To know more about Surprise package click on the link - https://surprise.readthedocs.io/en/stable/#

* The Dataset method downloads and store the MovieLens 100k data in an user-movie interaction matrix. The rows of this matrix represent users, and the columns represent movies. Using this load_builtin method, we get a sparse matrix with 943 rows and 1682 columns.

* Compute the cosine similarity between two movies’ rating vectors.

* Using Knn Algorithm for each user, we want to recommend a set of movies that we don't know.

* Training the model & creating TestSet.

* Top five movie recommendations for each user.
 

***

# Results:

![alt text](https://github.com/shreyaswankhede/MovieLens-Recommendation-System/blob/master/02.PNG
 "Correlation between features")
 
 ***

<br>Thank You!	
<p><!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/shreyaswankhede" aria-label="Follow @shreyaswankhede on GitHub">Follow @shreyaswankhede</a>
