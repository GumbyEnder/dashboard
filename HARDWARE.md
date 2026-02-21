# HARDWARE.md — My Physical Machine

**Device:** Dell XPS 15 9520  
**OS:** Linux Mint 22.2 (Ubuntu 24.04 based)  
**Kernel:** Linux 6.14.0-37-generic x86-64

## CPU
- **Model:** 12th Gen Intel Core i9-12900HK
- **Cores/Threads:** 20 CPUs (mixed P-cores + E-cores)
- **Speed:** Varies by load (17% scaling)

## Memory
- **Total RAM:** 31 GB
- **Current Usage:** ~18 GB (healthy headroom)
- **Architecture:** Single NUMA node

## GPU
- **Dedicated:** NVIDIA GeForce RTX 3050 Ti Mobile (GA107M)
  - VRAM: ~4 GB (estimated)
- **Integrated:** Intel Iris Xe Graphics (Alder Lake-P GT2)

## Storage
- **Primary:** NVMe SSD 938 GB (Dell)
- **Used:** 78 GB (~8%)
- **Available:** 813 GB

## Implications for Local LLM Work

### Current Situation
- **GPU VRAM:** RTX 3050 Ti has ~4GB (tight for large models)
- **CPU:** Strong (i9-12900HK is powerful)
- **RAM:** 31GB available (good for CPU offloading)
- **Disk:** Plenty of space for models

### Why AirLLM is Perfect for This Hardware
- 70B models need 4GB VRAM? That's exactly our RTX 3050 Ti limit
- Strong CPU can handle bandwidth optimization (AirLLM's strategy)
- 31GB RAM available for intermediate buffers
- This is exactly the use case AirLLM was built for

### Next Steps for Local Model Testing
1. Install CUDA toolkit for RTX 3050 Ti (if not done)
2. Try AirLLM with 70B model (Llama 2 or Llama 3.1)
3. Benchmark: inference speed, memory usage, power draw
4. Compare to previous failed attempts (what was blocking?)

---

**Updated:** 2026-02-20 21:44 EST  
**Status:** Ready for AirLLM testing on Dell XPS hardware
