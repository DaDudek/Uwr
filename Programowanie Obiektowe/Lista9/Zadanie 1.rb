class Funkcja
	def initialize(procedure)
		@proc = procedure
	end

	def value(x)
		@proc.call(x)
	end

	def zerowe(a, b, e)
		if(value(a) * value(b) > 0)
			nil
		elsif (value(a) == 0)
			a
		elsif (value(b) == 0)
			b
		end
		if ( (a-b).abs < e)
			nil
		elsif ( value( (a+b)/ 2.0 ) < e)
			(a+b)/ 2.0
		elsif ( value( (a+b)/ 2.0 ) * value(a)  > 0 )
			zerowe( (a+b)/ 2.0 , b, e)
		elsif ( value( (a+b)/ 2.0)  * value(b) > 0)
			zerowe(a, (a+b)/ 2.0, e)
		else
			nil
		end	
	end

	def pole(a,b)
		@@eps = 0.001
		
		if(a>=b)
			0
		else
			((value(a) + value(a + @@eps) ) * @@eps / 2.0) + pole(a+ @@eps, b)
		end
	end

	def poch(x)
		@@epsx = 0.0001
		(value(x + @@epsx) - value(x) ) / @@epsx 

	end
end


f = Funkcja.new(Proc.new{|x| x**2})
puts "Funkcja: x^2"
puts
puts "Pole pod wykresem dla przedziału (1, 2): ", f.pole(1, 2)
puts
puts "Pochodna w punkcie 5: ", f.poch(5)
puts
puts "miejsce zerowe między -3 a 3", f.zerowe(-3,3,001)
puts
