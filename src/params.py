import random
import numpy as np

random.seed(0)
np.random.seed(0)
RunID = 33


general = {
    'Comment': '',
    'RunId': RunID,
    'cuda': '1,2'
}
dal = {
    'path': ['../data/tweets_all.csv', '../data/tagmeannotation_1of16.csv'],
    'userModeling': True,
    'timeModeling': True,
    'start': '2010-11-01',
    'end': '2010-11-19',
    'timeInterval': 1,
    'preProcessing': False,
    'TagME': False,
    'lastRowsNumber': -1
}
tml = {
    'path2saveTML': f'../output/{RunID}/tml',
    'num_topics': 75,
    'library': 'gensim',
    'mallet_home': 'C:/Users/Soroush/Desktop/mallet-2.0.8/mallet-2.0.8',
    'filterExtremes': True,
    'JO': False,
    'Bin': False,
    'Threshold': 0.02
}
uml = {
    'UserSimilarityThreshold': 0.45,
    'path2saveUML': f'../output/{RunID}/uml'
}
gel = {
    'path2saveGEL': f'../output/{RunID}/gel',
    'EmbeddingDim': 30,
    'method': 'DynAERNN'
}
evl = {
    'EvaluationType': 'Extrinsic',  # ['Intrinsic', 'Extrinsic']
    # If intrinsic evaluation:
    'EvaluationMetrics': ['adjusted_rand', 'completeness', 'homogeneity', 'rand', 'v_measure',
                          'normalized_mutual_info', 'adjusted_mutual_info', 'mutual_info', 'fowlkes_mallows'],
    'GoldenStandardPath': '/path2GS',
    'Threshold': 0,
    'TopK': 20
}

# default parameters set for Gibbs Sampling Dirichlet Mixture Model
gsdmm = {
    "dataset": "News", # selected dataset from data folder
    "timefil": "timefil",
    "MaxBatch": 5,  # The number of saved batches + 1
    "AllBatchNum": 16,  # The number of batches you want to divide the dataset to
    "alpha": 0.03,  # document-topic density
    "beta": 0.03,  # topic-word density
    "iterNum": 5,  # number of iterations
    "sampleNum": 1,
    "wordsInTopicNum": 5,
    "K": 0
}
