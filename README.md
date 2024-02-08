# goit-algo-fp

## Probabilities of combinations outcome for throwing two 6-sided dices using Monte Carlo method with multiple iterations

| Sum | Calculated Probability | Monte Carlo 100 | Monte Carlo 1_000 | Monte Carlo 100_000 | Monte Carlo 1_000_000 |
| --- | ---------------------- | --------------- | ----------------- | ------------------- | --------------------- |
| 2   | 2.78% (1/36)           | 0.0500          | 0.0270            | 0.0275              | 0.0281                |
| 3   | 5.56% (2/36)           | 0.0600          | 0.0570            | 0.0550              | 0.0556                |
| 4   | 8.33% (3/36)           | 0.0800          | 0.0720            | 0.0823              | 0.0829                |
| 5   | 11.11% (4/36)          | 0.0800          | 0.1190            | 0.1113              | 0.1106                |
| 6   | 13.89% (5/36)          | 0.1100          | 0.1220            | 0.1386              | 0.1392                |
| 7   | 16.67% (6/36)          | 0.2200          | 0.1760            | 0.1667              | 0.1671                |
| 8   | 13.89% (5/36)          | 0.1500          | 0.1290            | 0.1387              | 0.1386                |
| 9   | 11.11% (4/36)          | 0.0800          | 0.1090            | 0.1110              | 0.1110                |
| 10  | 8.33% (3/36)           | 0.0900          | 0.1010            | 0.0846              | 0.0834                |
| 11  | 5.56% (2/36)           | 0.0400          | 0.0480            | 0.0559              | 0.0556                |
| 12  | 2.78% (1/36)           | 0.0400          | 0.0400            | 0.0284              | 0.0279                |

The Monte Carlo simulations provide a practical method to estimate the probabilities of rolling certain sums with two dice. With more iterations, the precision of these Monte Carlo predictions enhances, aligning more closely with the theoretical probabilities. Therefore using the Monte Carlo method for estimating the probabilities is only effective with the large amount of iterations.
