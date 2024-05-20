import smbus

class ADG728:

    # ADG728 default address
    address = 0x4c
   
   # Register addresses (with "normal mode" power-down bits)
    reg_write_dac = 0x00

    bus = None

    switches = []

    def __init__(self, channel = 1, address = 0x4c):
        # Initialize I2C (SMBus)
        self.bus = smbus.SMBus(channel)
        print("initialized bus on channel ", channel)
        self.address = address
        print("set address to ", self.address)
        self.switches = [0x00 & 0xff]

    def flip(self, switch:int):
        self.switches[0] = self.switches[0] ^ (0x01<<switch)
        # Write out I2C command: address, reg_write_dac, msg[0]
        self.bus.write_i2c_block_data(self.address, self.reg_write_dac, self.switches)

    def set_bits(self, states:int):
        self.switches[0] = states
        self.bus.write_i2c_block_data(self.address, self.reg_write_dac, self.switches)
    
    def reset(self):
        self.switches[0] = self.switches[0] & 0x00
        self.bus.write_i2c_block_data(self.address, self.reg_write_dac, self.switches)

