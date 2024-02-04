# marketing-compliance-llm

### How to run the application:
1. 

### Curl :-
##### RAG Model
```
curl -X 'POST' \
  'http://localhost:8000/rag' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://www.joinguava.com/index.html"
}'
```

##### FSCOT Model
```
curl -X 'POST' \
  'http://localhost:8000/fscot' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://www.joinguava.com/index.html"
}'
```
