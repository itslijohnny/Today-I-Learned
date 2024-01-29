## How to get file modify date/time

>https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times


```python
import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime(file)))
print("created: %s" % time.ctime(os.path.getctime(file)))
```