## Syntax

> [!definition] Private Information Retrieval
> A (single-server) polylogarithmic private information retrieval (PIR) scheme consists of a triple of algorithms $(\text{PEnc}, \text{PEval}, \text{PDec})$ that work as follow:
> - $\text{PEnc}(i, r)$: Outputs an encryption $C_i$ of query $i$ to a database $\text{DB}$ using randomness $r$,
> - $\text{PEval}(\text{DB}, C_i)$: Outputs a succinct blob $e_i$ "containing" the answer $\text{DB}[i]$,
> - $\text{PDec}(e_i)$: Decrypts the blob $e_i$ to an answer $\text{DB}[i]$.

