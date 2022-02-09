import datetime
from random import randint
import time
import hashlib
import json
class Blockchain:


	def __init__(self):
		self.chain = []
		self.create_block(proof=1, previous_hash='0')


	def create_block(self, proof, previous_hash):
		block = {'index': len(self.chain) + 1,
				'timestamp': str(datetime.datetime.now()),
				'proof': proof,
				'previous_hash': previous_hash,
                'transaction': randint(1,200)
                }
		self.chain.append(block)
		return block
	

	def print_previous_block(self):
		return self.chain[-1]
	

	def proof_of_work(self, previous_proof):
		new_proof = 1
		check_proof = False
		
		while check_proof is False:
			hash_operation = hashlib.sha256(
				str(new_proof**2 - previous_proof**2).encode()).hexdigest()
			if hash_operation[:x] == x*'0':
				check_proof = True
			else:
				new_proof += 1
				
		return new_proof

	def hash(self, block):
		encoded_block = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(encoded_block).hexdigest()

	def chain_valid(self, chain):
		previous_block = chain[0]
		block_index = 1
		
		while block_index < len(chain):
			block = chain[block_index]
			if block['previous_hash'] != self.hash(previous_block):
				return False
			
			previous_proof = previous_block['proof']
			proof = block['proof']
			hash_operation = hashlib.sha256(
				str(proof**2 - previous_proof**2).encode()).hexdigest()
			
			if hash_operation[:x] != x*'0':
				return False
			previous_block = block
			block_index += 1
		
		return True


blockchain = Blockchain()

def mine_block():
	previous_block = blockchain.print_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	block = blockchain.create_block(proof, previous_hash)
	
	response = {'message': 'A block is MINED',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
				'previous_hash': block['previous_hash'],
                'transaction': block['transaction'],
                'type':'user'
                }
	
	print(response)

def attack(cpu_power):
    prev_block = blockchain.print_previous_block()
    prev_proof = prev_block['proof']
    newproof = 1
    newproof_attack = 1
    #print(cpu_power)
    while (1):
     i=0
     j=0    
     while i < (100-cpu_power):
        hashing = hashlib.sha256(
             str(newproof**2 - prev_proof**2).encode()).hexdigest()
        if hashing[:5]==5*'0' :
             prev_hash = blockchain.hash(prev_block)
             block = blockchain.create_block(newproof,prev_hash)
             response = {'message': 'A block is MINED',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
				'previous_hash': block['previous_hash'],
                'transaction': block['transaction'],
                'type':'user'}    
             print(response)    
             return
        else :  
            newproof+=1
        i+=1    
        
            

     #print("attackkkkkkkkkkkkkkkkkkkkkkkkkk")        
     while (j < cpu_power):
        hashing = hashlib.sha256(
             str(newproof_attack**2 - prev_proof**2).encode()).hexdigest()
        if hashing[:5]==5*'0' :
             prev_hash = blockchain.hash(prev_block)
             block = blockchain.create_block(newproof_attack,prev_hash)
             response = {'message': 'A block is MINED',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
				'previous_hash': block['previous_hash'],
                'transaction': block['transaction'],
                'type':'attacker'}    
             print(response)    
             return
        else :  
            newproof_attack+=1          
        j+=1    


def display_chain():
	response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
	print(response)




def valid():
	valid = blockchain.chain_valid(blockchain.chain)
	
	if valid:
		response = {'message': 'The Blockchain is valid.'}
	else:
		response = {'message': 'The Blockchain is not valid.'}
	print(response)

global mine_time
mine_time = 0

global x
x = 5 #inital value for hardness

while(1):
  y=input('''ENTER VALUE :
  [1 for mining] 
  [2 for checking validity of chain ]
  [3 for displaying the chain ]
  [4 for attack simulation ]
  [5 to exit ]
   ''') 
  if (y=="1") :
     t1 = time.time()
     mine_block()
     t2 = time.time()
     mine_time = t2 - t1 
     print(mine_time)
     if(mine_time>1):
         if(x!=1):
             x-=1             
     else :
           x+=1      
     print(x)     
  elif (y=="2") :
      valid()
  elif (y=="3") :
      display_chain()
  elif (y=="4") :
    x=5 
    cpu=int(input("ENTER CPU POWER  "))   
    attack(cpu)    
  else :
      break      

