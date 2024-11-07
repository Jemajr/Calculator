class Calculator:
    
    '''This calculator class converts numbers from one base to the other.
    Returns values as strings for consistenxy with hexadecimal numbers'''

    def __init__(self):
        pass


    def bin_to_dec(self, num):
        decimal = 0
        power = 0
        num = str(num)[::-1]

        for digit in num:
            decimal += int(digit) * (2 ** power)
            power += 1

        return str(decimal)


    def dec_to_bin(self, num):
        if num == 0:
            return '0'
        
        rems = []
        current = int(num)

        while current >= 1:
            rem = current % 2
            rems.append(str(rem))
            current = current // 2

        binary = int(''.join(rems[::-1]))
        return str(binary)


    def bin_to_hex(self, num):
        decimal = self.bin_to_dec(num)
        hex_ = self.dec_to_hex(decimal)
        return hex_


    def hex_to_bin(self, num):
        decimal = self.hex_to_dec(num)
        binary = self.dec_to_bin(decimal)
        return binary


    def dec_to_hex(self, num):
        if num == 0:
            return '0'
        
        specs = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        rems = []

        while num >= 1:
            rem = num % 16
            if rem in specs:
                rems.append(specs[rem])
            else:
                rems.append(str(rem))
            num = num // 16

        hex_ = ''.join(rems[::-1])
        return str(hex_)
    

    def hex_to_dec(self, num):
        specs = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        nums = [x.upper() for x in str(num)]

        for i in range(len(nums)):
            if nums[i] in specs:
                nums[i] = str(specs[nums[i]])

        num = nums[::-1]
        decimal = 0
        power = 0

        for digit in num:
            decimal += int(digit) * (16 ** power)
            power += 1

        return str(decimal)


    def dec_to_oct(self, num):
        if num == 0:
            return '0'

        rems = []

        while num >= 1:
            rem = num % 8
            rems.append(str(rem))
            num = num // 8

        oct_ = ''.join(rems[::-1])
        return str(oct_)


    def oct_to_dec(self, num):
        decimal = 0
        power = 0
        num = str(num)[::-1]

        for digit in num:
            decimal += int(digit) * (8 ** power)
            power += 1

        return str(decimal)
    


my_calculator = Calculator()

trial1 = my_calculator.hex_to_dec('20F')
print(trial1)

trial2 = my_calculator.dec_to_hex(527)
print(trial2)

trial3 = my_calculator.dec_to_bin(527)
print(trial3)

trial4 = my_calculator.hex_to_bin('20F')
print(trial4)

trial5 = my_calculator.dec_to_hex(65535)
print(trial5)