# **CONTENTS**

| Preface                                            | xiii |
|----------------------------------------------------|------|
| <b>Prologue: The Exponential Function</b>          | 1    |
| <b>Abstract Integration</b><br><b>Chapter 1</b>    | 5    |
| Set-theoretic notations and terminology            | 6    |
| The concept of measurability                       | 8    |
| Simple functions                                   | 15   |
| Elementary properties of measures                  | 16   |
| Arithmetic in $[0, \infty]$                        | 18   |
| Integration of positive functions                  | 19   |
| Integration of complex functions                   | 24   |
| The role played by sets of measure zero            | 27   |
| Exercises                                          | 31   |
| <b>Positive Borel Measures</b><br><b>Chapter 2</b> | 33   |
| Vector spaces                                      | 33   |
| Topological preliminaries                          | 35   |
| The Riesz representation theorem                   | 40   |
| Regularity properties of Borel measures            | 47   |
| Lebesgue measure                                   | 49   |
| Continuity properties of measurable functions      | 55   |
| Exercises                                          | 57   |
| <b>Chapter 3</b> $L^p$ -Spaces                     | 61   |
|                                                    |      |
| Convex functions and inequalities                  | 61   |
| The $L^p$ -spaces                                  | 65   |
| Approximation by continuous functions              | 69   |

vii

### viii CONTENTS

|                  | <b>Chapter 4</b> Elementary Hilbert Space Theory          | 76         |
|------------------|-----------------------------------------------------------|------------|
|                  | Inner products and linear functionals                     | 76         |
|                  | Orthonormal sets                                          | 82         |
|                  | Trigonometric series                                      | 88         |
|                  | Exercises                                                 | 92         |
| <b>Chapter 5</b> | <b>Examples of Banach Space Techniques</b>                | 95         |
|                  | <b>Banach</b> spaces                                      | 95         |
|                  | Consequences of Baire's theorem                           | 97         |
|                  | Fourier series of continuous functions                    | 100        |
|                  | Fourier coefficients of $L^1$ -functions                  | 103        |
|                  | The Hahn-Banach theorem                                   | 104<br>108 |
|                  | An abstract approach to the Poisson integral<br>Exercises | 112        |
| <b>Chapter 6</b> | <b>Complex Measures</b>                                   | 116        |
|                  | Total variation                                           | 116        |
|                  | Absolute continuity                                       | 120        |
|                  | Consequences of the Radon-Nikodym theorem                 | 124        |
|                  | Bounded linear functionals on $L^p$                       | 126        |
|                  | The Riesz representation theorem                          | 129        |
|                  | Exercises                                                 | 132        |
| <b>Chapter 7</b> | Differentiation                                           | 135        |
|                  | Derivatives of measures                                   | 135        |
|                  | The fundamental theorem of Calculus                       | 144        |
|                  | Differentiable transformations                            | 150        |
|                  | Exercises                                                 | 156        |
| <b>Chapter 8</b> | Integration on Product Spaces                             | 160        |
|                  | Measurability on cartesian products                       | 160        |
|                  | <b>Product measures</b>                                   | 163        |
|                  | The Fubini theorem                                        | 164        |
|                  | Completion of product measures                            | 167        |
|                  | Convolutions<br><b>Distribution functions</b>             | 170        |
|                  | Exercises                                                 | 172<br>174 |
| Chapter 9        | <b>Fourier Transforms</b>                                 | 178        |
|                  | Formal properties                                         |            |
|                  | The inversion theorem                                     | 178<br>180 |
|                  | The Plancherel theorem                                    | 185        |
|                  | The Banach algebra $L^1$                                  | 190        |
|                  | <b>Exercises</b>                                          | 193        |

# **PREFACE**

This book contains a first-year graduate course in which the basic techniques and theorems of analysis are presented in such a way that the intimate connections between its various branches are strongly emphasized. The traditionally separate subjects of "real analysis" and "complex analysis" are thus united; some of the basic ideas from functional analysis are also included.

