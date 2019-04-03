# plot_go_benchmark

Tiny script to plot golang benchmark results of functions which depend on some value n, with the usual format (file to plot must include only the data rows), e.g.:

```
BenchmarkParallelMedian/2097152-4             50          27509265 ns/op
BenchmarkParallelMedian/4194304-4             20          95360383 ns/op
BenchmarkParallelMedian/8388608-4             10         161270545 ns/op
BenchmarkParallelMedian/16777216-4             3         360463878 ns/op

BenchmarkMedian/2-4                        50000             26534 ns/op
BenchmarkMedian/4-4                        50000             27027 ns/op
BenchmarkMedian/8-4                        50000             36279 ns/op
BenchmarkMedian/16-4                       50000             32538 ns/op

```

Only input parameter is name of the file containing benchmark results. Script will generate a file called output.png with the plot.
