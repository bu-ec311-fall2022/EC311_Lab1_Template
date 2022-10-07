`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/05/2022 10:12:08 PM
// Design Name: 
// Module Name: ha
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module ha(
    input a,
    input b,
    output carry,
    output sum
    );
    
    xor(sum,a,b);
    and(carry,a,b);
     
endmodule
