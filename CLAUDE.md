# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Personal coding interview practice collection. Solutions are standalone files — no build system, no test runner, no dependencies.

## Languages

- **Python** (`.py`) — used for most LeetCode, Coderbyte, HackerRank, and Teko problems. Uses `from typing import List` and standard library only.
- **TypeScript** (`.ts`) — used for Codility problems and some LeetCode variants. No `tsconfig.json`; files are standalone type-annotated solutions.

## Running Solutions

```bash
python3 leetcode/array/someFile.py
# or
npx ts-node codility/someFile.ts
```

## Directory Structure

| Directory | Source | Notes |
|---|---|---|
| `leetcode/` | LeetCode | Organized by topic (array, graph, dp, concurrency, etc.) |
| `leetcode/top150/` | LeetCode Top 150 | Organized by topic, often more polished solutions |
| `coderbyte/` | Coderbyte | Python only |
| `codility/` | Codility | TypeScript only |
| `hackerrank/` | HackerRank | Python |
| `teko/` | Teko company tests | Python; `testreal*.py` = real interview, `test*.py` = practice |
| `others/` | Misc | BFS reference implementations |

## Key Reference File

`leetcode/concurrency/CONCURRENCY_NOTES.md` — detailed notes on Python threading primitives (Lock, Semaphore, Barrier) with LeetCode 1114 as the running example. Read this before working on any concurrency problem.

## Conventions

- Each file is a single self-contained solution — typically one `class Solution` with one method, or a standalone function.
- No imports beyond standard library (`typing`, `threading`, `collections`, `heapq`, etc.).
- TypeScript files use plain interfaces and types with no external packages.
- `draft.py` and `test.py` / `test2.py` files in `leetcode/` are scratch/experiment files.
