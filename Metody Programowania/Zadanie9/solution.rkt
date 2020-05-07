#lang racket
;WSPÓŁPRACA DAWID DUDEK JAKUB PRZYDATEK PIOTR GUNIA
(provide (struct-out complex) parse eval)

(struct complex (re im) #:transparent)

(define value?
  complex?)



(struct const (val)    #:transparent)
(struct binop (op l r) #:transparent)
(struct variable () #:transparent) ; aby móc w abstrakcyjnej mieć i

(define (op->proc op)
  (match op ['+ +] ['- -] ['* *] ['/ /]))

(define (eval e)
  (match e
    [(const n) (complex n 0)]
    [(variable) (complex 0 1)]
    [(binop '+ l r)  (let* ((l (eval l))
                            (r (eval r)))
                       (complex (+ (complex-re l) (complex-re r))
                                (+ (complex-im l) (complex-im r))))]
    [(binop '- l r)  (let* ((l (eval l))
                            (r (eval r)))
                       (complex (- (complex-re l) (complex-re r))
                                (- (complex-im l) (complex-im r))))]
    [(binop '* l r)  (let* ((l (eval l)) ;; zwykle mnozenie nawiasow (a +b ) * (c + d)
                            (r (eval r)))
                       (complex (- (* (complex-re l) (complex-re r)) (* (complex-im l) (complex-im r)))
                                (+ (* (complex-re l) (complex-im r)) ( *(complex-im l) (complex-re r)))))]
    

    [(binop '/ l r) (let* ((l (eval l)) ; wzór na dzielenie liczb zespolonych znalazłem w internecie jednak zdaje mi się, że pojawił się on również na analizie matematycznej
                           (r (eval r)))
                      (complex (/ (+ (* (complex-re l) (complex-re r)) (* (complex-im l) (complex-im r)))
                                  (+ (* (complex-re r) (complex-re r)) (* (complex-im r) (complex-im r))))
                               (/ (- (* (complex-im l) (complex-re r)) (* (complex-re l) (complex-im r)))
                                  (+ (* (complex-re r) (complex-re r)) (* (complex-im r) (complex-im r))))))]))
(define (parse q)
  (cond [(number? q) (const q)]
        [(eq? q 'i) (variable)] ; aby obsluzyc "i" w konkretnej
        [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
         (binop (first q) (parse (second q)) (parse (third q)))]))

"TESTY" 
(eval (parse (list '+  5 2 ))) 
(eval (parse (list '-  5 2 )))
(eval (parse (list '*  5 2 ))) 
(eval (parse (list '/  5 2 )))
(eval (parse (list '+  'i 'i ))) 
(eval (parse (list '-  'i 'i )))
(eval (parse (list '*  'i 'i ))) 
(eval (parse (list '/  'i 'i )))

(eval (parse (list '+  5 (list '* 'i 'i ))))
