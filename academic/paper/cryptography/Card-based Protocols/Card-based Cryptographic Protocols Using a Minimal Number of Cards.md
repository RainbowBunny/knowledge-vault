---
parent: "[[Fleeting MOC]]"
tags:
  - 🪴weedy
authors: Alexander Koch, Stefan Walzer, and Kevin Härtel
date: 2025-09-24T10:10
---

## Abstract

Abstract. Secure multiparty computation can be done with a deck of playing cards. For example, den [[More Efficient Match-Making and Satisfiability The Five Card Trick|Boer (EUROCRYPT ’89)]] devised his famous “five-card trick”, which is a secure two-party AND protocol using five cards. However, **the output of the protocol is revealed in the process and it is therefore not suitable for general circuits with hidden intermediate results**. To overcome this limitation, protocols in committed format, i.e., with concealed output, have been introduced, among them the six-card AND protocol of ([Mizuki and Sone, FAW 2009]). In their paper, the authors ask whether six cards are minimal for committed format AND protocols. We give a comprehensive answer to this problem: there is a four-card AND protocol with a runtime that is finite in expectation (i.e., a Las Vegas protocol), but no protocol with finite runtime. Moreover, we show that five cards are sufficient for finite runtime. In other words, improving on ([Mizuki, Kumamoto, and Sone, ASIACRYPT 2012]) “The Five-Card Trick can be done with four cards”, our results can be stated as “The Five-Card Trick can be done in committed format” and furthermore it “can be done with four cards in Las Vegas committed format”. By devising a Las Vegas protocol for any k-ary boolean function using 2k cards, we address the open question posed by ([Nishida et al., TAMC 2015]) on whether 2k + 6 cards are necessary for computing any k-ary boolean function. For this we use the shuffle abstraction as introduced in the computational model of card-based protocols in ([Mizuki and Shizuya, Int. J. Inf. Secur., 2014]). We augment this result by a discussion on implementing such general shuffle operations.
## Content

**My first thought of the paper:**

The objective of the paper is clear:
-  introduce a four-card Las Vegas protocol for the AND of two players’ bits, –
- give a five-card variant, which has an a priori bound on the number of execution steps, i.e., a finite-runtime protocol, 
- show that this is optimal, as four-card finite-runtime protocols computing AND in committed format are impossible, 
- define a method of enriching the description of a protocol, that makes correctness and security transparent and gives a good understanding of how these protocols work, which can be used as a leverage to devise impossibility results. We therefore believe that this method is of general interest for research in card-based cryptography, 
- state a general 2k-card protocol for any k-ary boolean function, which can be seen as a touchstone for the practicability of the underlying computational model, –
- discuss the computational model of [MS14a] briefly