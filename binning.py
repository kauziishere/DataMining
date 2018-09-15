"""
    Dataset:
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
"""
import pandas as pd
"""
    Description:
            Function to calculate number of buckets buckets
    Pre:
            size of data: total number of datapoints
            bucket_size : maximum size of bucket
    Post:
            returns optimal no of bucket of buckets

"""
def calculate_no_of_buckets(size_of_data, bucket_size):
    min_size = size_of_data//bucket_size
    if bucket_size*min_size != size_of_data:
        return min_size+1
    return min_size

"""
    Description:
            Preprocess data to seperate it in buckets
    Pre:
            filepath   : location of data file
            bucket_size: maximum size of buckets
    Post:
            returns segregated data in form of list of lists
"""

def preprocess(filepath, bucket_size):
    data           = pd.read_csv(filepath)
    size_of_data   = data.shape[0]
    data           = data[data.columns.values[0]].values.tolist()
    num_of_buckets = calculate_no_of_buckets(size_of_data, bucket_size)
    new_data       = [0 for i in range(0, num_of_buckets)]
    for i in range(0, num_of_buckets):
        if(i*bucket_size+bucket_size < size_of_data):
            new_data[i] = data[i*bucket_size:i*bucket_size+bucket_size]
        else:
            new_data[i] = data[i*bucket_size:]
    return new_data

"""
    Description:
            Binning by mean
    Pre:
            filepath   : location of data file
            bucket_size: maximum size of buckets
"""

def binning_by_mean(filepath, bucket_size):
    data = preprocess(filepath, bucket_size)
    for i in range(0, len(data)):
        bucket     = data[i]
        no_of_vals = len(bucket)
        mean_of_bucket = 0.0
        for val in bucket:
            mean_of_bucket += val
        mean_of_bucket = mean_of_bucket/no_of_vals
        data[i] = [mean_of_bucket for j in range(0, no_of_vals)]
    print(data)

"""
    Description:
            Binning by median
    Pre:
            filepath   : location of data file
            bucket_size: maximum size of buckets
"""

def binning_by_median(filepath, bucket_size):
    data = preprocess(filepath, bucket_size)
    for i in range(0, len(data)):
        bucket     = data[i]
        no_of_vals = len(bucket)
        median = 0
        if(no_of_vals%2 == 1):
            median = bucket[no_of_vals//2]
        else:
            median = (bucket[(no_of_vals+1)//2]+bucket[(no_of_vals-1)//2])//2
        data[i] = [median for i in range(0, no_of_vals)]
    print(data)

"""
    Description:
            Binning by boundries
    Pre:
            filepath   : location of data file
            bucket_size: maximum size of buckets
"""

def binning_by_boundries(filepath, bucket_size):
    data = preprocess(filepath, bucket_size)
    for i in range(0, len(data)):
        bucket      = data[i]
        no_of_vals  = len(bucket)
        min         = bucket[0]
        max         = bucket[no_of_vals-1]
        for j in range(0, no_of_vals):
            if(abs(bucket[j] - min) < abs(bucket[j] - max)):
                bucket[j] = min
            else:
                bucket[j] = max
        data[i] = bucket
    print(data)

if __name__ == "__main__":
    filepath = "binning_data.csv"
    binning_by_mean(filepath, 4)
    binning_by_median(filepath, 4)
    binning_by_boundries(filepath, 4)
