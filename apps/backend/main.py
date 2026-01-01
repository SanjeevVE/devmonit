from fastapi import FastAPI

app = FastAPI(title='DevMonit API')

@app.get('/health')
def health():
    return {'status': 'ok'}
