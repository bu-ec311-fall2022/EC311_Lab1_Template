'''
A cocotb-pytest test (this file) has two parts:
1. Testbench 
    - Any python function decorated with @cocotb.test()
    - Drives signals into pins of the design, reads the output/intermediate pins and compares with expected results
    - Uses async-await: 
        - Declared as def async
        - when "await Event()", simulator advances in simulation time until the Event() happens
    - You can have multiple such testbenches too. Pytest would find and run them all
2. PyTest 
    - The setup that connects the simulator of your choice, 
    - Feeds the design files, 
    - Finds your testbenches (1), 
    - Parametrizes them to generate multiple versions of the designs & tests
    - Runs all such tests and prints a report of pass & fails
'''


import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ClockCycles

import random
# import numpy as np

'''
1. Testbench
'''
@cocotb.test()
async def add_sub_4_bit_tb(dut):

    ''' Clock Generation '''
    #clock = Clock(dut.clk, 10, units="ns") # create a clock for dut.clk pin with 10 ns period
    #cocotb.start_soon(clock.start()) # start clock in a seperate thread

    ''' Assign random values to input, wait for a clock and verify output '''
    
    
        
    exactA = 10 # generate randomized input
    exactB = 10
    exactM = 0
    dut.A_i.value = exactA # drive pins
    dut.B_i.value = exactB
    dut.M_i.value = exactM

    # addition test
    #sum_expected = 20
    #sum_expected = 4  # since there would be an over flow and 20 = b 0001 0100 .. so sum_expected = b0100 = 4
    sum_expected = 0b0100  # since there would be an over flow and 20 = b 0001 0100 .. so sum_expected = b0100 = 4
    V_expected = 1
    C_expected = 1    
    await Timer(10, units="ns") # wait for falling edge
    V_value = dut.V_o.value # Read pins as unsigned integer.
    C_value = dut.C_o.value
    sum_value = dut.S_o.value


    assert V_value == V_expected, f"Failed. Got {V_value}, expected {V_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {V_value} \t received value: {V_expected}")
    assert C_value == C_expected, f"Failed. Got {C_value}, expected {C_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {C_value} \t received value: {C_expected}")
    assert sum_value == sum_expected, f"Failed. Got {sum_value}, expected {sum_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {sum_value} \t received value: {sum_expected}")
    
    
    # Subtraction test # 1
    exactA = 10 # generate randomized input
    exactB = 9
    exactM = 1
    dut.A_i.value = exactA # drive pins
    dut.B_i.value = exactB
    dut.M_i.value = exactM
    
    sub_expected = 1
    V_expected = 0
    C_expected = 1    
    await Timer(10, units="ns") # wait for falling edge
    V_value = dut.V_o.value # Read pins as unsigned integer.
    C_value = dut.C_o.value
    sub_value = dut.S_o.value


    assert V_value == V_expected, f"Failed. Got {V_value}, expected {V_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {V_value} \t received value: {V_expected}")
    assert C_value == C_expected, f"Failed. Got {C_value}, expected {C_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {C_value} \t received value: {C_expected}")
    assert sub_value == sub_expected, f"Failed. Got {sub_value}, expected {sub_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {sub_value} \t received value: {sub_expected}")
    
    # Subtraction test#2
    exactA = 0 # generate randomized input
    exactB = 2
    exactM = 1
    dut.A_i.value = exactA # drive pins
    dut.B_i.value = exactB
    dut.M_i.value = exactM
    
    sub_expected = 0b1110 # 0b1110 represents -2 in 4 bits (2s compilment)
    V_expected = 0
    C_expected = 0    
    await Timer(10, units="ns") # wait for falling edge
    V_value = dut.V_o.value # Read pins as unsigned integer.
    C_value = dut.C_o.value
    sub_value = dut.S_o.value


    assert V_value == V_expected, f"Failed. Got {V_value}, expected {V_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {V_value} \t received value: {V_expected}")
    assert C_value == C_expected, f"Failed. Got {C_value}, expected {C_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {C_value} \t received value: {C_expected}")
    assert sub_value == sub_expected, f"Failed. Got {sub_value}, expected {sub_expected}" # If any assertion fails, the test fails, and the string would be printed in console
    print(f"Driven value: {sub_value} \t received value: {sub_expected}")



'''
2. Pytest Setup
'''

from cocotb_test.simulator import run
import pytest
import glob

@pytest.mark.parametrize(
    # Two sets of parameters to test across
    "parameters", [
        {"WIDTH_IN": "8", "WIDTH_OUT": "16"},
        {"WIDTH_IN": "16"}
        ])
def test_register(parameters):

    run(
        verilog_sources=glob.glob('add_sub_4_bit/hdl/*'),
        toplevel="add_sub_4_bit",    # top level HDL
        
        module="test_add_sub_4_bit", # name of the file that contains @cocotb.test() -- this file
        simulator="icarus",

        parameters=parameters,
        extra_env=parameters,
        sim_build="add_sub_4_bit/sim_build/" + ",".join((f"{key}={value}" for key, value in parameters.items())),
    )
