# BFS vs DFS Route Finding – SLE-2 Profiling

## Introduction

This project is created for SLE-2 of the course
**Introduction to Artificial Intelligence (02AML204)**.

The aim of this experiment is to implement and compare two basic
graph-search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on small unweighted graphs to study their
search behaviour and performance.

---

## Problem Statement

The problem used in this project is route finding in an unweighted graph.

A starting node and a goal node are given. BFS and DFS search the same
graph and attempt to find a route from the start node to the goal node.

Their performance is compared using:

- Execution time
- Nodes expanded
- Path returned
- Path length

---

## Algorithms Used

### Breadth-First Search (BFS)

BFS explores the graph level by level.

It uses a **queue** to store the nodes that have to be explored.

For an unweighted graph, BFS guarantees the shortest path in terms of
the number of edges.

### Depth-First Search (DFS)

DFS explores one branch of the graph as deeply as possible before
backtracking.

It uses a **stack** in this implementation.

DFS can sometimes reach a goal quickly, but the first path found is not
guaranteed to be the shortest path.

---

## Test Cases

Three graph sizes are used in the experiment.

| Test Case | Graph Size | Start | Goal |
|---|---:|---:|---:|
| Best Case | 5 nodes | 0 | 1 |
| Average Case | 10 nodes | 0 | 9 |
| Worst Case | 16 nodes | 0 | 15 |

This allows BFS and DFS to be observed under different search
conditions.

---

## Profiling Method

Python's `time.perf_counter_ns()` is used for high-resolution execution
time measurement.

Each algorithm is executed **5000 times** for every test case.

The average execution time is then converted from nanoseconds to
microseconds.

A manual counter is also used to record the number of nodes expanded
during the search.

---

## How to Run

Make sure Python is installed.

Clone or download this repository and open the project folder.

Run:

```bash
python bfs_dfs.py
