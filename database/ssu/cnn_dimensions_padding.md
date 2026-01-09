---
id: ssu_batch5_005
course: Statistical Machine Learning
tags: [cnn, layer-dimentions, padding, receptive-field]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(3p) A convolutional layer transforms an input volume $W_{in} \times H_{in} \times C$ into an output volume $W_{out} \times H_{out} \times D$, where $W_{in}$ and $H_{in}$ define spatial dimensions of the input and $C$ is the number of input channels. Similarly $W_{out}$ and $H_{out}$ denote spatial dimensions of the output and $D$ the number of filters. Consider stride $S$, zero padding $P$ and filters having receptive field of $F \times F$ units.

**(1)** Give types and total number of parameters of the layer.
**(2)** Consider padding $P$ preserving the size of the output in the $W$ dimension, i.e., $W_{in} = W_{out}$. Give $P$ as a function of $F, S$ and $W_{in}$.

---
# Solution
## (1) Parameters
The learnable parameters in a convolutional layer are the weights of the filters and the biases.
-   **Weights:** Each filter has size $F \times F \times C$. There are $D$ filters.
    Total weights = $F \cdot F \cdot C \cdot D$.
-   **Biases:** One bias per filter (output channel).
    Total biases = $D$.

**Total Parameters:** $(F^2 C + 1) D$.

## (2) Padding $P$ for Preserving Size
The formula relating input and output width is:
$$ W_{out} = \left\lfloor \frac{W_{in} - F + 2P}{S} \right\rfloor + 1 $$
We require $W_{out} = W_{in}$.
$$ W_{in} = \frac{W_{in} - F + 2P}{S} + 1 $$
Multiply by $S$:
$$ S \cdot W_{in} = W_{in} - F + 2P + S $$
$$ 2P = S \cdot W_{in} - W_{in} + F - S $$
$$ 2P = (S-1)W_{in} + F - S $$
$$ P = \frac{(S-1)W_{in} + F - S}{2} $$

*Note:* If $S=1$ (standard stride for preserving size), this simplifies to:
$$ P = \frac{(1-1)W_{in} + F - 1}{2} = \frac{F-1}{2} $$
This is the standard "Same" padding formula. The general formula depends on $W_{in}$ if $S > 1$.

## Related Concepts
- [[cnn]]
- [[layer-dimensions]]
- [[padding]]
