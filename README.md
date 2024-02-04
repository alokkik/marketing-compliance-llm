# marketing-compliance-llm



#### Curl :-

##### RAG model
curl -X 'POST' \
  'http://localhost:8000/rag' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://www.joinguava.com/index.html"
}'
