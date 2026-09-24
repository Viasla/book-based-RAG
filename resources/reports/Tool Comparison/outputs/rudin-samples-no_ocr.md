## CONTENTS

5

6

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

## viii  CONTENTS

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

This book contains a first-year graduate course in which the basic techniques and theorems  of analysis  are  presented in  such  a  way  that  the  intimate connections between its various branches are strongly emphasized. The traditionally separate subjects of "real analysis" and "complex analysis" are thus united; some of the basic ideas from functional analysis are also included.

Here are some examples of the way in which  these connections are demon­ strated  and  exploited.  The  Riesz  representation  theorem  and  the  Hahn-Banach theorem allow one to " guess" the Poisson integral formula. They team up in the proof of Runge's theorem. They combine with Blaschke's theorem on the zeros of bounded  holomorphic  functions  to  give  a  proof of the  Miintz-Szasz  theorem, which concerns approximation on an interval. The fact  that 13  is  a Hilbert space is  used in the  proof of the Radon-Nikodym theorem, which leads to the theorem about differentiation of indefinite integrals,  which  in turn  yields  the existence  of radial  limits  of bounded  harmonic  functions.  The  theorems  of Plancherel  and Cauchy combined give a theorem of Paley and Wiener which, in turn, is  used in the Denjoy-Carleman theorem about infinitely differentiable functions on the real line.  The  maximum modulus  theorem gives  information about linear transform­ ations on fl'-spaces.

Since most of the results presented here are quite classical (the novelty lies in the arrangement, and some of the proofs are new), I have not attempted to docu­ ment the source of every item.  References  are gathered at the  end, in Notes and Comments. They are not always to the original sources, but more often to more recent works where further  references can be found.  In no case does the absence of a reference imply any claim to originality on my part.

The  prerequisite  for this book  is a  good  course  in advanced  calculus (settheoretic  manipulations,  metric  spaces, uniform  continuity,  and  uniform convergence).  The first  seven chapters  of my earlier book" Principles of Mathe­ matical Analysis" furnish sufficient preparation.

Experience  with  the first  edition shows  that first-year  graduate students can study the first  15  chapters in  two  semesters, plus some topics from  1 or 2 of the remaining 5. These latter are quite independent of each other. The first  15 should be taken up in the order in which they are presented, except for Chapter 9, which can be postponed.

The most important difference  between  this  third  edition  and  the  previous ones is  the entirely new chapter on differentiation. The basic facts about differen­ tiation are now derived fro~ the existence of Lebesgue points, which in turn is an easy consequence of the so-called "weak type" inequality that is  satisfied by  the maximal functions of measures on euclidean spaces.  This approach yields  strong theorems  with  minimal  effort.  Even  more  important  is  that  it  familiarizes  stu­ dents  with  maximal  functions,'  since  these  have  become  increasingly  useful  in several areas of analysis.

One of these  is  the  study  of the  boundary  behavior  of Poisson integrals.  A related  one  concerns HP-spaces.  Accordingly,  large  parts of Chapters  11  and  17 were rewritten and, I hope, simplified in the process.

I have also made several smaller changes in order to improve certain details: For  example,  parts  of  Chapter 4  have  been  simplified;  the  notions  of  equi­ continuity  and  weak  convergence  are  presented  in  more  detail;  the  boundary behavior  of conformal  maps  is  studied  by  means  of Lindelof's theorem  about asymptotic valued of bounded holomorphic functions in a disc.

Over the last 20 years, numerous students and colleagues have offered com­ ments and criticisms concerning the content of this book. I sincerely appreciated all of these, and have tried to follow some of them. As regards the present edition, my thanks go to Richard Rochberg for some useful last-minute suggestions, and I especially thank Robert Burckel for  the meticulous care with which he examined the entire manuscript.

Walter Rudin

## PROLOGUE THE  EXPONENTIAL  FUNCTION

This is  the most important function in mathematics. It is  defined, for every com­ plex number z, by the formula

$$\exp \left ( z \right ) = \sum _ { n = 0 } ^ { \infty } \frac { z ^ { n } } { n ! } .$$

