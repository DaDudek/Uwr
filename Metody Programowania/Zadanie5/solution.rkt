#lang racket
(define (partition n xs) ;; rozdziela liste
  (define (partition-iter i l1 l2)
    (if (= i (length xs))
        (cons l1 l2)
        (if (<= (list-ref xs i) n)
            (partition-iter (+ i 1) (append l1 (list( list-ref xs i))) l2)
            (partition-iter (+ i 1) l1 (append l2 (list( list-ref xs i)))))))
  (partition-iter 0 (list) (list)))

(partition 6 (list 1 2 3 4 5 7 8 2 1 5 74 5 6))

(define (quicksort xs) ; sortuje
  (if (>= 1 (length xs))
      xs
      (let (
            [parts (partition (car xs) (cdr xs))])
        (append (quicksort (car parts)) (list (car xs)) (quicksort (cdr parts))))))

(quicksort (list 1 5 2))
(quicksort (list 1 5234 25 76 2 234 884 6))
(quicksort (list 1 5 2 235 8 5543 3))

(quicksort (list 11  5252  9754 463 213 754   5 2))


(quicksort (list 1 5 14 26 689 9  434 23 4256 2 22 9 5636 2124))
(quicksort (list 1 1 1 1 1 1 1 1 1 1  1 1 1 1 2))

          
(provide partition quicksort)
           