Here are some examples of the way in which these connections are demonstrated and exploited. The Riesz representation theorem and the Hahn-Banach theorem allow one to "guess" the Poisson integral formula. They team up in the proof of Runge's theorem. They combine with Blaschke's theorem on the zeros of bounded holomorphic functions to give a proof of the Müntz-Szasz theorem, which concerns approximation on an interval. The fact that  $L^2$  is a Hilbert space is used in the proof of the Radon-Nikodym theorem, which leads to the theorem about differentiation of indefinite integrals, which in turn vields the existence of radial limits of bounded harmonic functions. The theorems of Plancherel and Cauchy combined give a theorem of Paley and Wiener which, in turn, is used in the Denjoy-Carleman theorem about infinitely differentiable functions on the real line. The maximum modulus theorem gives information about linear transformations on  $L^p$ -spaces.

Since most of the results presented here are quite classical (the novelty lies in the arrangement, and some of the proofs are new), I have not attempted to document the source of every item. References are gathered at the end, in Notes and Comments. They are not always to the original sources, but more often to more recent works where further references can be found. In no case does the absence of a reference imply any claim to originality on my part.

The prerequisite for this book is a good course in advanced calculus (settheoretic manipulations, metric spaces, uniform continuity, and uniform convergence). The first seven chapters of my earlier book "Principles of Mathematical Analysis" furnish sufficient preparation.

xiii

xiv PREFACE

Experience with the first edition shows that first-year graduate students can study the first 15 chapters in two semesters, plus some topics from 1 or 2 of the remaining 5. These latter are quite independent of each other. The first 15 should be taken up in the order in which they are presented, except for Chapter 9, which can be postponed.

The most important difference between this third edition and the previous ones is the entirely new chapter on differentiation. The basic facts about differentiation are now derived from the existence of Lebesgue points, which in turn is an easy consequence of the so-called "weak type" inequality that is satisfied by the maximal functions of measures on euclidean spaces. This approach vields strong theorems with minimal effort. Even more important is that it familiarizes students with maximal functions, since these have become increasingly useful in several areas of analysis.

One of these is the study of the boundary behavior of Poisson integrals. A related one concerns H<sup>p</sup>-spaces. Accordingly, large parts of Chapters 11 and 17 were rewritten and, I hope, simplified in the process.

I have also made several smaller changes in order to improve certain details: For example, parts of Chapter 4 have been simplified; the notions of equicontinuity and weak convergence are presented in more detail; the boundary behavior of conformal maps is studied by means of Lindelöf's theorem about asymptotic valued of bounded holomorphic functions in a disc.

Over the last 20 years, numerous students and colleagues have offered comments and criticisms concerning the content of this book. I sincerely appreciated all of these, and have tried to follow some of them. As regards the present edition, my thanks go to Richard Rochberg for some useful last-minute suggestions, and I especially thank Robert Burckel for the meticulous care with which he examined the entire manuscript.

**Walter Rudin** 

# **PROLOGUE** THE EXPONENTIAL FUNCTION

This is the most important function in mathematics. It is defined, for every complex number z, by the formula

$$
\exp\left(z\right) = \sum_{n=0}^{\infty} \frac{z^n}{n!}.\tag{1}
$$

The series (1) converges absolutely for every  $z$  and converges uniformly on every bounded subset of the complex plane. Thus exp is a continuous function. The absolute convergence of (1) shows that the computation

$$
\sum_{k=0}^{\infty} \frac{a^k}{k!} \sum_{m=0}^{\infty} \frac{b^m}{m!} = \sum_{n=0}^{\infty} \frac{1}{n!} \sum_{k=0}^{n} \frac{n!}{k!(n-k)!} a^k b^{n-k} = \sum_{n=0}^{\infty} \frac{(a+b)^n}{n!}
$$

is correct. It gives the important addition formula

$$
\exp(a)\exp(b) = \exp(a+b),\tag{2}
$$

valid for all complex numbers  $a$  and  $b$ .

We define the number  $e$  to be  $exp(1)$ , and shall usually replace  $exp(z)$  by the customary shorter expression  $e^z$ . Note that  $e^0 = \exp(0) = 1$ , by (1).

#### **Theorem**

