import random
def main():
    print("Rolling dice...")
    total = 0
    for i in range(1,3):
        d = random.randint(1,6)
        print("Die {}: {}".format(i, d))
        total += d
    print("Total value: {}".format(total))

main()
