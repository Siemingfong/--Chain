# coding:utf-8
from block import Block
from account import get_account
from database import BlockChainDB
from lib.common import unlock_sig, lock_sig

MAX_COIN = 21000000
REWARD = 20

def coinbase():
    """
    First block generate. 
    cb = block_height, version, merkle_root, target(setting difficulity), hash
    """
    cb = Block(0, "00000001", "0000000000000000000000000000000000000000000000000000000000000000", "0001000000000000000000000000000000000000000000000000000000000000","")
    nouce = cb.pow()
    cb.make(nouce)
    # Save block and transactions to database.

    BlockChainDB().insert(cb.to_dict())
    return cb

def mine():
    """
    Main miner method.
    """
    # Found last block and unchecked transactions.
    last_block = BlockChainDB().last()

    if len(last_block) == 0:
        last_block = coinbase().to_dict()

    # Miner reward is the first transaction.
    cb = Block( last_block['block_height'] + 1, last_block['version'], last_block['merkle_root'], last_block['target'], last_block['hash'])
    nouce = cb.pow()
    cb.make(nouce)
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    # Broadcast to other nodes
    Block.spread(cb.to_dict())
    return cb