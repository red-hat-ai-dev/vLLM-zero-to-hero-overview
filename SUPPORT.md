# Validation across the learning path

Reviewed 2026-10-07. Each lesson owns its tested configurations and reproduction
steps. A launch option means the code has that path; it does not mean that its
exact model has passed a hardware test. Build-only, fake-engine regression,
manual historical evidence, and fresh hardware inference are reported separately.

| Lesson | Support record | Scope |
| --- | --- | --- |
| Part 1 | [Run support](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-pt1/blob/main/SUPPORT.md) | Server startup, requests, image publication and lifecycle |
| Part 2 | [Optimization support](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-pt2/blob/main/SUPPORT.md) | CPU/CUDA conversion, FP8 serving, speculative decoding, Metal differences |
| Part 3 | [Benchmark support](https://github.com/red-hat-ai-dev/vLLM-zero-to-hero-pt3/blob/main/SUPPORT.md) | GuideLLM, lm-eval, result preservation and comparable workloads |
| Extra credit | [Explainer validation](https://github.com/red-hat-ai-dev/vllm-zero-to-hero-extra-credit/blob/main/SUPPORT.md) | Local links/SVGs and conceptual review; no deployment lab |

The support links land when the corresponding lesson changes are merged.
Lesson repositories are intentionally private during development. GitHub access
is required for those links; an anonymous 404 is not evidence of a broken course
link and is not checked as a public availability requirement.

Linux lessons pin vLLM 0.28.0. Part 2 pins LLM Compressor 0.13.0; Part 3 pins
GuideLLM 0.7.4 and lm-eval 0.4.13. Metal installs the current stable release or
reuses the user's environment, so its actual versions must be recorded per run.
The overview does not promise one common GPU/model support matrix for all parts.

Run `python3 -m unittest discover -s tests -v` to check local references and SVG
XML. Pull-request CI runs those checks; it does not test inference. Maintainers
should update the lesson records after dependency/model changes and attach exact
hardware evidence to the relevant issue or PR. ROCm, XPU, and WSL2 remain
unverified for the complete sequence until matching tests are recorded.
