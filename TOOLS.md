# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## Hardware
- **Machine:** Dell XPS 15 9520 (Linux Mint 22.2)
- **GPU:** NVIDIA RTX 3050 Ti Mobile (~4GB VRAM)
- **CPU:** Intel i9-12900HK (20 cores)
- **RAM:** 31 GB total
- **Storage:** NVMe 938GB (78GB used)
- **Full details:** See HARDWARE.md

## AI/ML Setup
- **AirLLM target:** 70B models on 4GB GPU (perfect for RTX 3050 Ti)
- **Local models:** Testing phase — first AirLLM run pending
- **CUDA:** Check `/usr/local/cuda` for toolkit status

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
