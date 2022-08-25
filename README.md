# **PQC Alogrithm - SPHINCS+**
###### tags: `PQC` `SPHINCS+` `Hash-based` `Algorithm` `Cryptography`
## :memo: **Table of Contents**
[TOC]
## :key: **Introduction to Hash Functions**
### **Properties**
> A cryptographically secure hash function has certain properties：
:::info
* **Uniformity**
    * For any given hash value, the probability that a random input is mapped to it should be 1/2^n. ---> **pseudorandom**
* **Preimage Resistance**
    * It should be infeasible to find an input for any given output, i.e., we can’t find x if we only know y = h(x). ---> **one-way function**
* **Second Preimage Resistance**
    * It should be infeasible to find another input which produces the same output, i.e., we can’t find x' != x for a given x such that h(x) = h(x').
* **Collision Resistance**
    * It should be infeasible to find any two inputs with the same hash value, i.e., we can’t we can’t find x' != x for a given x such that h(x) != h(x').
:::
> References：
[Postquantum Crypto Minischool](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
## :lock: **Introduction to SPHINCS+**
> References:
> https://sphincs.org/resources.html
> 
> https://www.fraunhofer.sg/content/dam/singapur/FWS/FWS01-PQC/slides/07_FWS01_XMSS.pdf
### **SHA-256**

> References：
> [SHA 256 Algorithm Explanation(Youtube)](https://www.youtube.com/watch?v=nduoUEHrK_4&ab_channel=Simplilearn)
> 
> [How Does SHA-256 Work?(Youtube)](https://www.youtube.com/watch?v=f9EbD6iY9zI&ab_channel=learnmeabitcoin)
> 
> [SHA1 SHA2簡解](https://ithelp.ithome.com.tw/articles/10241695)
### **OTS ( Lamport One-Time Signature )**



#### Implement：
:::success
* **Signempty ( Python )**
:::spoiler
![](https://i.imgur.com/N2Au71b.png)
:::

:::success
* **Signbit ( Python )**
:::spoiler
![](https://i.imgur.com/ch0zz3M.png)
:::

:::success
* **Sign4bits ( Python )**
:::spoiler
![](https://i.imgur.com/LBwC4rY.png)
:::danger
**Do not use one secret key to sign two messages！**
:::

:::success
* **Signmessage ( Python )**
    * Sign arbitrary-length message by signing its 256-bit hash.
:::spoiler
![](https://i.imgur.com/SsPdxfa.png)
:::

> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> [一次性簽章 ](https://iotazh.gitbook.io/iota-guidebook/tangle/transaction/ots)

### **WOTS ( Winternitz One-Time Signatures )**
![](https://i.imgur.com/lJF51Lq.png)




![](https://i.imgur.com/wLnW7wn.png)
> References：
> https://asecuritysite.com/encryption/wint


### **WOTS+**

> References：
> https://huelsing.net/wordpress/wp-content/uploads/2013/05/wotsspr.pdf
> 
> https://www.cryptologie.net/article/306/hash-based-signatures-part-i-one-time-signatures-ots/


### **Merkle Tree**
![](https://i.imgur.com/lUSQbg6.png)

---
![](https://i.imgur.com/ilKNpVv.png)
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> https://ithelp.ithome.com.tw/articles/10215108
> 
>https://neoatlantis.org/%E7%94%B5%E5%B7%A5%E7%94%B5%E5%AD%90%E5%8F%8A%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF/2013/12/16/mss-principles.html
>
>https://www.796t.com/content/1544187062.html
### **XMSS ( eXtended Merkle Signature Scheme )**
![](https://i.imgur.com/sBT6H2r.png)

---
![](https://i.imgur.com/fymyxES.png)

:::info
**Overview:**
* Based on cryptographic hash functions.
* Foundations by Lamport, Diffie, Winternitz, and Merkle in the 1970’s and 1980’s.
* Uses masks do be independent from collision resistance.
* Only for signature schemes.
* Considered well trusted, reliable, and ready for use.
* Has relatively large signatures (20 kB to 100 kB); requires to manage a state.
:::
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> https://www.youtube.com/watch?v=VmdKoDKy2TA
> 
> https://www.youtube.com/watch?v=YraKuRUc0HM
> 
> https://crypto.stackexchange.com/questions/87718/pqc-xmss-l-trees
### **TreeHash Algorithm**
![](https://i.imgur.com/LG3Vgwg.png)

* TreeHash(v,i): Computes node on level v with leftmost descendant Li
```
TreeHash(v, i)
Init Stack, N1, N2
for j = i to i+2v-1 do
    N1 = LeafCalc(j)
    while N1.level() == Stack.top().level() do
        N2 = Stack.pop()
        N1 = ComputeParent(N2, N1)
    end while
    Stack.push(N1)
end for
return Stack.pop()
```
* Public Key Generation: run TreeHash(h,0)
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
### **BDS Algorithm**
* **Many nodes are computed many times!**
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> https://huelsing.net/wordpress/wp-content/uploads/2015/03/part-08.pdf
### **Multi-Tree XMSS**
![](https://i.imgur.com/uJ2Hx4Q.png)
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> https://crypto.stackexchange.com/questions/88438/what-exactly-is-the-purpose-of-the-multi-tree-variant-in-hash-based-schemes
### **Few-time Signatures: FORS ( Forest Of Random Subsets )**
![](https://i.imgur.com/1LemWea.png)
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> https://link.springer.com/chapter/10.1007/978-3-030-51938-4_12
> 
> https://crypto.stackexchange.com/questions/86874/is-there-a-difference-in-the-security-provided-by-a-ots-vs-a-mts-or-fts-or-are
### **HyperTree**
![](https://i.imgur.com/SvvQAvh.png)
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
> 
> https://en.wikipedia.org/wiki/Hypertree
### **Summary for Hash-based Cryptography**
:::info
• Only helpful for Signatures.
• Number of signatures per public key is limited.
• Tree structures allow to sign many messages, e.g., XMSS and LMS.
• There are sate free schemes, e.g., SPHINCS.
• Can get rid of needing collision resistance using masks.
• **SPHINCS+, XMSS, and LMS are (being) standardized!**
• Key generation is expensive.
• Signatures are relatively large.
:::
> References：
> [Postquantum Crypto Minischool ](https://troll.iis.sinica.edu.tw/school22/invited.shtml)
## :pushpin: **Software Implement - SPHINCS+**

### **Parameters**
|               | n  | h  | d  | log(t) | k  | w  | bit security | pk bytes | sk bytes | sig bytes |
| ------------- | ---| ---| ---| ------ | ---| ---| ------------ | -------- | -------- | --------- |
| SPHINCS+-128s | 16 | 63 |  7 | 12 | 14 | 16 | 133 | 32 |  64 |   7856 |
| SPHINCS+-128f | 16 | 66 | 22 |  6 | 33 | 16 | 128 | 32 |  64 | 17,088 |
| SPHINCS+-192s | 24 | 63 |  7 | 14 | 17 | 16 | 193 | 48 |  96 | 16,224 |
| SPHINCS+-192f | 24 | 66 | 22 |  8 | 33 | 16 | 194 | 48 |  96 | 35,664 |
| SPHINCS+-256s | 32 | 64 |  8 | 14 | 22 | 16 | 255 | 64 | 128 | 29,792 |
| SPHINCS+-256f | 32 | 68 | 17 |  9 | 35 | 16 | 255 | 64 | 128 | 48,856 |

### **Part of output**
![](https://i.imgur.com/CGdTne2.png)
> References：
> https://github.com/sphincs/sphincsplus


## :pushpin: **Hardware Implement - SPHINCS+**

> References：
> https://www.researchgate.net/publication/344627240_FPGA-based_SPHINCS_Implementations_Mind_the_Glitch
>
> https://www.mouser.tw/ProductDetail/Xilinx/EK-K7-KC705-G?qs=rrS6PyfT74c5qIqifanqKQ%3D%3D


:::warning
:warning: If I infringe any copyright, let me know and I will remove the offending material ASAP.
:::