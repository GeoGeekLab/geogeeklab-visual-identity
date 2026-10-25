# GeoGeekLab Visual Identity System

**One identity. Many forms.**

A shared identity architecture for GeoGeekLab’s scientific instruments, developer tools, reviewer skills, and educational projects.

> **Status: V0.2 — concepts for review, not approved artwork.** No target product repository has been changed by this central deployment.

[**Visual Gallery →**](GALLERY.md) · [中文规范 →](GUIDE.zh-CN.md) · [Project Registry →](manifests/registry.json) · [Asset Validation →](VALIDATION.md) · [Art & Provenance →](ARTWORK-NOTICE.md)

## The visual principles

**Tools have personalities. Instruments have precision.**

- **Mascots** give tools and agent skills a recognizable, approachable character.
- **RefFox family** shares one character across seven scientific reviewing domains.
- **Scientific logos** use meaningful geometry and real instrument screenshots; no forced animal identity.
- **Personal and website repositories** keep their existing design; no new mascot.

## Coverage

| Identity class | Projects | Status |
|---|---:|---|
| Existing mascots | 6 | Preserve canonical source artwork |
| RefFox reviewer variants | 7 | Structural concept SVGs; original RefFox must be respected |
| New mascot proposals | 3 | Concept SVGs; characters not yet approved |
| Scientific instrument logos | 8 | Six editable SVG applications per instrument; review required |
| No new design | 2 | Existing identity retained |
| **Total** | **26** | **V0.2 concept release** |

## See the work

| Earth in Change | Orbital Commons | Image to Trace | Water as Spectrum |
|---|---|---|---|
| <img src="logos/earth-in-change/primary.svg" width="120" alt="Earth in Change concept"> | <img src="logos/orbital-commons/primary.svg" width="120" alt="Orbital Commons concept"> | <img src="logos/image-to-trace/primary.svg" width="120" alt="Image to Trace concept"> | <img src="logos/water-as-spectrum/primary.svg" width="120" alt="Water as Spectrum concept"> |

[Browse all 18 design proposals and 6 canonical mascot links →](GALLERY.md)

## Source of truth and visual tokens

The parent brand tokens are based on the existing [GeoGeek website](https://github.com/GeoGeekLab/GeoGeekLab.github.io/blob/main/site/styles.css):

| Token | Value |
|---|---|
| Paper | `#F6F4EE` |
| Ink | `#152019` |
| Soft | `#435048` |
| Signal | `#A64624` |
| Atlas dark | `#17211B` |
| Interface | Instrument Sans |
| Editorial | Newsreader |
| Data / code | IBM Plex Mono |

**Project-specific palettes remain independent.** Do not recolor an existing mascot to force corporate uniformity.

## Repository structure

```text
GALLERY.md                   GitHub-native visual overview
GUIDE.zh-CN.md               Chinese design and approval manual
ARTWORK-NOTICE.md            Asset provenance and release guardrails
identity-sheets/             26 project-specific rules
logos/                       8 × 6 editable scientific instrument SVGs
family/ref-fox/              7 × 3 unapproved reviewer-concept SVGs
new-mascots/                 3 × 3 unapproved character-concept SVGs
manifests/registry.json      Machine-readable catalog
index.html                   Offline gallery (download files to open locally)
scripts/validate_vis.py      Structural validation
```

The local V0.2 package also contains raster previews and AI moodboards. **This GitHub deployment publishes text and editable SVG sources; raster moodboards are not canonical artwork.**

## Review → approval → production

`research → identity anchors → concept → revision → science and size QA → owner approval → project integration`

Publication to this *central design repository* does not approve the assets for use as official product logos. Do not replace an existing mascot or ship a RefFox concept as a production character without reconciling its original master.

*Geo to see. Geek to build.*
