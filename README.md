[![Contributors][contributors-shield]][contributors-url]
[![Commit-activity][commit-activity-shield]][commit-activity-url]
[![Issues][issues-shield]][issues-url]
[![Repo-size][repo-size-shield]][repo-size-url]
[![License][license-shield]][license-url]  
[![Forks][forks-shield]][forks-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Welcome to Arithmetic-Sequence !!!

A Python module for finding arithmetic sequences for a given sequence.  
Just enter a list and get back all arithmetic sequences from it! 🚀

## What does the script do?

Module returns a list of lists that contain arithmetic sequences found in the entered list

## `arithmeticSequences(A,n)` :
arithmeticSequences(A,n) returns a list of lists of all arithmetic sequences from list `A` with common difference `n` or all common differences if n = 0. This includes subsequences of existing sequences.  
An arithmetic sequence is valid only if it has more then 2 items.

## `distArSeq(A,n)` :
distArSeq(A,n) returns a list of lists of distinct arithmetic sequences from list `A` with common difference `n` or all common differences if n = 0.  
distArSeq(A,n) returns a list that has no arithmetic sequences that are a subsequence of an existing sequence.  
An arithmetic sequence is valid only if it has more then 2 items.

<!--- 
## How to use it
#### 1. Clone this repository:
```bash
$ git clone https://github.com/StokicDusan/Arithmetic-Sequence.git
$ cd Arithmetic-Sequence/
```
--->

## Examples
```python
>>> import arithmeticSequence as ASE

>>> arSeq = [61,10,11,30,21,20,40,41,50,60,1,70]
>>> ASE.distArSeq(arSeq)
[[1, 11, 21], [1, 21, 41, 61], [10, 20, 30, 40, 50, 60, 70], [10, 30, 50, 70], [10, 40, 70], [20, 40, 60]]
>>> ASE.distArSeq(arSeq,20)
[[1, 21, 41, 61], [10, 30, 50, 70], [20, 40, 60]]

>>> arSeq = [2,10,17,24,31,38,45,52,60]
>>> ASE.distArSeq(arSeq)
[[2, 31, 60], [10, 17, 24, 31, 38, 45, 52], [10, 24, 38, 52], [10, 31, 52], [17, 31, 45]]
>>> ASE.distArSeq(arSeq,7)
[[10, 17, 24, 31, 38, 45, 52]]
>>> ASE.distArSeq(arSeq,11)
[]

>>> arSeq = [1,10,30,40,80,110]
>>> ASE.distArSeq(arSeq)
[]
```

## Provide Feedback 👍

If you encounter any bugs or have suggestions, please file an issue in the [Issues][issues-url] section of the project.

[contributors-shield]: https://img.shields.io/github/contributors/StokicDusan/Arithmetic-Sequence
[contributors-url]: https://github.com/StokicDusan/Arithmetic-Sequence/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/StokicDusan/Arithmetic-Sequence?style=social
[forks-url]: https://github.com/StokicDusan/Arithmetic-Sequence/network/members
[issues-shield]: https://img.shields.io/github/issues/StokicDusan/Arithmetic-Sequence
[issues-url]: https://github.com/StokicDusan/Arithmetic-Sequence/issues
[commit-activity-shield]: https://img.shields.io/github/last-commit/StokicDusan/Arithmetic-Sequence
[commit-activity-url]: https://github.com/StokicDusan/Arithmetic-Sequence/graphs/commit-activity
[license-url]: https://github.com/StokicDusan/Arithmetic-Sequence/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/StokicDusan/Arithmetic-Sequence
[repo-size-shield]: https://img.shields.io/github/repo-size/StokicDusan/Arithmetic-Sequence
[repo-size-url]: https://img.shields.io/github/repo-size/StokicDusan/Arithmetic-Sequence
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=plastice&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/stokicdusan
