// Write your modules here!
module circuit(input [3:0] i, output score);
  assign x = i[0];
  assign y = i[1];
  assign z = i[2];
  assign w = i[3];
  assign first_option = (x || y || z);
  assign second_option = x || y || w;
  assign third_option = x || z || w;
  assign fourth_option = y || z || w;
  assign fifth_option = !y || !z || !w || !x;
  assign score = first_option && second_option && 
    third_option && fourth_option && fifth_option;
  
endmodule