The series (1)  converges absolutely. for every z and converges uniformly on every bounded  subset  of the  complex  plane.  Thus  exp  is  a  continuous  function.  The absolute convergence of (1) shows that the computation

$$\sum _ { k = 0 } ^ { \infty } \frac { a ^ { k } } { k ! } \sum _ { m = 0 } ^ { \infty } \frac { b ^ { m } } { m ! } = \sum _ { n = 0 } ^ { \infty } \frac { 1 } { n ! } \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } \, a ^ { k } b ^ { n - k } = \sum _ { n = 0 } ^ { \infty } \frac { ( a + b ) ^ { n } } { n ! }$$

is correct. It gives the important addition formula

$$\exp \left ( a \right ) \exp \left ( b \right ) = \exp \left ( a + b \right ) ,$$

valid for all complex numbers a and b.

We define the number e to be exp (1),  and shall usually replace exp (z) by the customary shorter expression e%. Note that eO = exp (0) = 1, by (1).

## Theorem

- (a) For every complex z we have e%  =I: O.
- (b) exp is its own derivative: exp' (z) = exp (z).

## 4  REAL  AND  COMPLEX  ANALYSIS

We shall encounter the integral of (1 + X 2 )-1  over  the  real  line.  To evaluate it,  put tp(t) = sin tlcos t in (-nI2, nI2). By (6), tp' = 1 + tp2. Hence tp is  a  mono­ tonically increasing mapping of ( -nI2, n12) onto (  - 00, (0), and we obtain

$$\int _ { - \infty } ^ { \infty } \frac { d x } { 1 + x ^ { 2 } } = \int _ { - \pi / 2 } ^ { \pi / 2 } \frac { \varphi ^ { \prime } ( t ) \ d t } { 1 + \varphi ^ { 2 } ( t ) } = \int _ { - \pi / 2 } ^ { \pi / 2 } d t = \pi .$$

<!-- image -->

## ABSTRACT  INTEGRATION

Toward  the end of the  nineteenth  century  it  became clear  to  many mathemati­ cians  that  the  Riemann  integral  (about  which  one  learns  in  calculus  courses) should be  replaced  by some other type  of integral, more general  and more flex­ ible,  better suited for  dealing with  limit  processes.  Among  the  attempts made in this  direction,  the  most  notable  ones  were  due  to Jordan,  Borel,  W.  H.  Young, and  Lebesgue. It was  Lebesgue's construction  which  turned  out  to be  the  most successful.

In  brief outline,  here  is  the  main  idea: The Riemann  integral  of a  function! over an interval [a,  b] can be approximated by sums of the form

$$\sum _ { i = 1 } ^ { n } f ( t _ { i } ) m ( E _ { i } )$$

where E 1 , ...  , En are  disjoint  intervals  whose  union  is [a,  b],  m(E;) denotes  the length of E;, and t; E E; for i = 1,  ...  , n. Lebesgue discovered  that a  completely satisfactory  theory  of  integration  results  if  the  sets E; in  the  above  sum  are allowed to belong to a larger class of  subsets of  the line, the so-called "measurable sets," and if the class of functions under consideration is enlarged to what  he called  "meas\lrable  functions." The  crucial set-theoretic  properties involved  are  the  following:  The  union  and  the  intersection  of  any  countable family  of measurable sets are measurable; so is  the complement of every measur­ able  set;  and,  most  important,  the  notion  of-" length" (now  called  "measure") can be extended to them in such a way that

$$m ( E _ { 1 } \cup E _ { 2 } \cup E _ { 3 } \cup \cdots ) = m ( E _ { 1 } ) + m ( E _ { 2 } ) + m ( E _ { 3 } ) + \cdots$$

If the range of J lies  in  the  real line (or in the com  plex plane), then J is  said to be a real Junction (or a complex Junction). For a complex function/, the statement "J;;::. 0" means that all valuesJ(x) ofJare nonnegative real numbers.

## The Con~ept of Measurability

