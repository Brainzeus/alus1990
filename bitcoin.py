import secp256k1 as ice
import random
import time
import dask

max_p = 115792089237316195423570985008687907852837564279074904382605163141518161494336

def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)

@dask.delayed
def Random_Bruteforce(startdec, stopdec):
    count = 0
    start_time = time.time()
    while True:
        dec = int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -= 2
            elapsed_time = time.time() - start_time
            print(f'Instance: Random_Bruteforce - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
        count += 1
        if count % 1000000 == 0:
            elapsed_time = time.time() - start_time
            print(f"{count} addresses scanned in {elapsed_time:.2f} seconds. Scan rate: {count/elapsed_time:.2f} addresses/second.")

def main():
    x = dask.delayed(Random_Bruteforce)(1579208923731619542357098500868790785283756427907490438260516314, max_p)
    dask.compute(x)

if __name__ == '__main__':
    address_to_find = input("Adresa ? ")
    main()

              