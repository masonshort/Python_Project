class Polynomial:
    def __init__(self, coeff):
        self.coeff = coeff
        
        
    def degree(self):
        return len(self.coeff)-1
    
    
    def __call__(self, x):
        copy_coeff = self.coeff.copy();
        copy_coeff.reverse(); 
        val = 0;
        
        for i in range(len(copy_coeff)):
            val += copy_coeff[i]*(x**i)
        
        return val
    
    
    def __repr__(self):
        string = "";
        n = self.degree();
        for i in self.coeff:
            string += f'{i}x^{n} + ';
            n -= 1;
            
        return string[:-2];
    
    
    def derivative(self):
        n = self.degree();
        der = [];
        for i in self.coeff:
            der.append(i*n);
            n -= 1;
            if n == 0:
                return Polynomial(der);
    
        

