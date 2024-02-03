## Linear Algebra
:label:`sec_linear-algebra`

Notes from [D2L](https://d2l.ai/index.html)

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
#### Hadamard Product
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
#### Non-Reduction Sum
keep the number of axes unchanged
```python
A.sum(axis=1, keepdims=True)
# output
# (tensor([[ 6],
#          [ 6],
#          [12]]),
#  torch.Size([3, 1]))
A.sum(axis=1)
# output
# tensor([ 6,  6, 12])
```
For instance, since `sum_A` keeps its two axes after summing each row, we can **divide `A` by `sum_A` with broadcasting** to create a matrix where each row sums up to 1.

```python
A / sum_A
# output
# tensor([[0.0000, 0.3333, 0.6667],
#         [0.2500, 0.3333, 0.4167]])
```

#### Dot Products
Given two **vectors** $\mathbf{x}, \mathbf{y} \in \mathbb{R}^d$, their *dot product* $\mathbf{x}^\top \mathbf{y}$ (also known as *inner product*, $\langle \mathbf{x}, \mathbf{y}  \rangle$) is a sum over the products of the elements at the same position: $\mathbf{x}^\top \mathbf{y} = \sum_{i=1}^{d} x_i y_i$.

```python
torch.sum(x * y)
# or
torch.dot(x, y)
```
For example, given some set of values, denoted by a vector $\mathbf{x}  \in \mathbb{R}^n$,and a set of weights, denoted by $\mathbf{w} \in \mathbb{R}^n$, the weighted sum of the values in $\mathbf{x}$ according to the weights $\mathbf{w}$ could be expressed as the dot product $\mathbf{x}^\top \mathbf{w}$. When the weights are nonnegative and sum to $1$, i.e., $\left(\sum_{i=1}^{n} {w_i} = 1\right)$, the dot product expresses a *weighted average*. 

