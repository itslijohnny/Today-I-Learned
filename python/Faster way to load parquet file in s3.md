# Faster way to load parquet file in s3

TIL that, the pandas `read_parquet` function allows read all parquet file in a folder. In this way, there is not need to load each file and concatenate later.  
  
Also, it seems the parameters of `engine` and `use_thread` and speed things up. However, I didn't find it change much.  
  
```python  
pd.read_parquet(folder_path,engine=pyrarrow, use_threads=True)  
```  
  
[aws](aws.md) [s3](s3.md) [pandas](pandas.md)  
