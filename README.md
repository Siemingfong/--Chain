# Blockchain-python

A blockchain implementation in Python only for hw2.

The Blockchain-python implements simple blockchain. The communication between nodes is via rpc based on http, rather than p2p network. Because the implementation of P2p is more complicated, it is too complicated to understand the framework of blockchain.   

## Usage

- Create Account
```
$ python console account create
```
- Run the miner
```
$ python console miner start 3008
```
```
- Blockchain shows.   
```
$ python console blockchain list
```
### Node Network
Copy the code resource to a new directory.While the miner before was running then:
```
$ cd {another_blockchain_directory}
$ python console node add 3008 
$ python console node run 3009
```
When a new block mined , block and transactions will broadcast to other nodes.

|  Module  |  Action    |  Params                            |  Desc                                            |
|----------|------------|------------------------------------|--------------------------------------------------|
| account  |  create    |  NONEED                            |  Create new account                              |
| account  |  get       |  NONEED                            |  Show all account                                |
| account  |  current   |  NONEED                            |  The miner reward account                        |
| miner    |  start     |  ip:port/port                      |  Such as 3008 or 127.0.0.1:3008                  |
| node     |  run       |  ip:port/port                      |  Such as 3008 or 127.0.0.1:3008                  |
| node     |  list      |  NONEED                            |  Show all node that will broadcast   to          |
| node     |  add       |  ip:port                           |  Add a node that will broadcast   to             |