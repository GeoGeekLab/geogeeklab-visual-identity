# GeoGeekLab Visual Identity System — V0.2

This package turns the approved visual direction into **individual project identity systems**. It follows the existing GeoGeekLab brand foundations rather than replacing them.

## Current coverage

- **8 scientific instruments:** Six editable SVG applications each: primary, two-tone monochrome, inverse, square icon, README hero, social preview.
- **7 RefFox specializations:** Three *concept-only* SVG applications each, plus a distinct discipline specification. They must be reconciled against the original RefFox asset before publication.
- **3 new mascots:** Three editable concept-only SVG applications each, with character anchors, states and specific project use cases.
- **6 existing mascot projects:** Individual identity sheets and canonical asset paths; original art not copied or replaced.
- **2 core repositories:** No added logo or mascot.

## Important status

These are **production-structure prototypes, not fully approved brand artwork**. All science logo icons need an expert visual-semantic pass. The seven illustrative RefFox drawings are placeholders and must not replace the official RefFox master. Mascot expressions and action scenes remain to be illustrated after character approval. The pre-existing art is stored in its current GitHub repositories and referenced by URL.

## How to inspect

Open `index.html`. Filter projects by identity type and open each project’s `identity-sheets/<repo>.md` for design constraints. SVG files contain editable vector instructions and are not flattened images.

## Folder conventions

```text
GeoGeekLab-VIS-v0.2/
  index.html
  identity-sheets/<26 project files>.md
  logos/<8 projects>/{primary,monochrome,inverse,app-icon,readme-hero,social-preview}.svg
  family/ref-fox/<7 projects>/{concept,concept-avatar,concept-readme-hero}.svg
  new-mascots/<3 projects>/{concept,concept-avatar,concept-readme-hero}.svg
  manifests/registry.json
  previews/overview.png
  references/ (AI moodboard, illustrative only)
```

## Visual standards

1. **Identity continuity:** Preserve each existing mascot’s silhouette, face, recognition anchors and palette.
2. **Color:** Parent brand is paper `#F6F4EE`, ink `#152019`, signal `#A64624`. Project palettes may differ. Do not recolor Geo Gecko to match the parent.
3. **Typography:** Interface = Instrument Sans; editorial = Newsreader; data = IBM Plex Mono. SVG mockups use system fallbacks; project builds should load licensed fonts independently.
4. **Scale:** Test at 32, 64 and 128px. Remove secondary props when they become unreadable.
5. **Scientific semantics:** No imagery may imply unverified results or official endorsements.
6. **Deliverable:** Canonical SVG, 32/64/128 PNGs, social preview and light/dark handling; mascot pose sheets where applicable.

## Approval stages

`research → master concept → shape lock → variants → size/contrast QA → owner approval → publish`

The package has not been pushed to GitHub. The page is an offline-first local reference. Existing source art is linked rather than embedded.

## Repository status

This repository tracks **draft visual identity concepts (V0.2)**. Existing mascots remain canonical in their original project repositories; scientific logo concepts and new character studies require review before rollout.
