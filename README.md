# Prog-Assignment2
Programming Assignment 2 for COP4533 - Algorithms Abstraction and Designs

### Team members:
- Paige Vanover UFID : 22473613
- Victoria Villasana UFID: 86143370

## To get started:
- Clone the repository into your desired Python supported IDE.
- No external dependencies

## Running the Program
- Run main.py and modify the filename variable inside main() to reference the input files that are inside the testfiles/ file.
- For each test(1-7).txt file in the testfiles/, there is a corresponding file test(1-7).out with the expected output in the tests/ folder. The output that is printed after running the program should match the contents of the corresponding .out file.

## Assumptions:
When creating the program, we created sample output files in the tests folder for corresponding input files. The output in those output files should match the print output when running the program with the same input files.

## Question 1:
<img width="795" height="399" alt="image" src="https://github.com/user-attachments/assets/f82f4aa5-c81b-41d4-b6a6-612f16b35acc" />


## Question 2:
Yes, there is a sequence that exists when k = 3. This can explicitly be seen with the file ex1.txt
we created as a test file. In this file, k = 3 and m = 12. The sequence is as follows: 1, 2, 3, 4, 1, 2,
5, 1, 2, 3, 4, 5. When tested, the results were FIFO = 9, LRU = 10, and OPTFF = 7. As tested,
OPTFF had less misses than LRU for this sequence. This happens because LRU only knows the
past so in every case, it will evict the page that seems the least useful based on recent
inputs/history. OPTFF is different in the way that it knows the future sequence that will be
requested. With the each miss that has a full cache, it will evict the page with the next use that is
farthest away in the future or just never used again. This avoids evicting something that could
potentially be used soon.

## Question 3:
Suppose there is another algorithm that is more optimal algorithm A than Belady’s Farthest-in-
Future algorithm with steps {j1, j2, …, jm} and the Belady algorithm has steps {i1, i2, …, in}.
Both algorithms are identical until a step w.l.o.g r where step r+1 differs.
At step r+1, both algorithms have the same pages in memory and need to evict a page. Suppose
Belady evicts some page p and the optimal algorithm evicts page q. Because Belady evicts the
page whose next use is further in the future, the next time p is used is no earlier than the next use
of q.
Because of this, we will replace step j(r+1) with step i(r+1) because it cannot increase the
number of misses. We continue replacing all differing steps that follow and each replacement
does not increase the number of misses.
This would mean that the optimal algorithm is now equal to Belady's farthest-in-the-future
algorithm which is a contradiction to another algorithm being more optimal. Therefore, Belady’s
algorithm is optimal and that its number of misses is no larger than that of A.

## Test Files Overview
These are the input files made to test different behaviors of LRU, FIFO, and OPTFF:

- test1.txt
This tests the minimum cache size (k=1). This will cause every change in page to cause a miss.

- test2.txt
This tests when all requests are identical. Only the first request here should cause a miss.

- test3.txt
This tests if a cache size is larger than the number of distinct pages. Here, no evictions will happen.

- test4.txt
This tests a perfect repeating cycle equal to cache size. After the first initial misses, all of the requests are hits.

- test5.txt
This tests the OPTFF function outperforming LRU and FIFO. OPTFF will make better decisions for pages to evict as it looks ahead.

- test6.txt
This tests if cache size is equal to working set size. After we get initial misses, all of the requests after are hits.

- test7.txt
This tests the OPTFF function when a page is never used again. This is meant to verify that pages are being evicted correctly with no use in the future.