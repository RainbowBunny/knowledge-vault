There are many excellent texts on the general topic of algorithms, including those by 
Aho, Hopcroft, and Ullman [5, 6]; 
Baase and Van Gelder [28]; 
Brassard and Bratley [55]; 
Dasgupta, Papadimitriou, and Vazirani [83]; 
Goodrich and Tamassia [148]; 
Hofri [175]; 
Horowitz, Sahni, and Rajasekaran [181]; 
Johnsonbaugh and Schaefer [193]; 
Kingston [205]; 
Kleinberg and Tardos [208]; 
Knuth [209, 210, 211]; 
Kozen [220]; 
Levitin [235]; 
Manber [242]; 
Mehlhorn [249, 250, 251]; 
Purdom and Brown [287]; 
Reingold, Nievergelt, and Deo [293]; 
Sedgewick [306]; 
Sedgewick and Flajolet [307]; 
Skiena [318]; 
and Wilf [356]. 
Some of the more practical aspects of algorithm design are discussed by 
Bentley [42, 43] and Gonnet [145]. 
Surveys of the field of algorithms can also be found in the Handbook of Theoretical Computer Science, Volume A [342] and the CRC Algorithms and Theory of Computation Handbook [25]. 
Overviews of the algorithms used in computational biology can be found in textbooks by Gusfield [156], Pevzner [275], Setubal and Meidanis [310], and Waterman [350].

The early history of proving programs correct is described by Gries [153], who credits P. Naur with the first article in this field. Gries attributes loop invariants to R. W. Floyd. The textbook by Mitchell [256] describes more recent progress in proving programs correct.

The  and ‚ notations were advocated by Knuth [213] to correct the popular, but technically sloppy, practice in the literature of using O-notation for both upper and lower bounds

Equation (3.20) is due to Robbins [297]

Abramowitz and Stegun [1] or Zwillinger [362], or in a calculus book, such as Apostol [18] or Thomas et al. [334]. Knuth [209] and Graham, Knuth, and Patashnik [152] contain a wealth of material on discrete mathematics as used in computer science.

Bollob´as [54], Hofri [174], and Spencer [321] contain a wealth of advanced probabilistic techniques. The advantages of randomized algorithms are discussed and surveyed by Karp [200] and Rabin [288]. The textbook by Motwani and Raghavan [262] gives an extensive treatment of randomized algorithms. Several variants of the hiring problem have been widely studied. These problems are more commonly referred to as “secretary problems.” An example of work in this area is the paper by Ajtai, Meggido, and Waarts [11].

The heapsort algorithm was invented by Williams [357], who also described how to implement a priority queue with a heap. The BUILD-MAX-HEAP procedure was suggested by Floyd [106]. We use min-heaps to implement min-priority queues in Chapters 16, 23, and 24. We also give an implementation with improved time bounds for certain operations in Chapter 19 and, assuming that the keys are drawn from a bounded set of nonnegative integers, Chapter 20. If the data are b-bit integers, and the computer memory consists of addressable b-bit words, Fredman and Willard [115] showed how to implement MINIMUM in O.1/ time and INSERT and EXTRACT-MIN in O.p lg n/ time. Thorup [337] has improved the O.p lg n/ bound to O.lg lg n/ time. This bound uses an amount of space unbounded in n, but it can be implemented in linear space by using randomized hashing. An important special case of priority queues occurs when the sequence of EXTRACT-MIN operations is monotone, that is, the values returned by successive EXTRACT-MIN operations are monotonically increasing over time. This case arises in several important applications, such as Dijkstra’s single-source shortestpaths algorithm, which we discuss in Chapter 24, and in discrete-event simulation. For Dijkstra’s algorithm it is particularly important that the DECREASE-KEY operation be implemented efficiently. For the monotone case, if the data are integers in the range 1; 2; : : : ; C, Ahuja, Mehlhorn, Orlin, and Tarjan [8] describe how to implement EXTRACT-MIN and INSERT in O.lg C / amortized time (see Chapter 17 for more on amortized analysis) and DECREASE-KEY in O.1/ time, using a data structure called a radix heap. The O.lg C / bound can be improved to O.p lg C / using Fibonacci heaps (see Chapter 19) in conjunction with radix heaps. Cherkassky, Goldberg, and Silverstein [66] further improved the bound to O.lg1=3C C / expected time by combining the multilevel bucketing structure of Denardo and Fox [86] with the heap of Thorup mentioned earlier. Raman [291] further improved these results to obtain a bound of O.min.lg1=4C C; lg1=3C n//, for any fixed  > 0.