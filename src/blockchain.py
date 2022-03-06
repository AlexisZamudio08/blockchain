import datetime as _dt
import hashlib as _hashlib
import json as _json

#build a blockchain
class Blockchain:
    
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block('Genesis Block', 1, '0', 1)
        self.chain.append(genesis_block)

    def _mine_block(self, data: str) -> dict:
        previous_block = self._get_previous_block()
        previous_proof = previous_block['proof']
        index = len(self.chain) + 1
        proof = self._proof_of_work(previous_proof, index, data)
        previous_hash = self._hash(previous_block)
        block = self._create_block(data, proof, previous_hash, index)
        self.chain.append(block)

        return block
    
    def _hash(self, block: dict) -> str:
        encoded_block = _json.dumps(block, sort_keys=True).encode()
        return _hashlib.sha256(encoded_block).hexdigest()

    def __to_digest(self, new_proof: int, previous_proof: int, index: int, data: str) -> bytes:
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index) + data
        return to_digest.encode()

    def _proof_of_work(self, previous_proof: str, index: int, data: str) -> int:
        new_proof = 1
        check_proof = False
        while check_proof is False:
            to_digest = self.__to_digest(new_proof, previous_proof, index, data)
            hash_value = _hashlib.sha256(to_digest).hexdigest()
            if hash_value[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def _get_previous_block(self) -> dict:
        return self.chain[-1]
    
    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
            'index': index,
            'timestamp': str(_dt.datetime.now()),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash
        }
        return block

    #validate chain
    def _validate_chain(self) -> bool:
        current_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            if next_block['previous_hash'] != self._hash(current_block):
                return False
            
            previous_proof = current_block.get('proof')
            next_index, next_data, new_proof = (next_block['index'], next_block['data'], next_block['proof'])

            hash_value = _hashlib.sha256(self.__to_digest(new_proof, previous_proof, next_index, next_data)).hexdigest()

            if hash_value[:4] != '0000':
                return False

            current_block = next_block
            block_index += 1
        return True

# bc = Blockchain()
# print(_json.dumps(bc.chain, indent=4, sort_keys=True))
# #print a line to separate the output
# print('-' * 100)
# print(_json.dumps(bc._mine_block('First Block'), indent=4, sort_keys=True))
# print('-' * 100)
# print(_json.dumps(bc.chain, indent=4, sort_keys=True))
# print('-' * 100)
# print(_json.dumps(bc._mine_block('Second Block'), indent=4, sort_keys=True))
# print('-' * 100)
# print(_json.dumps(bc.chain, indent=4, sort_keys=True))
# print('-' * 100)
# print(bc._validate_chain())
# print('-' * 100)
# bc.chain[1]['data'] = 'Changed data'
# print(bc._validate_chain())
# print('-' * 100)
# print(_json.dumps(bc.chain, indent=4, sort_keys=True))
