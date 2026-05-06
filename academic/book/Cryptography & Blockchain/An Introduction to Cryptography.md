
A cipher wheel with mixed up alphabets and with encryption performed using different offsets for different parts of the message is featured in a 15th century monograph by Leon Batista Alberti [58]
[61]
[126, Chapter 7]
For a more detailed proof of the fundamental theorem of arithmetic, see any basic number theory textbook, for example [33, 47, 53, 90, 101, 126]
[126, Chapter 20] or one of the texts [33, 47, 53, 90, 101]
In this section we have barely touched the surface of the history of cryptography from antiquity through the middle of the 20th century. Good starting points for further reading include Simon Singh’s light introduction [128] and David Kahn’s massive and comprehensive, but fascinating and quite readable, book The Codebreakers [58].

**Theorem (Kerckhoff's principle)**: The security of a cryptosystem should depend only on the secrecy of the key, and not on the secrecy of the encryption algorithm itself.

**Definition (Encoding scheme)**: An **encoding scheme** is a method of converting one sort of data into another sort of data.

Do pseudorandom number generators exist? If so, they would provide examples of the one-way functions defined by Diffie and Hellman in their groundbreaking paper [36],

[74].

To learn more about the fascinating history of public key cryptography, see for example [35, 39, 58, 128].

the RSA scheme of Rivest, Shamir, and Adleman [100] and the knapsack scheme of Merkle and Hellman [75]

the knapsack system of Merkle and Hellman was shown to be insecure at practical computational levels [114].


Taher ElGamal in 1985 [38]

[37], [48], [53]

see for example [53, §4.1] or [126, Chapter 21]

As far as is known, taking e = 3 is as secure as taking a larger value of e, although some doubts are raised in [22]

then the theory of continued fractions allows Eve to break RSA. See [17, 18, 19, 136] for details

No one knows whether such a method exists, although see [22] for a suggestion that computing roots modulo N may be easier than factoring N.

Although Carmichael numbers are rather rare, Alford, Granville, and Pomerance [5] proved in 1984 that there are infinitely many of them.

[121, Theorem 10.6].

The most direct proof uses complex analysis; see for example [7, Chapter 13].
[78]
Proof. The original algorithm was published in [1]. Further analysis and refinements may be found in [57]. The monograph [34] contains a nice description of primality testing, including the AKS test.

Revisit Proposition 3.24
Those readers interested in pursuing this subject might consult [26, 32, 99, 137] and the references cited in those works.

An important theorem in this direction was proven by Canfield, Erd˝os, and Pomerance [24]

The theory of continued fractions gives an algorithm for finding such a b . See [26, §10.1] for details.

see Pomerance’s delightful essay “A Tale of Two Sieves” [95].

The index calculus first appears in work of Western and Miller [135] in 1968

[33, 47, 53, 90, 101].

[53, Proposition 5.2.2]

Although not of optimal efficiency, it has the advantage of being easy to understand. (For more efficient methods, see [23], [26, §8.5], or [81].

Pollard [94]

owever, Teske [132, 133] has shown that f is not sufficiently random to give optimal results, and she gives examples of somewhat more complicated functions that work better in practice.

In 1948 and 1949, Claude Shannon published two papers [116, 117] that form the mathematical foundation of modern cryptography

In [117], Shannon develops a theory of security for cryptosystems that assumes that no bounds are placed on the

physicist E.T. Jaynes [54] argued that thermodynamic entropy

the Digital Encryption Standard [83]

Post’s correspondence problem [96].

Stephen Cook’s 1971 paper [28] entitled “The Complexity of Theorem

[43]
[131, Chapters 2 and 3]

Our interest in CVP stems from a famous result of Ajtai and Dwork [4] in

The subject of elliptic curves encompasses a vast amount of mathematics.1 Our aim in this section is to summarize just enough of the basic theory for cryptographic applications. For additional reading, there are a number of survey articles and books devoted to elliptic curve cryptography [14, 63, 72, 125], and many others that describe the number theoretic aspects of the theory of elliptic curves, including [25, 60, 68, 69, 123, 124, 127].

More perspicacious, but less elementary, proofs may be found in [69, 123, 127] and other books on elliptic curves.

Schoof [110] found an algorithm to compute #E(Fp) in time O (log p)6 ,
We will not describe SEA, which uses advanced techniques from the theory of elliptic curves, but see [111].

Hendrik Lenstra Jr. circulated a manuscript describing a new factorization method using elliptic curves. Lenstra’s algorithm [71]

Koblitz [62] and Miller [79] each published their ideas as academic papers, but neither of them pursued the commercial aspects of elliptic curve cryptography

Certicom

Hendrik Lenstra [71] made this analogy precise by devising a factorization algorithm that uses the group law on an elliptic curve E in place of multiplication modulo N.

The proof requires more tools than we have at our disposal; see for example [123, V §2] or [134].

The SEA algorithm and its variants [110, 111] that we mentioned in Remark 5.13 are reasonably efficient at counting the number of points in E(Fq) for any fields with a large number of elements. Satoh [103] devised an alternative method that is often faster than SEA when q = pe for a small prime p and (moderately) large exponent e. Satoh’s original paper dealt only with the case p ≥ 3, but subsequent work [41, 129] covers also the cryptographically important case of p = 2.

[123, Corollary III.6.4].
The key idea, which is due to Victor Miller [80]

Then the following algorithm of Menezes, Okamoto, and Vanstone [73] solves the elliptic curve discrete logarithm problem for P and Q.

. A number of people [104, 112, 130] more or less simultaneously observed that there is a very fast (linear time) algorithm to solve the ECDLP on anomalous elliptic curves, so such curves must be avoided in cryptographic constructions.

See [27, §22.3] for details.

This is possible using a clever pairingbased construction due to Antoine Joux [55, 56].

The idea of ID-based cryptography was initially described by Shamir in 1984 [115], and a practical ID-based system was devised by Boneh and Franklin in 2001 [20, 21]. This system, which we now describe, uses pairings on elliptic curves.

The first attempt to base a cryptosystem on an N P-complete problem1 was made by Merkle and Hellman in the late 1970s [75]

but after the publication of the famous LLL2 lattice reduction paper [70] in 1985, it became clear that knapsackbased cryptosystems have a fundamental weakness

For a proof that SVP is no harder than CVP, see [45], and for a thorough discussion of the complexity of different types of lattice problems, see [77].

For an excellent survey of knapsack cryptosystems, see the article by Odlyzko [93].

but after the publication of the famous LLL2 lattice reduction paper [70] in 1985

The properties of the gamma function are described in real and complex analysis textbooks; see for example [2] or [40]

The most important of these, in alphabetical order, were the Ajtai– Dwork cryptosystem [4], the GGH cryptosystem of Goldreich, Goldwasser, and Halevi [44], and the NTRU cryptosystem proposed by Hoffstein, Pipher, and Silverman [51]

Nguyen and Stern [88] subsequently showed that any practical and efficient implementation of the Ajtai–Dwork system is insecure

but using an idea of Micciancio [76]
Nguyen [86] showed that a transformation of the original GGH encryption scheme reduced the problem to an easier CVP.

The NTRU public key cryptosystem [51], whose original public presentation took place at the Crypto ’96 rump session, is most naturally described in terms of quotients of polynomial rings.

For further details, see [91]

A major advance came in 1982 with the publication of the LLL algorithm [70]

In [8], Babai suggested two ways to use LLL as part of an apprCVP algorithm.

We briefly describe two of these improvements in order to give the reader some idea of how they work and the trade-offs involved. For further reading, see [66, 105, 106, 107, 108, 109]

There are also lattice reduction attacks on RSA in certain situations, see for example [19, 18, 30, 31, 52].

see [84]

(See [6] for an official implementation of ECDSA.)

An algorithm to perform this task was given by Nguyen and Regev [87]

It is not immediately clear that the Gram matrix is sufficient to recover the private basis or to forge signatures, but an adaptation of the Nguyen–Regev attack on GGH signatures [87] leads to a method for recovering an NTRU private signing key using a transcript of just a few hundred signatures; see [89]. Thus the basic NTRU digital signature scheme described in Table 7.5 must be considered insecure. An easy and, so far as is known at present, effective method to make GGH and NTRU digital signatures secure is to introduce small biased perturbations into each signature. For details, see [49, 50].

See [85] for the official government description of SHA.)

In 1979 Rabin [98] introduced a method of public key encryption based on taking square roots modulo a composite modulus N = pq.

(An early padding scheme for RSA that lacked this randomness feature was broken by Bleichenbacher [16]

This crucial assumption, i.e., that hash functions are somehow simultaneously random and deterministic, was introduced by Bellare and Rogaway [12] in 1993. They called security proofs based on this assumption the random oracle model.

An early proposal called the Optimal Asymmetric Encryption Padding (OAEP) scheme was proposed by Bellare and Rogaway in 1994 [13].

Unfortunately, it was shown by Shoup in 2001 [120] that one of the assumptions in the security proof of OAEP was unreasonable, in the sense that it assumed that no amount of probing of a certain piece of information could produce useful information.

(An early padding scheme for RSA that lacked this randomness feature was broken by Bleichenbacher [16] by simply sending a large number of messages and seeing which ones were accepted as valid plaintexts, without even being told their decryptions!)

For some hint of the controversy that this has engendered, see for example [64]. For an overview of this subject we recommend the highly readable survey articles of Koblitz and Menezes [65] and Bellare [11].

Shor’s polynomial-time quantum algorithm [118] for factoring integers and for finding discrete logarithms. The following presentation owes a great deal to Shor’s accessible and beautifully written exposition [119], which would serve as a nice start for the interested reader familiar with the concept of a Hilbert space. For those with a less robust background in mathematics and quantum theory, see for example [59].

[1] M. Agrawal, N. Kayal, and N. Saxena. PRIMES is in P. Ann. of Math. (2), 160(2):781–793, 2004. 
[2] L. V. Ahlfors. Complex Analysis. McGraw-Hill Book Co., New York, third edition, 1978. An introduction to the theory of analytic functions of one complex variable, International Series in Pure and Applied Mathematics. 
[3] M. Ajtai. The shortest vector problem in L2 is NP-hard for randomized reductions (extended abstract). In STOC ’98: Proc. thirtieth annual ACM symposium on Theory of computing, pages 10–19, New York, NY, USA, 1998. ACM Press. 
[4] M. Ajtai and C. Dwork. A public-key cryptosystem with worst-case/averagecase equivalence. In STOC ’97 (El Paso, TX), pages 284–293 (electronic). ACM, New York, 1999. 
[5] W. R. Alford, A. Granville, and C. Pomerance. There are infinitely many Carmichael numbers. Ann. of Math. (2), 139(3):703–722, 1994. 
[6] ANSI-ECDSA. Public key cryptography for the financial services industry: The elliptic curve digital signature algorithm (ECDSA). ANSI Report X9.62, American National Standards Institute, 1998. 
[7] T. M. Apostol. Introduction to Analytic Number Theory. Springer-Verlag, New York, 1976. Undergraduate Texts in Mathematics. 
[8] L. Babai. On Lov´asz’ lattice reduction and the nearest lattice point problem. Combinatorica, 6(1):1–13, 1986. 
[9] E. Bach. Explicit bounds for primality testing and related problems. Math. Comp., 55(191):355–380, 1990. 
[10] E. Bach and J. Shallit. Algorithmic Number Theory. Vol. 1. Foundations of Computing Series. MIT Press, Cambridge, MA, 1996. Efficient algorithms. 
[11] M. Bellare. Practice oriented provable-security. In Proceedings of the First International Workshop on Information Security—ISW ’97, volume 1396 of Lecture Notes in Comput. Sci. Springer, Berlin, 1998. 
[12] M. Bellare and P. Rogaway. Random oracles are practical: a paradigm for designing efficient protocols. In Proc. First Annual Conf. Computer and Communications Security, pages 62–73. 1993. 
[13] M. Bellare and P. Rogaway. Optimal asymmetric encryption. In Advances in Cryptology—EUROCRYPT ’94 (Perugia), volume 950 of Lecture Notes in Comput. Sci., pages 92–111. Springer, Berlin, 1995. 
[14] I. F. Blake, G. Seroussi, and N. P. Smart. Elliptic Curves in Cryptography, volume 265 of London Mathematical Society Lecture Note Series. Cambridge University Press, Cambridge, 2000.
[15] G. Blakley. Safeguarding cryptographic keys. In Proceedings of AFIPS National Computer Conference (Zurich), volume 48, pages 313–317. 1979. 
[16] D. Bleichenbacher. Chosen ciphertext attacks against protocols based on RSA encryption standard PKCS #1. In Advances in cryptology—CRYPTO 1998 (Santa Barbara, CA), volume 1462 of Lecture Notes in Comput. Sci., pages 1–12. Springer, Berlin, 1998. 
[17] J. Bl¨omer and A. May. Low secret exponent RSA revisited. In Cryptography and Lattices (Providence, RI, 2001), volume 2146 of Lecture Notes in Comput. Sci., pages 4–19. Springer, Berlin, 2001. 
[18] D. Boneh and G. Durfee. Cryptanalysis of RSA with private key d less than N0.292. In Advances in Cryptology—EUROCRYPT ’99 (Prague), volume 1592 of Lecture Notes in Comput. Sci., pages 1–11. Springer, Berlin, 1999. 
[19] D. Boneh and G. Durfee. Cryptanalysis of RSA with private key d less than N0.292. IEEE Trans. Inform. Theory, 46(4):1339–1349, 2000. 
[20] D. Boneh and M. Franklin. Identity-based encryption from the Weil pairing. In Advances in Cryptology—CRYPTO 2001 (Santa Barbara, CA), volume 2139 of Lecture Notes in Comput. Sci., pages 213–229. Springer, Berlin, 2001. 
[21] D. Boneh and M. Franklin. Identity-based encryption from the Weil pairing. SIAM J. Comput., 32(3):586–615 (electronic), 2003. 
[22] D. Boneh and R. Venkatesan. Breaking RSA may not be equivalent to factoring (extended abstract). In Advances in Cryptology—EUROCRYPT ’98 (Espoo), volume 1403 of Lecture Notes in Comput. Sci., pages 59–71. Springer, Berlin, 1998. 
[23] R. P. Brent. An improved Monte Carlo factorization algorithm. BIT, 20(2):176–184, 1980. 
[24] E. R. Canfield, P. Erd˝os, and C. Pomerance. On a problem of Oppenheim concerning “factorisatio numerorum”. J. Number Theory, 17(1):1–28, 1983. 
[25] J. W. S. Cassels. Lectures on Elliptic Curves, volume 24 of London Mathematical Society Student Texts. Cambridge University Press, Cambridge, 1991. 
[26] H. Cohen. A Course in Computational Algebraic Number Theory, volume 138 of Graduate Texts in Mathematics. Springer-Verlag, Berlin, 1993. 
[27] H. Cohen, G. Frey, R. Avanzi, C. Doche, T. Lange, K. Nguyen, and F. Vercauteren, editors. Handbook of Elliptic and Hyperelliptic Curve Cryptography. Discrete Mathematics and Its Applications (Boca Raton). Chapman & Hall/CRC, Boca Raton, FL, 2006. 
[28] S. A. Cook. The complexity of theorem-proving procedures. In STOC ’71: Proceedings of the Third Annual ACM Symposium on Theory of Computing, pages 151–158, New York, NY, USA, 1971. ACM. 
[29] D. Coppersmith. Solving homogeneous linear equations over GF(2) via block Wiedemann algorithm. Math. Comp., 62(205):333–350, 1994. 
[30] D. Coppersmith. Small solutions to polynomial equations, and low exponent RSA vulnerabilities. J. Cryptology, 10(4):233–260, 1997. 
[31] D. Coppersmith. Finding small solutions to small degree polynomials. In Cryptography and Lattices (Providence, RI, 2001), volume 2146 of Lecture Notes in Comput. Sci., pages 20–31. Springer, Berlin, 2001. 
[32] R. Crandall and C. Pomerance. Prime Numbers. Springer-Verlag, New York, 2001. 
[33] H. Davenport. The Higher Arithmetic. Cambridge University Press, Cambridge, 1999. References 495 
[34] M. Dietzfelbinger. Primality Testing in Polynomial Time, volume 3000 of Lecture Notes in Computer Science. Springer-Verlag, Berlin, 2004. From randomized algorithms to “PRIMES is in P”. 
[35] W. Diffie. The first ten years of public key cryptology. In Contemporary Cryptology, pages 135–175. IEEE, New York, 1992. 
[36] W. Diffie and M. E. Hellman. New directions in cryptography. IEEE Trans. Information Theory, IT-22(6):644–654, 1976. 
[37] D. S. Dummit and R. M. Foote. Abstract Algebra. John Wiley & Sons Inc., Hoboken, NJ, third edition, 2004. 
[38] T. ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithms. IEEE Trans. Inform. Theory, 31(4):469–472, 1985. 
[39] J. Ellis. The story of non-secret encryption, 1987 (released by CSEG in 1997). http://www.cesg.gov.uk/ellisdox.ps. 
[40] W. Fleming. Functions of Several Variables. Springer-Verlag, New York, second edition, 1977. Undergraduate Texts in Mathematics. 
[41] M. Fouquet, P. Gaudry, and R. Harley. An extension of Satoh’s algorithm and its implementation. J. Ramanujan Math. Soc., 15(4):281–318, 2000. 
[42] J. Fraleigh. A First Course in Abstract Algebra. Addison Welsley, seventh edition, 2002. 
[43] M. R. Garey and D. S. Johnson. Computers and Intractability. W. H. Freeman and Co., San Francisco, Calif., 1979. A guide to the theory of NPcompleteness, A Series of Books in the Mathematical Sciences. 
[44] O. Goldreich, S. Goldwasser, and S. Halevi. Public-key cryptosystems from lattice reduction problems. In Advances in Cryptology—CRYPTO ’97 (Santa Barbara, CA, 1997), volume 1294 of Lecture Notes in Comput. Sci., pages 112–131. Springer, Berlin, 1997. 
[45] O. Goldreich, D. Micciancio, S. Safra, and J.-P. Seifert. Approximating shortest lattice vectors is not harder than approximating closest lattice vectors. Inform. Process. Lett., 71(2):55–61, 1999. 
[46] G. R. Grimmett and D. R. Stirzaker. Probability and Random Processes. Oxford University Press, New York, 3rd edition, 2001. 
[47] G. H. Hardy and E. M. Wright. An Introduction to the Theory of Numbers. The Clarendon Press Oxford University Press, New York, fifth edition, 1979. 
[48] I. N. Herstein. Topics in Algebra. Xerox College Publishing, Lexington, Mass., second edition, 1975. 
[49] J. Hoffstein, N. Howgrave-Graham, J. Pipher, J. H. Silverman, and W. Whyte. NTRUSign: digital signatures using the NTRU lattice. In Topics in cryptology—CT-RSA 2003, volume 2612 of Lecture Notes in Comput. Sci., pages 122–140. Springer, Berlin, 2003. extended version http://www.ntru.com/cryptolab/pdf/NTRUSign-preV2.pdf. 
[50] J. Hoffstein, N. Howgrave-Graham, J. Pipher, J. H. Silverman, and W. Whyte. Performance improvements and a baseline parameter generation algorithm for NTRUSign. Cryptology ePrint Archive, Report 2005/274, 2005. http://eprint.iacr.org/. 
[51] J. Hoffstein, J. Pipher, and J. H. Silverman. NTRU: a ring-based public key cryptosystem. In Algorithmic Number Theory (Portland, OR, 1998), volume 1423 of Lecture Notes in Comput. Sci., pages 267–288. Springer, Berlin, 1998. 
[52] N. Howgrave-Graham. Approximate integer common divisors. In Cryptography and Lattices (Providence, RI, 2001), volume 2146 of Lecture Notes in Comput. Sci., pages 51–66. Springer, Berlin, 2001. 496 References 
[53] K. Ireland and M. Rosen. A Classical Introduction to Modern Number Theory, volume 84 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1990. 
[54] E. T. Jaynes. Information theory and statistical mechanics. Phys. Rev. (2), 106:620–630, 1957. 
[55] A. Joux. A one round protocol for tripartite Diffie-Hellman. In Algorithmic number theory (Leiden, 2000), volume 1838 of Lecture Notes in Comput. Sci., pages 385–393. Springer, Berlin, 2000. 
[56] A. Joux. A one round protocol for tripartite Diffie-Hellman. J. Cryptology, 17(4):263–276, 2004. 
[57] L. H. W. Jr. and P. C. Primality testing with Gaussian periods. preprint, March 2003. 
[58] D. Kahn. The Codebreakers: The Story of Secret Writing. Scribner Book Company, 1996. 
[59] P. Kaye, R. Laflamme, and M. Mosca. An Introduction to Quantum Computing. Oxford University Press, Oxford, 2007. 
[60] A. W. Knapp. Elliptic Curves, volume 40 of Mathematical Notes. Princeton University Press, Princeton, NJ, 1992. 
[61] D. Knuth. The Art of Computer Programming, Vol. 2: Seminumerical Algorithms. Addison-Wesley, Reading, Mass., 2nd edition, 1981. 
[62] N. Koblitz. Elliptic curve cryptosystems. Math. Comp., 48(177):203–209, 1987. 
[63] N. Koblitz. Algebraic Aspects of Cryptography, volume 3 of Algorithms and Computation in Mathematics. Springer-Verlag, Berlin, 1998. 
[64] N. Koblitz. The uneasy relationship between mathematics and cryptography. Notices Amer. Math. Soc., 54:972–979, 2007. 
[65] N. Koblitz and A. J. Menezes. Another look at “provable security”. J. Cryptology, 20(1):3–37, 2007. 
[66] J. C. Lagarias, H. W. Lenstra, Jr., and C.-P. Schnorr. Korkin–Zolotarev bases and successive minima of a lattice and its reciprocal lattice. Combinatorica, 10(4):333–348, 1990. 
[67] B. A. LaMacchia and A. M. Odlyzko. Solving large sparse linear systems over finite fields. In Advances in Cryptology—CRYPTO ’90 (Santa Barbara, Calif., 1990), Lecture Notes in Comput. Sci. Springer, Berlin, 1990. 
[68] S. Lang. Elliptic Curves: Diophantine Analysis, volume 231 of Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer-Verlag, Berlin, 1978. 
[69] S. Lang. Elliptic Functions, volume 112 of Graduate Texts in Mathematics. Springer-Verlag, New York, 2nd edition, 1987. With an appendix by J. Tate. 
[70] A. K. Lenstra, H. W. Lenstra, Jr., and L. Lov´asz. Factoring polynomials with rational coefficients. Math. Ann., 261(4):515–534, 1982. 
[71] H. W. Lenstra, Jr. Factoring integers with elliptic curves. Ann. of Math. (2), 126(3):649–673, 1987. 
[72] A. Menezes. Elliptic Curve Public Key Cryptosystems. The Kluwer International Series in Engineering and Computer Science, 234. Kluwer Academic Publishers, Boston, MA, 1993. 
[73] A. J. Menezes, T. Okamoto, and S. A. Vanstone. Reducing elliptic curve logarithms to logarithms in a finite field. IEEE Trans. Inform. Theory, 39(5):1639– 1646, 1993. References 497 
[74] R. C. Merkle. Secure communications over insecure channels. In Secure Communications and Asymmetric Cryptosystems, volume 69 of AAAS Sel. Sympos. Ser., pages 181–196. Westview, Boulder, CO, 1982. 
[75] R. C. Merkle and M. E. Hellman. Hiding information and signatures in trapdoor knapsacks. In Secure Communications and Asymmetric Cryptosystems, volume 69 of AAAS Sel. Sympos. Ser., pages 197–215. Westview, Boulder, CO, 1982. 
[76] D. Micciancio. Improving lattice based cryptosystems using the Hermite normal form. In Cryptography and Lattices (Providence, RI, 2001), volume 2146 of Lecture Notes in Comput. Sci., pages 126–145. Springer, Berlin, 2001. 
[77] D. Micciancio and S. Goldwasser. Complexity of Lattice Problems. The Kluwer International Series in Engineering and Computer Science, 671. Kluwer Academic Publishers, Boston, MA, 2002. A cryptographic perspective. 
[78] G. L. Miller. Riemann’s hypothesis and tests for primality. J. Comput. System Sci., 13(3):300–317, 1976. Working papers presented at the ACM-SIGACT Symposium on the Theory of Computing (Albuquerque, N.M., 1975). 
[79] V. S. Miller. Use of elliptic curves in cryptography. In Advances in Cryptology—CRYPTO ’85 (Santa Barbara, Calif., 1985), volume 218 of Lecture Notes in Comput. Sci., pages 417–426. Springer, Berlin, 1986. 
[80] V. S. Miller. The Weil pairing, and its efficient calculation. J. Cryptology, 17(4):235–261, 2004. Updated and expanded version of unpublished manuscript Short programs for functions on curves, 1986. 
[81] P. L. Montgomery. Speeding the Pollard and elliptic curve methods of factorization. Math. Comp., 48(177):243–264, 1987. 
[82] NBS–AES. Advanced Encryption Standard (AES). FIPS Publication 197, National Bureau of Standards, 2001. http://csrc.nist.gov/publications/ fips/fips197/fips-197.pdf. 
[83] NBS–DES. Data Encryption Standard (DES). FIPS Publication 46-3, National Bureau of Standards, 1999. http://csrc.nist.gov/publications/ fips/fips46-3/fips46-3.pdf. 
[84] NBS–DSS. Digital Signature Standard (DSS). FIPS Publication 186-2, National Bureau of Standards, 2004. http://csrc.nist.gov/publications/ fips/fips180-2/fips180-2withchangenotice.pdf. 
[85] NBS–SHS. Secure Hash Standard (SHS). FIPS Publication 180-2, National Bureau of Standards, 2003. http://csrc.nist.gov/publications/fips/ fips180-2/fips180-2.pdf. 
[86] P. Nguyen. Cryptanalysis of the Goldreich–Goldwasser–Halevi cryptosystem from crypto’97. In Advances in Cryptology—CRYPTO ’99 (Santa Barbara, CA, 1999), volume 1666 of Lecture Notes in Comput. Sci., pages 288–304. Springer, Berlin, 1999. 
[87] P. Nguyen and O. Regev. Learning a parallelepiped: Cryptanalysis of GGH and NTRU signatures. In Advances in Cryptology—EUROCRYPT ’06, volume 4004 of Lecture Notes in Comput. Sci. Springer, Berlin, 2006. 
[88] P. Nguyen and J. Stern. Cryptanalysis of the Ajtai-Dwork cryptosystem. In Advances in Cryptology—CRYPTO ’98 (Santa Barbara, CA, 1998), volume 1462 of Lecture Notes in Comput. Sci., pages 223–242. Springer, Berlin, 1998. 
[89] P. Q. Nguyen. A note on the security of NTRUSign. Cryptology ePrint Archive, Report 2006/387, 2006. http://eprint.iacr.org/.
[90] I. Niven, H. S. Zuckerman, and H. L. Montgomery. An Introduction to the Theory Of Numbers. John Wiley & Sons Inc., New York, 1991. 
[91] Ntru Cryptosystems. A meet-in-the-middle attack on an Ntru private key. Technical report, 1997, updated 2003. Tech. Note 004, www.ntru.com/cryptolab/tech_notes.htm. 
[92] Ntru Cryptosystems. Estimated breaking times for Ntru lattices. Technical report, 1999, updated 2003. Tech. Note 012, www.ntru.com/cryptolab/tech_notes.htm. 
[93] A. M. Odlyzko. The rise and fall of knapsack cryptosystems. In Cryptology and Computational Number Theory (Boulder, CO, 1989), volume 42 of Proc. Sympos. Appl. Math., pages 75–88. Amer. Math. Soc., Providence, RI, 1990. 
[94] J. M. Pollard. Monte Carlo methods for index computation (mod p). Math. Comp., 32(143):918–924, 1978. 
[95] C. Pomerance. A tale of two sieves. Notices Amer. Math. Soc., 43(12):1473– 1485, 1996. 
[96] E. L. Post. A variant of a recursively unsolvable problem. Bull. Amer. Math. Soc., 52:264–268, 1946. 
[97] J. Proos and C. Zalka. Shor’s discrete logarithm quantum algorithm for elliptic curves. Quantum Inf. Comput., 3(4):317–344, 2003. 
[98] M. O. Rabin. Digitized signatures and public-key functions as intractible as factorization. Technical report, MIT Laboratory for Computer Science, 1979. Technical Report LCS/TR-212. 
[99] H. Riesel. Prime Numbers and Computer Methods for Factorization, volume 126 of Progress in Mathematics. Birkh¨auser Boston Inc., Boston, MA, 1994. 
[100] R. L. Rivest, A. Shamir, and L. Adleman. A method for obtaining digital signatures and public-key cryptosystems. Comm. ACM, 21(2):120–126, 1978. 
[101] K. H. Rosen. Elementary Number Theory and Its Applications. AddisonWesley, Reading, MA, 4th edition, 2000. 
[102] S. Ross. A First Course in Probability. Prentice Hall, 6th edition, 2001. 
[103] T. Satoh. The canonical lift of an ordinary elliptic curve over a finite field and its point counting. J. Ramanujan Math. Soc., 15(4):247–270, 2000. 
[104] T. Satoh and K. Araki. Fermat quotients and the polynomial time discrete log algorithm for anomalous elliptic curves. Comment. Math. Univ. St. Paul., 47(1):81–92, 1998. 
[105] C.-P. Schnorr. A hierarchy of polynomial time lattice basis reduction algorithms. Theoret. Comput. Sci., 53(2-3):201–224, 1987. 
[106] C. P. Schnorr. Fast LLL-type lattice reduction. Inform. and Comput., 204(1):1–25, 2006. 
[107] C.-P. Schnorr and M. Euchner. Lattice basis reduction: improved practical algorithms and solving subset sum problems. In Fundamentals of Computation Theory (Gosen, 1991), volume 529 of Lecture Notes in Comput. Sci., pages 68–85. Springer, Berlin, 1991. 
[108] C.-P. Schnorr and M. Euchner. Lattice basis reduction: improved practical algorithms and solving subset sum problems. Math. Programming, 66(2, Ser. A):181–199, 1994. 
[109] C. P. Schnorr and H. H. H¨orner. Attacking the Chor–Rivest cryptosystem by improved lattice reduction. In Advances in Cryptology—EUROCRYPT ’95 (Saint-Malo, 1995), volume 921 of Lecture Notes in Comput. Sci., pages 1–12. Springer, Berlin, 1995. References 499 
[110] R. Schoof. Elliptic curves over finite fields and the computation of square roots mod p. Math. Comp., 44(170):483–494, 1985. 
[111] R. Schoof. Counting points on elliptic curves over finite fields. J. Th´eor. Nombres Bordeaux, 7(1):219–254, 1995. Les Dix-huitiemes Journ´ees Arithm´etiques (Bordeaux, 1993).
[112] I. A. Semaev. Evaluation of discrete logarithms in a group of p-torsion points of an elliptic curve in characteristic p. Math. Comp., 67(221):353–356, 1998. 
[113] A. Shamir. How to share a secret. Comm. ACM, 22(11):612–613, 1979. 
[114] A. Shamir. A polynomial-time algorithm for breaking the basic MerkleHellman cryptosystem. IEEE Trans. Inform. Theory, 30(5):699–704, 1984. 
[115] A. Shamir. Identity-based cryptosystems and signature schemes. In Advances in Cryptology (Santa Barbara, Calif., 1984), volume 196 of Lecture Notes in Comput. Sci., pages 47–53. Springer, Berlin, 1985. 
[116] C. E. Shannon. A mathematical theory of communication. Bell System Tech. J., 27:379–423, 623–656, 1948. 
[117] C. E. Shannon. Communication theory of secrecy systems. Bell System Tech. J., 28:656–715, 1949. 
[118] P. W. Shor. Algorithms for quantum computation: discrete logarithms and factoring. In 35th Annual Symposium on Foundations of Computer Science (Santa Fe, NM, 1994), pages 124–134. IEEE Comput. Soc. Press, Los Alamitos, CA, 1994. 
[119] P. W. Shor. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM J. Comput., 26(5):1484–1509, 1997. 
[120] V. Shoup. OAEP reconsidered. In Advances in Cryptology—CRYPTO 2001 (Santa Barbara, CA), volume 2139 of Lecture Notes in Comput. Sci., pages 239–259. Springer, Berlin, 2001. 
[121] V. Shoup. A Computational Introduction to Number Theory and Algebra. Cambridge University Press, 2005. http://shoup.net/ntb/ntb-b5.pdf. 
[122] C. L. Siegel. A mean value theorem in geometry of numbers. Ann. of Math. (2), 46:340–347, 1945.
[123] J. H. Silverman. The Arithmetic of Elliptic Curves, volume 106 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1986. 
[124] J. H. Silverman. Advanced Topics in the Arithmetic of Elliptic Curves, volume 151 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1994. 
[125] J. H. Silverman. Elliptic curves and cryptography. In Public-Key Cryptography, volume 62 of Proc. Sympos. Appl. Math., pages 91–112. Amer. Math. Soc., Providence, RI, 2005. 
[126] J. H. Silverman. A Friendly Introduction to Number Theory. Prentice Hall, Upper Saddle River, NJ, 3rd edition, 2006. 
[127] J. H. Silverman and J. Tate. Rational Points on Elliptic Curves. Undergraduate Texts in Mathematics. Springer-Verlag, New York, 1992. 
[128] S. Singh. The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography. Knopf Publishing Group, 2000. 
[129] B. Skjernaa. Satoh’s algorithm in characteristic 2. Math. Comp., 72(241):477– 487 (electronic), 2003. 
[130] N. P. Smart. The discrete logarithm problem on elliptic curves of trace one. J. Cryptology, 12(3):193–196, 1999. 
[131] J. Talbot and D. Welsh. Complexity and Cryptography: An Introduction. Cambridge University Press, 2006. 
[132] E. Teske. Speeding up Pollard’s rho method for computing discrete logarithms. In Algorithmic Number Theory (Portland, OR, 1998), volume 1423 of Lecture Notes in Comput. Sci., pages 541–554. Springer, Berlin, 1998. 
[133] E. Teske. Square-root algorithms for the discrete logarithm problem (a survey). In Public-Key Cryptography and Computational Number Theory (Warsaw, 2000), pages 283–301. de Gruyter, Berlin, 2001. 
[134] L. C. Washington. Elliptic Curves: Number Theory and Cryptography. Discrete Mathematics and Its Applications. Chapman & Hall/CRC, 2003. 
[135] A. E. Western and J. C. P. Miller. Tables of Indices and Primitive Roots. Royal Society Mathematical Tables, Vol. 9. Published for the Royal Society at the Cambridge University Press, London, 1968. 
[136] M. J. Wiener. Cryptanalysis of short RSA secret exponents. IEEE Trans. Inform. Theory, 36(3):553–558, 1990. 
[137] S. Y. Yan. Primality Testing and Integer Factorization in Public-Key Cryptography, volume 11 of Advances in Information Security. Kluwer Academic Publishers, Boston, MA, 2004.