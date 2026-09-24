## CONTENTS

|           | Preface                                       |   xiii |
|-----------|-----------------------------------------------|--------|
|           | Prologue: The Exponential Function            |        |
| Chapter 1 | Abstract Integration                          |      5 |
|           | Set-theoretic notations and terminology       |      6 |
|           | The concept of measurability                  |      8 |
|           | Simple functions                              |     15 |
|           | Elementary properties of measures             |     16 |
|           | Arithmetic in [0, 00]                         |     18 |
|           | Integration of positive functions             |     19 |
|           | Integration of complex functions              |     24 |
|           | The role played by sets of measure zero       |     27 |
|           | Exercises                                     |     31 |
| Chapter 2 | Positive Borel Measures                       |     33 |
|           | Vector spaces                                 |     33 |
|           | Topological preliminaries                     |     35 |
|           | The Riesz representation theorem              |     40 |
|           | Regularity properties of Borel measures       |     47 |
|           | Lebesgue measure                              |     49 |
|           | Continuity properties of measurable functions |     55 |
|           | Exercises                                     |     57 |
| Chapter 3 | LP-Spaces                                     |     61 |
|           | Convex functions and inequalities             |     61 |
|           | The LP-spaces                                 |     65 |
|           | Approximation by continuous functions         |     69 |
|           | Exercises                                     |     71 |

vii

## viii CONTENTS

| Chapter 4   | Elementary Hilbert Space Theory              |   76 |
|-------------|----------------------------------------------|------|
|             | Inner products and linear functionals        |   76 |
|             | Orthonormal sets                             |   82 |
|             | Trigonometric series                         |   88 |
|             | Exercises                                    |   92 |
| Chapter 5   | Examples of Banach Space Techniques          |   95 |
|             | Banach spaces                                |   95 |
|             | Consequences of Baire's theorem              |   97 |
|             | Fourier series of continuous functions       |  100 |
|             | Fourier coefficients of LI-functions         |  103 |
|             | The Hahn-Bana.eh theorem                     |  104 |
|             | An abstract approach to the Poisson integral |  108 |
|             | Exercises                                    |  112 |
| Chapter 6   | Complex Measures                             |  116 |
|             | Total variation                              |  116 |
|             | Absolute continuity                          |  120 |
|             | Consequences of the Radon-Nikodym theorem    |  124 |
|             | Bounded linear functionals on LP             |  126 |
|             | The Riesz representation theorem             |  129 |
|             | Exercises                                    |  132 |
| Chapter 7   | Differentiation                              |  135 |
|             | Derivatives of measures                      |  135 |
|             | The fundamental theorem of Calculus          |  144 |
|             | Differentiable transformations               |  150 |
|             | Exercises                                    |  156 |
| Chapter 8   | Integration on Product Spaces                |  160 |
|             | Measurability on cartesian products          |  160 |
|             | Product measures                             |  163 |
|             | The Fubini theorem                           |  164 |
|             | Completion of product measures               |  167 |
|             | Convolutions                                 |  170 |
|             | Distribution functions                       |  172 |
|             | Exercises                                    |  174 |
| Chapter 9   | Fourier Transforms                           |  178 |
|             | Formal properties                            |  178 |
|             | The inversion theorem                        |  180 |
|             | The Plancherel theorem                       |  185 |
|             | The Banach algebra LI                        |  190 |
|             | Exercises                                    |  193 |

## PREFACE

This book contains a first-year graduate course in which the basic techniques and theorems of analysis are presented in such way that the intimate connections between its various branches are strongly emphasized  The traditionally separate subjects of real analysis and complex analysis are thus united; some of the basic ideas from functional analysis are also included.

Since most of the results presented here are quite classical (the novelty lies in the arrangement; and some of the proofs are new), I have not attempted to document the source of every item: References are gathered at the end, in Notes and Comments They are not always to the original sources, but more often to more recent works where further references can be found. In no case does the absence of a reference imply any claim to originality on my part.