- (a) For every complex z we have  $e^z \neq 0$ .
- (b) exp is its own derivative:  $exp'(z) = exp(z)$ .

 $\mathbf{1}$ 

#### 4 REAL AND COMPLEX ANALYSIS

We shall encounter the integral of  $(1 + x^2)^{-1}$  over the real line. To evaluate it, put  $\varphi(t) = \sin t/\cos t$  in  $(-\pi/2, \pi/2)$ . By (6),  $\varphi' = 1 + \varphi^2$ . Hence  $\varphi$  is a monotonically increasing mapping of  $(-\pi/2, \pi/2)$  onto  $(-\infty, \infty)$ , and we obtain

$$
\int_{-\infty}^{\infty} \frac{dx}{1+x^2} = \int_{-\pi/2}^{\pi/2} \frac{\varphi'(t) \ dt}{1+\varphi^2(t)} = \int_{-\pi/2}^{\pi/2} dt = \pi.
$$

## **CHAPTER** ONE

# **ABSTRACT INTEGRATION**

Toward the end of the nineteenth century it became clear to many mathematicians that the Riemann integral (about which one learns in calculus courses) should be replaced by some other type of integral, more general and more flexible, better suited for dealing with limit processes. Among the attempts made in this direction, the most notable ones were due to Jordan, Borel, W. H. Young, and Lebesgue. It was Lebesgue's construction which turned out to be the most successful

In brief outline, here is the main idea: The Riemann integral of a function  $f$ over an interval  $[a, b]$  can be approximated by sums of the form

$$
\sum_{i=1}^n f(t_i)m(E_i)
$$

where  $E_1, \ldots, E_n$  are disjoint intervals whose union is [a, b],  $m(E_i)$  denotes the length of  $E_i$ , and  $t_i \in E_i$  for  $i = 1, ..., n$ . Lebesgue discovered that a completely satisfactory theory of integration results if the sets  $E_i$  in the above sum are allowed to belong to a larger class of subsets of the line, the so-called "measurable sets," and if the class of functions under consideration is enlarged to what he called "measurable functions." The crucial set-theoretic properties involved are the following: The union and the intersection of any countable family of measurable sets are measurable; so is the complement of every measurable set; and, most important, the notion of "length" (now called "measure") can be extended to them in such a way that

$$
m(E_1 \cup E_2 \cup E_3 \cup \cdots) = m(E_1) + m(E_2) + m(E_3) + \cdots
$$

5

8 REAL AND COMPLEX ANALYSIS

If the range of f lies in the real line (or in the complex plane), then f is said to be a real function (or a complex function). For a complex function  $f$ , the statement " $f \ge 0$ " means that all values  $f(x)$  of f are nonnegative real numbers.

### The Concept of Measurability

The class of measurable functions plays a fundamental role in integration theory. It has some basic properties in common with another most important class of functions, namely, the continuous ones. It is helpful to keep these similarities in mind. Our presentation is therefore organized in such a way that the analogies between the concepts *topological space*, *open set*, and *continuous function*, on the one hand, and *measurable space*, *measurable set*, and *measurable function*, on the other, are strongly emphasized. It seems that the relations between these concepts emerge most clearly when the setting is quite abstract, and this (rather than a desire for mere generality) motivates our approach to the subject.

### 1.2 Definition

- (a) A collection  $\tau$  of subsets of a set X is said to be a *topology* in X if  $\tau$  has the following three properties:
  - (i)  $\varnothing \in \tau$  and  $X \in \tau$ .
  - (ii) If  $V_i \in \tau$  for  $i = 1, ..., n$ , then  $V_1 \cap V_2 \cap \cdots \cap V_n \in \tau$ .
  - (iii) If  $\{V_{\alpha}\}\$ is an arbitrary collection of members of  $\tau$  (finite, countable, or uncountable), then  $\bigcup_{\alpha} V_{\alpha} \in \tau$ .
- (b) If  $\tau$  is a topology in X, then X is called a *topological space*, and the members of  $\tau$  are called the *open sets* in X.
- (c) If X and Y are topological spaces and if  $f$  is a mapping of X into Y, then f is said to be *continuous* provided that  $f^{-1}(V)$  is an open set in X for every open set  $V$  in  $Y$ .

### 1.3 Definition

- (a) A collection  $\mathfrak M$  of subsets of a set X is said to be a  $\sigma$ -algebra in X if  $\mathfrak M$ has the following properties:
  - (i)  $X \in \mathfrak{M}$ .
  - (ii) If  $A \in \mathfrak{M}$ , then  $A^c \in \mathfrak{M}$ , where  $A^c$  is the complement of A relative to  $X_{\cdot}$
  - (iii) If  $A = \bigcup_{n=1}^{\infty} A_n$  and if  $A_n \in \mathfrak{M}$  for  $n = 1, 2, 3, \dots$ , then  $A \in \mathfrak{M}$ .
- (b) If  $\mathfrak{M}$  is a  $\sigma$ -algebra in X, then X is called a *measurable space*, and the members of  $\mathfrak{M}$  are called the *measurable sets* in X.
- (c) If X is a measurable space, Y is a topological space, and f is a mapping of X into Y, then f is said to be measurable provided that  $f^{-1}(V)$  is a measurable set in  $X$  for every open set  $V$  in  $Y$ .

**ABSTRACT INTEGRATION 21** 

Next, let s be as before, let  $\beta_1, \ldots, \beta_m$  be the distinct values of t, and let  $B_i = \{x : t(x) = \beta_i\}$ . If  $E_{ij} = A_i \cap B_j$ , then

$$
\int_{E_{ij}} (s+t) d\mu = (\alpha_i + \beta_j) \mu(E_{ij})
$$
  
and  
$$
\int_{E_{ij}} s d\mu + \int_{E_{ij}} t d\mu = \alpha_i \mu(E_{ij}) + \beta_j \mu(E_{ij}).
$$

Thus (2) holds with  $E_{ij}$  in place of X. Since X is the disjoint union of the sets  $E_{ii}$   $(1 \le i \le n, 1 \le j \le m)$ , the first half of our proposition implies that (2) holds.  $1111$ 

We now come to the interesting part of the theory. One of its most remarkable features is the ease with which it handles limit operations.

**1.26 Lebesgue's Monotone Convergence Theorem** Let  $\{f_n\}$  be a sequence of measurable functions on  $X$ , and suppose that

(a)  $0 \le f_1(x) \le f_2(x) \le \cdots \le \infty$  for every  $x \in X$ , (b)  $f_n(x) \to f(x)$  as  $n \to \infty$ , for every  $x \in X$ .

Then f is measurable, and

$$
\int_X f_n \, d\mu \to \int_X f \, d\mu \qquad \text{as } n \to \infty.
$$

**PROOF** Since  $f_n \leq f_{n+1}$ , there exists an  $\alpha \in [0, \infty]$  such that

$$
\int_X f_n \, d\mu \to \alpha \qquad \text{as } n \to \infty. \tag{1}
$$

By Theorem 1.14, f is measurable. Since  $f_n \le f$ , we have  $\int f_n \le \int f$  for every *n*, so  $(1)$  implies

$$
\alpha \le \int_X f \, d\mu. \tag{2}
$$

Let s be any simple measurable function such that  $0 \le s \le f$ , let c be a constant,  $0 < c < 1$ , and define

$$
E_n = \{x : f_n(x) \ge cs(x)\} \qquad (n = 1, 2, 3, \ldots).
$$
 (3)

Each  $E_n$  is measurable,  $E_1 \subset E_2 \subset E_3 \subset \cdots$ , and  $X = \bigcup E_n$ . To see this equality, consider some  $x \in X$ . If  $f(x) = 0$ , then  $x \in E_1$ ; if  $f(x) > 0$ , then  $cs(x) < f(x)$ , since  $c < 1$ ; hence  $x \in E_n$  for some *n*. Also

$$
\int_X f_n \ d\mu \ge \int_{E_n} f_n \ d\mu \ge c \int_{E_n} s \ d\mu \qquad (n = 1, 2, 3, \ldots).
$$
 (4)

**ABSTRACT INTEGRATION 31** 

 $^{\prime\prime\prime\prime}$ 

**PROOF** Let  $\Delta$  be a closed circular disc (with center at  $\alpha$  and radius  $r > 0$ , say) in the complement of S. Since  $S<sup>c</sup>$  is the union of countably many such discs, it is enough to prove that  $\mu(E) = 0$ , where  $E = f^{-1}(\Delta)$ .

If we had  $\mu(E) > 0$ , then

$$
|A_E(f) - \alpha| = \frac{1}{\mu(E)} \left| \int_E (f - \alpha) d\mu \right| \leq \frac{1}{\mu(E)} \int_E |f - \alpha| d\mu \leq r,
$$

which is impossible, since  $A_{\kappa}(f) \in S$ . Hence  $\mu(E) = 0$ .

**1.41 Theorem** Let  $\{E_k\}$  be a sequence of measurable sets in X, such that

$$
\sum_{k=1}^{\infty} \mu(E_k) < \infty. \tag{1}
$$

Then almost all  $x \in X$  lie in at most finitely many of the sets  $E_k$ .

**PROOF** If A is the set of all x which lie in infinitely many  $E_k$ , we have to prove that  $\mu(A) = 0$ . Put

$$
g(x) = \sum_{k=1}^{\infty} \chi_{E_k}(x) \qquad (x \in X). \tag{2}
$$

For each x, each term in this series is either 0 or 1. Hence  $x \in A$  if and only if  $q(x) = \infty$ . By Theorem 1.27, the integral of g over X is equal to the sum in (1). Thus  $q \in L^1(\mu)$ , and so  $q(x) < \infty$  a.e.  $^{\prime\prime\prime\prime}$ 

### **Exercises**

1 Does there exist an infinite  $\sigma$ -algebra which has only countably many members?

2 Prove an analogue of Theorem 1.8 for *n* functions.

3 Prove that if f is a real function on a measurable space X such that  $\{x: f(x) \ge r\}$  is measurable for every rational  $r$ , then  $f$  is measurable.

4 Let  $\{a_n\}$  and  $\{b_n\}$  be sequences in  $[-\infty, \infty]$ , and prove the following assertions:

(a) 
$$
\limsup_{n \to \infty} (-a_n) = -\liminf_{n \to \infty} a_n.
$$

(b) 
$$
\limsup_{n \to \infty} (a_n + b_n) \leq \limsup_{n \to \infty} a_n + \limsup_{n \to \infty} b_n
$$

provided none of the sums is of the form  $\infty - \infty$ .

(c) If  $a_n \leq b_n$  for all *n*, then

$$
\liminf_{n \to \infty} a_n \le \liminf_{n \to \infty} b_n.
$$

Show by an example that strict inequality can hold in (b).

36 REAL AND COMPLEX ANALYSIS

" neighborhood of  $p$ " for any set which contains an open set containing  $p.$ 

- (e) X is a Hausdorff space if the following is true: If  $p \in X$ ,  $q \in X$ , and  $p \neq q$ , then  $p$  has a neighborhood  $U$  and  $q$  has a neighborhood  $V$  such that  $U \cap V = \emptyset$ .
- $(f)$  X is locally compact if every point of X has a neighborhood whose closure is compact.

Obviously, every compact space is locally compact.

We recall the Heine-Borel theorem: The compact subsets of a euclidean space  $R<sup>n</sup>$  are precisely those that are closed and bounded ( $[26]$ ,† Theorem 2.41). From this it follows easily that  $R<sup>n</sup>$  is a locally compact Hausdorff space. Also, every metric space is a Hausdorff space.

**2.4 Theorem** Suppose K is compact and F is closed, in a topological space X. If  $F \subset K$ , then F is compact.

**PROOF** If  $\{V_{\alpha}\}\$ is an open cover of F and  $W = F^{c}$ , then  $W \cup \bigcup_{\alpha} V_{\alpha}$  covers X; hence there is a finite collection  $\{V_{\alpha}\}\$  such that

$$
K\subset W\cup V_{\alpha_1}\cup\cdots\cup V_{\alpha_n}.
$$

 $1111$ 

Then  $F \subset V_{\alpha_1} \cup \cdots \cup V_{\alpha_n}$ .

**Corollary** If  $A \subseteq B$  and if B has compact closure, so does A.

**2.5 Theorem** Suppose X is a Hausdorff space,  $K \subset X$ , K is compact, and  $p \in K^{c}$ . Then there are open sets U and W such that  $p \in U$ ,  $K \subset W$ , and  $U \cap W = \varnothing$ .

**PROOF** If  $q \in K$ , the Hausdorff separation axiom implies the existence of disjoint open sets  $U_q$  and  $V_q$ , such that  $p \in U_q$  and  $q \in V_q$ . Since K is compact, there are points  $q_1, \ldots, q_n \in K$  such that

$$
K\subset V_{q_1}\cup\cdots\cup V_{q_n}.
$$

Our requirements are then satisfied by the sets

$$
U = U_{q_1} \cap \cdots \cap U_{q_n} \quad \text{and} \quad W = V_{q_1} \cup \cdots \cup V_{q_n}. \qquad \qquad \text{with}
$$

#### **Corollaries**

- (a) Compact subsets of Hausdorff spaces are closed.
- (b) If F is closed and K is compact in a Hausdorff space, then  $F \cap K$  is compact.

Corollary (b) follows from  $(a)$  and Theorem 2.4.

† Numbers in brackets refer to the Bibliography.

 $L^{p}$ -SPACES 63

 $(4)$  becomes

$$
\exp\left\{\frac{1}{n}\left(x_1 + \dots + x_n\right)\right\} \le \frac{1}{n}\left(e^{x_1} + \dots + e^{x_n}\right),\tag{5}
$$

for real  $x_i$ . Putting  $y_i = e^{x_i}$ , we obtain the familiar inequality between the arithmetic and geometric means of *n* positive numbers:

$$
(y_1 y_2 \cdots y_n)^{1/n} \le \frac{1}{n} (y_1 + y_2 + \cdots + y_n).
$$
 (6)

Going back from this to (4), it should become clear why the left and right sides of

$$
\exp\left\{\int_{\Omega}\log g \ d\mu\right\} \le \int_{\Omega} g \ d\mu \tag{7}
$$

are often called the geometric and arithmetic means, respectively, of the positive function *a*.

### If we take $\mu({p_i}) = \alpha_i > 0$ , where $\sum \alpha_i = 1$ , then we obtain

$$
y_1^{\alpha_1} y_2^{\alpha_2} \cdots y_n^{\alpha_n} \le \alpha_1 y_1 + \alpha_2 y_2 + \cdots + \alpha_n y_n \tag{8}
$$

in place of (6). These are just a few samples of what is contained in Theorem 3.3.

For a converse, see Exercise 20.

**3.4 Definition** If p and q are positive real numbers such that  $p + q = pq$ , or equivalently

$$
\frac{1}{p} + \frac{1}{q} = 1,\tag{1}
$$

then we call p and q a pair of *conjugate exponents*. It is clear that  $(1)$  implies  $1 < p < \infty$  and  $1 < q < \infty$ . An important special case is  $p = q = 2$ .

As  $p \rightarrow 1$ , (1) forces  $q \rightarrow \infty$ . Consequently 1 and  $\infty$  are also regarded as a pair of conjugate exponents. Many analysts denote the exponent conjugate to  $p$  by  $p'$ , often without saying so explicitly.

**3.5 Theorem** Let p and q be conjugate exponents,  $1 < p < \infty$ . Let X be a measure space, with measure  $\mu$ . Let f and q be measurable functions on X, with range in [0,  $\infty$ ]. Then

$$
\int_X fg \ d\mu \le \left\{ \int_X f^p \ d\mu \right\}^{1/p} \left\{ \int_X g^q \ d\mu \right\}^{1/q} \tag{1}
$$

and

$$
\left\{\int_{X}(f+g)^{p} d\mu\right\}^{1/p} \leq \left\{\int_{X} f^{p} d\mu\right\}^{1/p} + \left\{\int_{X} g^{p} d\mu\right\}^{1/p}.
$$
 (2)

The inequality (1) is Hölder's; (2) is Minkowski's. If  $p = q = 2$ , (1) is known as the Schwarz inequality.