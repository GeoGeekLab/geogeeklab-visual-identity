# Earth Pulse · Visual Identity System

**Project:** [earth-pulse](https://github.com/GeoGeekLab/earth-pulse)  
**Batch:** 03 · Scientific instruments  
**Status:** Formal design candidate; not automatically adopted in the product repository.

## Design premise

Locate the event. Read the signal.

The mark represents **Seismic catalog · magnitude · time-window analysis** through a geometric shorthand. It is a visual metaphor, not a scientific plot or measurement.

## Scientific guardrails

The waveform is a graphic metaphor, not a real seismogram or earthquake prediction.

## Color tokens

| Token | Value | Role |
|---|---|---|
| `accent` | `#237E9A` | Distinct project signal |
| `secondary` | `#D46E3E` | Secondary scientific layer |
| `pale` | `#DCEEF0` | Light icon surface |
| `dark` | `#163E50` | Dark field / typography |
| `brand-paper` | `#F6F4EE` | Shared GeoGeekLab ground |

## Canonical assets

- `primary.svg`: 512 × 512 full-color app tile.
- `symbol.svg`: 512 × 512 scalable, transparent primary mark.
- `monochrome.svg`: 512 × 512 grayscale vector mark.
- `inverse.svg`: 512 × 512 dark-mode tile.
- `favicon.svg`: 256 × 256 compact icon.
- `readme-hero.svg`: 1200 × 400 documentation header.
- `social-preview.svg`: 1280 × 640 social card.
- `construction.svg`: 640 × 640 geometric reference grid.
- `tokens.json`: machine-readable color, descriptive metadata, QA status.

## QA and approval gate

1. Check that the mark represents the scientific process without claiming measured values.
2. Compare 32, 64 and 128 px rendering in both GitHub themes.
3. Review color contrast and a monotone print variant.
4. Validate XML/SVG security: no scripts, remote images or external fonts.
5. Confirm project identity and permission before copying a candidate into the product repository.

**IPCC disclaimer:** all marks in this identity collection are independent GeoGeekLab designs. They do not imply affiliation with, approval by, or endorsement from IPCC.
