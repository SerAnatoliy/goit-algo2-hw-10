### Conclusions for Task 1

- For each array size tested (1000, 5000, 10000, and 50000), the deterministic QuickSort consistently achieved lower
  average execution times compared to the randomized QuickSort.
- It is important to note that the sizes of the test arrays were intentionally kept lower than typical production sizes to
  ensure that the tests would run more quickly. This choice helped in obtaining rapid feedback during experimentation.
- The slight advantage of deterministic QuickSort in these experiments may be attributed to the fixed pivot selection
  method, which in these cases resulted in marginally faster performance. However, while deterministic QuickSort performed
  better in these tests, randomized QuickSort is generally preferred in practice for its robustness against worst-case
