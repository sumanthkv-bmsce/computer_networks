import random

bucketSize=512

def bktInput(a,b):
    if a > bucketSize:
        print("\n\t\tBucket overflow");
    else:

        while(a>b):
            print(f"\n\t\t{b} bytes outputted.")
            a-=b 

        if a>0:
            print(f"\n\t\t Last {a} bytes sent\t")

        print("\n\t\tBucket output successful")


def main():
    
    print("Enter output rate : ")
    op = int(input())

    for i in range(5):
        pktSize = random.randint(0,600)
        print(f"\n Packet no {i} \t Packet Size = {pktSize}")
        bktInput(pktSize,op)

main()