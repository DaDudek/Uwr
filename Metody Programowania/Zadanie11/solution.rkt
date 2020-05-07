#lang racket
;WSPÓŁPRACA: DAWID DUDEK, SZYMON RYSZ, PIOTR GUNIA

(provide (struct-out const) (struct-out binop)
         (struct-out var-expr) (struct-out let-expr)
         (struct-out pos) (struct-out var-free)
         (struct-out var-bound) annotate-expression)

;; ---------------
;; Jezyk wejsciowy
;; ---------------

(struct pos (file line col)     #:transparent)
  
(struct const    (val)          #:transparent)
(struct binop    (op l r)       #:transparent)
(struct var-expr (id)           #:transparent)
(struct let-expr (loc id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n)      (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x)   (symbol? x)]
    [(let-expr loc x e1 e2)
     (and (pos? loc) (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (make-pos s)
  (pos (syntax-source s)
       (syntax-line   s)
       (syntax-column s)))

(define (parse e)
  (let ([r (syntax-e e)])
    (cond
      [(number? r) (const r)]
      [(symbol? r) (var-expr r)]
      [(and (list? r) (= 3 (length r)))
       (match (syntax-e (car r))
         ['let (let* ([e-def (syntax-e (second r))]
                      [x     (syntax-e (first e-def))])
                 (let-expr (make-pos (first e-def))
                           (if (symbol? x) x (error "parse error!"))
                           (parse (second e-def))
                           (parse (third r))))]
         [op   (binop op (parse (second r)) (parse (third r)))])]
      [else (error "parse error!")])))

;; ---------------
;; Jezyk wyjsciowy
;; ---------------

(struct var-free  (id)     #:transparent)
(struct var-bound (pos id) #:transparent)

(define (expr-annot? e)
  (match e
    [(const n)         (number? n)]
    [(binop op l r)    (and (symbol? op) (expr-annot? l) (expr-annot? r))]
    [(var-free x)      (symbol? x)]
    [(var-bound loc x) (and (pos? loc) (symbol? x))]
    [(let-expr loc x e1 e2)
     (and (pos? loc) (symbol? x) (expr-annot? e1) (expr-annot? e2))]
    [_ false]))


(define (annotate-expression e)  ; środowisko z wykładu  
  (struct environ (xs)) ;naszą wartością będą locki
  (define env-empty (environ null))
  (define (env-add x loc env) 
    (environ (cons (cons x loc) (environ-xs env))))
  (define (env-lookup x env)
    (define (assoc-lookup xs)
      (cond [(null? xs) #f]
            [(eq? x (car (car xs))) (cdr (car xs))]
            [else (assoc-lookup (cdr xs))]))
    (assoc-lookup (environ-xs env)))
  
;IDEA
; chcemy podzielić zmienne na wolne i związane - jeśli są związane to chcemy rownież wiedzieć gdzie
; musimy zastanowić się co wiąże zmienne - jest to oczywiście let
; wykorzystamy tutaj środowisko - jako że let wiąże zmienną id w e2 to gdy dojdziemy do leta
; to będziemy dodawać do środowiska e2 zmienną id oraz pozycje loc związania
; e1 natomiast ma to samo środowisko ponieważ id nie jest w nim związane tym letem
; w tym momencie gdy dojdziemy do zmiennej wystarczy sprawdzić czy jest w środowisku
  
  (define (helper e env)
    (match e
      [(const n)  (const n)]
      [(binop op l r)  (binop op (helper l env) (helper r env))]
      [(let-expr loc id e1 e2) (let-expr loc 
                                         id 
                                         (helper e1 env)
                                         (helper e2 (env-add id loc env))) ]
      [(var-expr id) (let ([bound (env-lookup id env)])
                       (if (eq? #f bound)
                           (var-free id)
                           (var-bound bound id )))]))
  (helper e env-empty))

(annotate-expression (parse #'(let [x 5] (* y x))))
(annotate-expression (parse #'(+ x (let [y (+ x 1)] (* 2 y)))))