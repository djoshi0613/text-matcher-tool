# Introduction:
Calculating similarity index of two given texts from scale 0 to 1. 0 being 0% match and 1 being 100% match.

# Approach 
 - We are using BoW (Bag of Words) approach where :
    1. Punctuations are ignored.
    2. All words are provided equal weightage.
    3. Ordering of words are ignored.
    4. BoW Similarity  

# Build
## Without Docker
1. Install dependencies
```pip install requirements.txt```

2. Build web service 
```bash
python3 MatcherApi.py
```

## With Docker
 1. ```docker build -t matchertool:latest .```
    
 2. ```docker run -it -p 5000:5000 matchertool```

# Usage

1. Build Web-Service
2. Navigate to http://localhost:5000/  
3. Enter Text 1 and Text 2
4. Submit to view Similarity Index


