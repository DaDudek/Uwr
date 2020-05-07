class Fixnum
    def czynniki
        tab = []
        counter  = 1
        while counter <= self
            if self % counter == 0
                tab << counter
            end
			counter = counter + 1
        end
        return tab
    end

	def ack(y)
		if self == 0 
			return y +1
		elsif y == 0
			return (self-1).ack(1)
		else
			return (self-1).ack(self.ack(y-1))
		end
	end

	def doskonala
		suma = 0
		czynniki = self.czynniki
		for czynnik in czynniki
			if czynnik < self
				suma = suma + czynnik
			end
		end
		if suma == self
			return true
		else
			return false
		end
	end

	def slownie
		dict = {
		0 => "zero",
		1 => "jeden",
		2 => "dwa",
		3 => "trzy",
		4 => "cztery",
		5 => "piec",
		6 => "szesc",
		7 => "siedem",
		8 => "osiem",
		9 => "dziewiec"
		}

	tmp = self
	score = ''

	while tmp > 0
		letter = tmp % 10;
		score = dict[letter] + " " + score
		tmp = tmp / 10
	end

	return score
	end
end


$\ = "\n"
print 15.czynniki
print 100.czynniki
print 2.czynniki
print 6.czynniki
print 2.ack(1)
print 6.doskonala
print 28.doskonala
print 5.doskonala
print 123.slownie

