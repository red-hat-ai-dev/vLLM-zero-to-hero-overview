# Behind the scenes

The [overview](../README.md) is the starting point for the course. It connects
the lessons; there is nothing to install or run in this repository.

## How the lessons fit together

| Step | What happens | What you carry forward |
| --- | --- | --- |
| [Part 1: Run](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-pt1) | Start a model server and send a request to its local API. | An understanding of starting, using, and stopping vLLM. |
| [Part 2: Optimize](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-pt2) | Create a compressed checkpoint and explore speculative decoding. | A checkpoint you can reuse and techniques you can measure. |
| [Part 3: Benchmark](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-pt3) | Measure an endpoint's speed and answer quality, then compare models. | Saved reports for understanding the tradeoffs. |
| [Extra credit](https://github.com/red-hat-ai-dev/vllm-zero-to-hero-extra-credit) | Explore additional inference concepts through optional lessons. | Context for going beyond one local server. |

Each lesson's README is its walkthrough. Its linked “Behind the scenes” guide
explains the supporting files and what the commands do. Follow the walkthrough
first; open the guide when you want more detail.

The lessons do not run automatically in sequence. Finish and stop the server
from one step before starting the next. Each hands-on repository contains its
own launch commands and requirements.

## What is in this repository?

- [`README.md`](../README.md) introduces the course and links to each lesson.
- [`docs/`](.) holds this guide and the course illustration.
- [`docs/assets/vllm-journey-extra-credit.svg`](assets/vllm-journey-extra-credit.svg)
  is the diagram shown on the overview page. GitHub displays it directly; no
  website build is needed.

Some course repositories are intentionally private while they are being
prepared. A link requiring access does not mean your local setup is broken.

## Where validation lives

The [course RFC](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-overview/issues/3)
tracks ongoing review. Each lesson keeps its own platform evidence and open
checks in its RFC. A command being present is different from that path having
been tested on a particular machine.

[Back to the course](../README.md)
