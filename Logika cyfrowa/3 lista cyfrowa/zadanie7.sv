module block(input [3:0]a,
              input [3:0]b, 
              input [0:0] c0, 
              output [3:0]s, 
              output[0:0]P0,
              output[0:0]G0);
  assign g0 = a[0] && b[0];
  assign p0 = a[0] || b[0];
  assign s[0] = a[0] ^ b[0] ^ c0;
  
  logic c1;
  assign g1 = a[1] && b[1];
  assign p1 = a[1] || b[1];
  assign c1 = g0 || p0 && c0;
  assign s[1] = a[1] ^ b[1] ^ c1;
  
  logic c2;
  assign g2 = a[2] && b[2];
  assign p2 = a[2] || b[2];
  assign c2 = p0 & p1 & c0 | p1 & g0 | g1;
  assign s[2] = a[2] ^ b[2] ^ c2;
  
  logic c3;
  assign g3 = a[3] && b[3];
  assign p3 = a[3] || b[3];
  assign c3 = p0 & p1 & p2 & c0 | p1 & p2 & g0 | p2 & g1 | g2;
  assign s[3] = a[3] ^ b[3] ^ c3;
  
  assign P0 = p0 && p1 && p2 && p3;
  assign G0 = (g0 && p1 && p2 && p3) || (g1 && p2 && p3) || (g2 && p3) || g3;
endmodule

module prediction1(input G0,G1,P1, output c8);
  assign c8 = G0 && P1 || G1 ;
endmodule 

module prediction2(input G0,G1,P1,G2,P2, output c12);
  assign c12 = (G0 && P1 && P2) || (G1 && P2) || G2 ;
endmodule 

module prediction3(input G0,G1,P1,G2,P2,G3,P3, output c16);
  assign c16 = G0 && P1 && P2 && P3 || 
    G1 && P1 && P2  || G2 && P2 || G3 ;
endmodule 

module toplevel(input [15:0]a, 
                input [15:0]b, 
                output [15:0] o);
  
  logic P0, G0, c4;
  block b0(a[3:0],b[3:0],0,o[3:0],P0,G0);
  
  logic P1,G1, c8;
  block b1(a[7:4],b[7:4],G0,o[7:4],P1,G1);
  prediction1 pred1(G0,G1,P1,c8);
  
  logic P2,G2,c12;
  block b2(a[11:8],b[11:8],c8,o[11:8],P2,G2);
  prediction2 pred2(G0,G1,P1,G2,P2,c12);
  
  logic P3,G3,c16;
  block b3(a[15:12],b[15:12],c12,o[15:12],P3,G3);
  prediction3 pred3(G0,G1,P1,G2,P2,G3,P3,c16);
endmodule
