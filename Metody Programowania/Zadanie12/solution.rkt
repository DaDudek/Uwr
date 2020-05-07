#lang racket
;WSPÓŁPRACA DAWID DUDEK, MICHAŁ SOBECKI ,DOMINIK KOMŁA
; --------- ;
; Wyrazenia ;
; --------- ;
(provide (struct-out const) (struct-out binop) (struct-out var-expr) (struct-out let-expr) (struct-out var-dead) find-dead-vars)

(struct const    (val)      #:transparent)
(struct binop    (op l r)   #:transparent)
(struct var-expr (id)       #:transparent)
(struct var-dead (id)       #:transparent)
(struct let-expr (id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(var-dead x) (symbol? x)]
    [(let-expr x e1 e2) (and (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (parse q)
  (cond
    [(number? q) (const q)]
    [(symbol? q) (var-expr q)]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'let))
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))

; ---------------------------------- ;
; Wyszukaj ostatnie uzycie zmiennych ;
; ---------------------------------- ;

;OBSERWACJE NA POCZĄTEK
;Mamy założenie, że w fornule nie ma zmiennych wolnych, oraz że
;obliczamy wyrażenia od lewej strony.
;zróbmy zatem kilka obserwacji
;stała nie powinna się zmieniać
;jeśli będziemy mieli środowisko tylko żywych zmiennych ( w danym miejscu) 
;to gdy natrafimy na zmienną i mamy ją w środowisku to jest żywa
;w przeciwnym przypadku jest martwa
;zauważmy teraz, że jeśli wystąpił binop i po prawej stronie wystąpią wolne zmienne
;to dzięki naszemu początkowemu założeniu wiemy, że wiązanie nastąpiło wcześniej
;więc dotyczy też lewej strony
;zatem wszystkie zmienne wolne z prawej strony będą żywe w lewej
;zatem możemy zaaktualizować środowisko
;pozostały nam lety - tutaj sytuacja jest podoba z jedną małą zmianą
;chcielibyśmy móc powiedzieć, że let-expr x e1 e2
;możemy policzyć tak że sprawdziwmy zmienne wolne w e2 i one musiały być
;wcześniej związane więc są też w e1 (tak jak w binopie)
;jest jednak jedna mała zmiana - jak szukamy wolnych w e2 to on myśli
;że nas x jest wolny - tak jednak nie jest bo go zwiazalismy
;musimy go zatem wyrzucić ręcznie
;tak samo ze srodowiska e2 trzeba wyrzucic x bo to juz nie jest ten sam x co wczesniej


(define (find-dead-vars e)
  ;srodowisko również z wykładu
  (define env-empty          (set))
  (define (env-add x env)    (set-add env x))
  (define (env-lookup x env) (set-member? env x))
  (define (env-update new env) (set-union env new))
  
  (define (free-vars e)
    (define (free-vars-env e env) ; funkcja z wykładu
      (match e
        [(const n) (set)]
        [(binop op l r)
         (set-union (free-vars-env l env)
                    (free-vars-env r env))]
        [(let-expr x e1 e2)
         (set-union (free-vars-env e1 env)
                    (free-vars-env e2 (env-add x env)))]
        [(var-expr x)
         (if (env-lookup x env)
             (set) (list->set (list x)))]))
    (free-vars-env e env-empty)) 
  
  (define (find-env e env)
    (match e
      [(const n) (const n)]
      [(var-expr x) (if (eq? #f (env-lookup x env))
                        (var-dead x)
                        (var-expr x))]
      [(binop op l r) (binop op (find-env l (env-update env (free-vars r))) (find-env r env))]
      [(let-expr x e1 e2) (let-expr x (find-env e1 (env-update env (set-remove (free-vars e2) x))) (find-env e2 (set-remove env x)))]))
  (find-env e env-empty))



(find-dead-vars (let-expr 'x (const  3)(binop '+ (var-expr 'x) (var-expr 'x)))) ; przykład z listy
(find-dead-vars (let-expr 'x (const  3)(binop '+ (var-expr 'x) (let-expr 'x (const  5)(binop '+ (var-expr 'x)(var-expr 'x)))))) ; przykład z listy
