import blockchain as _bc
import fastapi as _fastapi
from starlette.responses import RedirectResponse

blockchain = _bc.Blockchain()
app = _fastapi.FastAPI()

#endpoint to mine a  block
@app.get("/")
async def docs():
    response = RedirectResponse(url='/docs')
    return response


#endpoint to mine a  block
@app.post('/mine_block')
def mine_block(data: str):
    if not blockchain._validate_chain():
        return _fastapi.Response(status_code=400, detail='Invalid Chain')
    else:
        block = blockchain._mine_block(data)

    return block

#endpoint to get the full blockchain
@app.get('/chain')
def get_chain():
    if not blockchain._validate_chain():
        return _fastapi.Response(status_code=400, detail='Invalid Chain')
    else:
        chain =  blockchain.chain
        return chain

#endpoint to check if the blockchain is valid
@app.get('/is_valid')
def is_valid():
    if not blockchain._validate_chain():
        return _fastapi.Response(status_code=400, detail='Invalid Chain')
    else:
        response = "Valid Chain"
        return response