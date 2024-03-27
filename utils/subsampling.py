import numpy as np

def random_subsample(df, num_samples):
    np.random.seed(42)
    indices = np.random.choice(df.index, num_samples, replace=False)
    subsampled_df = df.loc[indices]
    return subsampled_df 
