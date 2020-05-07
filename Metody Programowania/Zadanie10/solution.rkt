#lang racket
; WSPÓŁPRACA DAWID DUDEK JAKUB PRZYDATEK PIOTR GUNIA
;; -------------------------------
;; Wyrazenia w odwr. not. polskiej
;; -------------------------------

(provide (struct-out const) (struct-out binop) rpn->arith);
(define (rpn-expr? e) ;; z wykładu
  (and (list? e)
       (pair? e)
       (andmap (lambda (x) (or (number? x) (member x '(+ - * /))))
               e)))

;; ----------------------
;; Wyrazenia arytmetyczne
;; ----------------------

(struct const (val)    #:transparent) ;; z wykładu
(struct binop (op l r) #:transparent)

(define (arith-expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r)
     (and (symbol? op) (arith-expr? l) (arith-expr? r))]
    [_ false]))

;; ----------
;; Kompilacja
;; ----------

(define (rpn->arith e)
  (struct stack (xs))

  (define empty-stack (stack null)) ;; struktura stack z wykładu
  (define (empty-stack? s) (null? (stack-xs s)))
  (define (top s) (car (stack-xs s)))
  (define (push a s) (stack (cons a (stack-xs s))))
  (define (pop s) (stack (cdr (stack-xs s))))

  (define (rpn-converter e s) ;; funkcja własna
    (cond
      [(empty? e) (top s) ] ; jeśli formuła się kończy to zwracam top stosu - jeśli formuła była poprawna to znajduje się tam formuła równoważna w arith
      [(number? (car e)) (rpn-converter (cdr e) (push (const (car e)) s))] ;; jeżeli pierwszy element listy to liczba to ją wrzucamy na stos w postaci const
      [(symbol? (car e)) (let*(
                               (r (top s))
                               (s (pop s))
                               (l (top s))
                               (new-s (pop s)))
                           (rpn-converter (cdr e) (push (binop (car e) l r) new-s)))])) ;; jeśli był to operator to tworzymy wyrażenie z binop
  ;gdzie l to drugi element stosu a r to pierwszy element stosu (top)
  (rpn-converter e empty-stack))

; tutaj mozemy zobaczyc jak dana formula wyglada w arith
(rpn->arith (list 1 2 4 '+ '*))
(rpn->arith (list 1 2 3 '* 4 5 '- 6 7 '+ '- '/ '+))
(rpn->arith (list  1 2 '+ 3 4 '- '* 5 6 '/ '*))
(rpn->arith (list 3 4 5 '+ 2 7 '+ '- '*)) ;test z WDI



(define (eval e) ;; funkcja z wykładu do testów
  (define (op->proc op)
    (match op ['+ +] ['- -] ['* *] ['/ /]))
  (match e
    [(const n) n]
    [(binop op l r) ((op->proc op) (eval l) (eval r))]))


(eval (rpn->arith (list 1 2 4 '+ '*)))
(eval (rpn->arith (list 1 2 3 '* 4 5 '- 6 7 '+ '- '/ '+)))
(eval (rpn->arith (list  1 2 '+ 3 4 '- '*)))
(eval (rpn->arith (list 3 4 5 '+ 2 7 '+ '- '*))) ;test z WDI
(eval (rpn->arith (list 1 2 '-)))
