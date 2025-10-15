def main( ):


    abc = [['a1', 'b1', 'c1'], 
           ['a2', 'b2', 'c2'], 
           ['a3', 'b3', 'c3'], ]
        
    xyz = [['x1', 'y1', 'z1'], 
           ['x2', 'y2', 'z2'], 
           ['x3', 'y3', 'z3'], ]    
    
    result = [ ['', '', ''], 
               ['', '', ''], 
               ['', '', ''], ]  
    
    for row_abc in range(len(abc)):
        for row_xyz in range(len(xyz)):
            for col in range(len(xyz[0])):
                result[row_abc][row_xyz] = result[row_abc][row_xyz] + abc[row_abc][col] +"*"+ xyz[col][row_xyz] + " + " 
            else: 
                result[row_abc][row_xyz] = result[row_abc][row_xyz][:-3]
    
    for i in range(len(result)):
        print(result[i])

main( )