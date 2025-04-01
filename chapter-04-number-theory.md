**📘 Chapter 4: Number Theory and Cryptography**

------------------------------------------------------------------------

**🔢 4.1 Divisibility and Modular Arithmetic**

- **Divides**: a \| b ⇔ ∃k ∈ ℤ such that b = ak

- **Mod (modulo)**: a ≡ b (mod n) ⇔ n divides (a - b)

**Examples:**

- 17 ≡ 5 (mod 12) → because (17 - 5 = 12), and 12 is divisible by 12

- 9 mod 4 = 1 (because 9 = 2×4 + **1**)

------------------------------------------------------------------------

**🔁 4.2 Integer Division**

- For integers a, d (d ≠ 0), ∃ unique q, r:\
    **a = dq + r**,  0 ≤ r \< \|d\|

- q: quotient, r: remainder

------------------------------------------------------------------------

**🧮 4.3 GCD and LCM**

- **gcd(a, b)**: largest integer that divides both a and b

- **lcm(a, b)** = (a × b) / gcd(a, b)

**Euclidean Algorithm:**

css

CopyEdit

function gcd(a, b)

while b ≠ 0

r ← a mod b

a ← b

b ← r

return a

**🧠 4.4 Modular Arithmetic Rules**

- If a ≡ b (mod n), then:

  - a + c ≡ b + c (mod n)

  - a - c ≡ b - c (mod n)

  - a \* c ≡ b \* c (mod n)

  - (if c is invertible) a / c ≡ b / c (mod n)

------------------------------------------------------------------------

**🔐 4.5 Applications: Cryptography**

**Caesar Cipher:**

- Shift each letter by k places in alphabet

- Example (k = 3): A → D, B → E, ...

**Modular Inverse:**

- a⁻¹ mod n is the number such that a \* a⁻¹ ≡ 1 (mod n)

------------------------------------------------------------------------

**💥 4.6 RSA Encryption (Basics)**

1.  Choose primes p, q

2.  Compute n = p × q

3.  Compute φ(n) = (p-1)(q-1)

4.  Choose e such that gcd(e, φ(n)) = 1

5.  Compute d ≡ e⁻¹ mod φ(n)

6.  Public key: (n, e), Private key: (n, d)
