#lang racket
; WSPÓŁPRACA JAKUB PRZYDATEK DAWID DUDEK

(define (inc n)
  (+ n 1))

;;; tagged lists
(define (tagged-list? len-xs tag xs)
  (and (list? xs)
       (= len-xs (length xs))
       (eq? (first xs) tag)))

;;; ordered elements
(define (make-elem pri val)
  (cons pri val))

(define (elem-priority x)
  (car x))

(define (elem-val x)
  (cdr x))

;;; leftist heaps (after Okasaki)

;; data representation

;(hnode element ranga lewe prawe) - reprezentacja kopca
(define leaf 'leaf)

(define (leaf? h) (eq? 'leaf h))

(define (hnode? h)
  (and (tagged-list? 5 'hnode h)
       (natural? (caddr h))))

(define (make-hnode elem heap-a heap-b)
  ;;; ranga lewego poddrzewa jest nie mniejsza niz ranga prawego
  ;;; czyli ranga lewego >= ranga prawego
  (if (>= (rank heap-a) (rank heap-b))
      (list 'hnode elem (inc (rank heap-b)) heap-a heap-b)
      (list 'hnode elem (inc (rank heap-a)) heap-b heap-a)))

(define (hnode-elem h)
  (second h))

(define (hnode-left h)
  (fourth h))

(define (hnode-right h)
  (fifth h))

(define (hnode-rank h)
  (third h))

(define (hord? p h)
  (or (leaf? h)
      (<= p (elem-priority (hnode-elem h)))))

(define (heap? h)
  (or (leaf? h)
      (and (hnode? h)
           (heap? (hnode-left h))
           (heap? (hnode-right h))
           (<= (rank (hnode-right h))
               (rank (hnode-left h)))
           (= (rank h) (inc (rank (hnode-right h))))
           (hord? (elem-priority (hnode-elem h))
                  (hnode-left h))
           (hord? (elem-priority (hnode-elem h))
                  (hnode-right h)))))

(define (rank h)
  (if (leaf? h)
      0
      (hnode-rank h)))


;; operations

(define empty-heap leaf)

(define (heap-empty? h)
  (leaf? h))

(define (heap-insert elt heap)
  (heap-merge heap (make-hnode elt leaf leaf)))

(define (heap-min heap)
  (hnode-elem heap))

(define (heap-pop  heap)
  (heap-merge (hnode-left  heap) (hnode-right  heap)))

(define (heap-merge h1 h2)
  (cond
   [(leaf? h1) h2]
   [(leaf? h2) h1]
   ;; trzeba zaimplementowac dwie mozliwosci - min jest w h1 lub min jest w h2
   [(< (elem-priority (heap-min h1)) (elem-priority (heap-min h2)))
    (make-hnode (heap-min h1)
                (hnode-left h1)
                (heap-merge (hnode-right h1) h2))]
   [else (make-hnode (heap-min h2)
                     (hnode-left h2)
                     (heap-merge (hnode-right h2) h1))]))

(provide make-elem elem-priority elem-val empty-heap heap-insert heap-merge heap-min heap-pop heap-empty? make-hnode)