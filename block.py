# coding:utf-8
import hashlib
from model import Model
from rpc import BroadCast

class Block(Model):

    def __init__(self, block_height, version, merkle_root, target, previous_hash):
        self.block_height = block_height
        """
        check the gensis block
        """
        if self.block_height == 0:
            self.prev_block = "0000000000000000000000000000000000000000000000000000000000000000"
        else:
            self.prev_block = previous_hash
        self.version = version
        self.merkle_root = merkle_root
        self.target = target

    def header_hash(self):
        """
        Refer to bitcoin block header hash
        """  

        return hashlib.sha256((str(self.block_height) + (self.version) + str(self.merkle_root) + str(self.target) + str(self.prev_block)).encode('utf-8')).hexdigest()

    def pow(self):
        """
        Proof of work. Add nouce to block.
        """        
        nouce = 0
        while self.valid(nouce) is False:
            nouce += 1
        self.nouce = nouce
        return nouce

    def make(self, nouce):
        """
        Block hash generate. Add hash to block.
        """
        self.hash = self.ghash(nouce)
    
    def ghash(self, nouce):
        """
        Block hash generate.
        """        
        header_hash = self.header_hash()
        token = f'{header_hash}{nouce}'.encode('utf-8')
        return hashlib.sha256(token).hexdigest()

    def valid(self, nouce):
        """
        Validates the Proof
        """
        return self.ghash(nouce)[:4] == "0000"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, bdict):
        b = cls(bdict['block_height'], bdict['version'], bdict['merkle_root'], bdict['target'], bdict['prev_block'])
        b.hash = bdict['hash']
        b.nouce = bdict['nouce']
        return b

    @staticmethod
    def spread(block):
        BroadCast().new_block(block)