#lang racket
(require rackunit)
(require rackunit/text-ui)
(require "leftist.rkt")

;WSPÓŁPRACA JAKUB PRZYDATEK

;;; heapsort. sorts a list of numbers.
(define (heapsort xs) ; na poczatku przerabiamy liste na kopiec - bierzemy pierwszy element listy, wkładamy do kopca i powtarzamy rekurencyjnie dla (cdr lista)
  (define (list-to-heap xs heap)
    (if (null? xs)
        heap
        (list-to-heap (cdr xs) (heap-insert (make-elem (car xs) (car xs)) heap))))
  (define (find-and-remove-min heap) ; jako ze umiemy znajdowac minimalny element oraz go usuwac to mozemy pobierac aktualne min az oproznimy caly kopiec
    (if (heap-empty? heap)
        null
        (cons (elem-val (heap-min heap)) (find-and-remove-min (heap-pop heap)))))
    (find-and-remove-min (list-to-heap xs empty-heap)))


;;; check that a list is sorted (useful for longish lists)
(define (sorted? xs)
  (cond [(null? xs)              true]
        [(null? (cdr xs))        true]
        [(<= (car xs) (cadr xs)) (sorted? (cdr xs))]
        [else                    false]))

(provide heapsort)


;testy
(define heap-sort-tests
  (test-suite "heap-sort-procedure-tests"
              (test-case "heap-sort-test-number-1"
                         (sorted? (heapsort (list))))
             
              (test-case "heap-sort-test-number-2"
                         (sorted? (heapsort (list 1 2 3 4 5 6 7 0))))
             
              (test-case "heap-sort-test-number-3"
                         (sorted? (heapsort (list 1 1 1 1 1 1))))
             
              (test-case "heap-sort-test-number-4"
                         (sorted? (heapsort (list 8 7 6 5 4 3 2 1 ))))
             
              (test-case "heap-sort-test-number-5"
                         (sorted? (heapsort (list 2 15 7 8 1 6 8 4))))
             
              (test-case "heap-sort-test-number-6"
                         (sorted? (heapsort (list 1 2 4 6 0 6 2 2414 5236 73456 121 2541))))
             
              (test-case "heap-sort-test-number-7"
                         (sorted? (heapsort (list 0 1 0 1 0 1 0 1 0 1 0 1 0 1))))
              ))
 
(run-tests heap-sort-tests)