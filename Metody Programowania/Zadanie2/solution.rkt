#lang racket
; ZADANIE DOMOWE 10
; WSPÓŁPRACA:  JAKUB PRZYDATEK, MICHAŁ SOBECKI, DAWID DUDEK, SZYMON RYSZ


(define (cont-frac num den)
    
(define (dist x y) ; funkcja pomocnicza
    (abs (- x y)))
  
  (define (good-enough? a b) ; funkcja pomocnicza sprawdza czy przyblizenie dostateczne
    (< (dist a b)
       0.0000003))

  (define (count-k-fraction a b next-a next-b k) ; funkcja glowna
      
    (define (count-pattern x prev-x) ; funkcja pomocnicza oblicz an/bn
      (+ (* (den k)
            x)
         (* (num k)
            prev-x)))
  
    (if (good-enough? (/ a b) (/ next-a next-b)) ; glowna logika - jesli przyblizenie dostateczne to je zwraca
        (/ a b)
        (count-k-fraction next-a
                          next-b
                          (count-pattern next-a a ) ; w.p.p wyoluje sama siebie ze zmienonymi argumentami
                          (count-pattern next-b b) ; calosc dziala iteracyjnie bo nie musi czekac na obliczenie poprzednich wyrazow tylko
                          (+ 1 k)))) ; oblicza sie na biezaco az do dostatecznie dobrego przyblizenia (kolejne wywolania maja taka sama "dlugosc")
  (count-k-fraction 1.0   
                    0.0  ; wywolanie ze startowymi wartosciami
                    0.0
                    1.0
                    1))


(define (atan-cf x) ; funkcja na podstawie pracowni
  (define (den k)
        (+(- 0 1) (* 2 k))
        )
  
  (define (num k)
    (if (= k 1 )
        x
        ((lambda (x) (* x x)) (* x (- k 1)))))  ; funkcja na podstawie pracowni
  
  (cont-frac num den))

(define (pi); funkcja na podstawie pracowni
  (define (square x) (* x x))
  (define (dens k)
  6)
(define (nums k)
  (define (numcounter)
    (square (+ (- 0 1) (* 2 k))))
  (numcounter))
  (+ 3 (cont-frac nums dens)))

(define (count-gold-fraction)
  (cont-frac (lambda(i) 1.0) (lambda(i) 1.0))) ; test iteracji

(provide cont-frac)

; testy dla x> 13 funkcja nie jest zbiezna
; atan-cf funkcja wlasna, atan - funkcja wbudowana
(atan-cf 1)
(atan 1)
0
(atan-cf 2)
(atan 2)
0
(atan-cf 3)
(atan 3)
0
(atan-cf 4)
(atan 4)
0
(atan-cf 5)
(atan 5)
0
(atan-cf 6)
(atan 6)
0
(atan-cf 7)
(atan 7)
0
(atan-cf 13)
(atan 13)

(pi) ; obliczenie pi jako ułamka łancuchowego +3

(count-gold-fraction) ; 1/x gdzie x=zloty podzial





