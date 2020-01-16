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
        final_fuel = 0

        fuel = int(mass) // 3 - 2
        final_fuel += fuel
        print('Fuel required: {}'.format(fuel))

        while fuel // 3 - 2 > 0:
            fuel = fuel // 3-2
            print('Negative fuel: {}'.format(fuel))
            final_fuel += fuel
        
        print('Final Fuel: {}'.format(final_fuel))
        totalFuel += final_fuel
    
    print('Total fuel: {}'.format(totalFuel))
    filein.close()

main()

# Tear all the bytes!