The class of measurable functions plays a fundamental role in integration theory. It has  some  basic  properties  in  common  with  another  most  important class  of functions,  namely,  the  continuous  ones. It is  helpful  to  keep  these  similarities  in mind.  Our presentation is  therefore  organized  in  such  a  way  that the  analogies between  the concepts topological space,  open set, and continuous Junction, on the one hand,  and measurable space, measurable set, and measurable Junction, on the other, are strongly emphasized. It seems that the relations between these concepts emerge  most  clearly  when  the  setting  is  quite  abstract,  and  this  (rather  than  a desire for mere generality) motivates our approach to the subject.

## 1.2  Definition

- (a) A collection 't of subsets of a set X is  said  to  be  a topology  in  X if 't has the following three properties:
- (i)  0 E  't and X E  'to
- (ii) If V; E  dor i = 1, ...  , n, then VI n V 2 n  ...  n v.. E  'to
- (iii) If {~} is  an arbitrary collection of members of't  (finite, countable, or uncountable), then  Ua ~ E  'to
- (b) If 't  is  a  topology  in X, then X is  called  a topological  space, and  the members of't are called the open sets in X.
- (c) If X and  Yare topological spaces and ifJis a mapping of X into Y, then J is  said  to  be continuous provided  that J -l( V) is  an  open  set  in X for every open set V in Y.

## 1.3  Definition

- (a) A collection IDl  of subsets of a  set X is  said  to  be  a a-algebra  in  X if IDl has the following properties:
- (i) X E  IDl.
- (ii) If A E  IDl,  then AC E  IDl,  where AC is  the  complement of A relative to X.
- (iii) If A = U:,= I An and if An E  IDl  for n = 1,2, 3, ...  , then A E  IDl.
- (b) If IDl  is  a  a-algebra  in X, then X is  called  a measurable  space, and  the members of IDl are called the measurable sets in X. .
- (c) If X is  a  measurable space, Y is  a  topological  space,  andJis a mapping of X into Y, then J is  said  to  be measurable provided  that J -1(V) is  a measurable set in X for every open set V in Y.

Next, let s be as  before, let PI' ...  , Pm be the distinct values  of t, and let HJ = {x: t(x) = Pj}.1f Eij = A; ("\ Hj , then

$$( s + t ) \, d \mu = ( \alpha _ { i } + \beta _ { j } ) \mu ( E _ { i j } )$$

$$\int _ { E _ { i j } } ( s +$$

and

Thus (2) holds with Eij in place of X. Since X is the disjoint union of the sets Eij (1 ~ i ~ n, 1 ~ j ~ m), the  first  half of our  proposition  implies  that  (2) holds. IIII

We now come to the interesting part of the theory.  One of its most remark­ able features is the ease with which it handles limit operations.

1.26  Lebesgue's  Monotone  Convergence  Theorem Let  {fn}  be  a  sequence  of measurable functions on X, and suppose that

- (a) 0 ~f1(X) ~f2(X) ~ ... ~ 00 for every x E X,
- (b) fn(x)--4 f(x) as n--4 oo,/or every x E

$$X _ { \cdot }$$

Thenfis measurable, and

f f

$$a s \, n \rightarrow \infty .$$

PROOF  Since fn ~ fn + 1,  there exists an (X  E  [0,  00] such that

$$\int _ { X } f _ { n } \, d \mu \rightarrow \alpha \quad a s \ n \rightarrow \infty .$$

By Theorem 1.l4,fis measurable. Sincefn ~f, we  have f In ~ f ffor every n, so (1) implies

$$( 2 )$$

Let s  be  any  simple  measurable  function  such  that O:s;  s :s;f, let c be  a

constant, 0 &lt; c &lt;  1, and define

$$E _ { n } = \{ x \colon f _ { n } ( x ) \geq c s ( x ) \} \quad ( n = 1 , \, 2 , \, 3 , \, \dots ) .$$

$$( 3 )$$

Each En is  measurable, E1 c E2 C E3 C  "', and X = U En. To  see  this equality,  consider  some x E X. If f(x) = 0,  then x E E1; if f(x) &gt; 0,  then cs(x) &lt; f(x), since c &lt;  1; hence x E En for some n. Also

$$\int _ { X } f _ { n } \, d \mu \geq \int _ { \int _ { X } f _ { n } } f _ { n } \, d \mu \geq c \, \int _ { \int _ { X } s \, d \mu } \quad ( n = 1 , \, 2 , \, 3 , \, \dots ) .$$

$$\int _ { X } f _ { n } \, d \mu \geq \int _ { E _ { n } } f _ { n } \, d \mu \geq c \, \int _ { E _ { n } } s \, d \mu$$

PROOF Let a be a closed circular disc (with center at IX and radius r &gt; 0, say) in the complement of S. Since SC is the union of  countably many such discs, it is enough to prove that p.(E) = 0, where E = f - 1(a).

If we had p.(E) &gt; 0, then

$$| A _ { E } ( f ) - \alpha | = \frac { 1 } { \mu ( E ) } \left | \, \int _ { E } ( f - \alpha ) \, d \mu \, \left | \leq \frac { 1 } { \mu ( E ) } \int _ { E } | \, f - \alpha | \, d \mu \leq r ,$$

which is impossible, since A~f) E S.  Hence p.(E)

= O. IIII

1.41 Theorem Let {Ek}  be a sequence of  measurable sets in X, such that

$$\sum _ { k = 1 } ^ { \infty } \mu ( E _ { k } ) < \infty .$$

Then almost all x E X  lie in at most  finitely many of  the sets  E k ·

PROOF  If A is  the  set  of all x which  lie  in  infinitely  many Ek , we  have  to prove that p.(A) = O.  Put

$$g ( x ) = \sum _ { k = 1 } ^ { \infty } \chi _ { E _ { k } } ( x ) \quad ( x \in X ) .$$

$$( 2 )$$

For each x, each term in this series is either 0 or 1.  Hence x E A if and only if g(x) = 00.  By  Theorem  1.27,  the  integral  of g over X is  equal to the sum in (1).  Thus g E I!(p.), and so g(x) &lt; 00  a.e. IIII

## Exercises

- 1  Does there exist an infinite a-algebra which has only countably many members?
- 1  Prove an analogue of Theorem 1.8 for n functions.
- 3  Prove that iffis a  real function  on a measurable space X such that {x:f(x) ~ r}  is  measurable for every rational r, thenfis measurable.
- 4  Let {an} and {bnl be sequences in [- &lt;Xl,  &lt;Xl], and prove the following assertions:

$$( a ) & & \lim _ { n \to \infty } \sup \left ( - a _ { n } \right ) = - \liminf _ { n \to \infty } a _ { n } . \\ ( b ) & & \lim _ { n \to \infty } \sup \left ( a _ { n } + b _ { n } \right ) \leq \lim \sup _ { n \to \infty } a _ { n } + \lim \sup _ { n \to \infty } b _ { n } .$$

$$\lim _ { n \to \infty } \sup _ { n \to b _ { n } } ( a _ { n } + b _ { n } ) \leq \lim _ { n \to \infty } \sup _ { n } a _ { n } + \lim _ { n \to \infty } \sup _ { n \to b _ { n } } b _ { n } & * \\$$

provided none of  the sums is of  the form &lt;Xl  - &lt;Xl.

(c) If  an S; b. for all n, then

$$\liminf a _ { n } \leq \liminf b _ { n } .$$

Show by an example that strict inequality can hold in (b).

"neighborhood of p" for  any set  which contains an open set containing p.)

- (e) X is  a Hausdorff space if the following is  true: If p E X, q E X, and p =Iq, then p has  a  neighborhood U and q has  a  neighborhood V such  that U (") V = 0.
- (f) X is locally  compact if  every  point  of X has  a  neighborhood  whose closure is compact.

Obviously, every compact space is locally compact.

We recall the Heine-Borel theorem: The compact subsets of  a euclidean space R n  are  precisely  those  that  are  closed  and  bounded ([26],t  Theorem  2.41).  From this  it  follows  easily  that R n is  a  locally  compact  Hausdorff space.  Also,  every metric space is  a Hausdorff space.

2.4  Theorem Suppose  K is compact and  F is closed,  in  a  topological space  X. If  F c K, then F is compact.

PROOF  If {v,.} is  an open cover of F and W = P, then W u  U. v,.  covers X; hence there is a finite collection {v,.J  such that

$$K \subset W \cup V _ { \alpha _ { 1 } } \cup \cdots \cup V _ { \alpha _ { n } } .$$

$$V _ { \alpha _ { 1 } }$$

$$\text {Then } F \subset V _ { \alpha _ { 1 } } \cup \cdots \cup V _ { \alpha _ { n } } .$$

Then F c U ...  u

Corollary If  A c B and if B has compact closure, so does A.

2.5  Theorem Suppose  X is a  Hausdorff space,  K c X,  K is compact,  and p E K C · Then  there  are  open  sets  U  and  W such  that  p E U,  K c W,  and U (") W = 0.

PROOF  If q E K, the Hausdorff separation axiom implies the existence of dis­ joint open sets U q and Vq, such that p E U q and q E Vq. Since K is  compact, there are points qh ...  , qn  E K such that

$$K \subset V _ { q _ { 1 } } \cup \cdots \cup V _ { q _ { n } } .$$

Our requirements are then satisfied by the sets

$$U = U _ { q _ { 1 } } \cap \cdots \cap U _ { q _ { n } } \text { and } W = V _ { q _ { 1 } } \cup \cdots \cup V _ { q _ { n } } .$$

## Corollaries

- (a) Compact subsets of  Hausdorff  spaces are closed.
- (b) If F is closed  and  K is  compact  in  a  Hausdorff space,  then  F (") K  is compact.

Corollary (b) follows from (a) and Theorem 2.4.

- t Numbers in brackets refer to the Bibliography.

(4)  becomes

$$\exp \left \{ \frac { 1 } { n } \left ( x _ { 1 } + \cdots + x _ { n } \right ) \right \} & \leq \frac { 1 } { n } \left ( e ^ { x _ { 1 } } + \cdots + e ^ { x _ { n } } \right ) ,$$

for  real Xi' Putting Yi = e Xi , we  obtain the familiar  inequality between the arith­ metic and geometric means of n positive numbers:

$$( y _ { 1 } y _ { 2 } \cdots y _ { n } ) ^ { 1 / n } \leq \frac { 1 } { n } \left ( y _ { 1 } + y _ { 2 } + \cdots + y _ { n } \right ) .$$

Going back from this to (4), it should become clear why the left and right sides of

$$\exp \left \{ \int _ { \Omega } \log g \, d \mu \right \} \leq \int _ { \Omega } g \, d \mu$$

are often called the geometric and arithmetic means,  respectively,  of the positive function g.

If we take J.L({p;}) = lXi &gt; 0, where lXi =

$$h e r e \sum \alpha _ { i } = 1 , \text { then we obtain}$$

and

$$( 8 )$$

in place of  (6).  These are just a few  samples of what is contained in Theorem 3.3. For a converse, see Exercise 20.

3.4 Definition If p and q are positive  real  numbers such  that p + q = pq, or equivalently

$$\frac { 1 } { p } + \frac { 1 } { q } = 1 ,$$

then we call p and q a  pair of conjugate exponents. It is  clear that (1)  implies 1 &lt; p &lt; 00  and 1 &lt; q &lt; 00.  An important special case is p = q = 2.

As p-+ 1, (1) forces q-+ 00.  Consequently 1 and 00  are also regarded as a pair of conjugate exponents.  Many analysts denote  the exponent conjugate to p by p', often without saying so explicitly.

3.5 Theorem Let  p  and  q  be  conjugate  exponents, 1 &lt; p &lt; 00. Let  X be  a measure space, with measure J.L.  Let  f  and g be measurable functions on X, with range in [0,  00]. Then

$$( 1 )$$

$$( 2 )$$

The inequality (1)  is  Holder's; (2)  is  Minkowski's. If p = q = 2,  (1)  is  known as the Schwarz inequality.