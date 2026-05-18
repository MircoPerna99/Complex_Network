from sklearn.metrics import adjusted_rand_score, rand_score, jaccard_score, fowlkes_mallows_score
import numpy as np

def evaluate_adjusted_rand_score(partition_1, partition_2):
        ari = adjusted_rand_score(partition_1, partition_2)
        return ari
    
def evaluate_rand_score(partition_1, partition_2):
        ri = rand_score(partition_1, partition_2)
        return ri
    
def evaluate_jaccard_score(partition_1, partition_2):
        js = adjusted_rand_score(partition_1, partition_2)
        return js
    
def evaluate_fowlkes_mallows_score(partition_1, partition_2):
        fms = fowlkes_mallows_score(partition_1, partition_2)
        return fms
    
def evaluate_mean_and_standard_deviation(metric): 
    mean = np.mean(metric)
    std = np.std(metric)
    return mean, std