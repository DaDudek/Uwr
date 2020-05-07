class Jawna
	def initialize(wiadomosc)
		@haslo = wiadomosc
	end

	def zaszyfruj(klucz)
		tmp = ''
		@haslo.each_char do |letter|
			tmp = tmp + klucz[letter]
		end
		return Zaszyfrowana.new(tmp)
	end

	def to_s
		return @haslo
	end
end

class Zaszyfrowana
	def initialize(wiadomosc)
		@haslo = wiadomosc
	end

	def zaszyfruj(klucz)
		tmp = ''
		klucz = klucz.invert
		@haslo.each_char do |letter|
			tmp = tmp + klucz[letter]
		end
		return Jawna.new(tmp)
	end

	def to_s
		return @haslo
	end
end
szyfr = {" " => " ", "a" => "b", "b" => "c", "c" => "d", "d" => "e",
"e" => "f", "f" => "g", "g" => "h", "h" => "i", "i" => "j",
"j" => "k", "k" => "l", "l" => "m", "m" => "n", "n" => "o",
"o" => "p", "p" => "r", "r" => "s", "s" => "t", "t" => "u",
"u" => "v", "v" => "w", "w" => "x", "x" => "y", "y" => "z", "z" => "a"}

jawna = Jawna.new("dawid")
zaszyfrowana = jawna.zaszyfruj(szyfr)
odszyfrowana = zaszyfrowana.zaszyfruj(szyfr)
puts jawna.to_s
puts zaszyfrowana.to_s
puts odszyfrowana.to_s

