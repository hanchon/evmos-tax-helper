from web3 import Web3
import sys

WEB3_ENDPOINT = 'https://eth.bd.evmos.org:8545/'

def main():
    tx:str = sys.argv[1]
    w3 = Web3(Web3.HTTPProvider(WEB3_ENDPOINT))

    # txRes = w3.eth.get_transaction(tx)
    # if txRes['value'] is not None:
    #     print(f'{Web3.fromWei(txRes["value"], "ether")}')
    #     print('Evmos')
    # print('------')

    txRec = w3.eth.get_transaction_receipt(tx)
    data = txRec['logs'][-1]['data'][2:]
    # function
    # print(data[0:64])
    # Evmos payed
    # print(data[64:128])
    evmos = int(data[64:128],16)
    # print(evmos)
    print(Web3.fromWei(evmos, "ether"))
    # Coins received
    # print(data[128:192])
    usdc = int(data[128:192], 16)
    # print(usdc)
    print(Web3.fromWei(usdc, "mwei"))

if __name__ == '__main__':
    main()
