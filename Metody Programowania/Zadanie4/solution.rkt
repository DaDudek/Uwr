#lang racket
;;współpraca Jakub Przydatek
(define (merge list1 list2)
  (define len1 (length list1))
  (define len2 (length list2))
  (define (merge_iter  new_list i j) ;; lacze uzywajac wskaznikow
    (cond [(and (= i len1) (= j len2)) new_list]
          [(and (= i len1) (< j len2)) (merge_iter (append new_list (list (list-ref list2 j))) i (+ 1 j))]
          [(and (= j len2) (< i len2)) (merge_iter (append new_list (list (list-ref list1 i))) (+ i 1) j)]
          [(< (list-ref list1 i) (list-ref list2 j)) (merge_iter (append new_list (list (list-ref list1 i))) (+ 1 i) j)]
          [else (merge_iter (append new_list (list (list-ref list2 j))) i (+ 1 j))]))
  (merge_iter (list) 0 0))

(merge (list 1 6 8 9 10 231) (list 2 4 5 6 8 11 13 14))
    
(define (split list-to-split)
  (define even? (if (= (modulo (length list-to-split) 2) 0)
                    #t
                    #f)) ;; szukam polowy
  (define where-split (if even?
                   (/ (length list-to-split) 2)
                   (floor (/ (length list-to-split) 2))))
  
  (define (split-iter i l1 l2 start-list)
    (if (= i where-split)
        (cons l1 start-list)
        (split-iter (+ 1 i) (append l1 (list(car start-list))) l2 (cdr start-list))))
  (split-iter 0 (list) (list) list-to-split))

(split (list 1 6 8 9 10 231 ))

(define (mergesort list-to-sort) ;; wykorzystuje split i merge
  (if (>= 1 (length list-to-sort))
      list-to-sort
      (let (
             [splitted (split list-to-sort)])
       (merge (mergesort (car splitted)) (mergesort (cdr splitted))))))


(provide merge split mergesort)


(mergesort (list 1 2 64 2 123 6 7 2))
(mergesort (list 4 2 1 3))
(mergesort (list 4 2 1 3 8 6 32 231 5 36 1231 ))
(mergesort (list 17 3 1 14 2 9 10 11 0))
(mergesort (list))
(mergesort (list 1))
(mergesort (list 1 1 1 1 1 1 ))
(split (list))


(split (list 1 2 3 4 5))
(split (list 1 2 3 4))