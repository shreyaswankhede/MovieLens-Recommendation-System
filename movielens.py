
#importing surprise package and builtin data
from surprise import Dataset, evaluate
from surprise import KNNBasic
from collections import defaultdict


# loading data
dataset = Dataset.load_builtin("ml-100k")
trainingSet = dataset.build_full_trainset()
trainingSet

# cosine similarity between 2 vectors
sim_options = {
    'name': 'cosine',
    'user_based': False
}
knn = KNNBasic(sim_options=sim_options)

# training the model
knn.train(trainingSet)

# movie recommendations for users
testSet = trainingSet.build_anti_testset()
predictions = knn.test(testSet)

#top three movie recommendations for each user.
 
def get_top5_recommendations(predictions, topN = 5):
     
    top_recs = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_recs[uid].append((iid, est))
     
    for uid, user_ratings in top_recs.items():
        user_ratings.sort(key = lambda x: x[1], reverse = True)
        top_recs[uid] = user_ratings[:topN]
     
    return top_recs

# in data we have movieid's.read_item_names maps each movie’s ID to its name.
import os, io
 
def read_item_names():
    """Read the u.item file from MovieLens 100-k dataset and returns a
    mapping to convert raw ids into movie names.
    """
 
    file_name = (os.path.expanduser('~') +
                 '/.surprise_data/ml-100k/ml-100k/u.item')
    rid_to_name = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]
 
    return rid_to_name

# top 3 recommendations
top5_recommendations = get_top5_recommendations(predictions)
rid_to_name = read_item_names()
for uid, user_ratings in top5_recommendations.items():
    print(uid, [rid_to_name[iid] for (iid, _) in user_ratings])
 
    