Here are some examples of the way in which these connections are demonstrated and exploited  The Riesz representation theorem and the Hahn-Banach theorem allow one to guess the Poisson integral formula. They team up in the proof of Runge's theorem. They combine with Blaschke's theorem on the zeros of bounded  holomorphic functions to give a proof of the Miintz-Szasz theorem; which concerns is used in the proof of the Radon-Nikodym theorem; which leads to the theorem about differentiation of indefinite integrals, which in turn yields the existence of radial limits  of bounded harmonic functions The theorems of Plancherel and Cauchy combined give a theorem of and Wiener which, in turn; is used in the Denjoy-Carleman theorem about infinitely differentiable functions on the real line. The maximum modulus theorem gives information about linear transformations on L-spaces. Paley

The   prerequisite for this book is course in advanced calculus (settheoretic   manipulations, metric   spaces; uniform continuity, and uniform convergence): The first seven chapters of my earlier book Principles of Mathematical Analysis furnish sufficient preparation: good Experience with the first edition shows that first-year graduate students can study the first 15 chapters in two semesters, plus some topics from 1 or 2 of the remaining $. These latter are quite independent of each other: The first 15 should be taken up in the order in which are presented, except for Chapter 9, which can be postponed. they One of these is the study of the boundary behavior of Poisson integrals A related one concerns HP-spaces  Accordingly, of Chapters 11 and 17 were rewritten and, I hope, simplified in the process large parts The most important difference between this third edition and the previous ones is the entirely new chapter on differentiation: The basic facts about differentiation are now derived from the existence of Lebesgue points, which in turn is an easy consequence of the sO-called weak type inequality that is satisfied by the maximal functions of measures on euclidean spaces. This approach yields strong theorems with minimal effort: Even more dents   with   maximal  functions, ' since  these have become increasingly useful  in several areas of analysis I have also made several smaller changes in order to improve certain details: For  example, parts   of Chapter 4 have been   simplified; the notions   of equiweak convergence are presented in more detail; the boundary behavior of conformal maps is studied by means of Lindelof's theorem about asymptotic valued of bounded holomorphic functions in a disc Over the last 20 years, numerous students and colleagues have offered comments and criticisms concerning the content of this book: I sincerely appreciated all of these, and have tried to follow some of them: As regards the present edition, my thanks go to Richard Rochberg for some useful last-minute suggestions, and I especially thank Robert Burckel for the meticulous care with which he examined the entire manuscript.

Walter Rudin

## PROLOGUE THE EXPONENTIAL FUNCTION

This is the most important function in mathematics It is defined, for every complex number 2, by the formula

<!-- formula-not-decoded -->

The series (1) converges absolutely for every and converges uniformly on every bounded subset of the complex plane. Thus exp is a continuous function: The absolute convergence of (1) shows that the computation

<!-- formula-not-decoded -->

is correct: It gives the important addition formula

<!-- formula-not-decoded -->

valid for all complex numbers a and b.

customary shorter expression e. Note that eo exp (0) = 1,by (1) (z) by the =

## Theorem

- (a) For every complex 2 we have e? # 0.
- (b) exp is its own derivative: exp' (2) = exp (2)

## REAL AND COMPLEX ANALYSIS

We shall encounter the integral of (1 + x2)-1 over the real line To evaluate it, put o(t) sin t/cos mono-= in (-nI2, nI2). By (6), tp' = 1 tp2. Hence tp tonically increasing mapping of ( -nI2, n12) onto (  - 00, (0), and we obtain

<!-- formula-not-decoded -->

<!-- image -->

## ABSTRACT INTEGRATION

Toward the end of the nineteenth century it became clear to many mathematicians that the Riemann integral (about which one learns in   calculus courses) should be replaced by some other type of integral, more general and more flexible, better suited for dealing with limit processes. Among the attempts made in this direction, the most notable ones were due to Jordan, Borel, W. H. Young, and Lebesgue It was Lebesgue's construction which turned out to be the most successful

In brief outline, here is the main idea: The Riemann integral of a function f over an interval [a, b] can be approximated by sums of the form

<!-- formula-not-decoded -->

