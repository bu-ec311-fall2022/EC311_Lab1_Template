`timescale 1ns / 1ps

// EC-311 Lab-1 Part-2
  // The names of the variables are as described in the lab handout

module alu_4_bit #
(
  parameter INPUT_WIDTH = 4,
  parameter OUTPUT_WIDTH = 8,
  parameter SELECT_WIDTH = 2
)
(
  // The inputs 
  input wire [INPUT_WIDTH-1:0]      A_input,
  input wire [INPUT_WIDTH-1:0]      B_input,
  input wire [SELECT_WIDTH-1:0]     S_input,

  // The outputs
  output wire [OUTPUT_WIDTH-1:0]           Y_output

);



endmodule
