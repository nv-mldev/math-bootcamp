# Math Bootcamp — Project Conventions

## Historical notes

When a formula, theorem, or concept has interesting historical context (who invented it, when, why), add it as a **collapsible callout-tip block** in the `.qmd` file — never inline in the main flow.

Use this Quarto pattern (matches the existing "A short history" section in `book-web/chapters/probability/what_is_probability.qmd`):

```markdown
::: {.callout-tip collapse="true"}
## ▶ Short title — what the reader gets if they open it

Body of the historical note. Keep it 3–6 short paragraphs or a bulleted
list of named contributors with dates. Bold names and dates. Cross-link
to other historical figures already covered in the chapter when
possible.
:::
```

**Rules:**

- Always `collapse="true"` — the main flow stays clean for readers who don't want the detour.
- Title prefix `▶` signals "click to expand" visually.
- Cite primary sources (book title + year) when known: e.g. *Ars Conjectandi* (1713), *De Ratiociniis in Ludo Aleae* (1657).
- Prefer named contributors over generic phrasing ("Huygens introduced…" beats "it was introduced…").
- If a portrait is available in `book-web/figures/history/`, use the two-column layout pattern from the existing biographical callouts.

This applies to both the `book-web/` (Quarto) and `book/` (LaTeX) versions of the book — in LaTeX, use the equivalent `funfactsbreak` or a similar custom box.
