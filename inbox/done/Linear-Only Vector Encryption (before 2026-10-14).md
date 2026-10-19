Reference:
- https://eprint.iacr.org/2022/1690.pdf

## Syntax

> [!definition] Linear-Only Vector Encryption
> Let $\mathbb F$ be a finite field. A secret-key additively-homomorphic vector encryption scheme over a vector space $\mathbb F^\ell$ consists of a tuple of algorithms $\Pi_\mathsf{Enc} = (\mathsf{Setup}, \mathsf{Enc}, \mathsf{Add}, \mathsf{Dec})$ which are defined as follows:
> - $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$: On input the security parameter $\lambda$ and the plaintext dimension $\ell$, the setup algorithm outputs public parameter $\mathrm{pp}$ and a secret key $\mathrm{sk}$.
> - $\mathbf{C} \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf{v})$: On input the secret key $\mathrm{sk}$ and a vector $\mathbf{v} \in \mathbb F^\ell$, the encryption algorithm output ciphertext $\mathbf{C}$.
> - $\mathbf{C}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathbf{C}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]})$: On input the public parameters, a collection of ciphertexts $\{\mathbf{C}_i\}_{i \in [m]}$ and scalars $\{y_i\} \in \mathbb F, i \in [m]$, the addition algorithm outputs a new ciphertext $\mathbf{c}^*$.
> - $\mathbf{v} / \perp \leftarrow \mathsf{Dec}(\mathrm{sk}, \mathbf{C})$: On input the secret key $\mathrm{sk}$ and a ciphertext $\mathbf{C}$, the decryption algorithm either outputs a vector $\mathbf{v} \in \mathbb F^\ell$ or a special symbol $\perp$.

## Property

### Additive Homomorphism

> [!definition] Additive Homomorphism
> For any adversary $\mathcal A = (\mathcal A_\mathsf{find})$, we define the additive homomorphic advantage:
> $$\mathsf{Adv}_{\Pi_{\mathsf{Enc}}}^{\mathsf{AH}}(\mathcal A) = \Pr\!\left[ 
\begin{array}{l}
\sum_{i \in [m]} y_i v_i = m^*
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell) \\
\{\mathbf{v}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]} \leftarrow \mathcal{A}_\mathsf{find}(\mathrm{pp}, \mathrm{sk}) \\
\{\mathbf{C}_i\}_{i \in [m]} \leftarrow \{\mathsf{Enc}(\mathrm{sk}, \mathbf{v}_i)\}_{i \in [m]} \\
\mathbf{C}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathbf{C}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]}) \\
m^* \leftarrow \mathsf{Dec}(\mathbf{sk}, \mathbf{C}^*)
\end{array} \right]$$

> [!remark]
> We say that the scheme $\Pi_\mathsf{Enc}$ is additively homomorphic with respect to a set $S \in R_p^m$ holds for all $(y_1, \dots, y_m) \in S$.

## Security

### Circuit Privacy

> [!definition] Circuit Privacy
> For any adversary $\mathcal A = (\mathcal{A}_\mathsf{choose}, \mathcal{A}_\mathsf{eval}, \mathcal{A}_\mathsf{guess})$ and simulator $\mathcal S$, we define the circuit privacy advantage:
> $$\mathsf{Adv}_{\Pi_\mathsf{Enc}}^\mathsf{CP}(\mathcal A) = 
\left|\; \Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell) \\
(\mathbf{v}_1, \dots, \mathbf{v}_m) \leftarrow \mathcal{A}_\mathsf{choose}(\mathrm{pp}, \mathrm{sk}) \\
\{\mathbf{C}_i\}_{i \in [m]} \leftarrow \{\mathsf{Enc}(i, \mathrm{sk}, \mathbf{v}_i)\}_{i \in [m]} \\
\{y_i\}_{i \in [m]} \leftarrow \mathcal{A}_\mathsf{eval}(\{\mathbf{C}_i\}_{i \in [m]}) \\
c^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathbf{C}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]}) \\
b \leftarrow \mathcal{A}_\mathsf{guess}(c^*)
\end{array} \right] 
\;- 
\Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell) \\
(\mathbf{v}_1, \dots, \mathbf{v}_m) \leftarrow \mathcal{A}_\mathsf{choose}(\mathrm{pp}, \mathrm{sk}) \\
\{\mathbf{C}_i\}_{i \in [m]} \leftarrow \{\mathsf{Enc}(i, \mathrm{sk}, \mathbf{v}_i)\}_{i \in [m]} \\
\{y_i\}_{i \in [m]} \leftarrow \mathcal{A}_\mathsf{eval}(\{\mathbf{C}_i\}_{i \in [m]}) \\
c^* \leftarrow \mathcal{S}(1^\lambda, \mathrm{pp}, \mathrm{sk}, \sum_{i \in [m]} y_i \mathbf{v}_i) \\
b \leftarrow \mathcal{A}_\mathsf{guess}(c^*)
\end{array} \right] 
\right|.$$

### Strictly Linear Targeted Malleability

> [!definition] Strictly Linear Targeted Malleability
> For any adversary $\mathcal A = (\mathcal A_\mathsf{find})$, we define the strictly linear targeted malleability advantage:
> $$\mathsf{Adv}_{}^\mathsf{SLTM}(\mathcal A) = 
\left|\; \Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
h
\end{array} \right] 
\;- 
\Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
j
\end{array} \right] 
\right|.$$