where E1, En are disjoint intervals whose union is [a, b], m(E;) denotes the length of E;, and t; € E; for i = 1, n. Lebesgue discovered that a completely satisfactory theory of integration results if the sets the above sum are allowed to belong to a larger class of subsets of the line, the SO-called measurable sets; and if the class of functions under consideration is enlarged to what he called measurable functions. The crucial set-theoretic   properties involved are the following: The union and the intersection of any countable family of measurable sets are measurable; so is the complement of every measurable set; and, most important, the notion of length (now called measure can be extended to them in such a way that ...  , E;

If the range of f lies in the real line (or in the complex plane), then f is said to be a real function (or a complex function) For a complex function f, the statement means that all values f (x) off are nonnegative real numbers

## The Concept of Measurability

The class of measurable functions plays a fundamental role in integration theory: It has some basic properties in common with another most important class of functions, namely, the continuous ones. It is helpful to keep these similarities in mind. Our presentation is therefore organized in such way that the analogies between the concepts topological space, open set, and continuous function, on the other; are strongly emphasized: It seems that the relations between these concepts emerge most clearly when the setting is quite abstract; and this (rather than desire for mere generality) motivates our approach to the subject: one hand,  and

## 1.2 Definition

- (a) A collection of subsets of a set X is said to be a topology in X if r has the following three properties:
- (i)  0 E  't and X E  'to
- (ii) If V; E  dor i n, then VI n V 2 n  ...  n E  'to
- (iii) If {Va} is an arbitrary collection of members of € (finite, countable, O uncountable), then Uz V e €
- (b) a topology in X, then X is called topological space, and the members of € are called the open sets in X. If
- (c) If X and Y are topological spaces and if f is a mapping of X into Y, then f is said to be continuous provided that f - I(V) is an open set in X for every open set V in Y.

## 1.3 Definition

- (a) A collection It of subsets of a set X is said to be a G-algebra in X if It has the following properties:
- (i) X E  IDl.
- (ii) If A e 9, then AC E  IDl,  where AC is  the  complement of A relative to X.
- then A e I (iii) If A = U:,= I An and if An E  IDl  for n
- (b) If 9 is a G-algebra in X, then X is called measurable space, and the members of It are called the measurable sets in X. .
- (c) If X is a measurable Space; Y is a topological space, and f is a mapping measurable set in X for every open set V in Y. of X into Y, then J is  said  to  be measurable provided  that J -1(V) is  a

Bn be the distinct values of t, and let Next, let s be as  before, let PI' HJ = {x: t(x) = Pj}.1f Eij = A; ("\ Hj , then

and

<!-- formula-not-decoded -->

Thus (2) holds with Eij in place of X. Since X is the disjoint union of the sets our proposition implies that (2) holds Eij (1 i n, 1 j m),

We now come to the interesting of the theory. One of its most remarkable features is the ease with which it handles limit operations part

1.26 Lebesgue's Monotone Convergence Theorem measurable functions on X, and suppose that Let  {fn}  be  a  sequence  of

- (a) 0 &lt;fikx) &lt;fzkx) &lt; &lt; 00 for every x e X, (b) fn(x)--4 f(x) as n--4 oo,/or every x E X.

Then f is measurable, and

f f

constant; 0 &lt; c &lt; 1,and define

<!-- formula-not-decoded -->

PROOF  Since fn ~ fn + 1,  there exists an (X  E  [0,  00] such that

<!-- formula-not-decoded -->

SO (1) implies By Theorem 1.l4,fis measurable. Sincefn ~f, we  have f In ~ f ffor every n,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let be any simple measurable function such that 0 &lt; $ &lt; f, let c be

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

equality, consider some then x e E,; if f(x) &gt; 0, then Each En is  measurable, E1 c E2 C E3 C  "', and X = En. To  see  this x E X. If f(x) =

cs(x) &lt; f(x), since c &lt; 1; hence x € E, for some n. Also U

<!-- formula-not-decoded -->

PROOF Let 4 be a closed circular disc (with center at &amp; and radius r &gt; 0, say) in the complement of S. Since Sc is the union of countably many such discs, it is enough to prove that u(E) = 0, where E =f -1(A)

If we had U(E) &gt; 0, then

<!-- formula-not-decoded -->

= which is impossible, since A~f) E S.  Hence p.(E)

