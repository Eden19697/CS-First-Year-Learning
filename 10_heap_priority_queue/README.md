# Chapter 10: Heap / Priority Queue

This chapter practices Python's `heapq` module: a min heap that always keeps the smallest item at index `0`,
and the "keep only the best k so far" pattern that comes up in a lot of top-k / closest / priority problems.

## Core ideas

| Tool | Best use | Example |
| --- | --- | --- |
| `heapq.heappush` / `heappop` | Push/pop while keeping the smallest item at `heap[0]` | `heapq.heappush(heap, num)` |
| `heapq.heapify` | Turn an existing list into a heap in place | `heapq.heapify(numbers)` |
| Negate to simulate a max heap | `heapq` is min-only, so push `-number` and negate again on pop | `heapq.heappush(heap, -number)` |
| Bounded heap of size k | Push everything, pop whenever size exceeds k, so only the "best k so far" survive | `if len(heap) > k: heapq.heappop(heap)` |
| Tuple ordering | A tuple like `(priority, name)` sorts by its first element first | `heapq.heappush(heap, (priority, task_name))` |

Every heap operation runs in **O(log n)**, which is why a heap beats re-sorting the whole list every time you need the current min/max.

## Practice files

| File | Main pattern |
| --- | --- |
| `heap_basic.py` | Build a min heap with `heappush`, peek `heap[0]`, pop everything in sorted order |
| `heapify_basic.py` | Convert an existing list into a heap in place with `heapify` |
| `max_heap_basic.py` | Simulate a max heap by pushing/popping negated numbers |
| `k_largest.py` | Bounded min heap of size k → the k largest values |
| `kth_largest.py` | Same bounded heap, but only `heap[0]` (the kth largest) is needed |
| `k_closest_points.py` | Push `(distance_squared, point)` tuples, pop the k smallest distances |
| `top_k_frequent.py` | Count with a `dict`, then bound a heap of `(count, number)` by size k |
| `priority_task_queue.py` | A `PriorityTaskQueue` class wrapping `heapq` with add/pop/peek/is_empty |
| `merge_k_sorted_arrays.py` | Heap of `(value, array_index, element_index)`, push the next element after each pop |
| `dijkstra_basic.py` | Dijkstra's shortest path: always expand the node with the smallest known distance |

## A useful problem-solving template

Before writing code, ask:

1. Do I only need the current min/max, not a full sort? Use a heap instead of re-sorting every time.
2. Do I need "the best k so far," not everything? Keep a heap bounded to size k, popping whenever it grows past k.
3. Am I comparing more than one field (priority + name, distance + point)? Push a tuple — Python compares tuples
   element by element, so the first field decides the order.

## Run a practice file

From the repository root:

```bash
python3 10_heap_priority_queue/heap_basic.py
python3 10_heap_priority_queue/heapify_basic.py
python3 10_heap_priority_queue/max_heap_basic.py
python3 10_heap_priority_queue/k_largest.py
python3 10_heap_priority_queue/kth_largest.py
python3 10_heap_priority_queue/k_closest_points.py
python3 10_heap_priority_queue/top_k_frequent.py
python3 10_heap_priority_queue/priority_task_queue.py
python3 10_heap_priority_queue/merge_k_sorted_arrays.py
python3 10_heap_priority_queue/dijkstra_basic.py
```

## Common reminders

- `heapq` only implements a **min** heap. To get max-heap behavior, push negated values and negate again on pop.
- When wrapping a heap in a class, keep the "return just the value the caller asked for" contract consistent —
  a method that peeks or pops should return the piece of data the docstring promises (e.g. just the task name),
  not the raw `(priority, value)` tuple the heap actually stores internally.
- A bounded heap of size k doesn't need to track "is this in the top k" directly — just push everything and pop
  whenever the heap grows past k; whatever survives at the end is the answer.
- Heap order is not stable across equal keys, and "any order" in an expected output means exactly that — don't
  worry if two runs return the same *values* in a different order.
