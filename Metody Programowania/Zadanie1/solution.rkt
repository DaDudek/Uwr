#lang racket
; kod na podstawie wykładu + podręcznika

(define (cubed x) (* x x x))

(define (dist x y)
  (abs (- x y)))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (cube-root x)
  (define (improve guess)
    (/ (+ (* 2 guess)
          (/ x
             (* guess guess)))
       3))
  (define (good-enough? g)
    (< (dist x (cubed g))
       0.0000003))
  (define (iter guess)
    (if (good-enough? guess)
        guess
        (iter (improve guess))))
  (iter 1.0))

(provide cube-root)

(cube-root 8)
(cube-root 27)
(cube-root -8)
(cube-root (cubed 10))
(cube-root (cubed -10))
(cube-root -27)
(cube-root 7)