0\_ IIII

1.41 Theorem Let {Ek} be a sequence 0f measurable sets in X, such that

<!-- formula-not-decoded -->

Then almost all x € X lie in at most finitely many Of the sets Ek:

PROOF   If A is the set of all x which lie in infinitely many Ek, we have to prove that p.(A) = O.  Put

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For each X, each term in this series is either 0 Or 1. Hence x € A if and only if g(x) = By Theorem 1.27, the integral of g over X is equal to the sum in 00 a.e. (1).  Thus g E I!(p.), and so g(x) &lt; IIII

## Exercises

- 1 Does there exist an infinite G-algebra which has only countably many members?
- 2 Prove an analogue of Theorem 1.8 for n functions
- 3 Prove that if f is a real function on a measurable space X such that {x: f(x) &gt;r} is measurable for every rational r, then f is measurable\_
- Let {a,} and {b,} be sequences in [\_ 0, w], and prove the following assertions:

<!-- formula-not-decoded -->

provided none of the sums is of the form 0 00

(c) If an &lt; b, for all n, then

<!-- formula-not-decoded -->

Show by an example that strict inequality can hold in (b).

neighborhood of p for any set which contains an open set containing p.)

- X is locally compact if every of X has neighborhood whose closure is compact. point (f)
- (e) X is a Hausdorff space if the following is true: If p e X, q € X, and p # 4, then p has neighborhood U and q has neighborhood Vsuch that U 0 V =

Obviously, every compact space is locally compact:

We recall the Heine-Borel theorem: The compact subsets 0f a euclidean space R" are precisely those that are closed and bounded ([26],t Theorem 2.41). From this it follows easily that Rr is a locally compact Hausdorff space. Also, every metric space is a Hausdorff space

2.4 Theorem   Suppose K is compact and F is closed, in a topological space X. If F &lt; K,then F is compact\_

PROOF If {Va} is an open cover of F and W = Fc; then W U Uz V covers X; hence there is a finite collection {Va;} such that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then F c U ...  u

Corollary If A = B and if B has compact closure, so does A.

25 Theorem   Suppose X is Hausdorff space, K &lt;X, K is compact, and p e K. Then there are U and W such that p e U, K cW, and U (") W = 0.

PROOF If q € K, the Hausdorff separation axiom implies the existence of dissuch that p € Uq and q € Vq - Since K is compact, q Vq,

there are points 41, qn € K such that

<!-- formula-not-decoded -->

Our requirements are then satisfied by the sets

<!-- formula-not-decoded -->

## Corollaries

- (a) Compact subsets 0f Hausdorff spaces are closed.
- If F is closed and K is compact in Hausdorff space, then F 0 K is compact\_ (b)

Corollary (b) follows from and Theorem 2.4. (a)

- Numbers in brackets refer to the Bibliography.

(4) becomes

and

<!-- formula-not-decoded -->

for real XiPutting Yi = we obtain the familiar inequality between the arithmetic and geometric means of n positive numbers: ext;

<!-- formula-not-decoded -->

Going back from this to (4), it should become clear why the left and right sides of

<!-- formula-not-decoded -->

are often called the geometric and arithmetic means, respectively, of the positive function g.

If we take J.L({p;}) = lXi &gt; 0, where lXi =

<!-- formula-not-decoded -->

in place of (6). These are just a few samples of what is contained in Theorem 3.3. For a converse, see Exercise 20.

3.4 Definition If p and q are equivalently p + q = pq, or

<!-- formula-not-decoded -->

then we call p and q a of conjugate exponents It is clear that (1) implies 1 &lt; p &lt; and 1 &lt; q &lt; An important special case is p = q = 2. pair

are also regarded as a of conjugate exponents   Many analysts denote the exponent conjugate to p by p', often without saying so explicitly. pair As p-+ 1, (1) forces q-+

3.5 Theorem Let p Let X be a measure space, with measure U. Let f and g be measurable functions on X, with range in [0, 0]: Then 1 &lt; p &lt; 00.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The inequality (1) is Holder's; (2) is Minkowskis. If p = q = 2, (1) is known as the Schwarz inequality: