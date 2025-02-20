# An EXPOENTIAL SPACETIME-complete problem

## EXPSPACE

An **EXPSPACE-complete** problem is one that is both in **EXPSPACE** (solvable with exponential space) and **EXPSPACE-hard** (at least as hard as every problem in EXPSPACE under polynomial-time reductions). These problems require **exponential space** to solve in the worst case and are among the hardest problems in **EXPSPACE**.

### **Definition of EXPSPACE**
EXPSPACE is the class of decision problems solvable by a **deterministic Turing machine** using at most **\(2^{p(n)}\)** space, where \( p(n) \) is a polynomial function of the input size \( n \). That is:
\[
\text{EXPSPACE} = \bigcup_{k \geq 1} \text{DSPACE}(2^{n^k})
\]

### **An Example of an EXPSPACE-Complete Problem**
A classic EXPSPACE-complete problem is **Generalized Reversi (Othello)** or **Generalized Chess**, played on an \( n \times n \) board. However, a well-known theoretical example is:

#### **Generalized Regular Expression Inequality Problem**
Given two **regular expressions** \( R \) and \( S \), does there exist a string \( w \) such that \( w \) is in the language of \( R \) but **not** in the language of \( S \)?
\[
L(R) \not\subseteq L(S)
\]
- This problem is known to be **EXPSPACE-complete** because it requires storing exponentially large automata when converting the regular expressions into equivalent deterministic finite automata (DFA).
- The conversion from an **NFA to DFA** can cause an exponential blowup in states, requiring **exponential space** to store.

### **Other EXPSPACE-Complete Problems**
1. **Generalized Chess (n × n board)**
   - Deciding whether a player has a winning strategy in an \( n \times n \) chess game.
   - The game tree can have an **exponential height**, requiring exponential space to evaluate.
   
2. **Generalized Go (n × n board)**
   - Determining whether the first player has a winning move in **generalized Go**.
   - Similar to Chess, the game tree grows exponentially.

3. **Generalized Reversi (Othello)**
   - Determining whether the first player has a winning move in an arbitrary-sized **Reversi** game.
   - Also requires **exponential space** to explore all possible moves.

4. **Succinct Circuit Value Problem (SCVP)**
   - Given a Boolean circuit represented **succinctly** (e.g., via a compressed encoding), decide whether it evaluates to **true**.
   - Requires storing and evaluating an exponentially large circuit.

### **Conclusion**
EXPSPACE-complete problems are among the hardest problems solvable in exponential space. Many of these problems arise from **games with exponential branching**, **compressed automata representations**, or **succinctly described circuits**. These problems are believed to be **strictly harder** than PSPACE-complete problems, meaning they require more than just polynomial space to solve.
