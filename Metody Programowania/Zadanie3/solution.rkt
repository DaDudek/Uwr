#lang racket
;WSPÓŁPRACA : JAKUB PRZYDATEK, DAWID DUDEK
(define (repeated p n) ; funkcja napisana w ramach pracowni
  (define (compose f g)
    (lambda (x) (f (g x))))
  (define (identity x) x)
  (if (= n 0)
      (identity p)
      (compose p
               (repeated p (- n 1)))
      ))

(define (average a b) ; funkcja z wykładu 
    (/ (+ a b) 2))

(define (average-damp f) ; kod z wykładu
    (lambda (x)
      (average x (f x))))



(define (fixed-point f first-guess) ; funkcja z podręcznika
  (define tolerance 0.00001) 
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
    (define (try guess)
      (let ([next (f guess)])
        (if (close-enough? guess next)
            next
            (try next))))
  (try first-guess))


(define (nth-pow x n) ; funkcja pomocnicza- wylicza x^n
    (if (= n 1)
        x
        (* x (nth-pow x (- n 1)))))


"TESTY ILOŚCI TŁUMIEŃ"

(define (test-how-many x n how-many)
  (fixed-point ((repeated average-damp how-many) (lambda (y) (/ x (nth-pow y (- n 1))))) 1.0))

"test 1"
;(test-how-many 10000 4 1) 1 to za mało
(test-how-many 10000 4 2)
"test 2"
;(test-how-many 100000 5 1) 1 to za mało
(test-how-many 100000 5 2)
"test 3"
;(test-how-many 32 5 1) 1 to za mało
(test-how-many 32 5 2)



(define (nth-root n x)
  (define (testing-f) ; tworzy transformacje funkcji ktorej punktu stalego bedziemy szukac
    (lambda (y) (/ x (nth-pow y (- n 1))))) 
  (define (good-suppression) ; tworzy wystarczające stłumienie 
    (repeated average-damp (floor (log n 2))))
  (fixed-point ((good-suppression) (testing-f)) 1.0)) ;


(provide nth-root)
"TESTY FUNKCJI"

(nth-root 9 512)
(nth-root 3 216)
(nth-root 6 1000000)
(nth-root 8 6561)




