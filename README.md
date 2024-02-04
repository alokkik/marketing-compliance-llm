# marketing-compliance-llm

### How to run the application on your local:
1. Go to ```marketing-compliance-llm```
2. To create a ```.venv```, run ```python3 -m venv .venv```
3. Run ```source .venv/bin/activate``` to activate virtual environment.
4. Create ```.env``` and paste shared env variables to it.
   Run ```1. set -a``` ```2. source .env``` ```3. set +a``` to set env variables. Or, export them manually ```export VAR=value``` in terminal.
5. Now, install dependencies ```pip3 install -r requirements.txt```.
6. Finally, run ```uvicorn app.main:app```

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
