## Linear Algebra
:label:`sec_linear-algebra`

>Notes from D2L

### Scalars:  
the expression $x \in \mathbb{R}$
is a formal way to say that $x$ is a real-valued scalar.
The symbol $\in$ (pronounced "in")
denotes membership in a set.
For example, $x, y \in \{0, 1\}$
indicates that $x$ and $y$ are variables
that can only take values $0$ or $1$.

### Vectors:
Caution: in Python, as in most programming languages, vector indices start at $0$, also known as *zero-based indexing*, whereas in linear algebra subscripts begin at $1$ (one-based indexing).

$$\mathbf{x} =\begin{bmatrix}x_{1}  \\ \vdots  \\x_{n}\end{bmatrix},$$

### Matrices:  
Just as scalars are $0^{\textrm{th}}$-order tensors and vectors are $1^{\textrm{st}}$-order tensors, matrices are $2^{\textrm{nd}}$-order tensors.

The expression $\mathbf{A} \in \mathbb{R}^{m \times n}$ indicates that a matrix $\mathbf{A}$ contains $m \times n$ real-valued scalars, arranged as $m$ rows and $n$ columns. When $m = n$, we say that a matrix is *square*.

`transpose:` Flip the axes. Formally, we signify a matrix $\mathbf{A}$'s transpose by $\mathbf{A}^\top$ and if $\mathbf{B} = \mathbf{A}^\top$, then $b_{ij} = a_{ji}$ for all $i$ and $j$.

### Properties
The [**elementwise product of two matrices is called their *Hadamard product***] (denoted $\odot$). We can spell out the entries of the Hadamard product of two matrices $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}$:

$$
\mathbf{A} \odot \mathbf{B} =
\begin{bmatrix}
    a_{11}  b_{11} & a_{12}  b_{12} & \dots  & a_{1n}  b_{1n} \\
    a_{21}  b_{21} & a_{22}  b_{22} & \dots  & a_{2n}  b_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1}  b_{m1} & a_{m2}  b_{m2} & \dots  & a_{mn}  b_{mn}
\end{bmatrix}.
$$

```python
A*B #Hadamard product in python
```

### Reduction

#### Sum
$\sum_{i=1}^n x_i$ 

$\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}$.

```python
a.sum()
a.sum(axis=0) #To sum over all elements along the rows (axis 0)
a.sum(axis=[0, 1]) # 
```
#### Mean

```python
A.mean(), A.sum() / A.numel()
A.mean(axis=0), A.sum(axis=0) / A.shape[0]
```
