'''
Author: Jeremy T.
Copyright: Public Use
'''

'''
 Main Brains!
'''
def main():
    totalFuel = 0
    filein = open('day1/input.txt', 'r')
    for mass in filein:
        fuel = int(mass) // 3 - 2
        print('Fuel required: {}'.format(fuel))
        totalFuel += fuel
    
    print('Total fuel: {}'.format(totalFuel))
    filein.close()

main()

# Tear all the bytes!