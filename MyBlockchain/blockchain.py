"""blockchain """
from ast import Import
from codecs import encode
from crypt import methods
import datetime
import json
import hashlib
from urllib import response
from flask import Flask, jsonify 

class Blockchain:    #Create Class Block
    def __init__(self):     #Method ใช้ ส่งค่าโดยมี parameter เป็น self
        self.chain = []     #Creat list empty block
        self.transaction = 0
        self.creat_block(nonce = 1 , previos_hash = "0")      #Genesis blockchain
              
        
    def creat_block(self,nonce,previos_hash):          #component block 
        block = {
            "index":len(self.chain)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "data":self.transaction,
            "previos_hash":previos_hash
        }
        self.chain.append(block)
        return block
    
   
    def get_previos_block(self):     #เรียกใช้ previos block
        return self.chain[-1]
    
    
    def  hash(self,block):             #Method use to key block
        encode_block = json.dumps(block,sort_keys=True).encode()   
        return hashlib.sha256(encode_block).hexdigest()
    
    def proof_of_work(self,previos_nonce):   #Method find nonce by Minning
        new_nonce = 1  #ค่า nonce ที่จะทำให้ ค่า hash เป็น => 0000xxxxxxxxxx
        check_proof = False #ตัวแปรเช็คค่า nonce 

        while check_proof is False:
            #เลขฐาน 16 มา 1 ชุด
            hashoperation = hashlib.sha256(str(new_nonce**2 - previos_nonce**2).encode()).hexdigest() 
            #Want  to make hash number => 0000xxxxxxxxx 
            if hashoperation[:4] == "0000":    #กำหนดถ้า  hash 4ตัวแรก เป็น 0000xxxxx  จะผ่านไปได้
                check_proof = True 
            else:
                new_nonce += 1 
        return new_nonce

    def is_chain_valid(self,chain):        #Method สำหรับตรวจสอบ Block โดยดึงข้อมูล จาก chain มา
        previos_block = chain[0]  #ดึง block genesis มาตรวจสอบ เก็บใน previos_block
        block_index = 1 #กำนด index block เริ่มจาก 1
        
        while block_index < len(chain):  #ทำการ loop while ใน แต่ละ block ที่มี scoop เมื่อ ลำดับ chain < ขนาดของ chain
            block = chain[block_index] #block ที่ตรวจสอบ โดยเริ่มจาก index = 1 หรือ block ตัวหลังจาก genesis block คือ block[1]
            if block["previos_hash"] != self.hash(previos_block):     #ตรวจสอบ previoshash
                return False
            
            previos_nonce = previos_block["nonce"]    #ดึง previosnonce  block ก่อนหน้า
            nonce = block["nonce"] #ดึง nonce จาก block ที่ตรวจสอบ
            hashoperation = hashlib.sha256(str(nonce**2 - previos_nonce**2).encode()).hexdigest()
            if hashoperation[:4] != "0000":  #ตรวจสอบ hash operation ถ้า 4ตัวแรก != "0000" is False
                return False
            previos_block = block      #ให้ ตัว block ที่ตวรจสอบเป็น previos block แล้ว loop ตัวต่อไป                                
            block_index +=1 #เพิ่ม index block ในการตวรจสอบตัวต่อไป
        return True 



#Web server
app = Flask(__name__) 


#เรียกใช้งาน Blockchain
blockchain = Blockchain() 

#routing

@app.route('/')
def hello():
    return "<p>Hello Blockchain</p>"

@app.route('/get_block',methods=["GET"])
def get_block():
    response = {
        "chain":blockchain.chain,
        "length":len(blockchain.chain)
    }
    return jsonify(response),200

@app.route('/mining',method = ["GET"])
def mine_block():
    amount = 110000
    blockchain.transaction = blockchain.transaction+amount
    previos_block = blockchain.get_previos_block()  #ดึง เอา previsblock มา ใส่ในตัสแปร previos_block ด้วย method get_previosBlock
    previos_nonce = previos_block["nonce"] #ดึงค่า nonce ในpreviosblock มาเก็บ ด้วย previos_block["nonce"]
    nonce =  blockchain.proof_of_work(previos_nonce)  #หาค่า nonce ของ block ใหม่ ด้วยวิธี proof of work โดยใส่ prameter เป็น previosnonce ที่ดึงมาเก็บ
    previos_hash = blockchain.hash(previos_block) #สร้าง hash ด้วยการเข้ารหัส ใหม่ด้วยmethod  hash
    block = blockchain.creat_block(nonce,previos_hash) #Create new Block ด้วย Method  create block 
    response = {
        "Message":"Mining Complete!!",
        "index": block["index"],
        "data":block["data"],
        "timestamp":block["timestamp"],
        "nonce":block["nonce"],
        "previos_hash":block["previos_hash"]
    }
    return jsonify(response),200

@app.route('/is_valid',method=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response ={"message":"Blockchain is valid"}
    else :
        response ={"message":"Have Problem , Blockchain is Not valid"}
    return jsonify(response),200
        

#run server 
if __name__ =="__main__":
    app.run()