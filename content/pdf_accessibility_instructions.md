Title: How to Make a PDF Accessible Under the 2024 ADA Title II Rule (WCAG 2.1 AA, Section 508, PDF-UA)
Date: 2026-08-25 09:00 EDT
Category: LaTeX
Tags: LaTeX, LuaLaTeX, PDF, Accessibility, Section 508, ADA, ADA Title II, WCAG, PDF-UA, Screen Readers, Microsoft Word, Adobe Acrobat
Slug: pdf-accessibility-instructions
Author: Joseph C. Slater
Summary: A step-by-step guide to producing an accessible (tagged) PDF from LaTeX using LuaLaTeX's native tagging support, plus options for Word and Adobe Acrobat, aligned with the 2024 ADA Title II rule's WCAG 2.1 AA requirements.
Status: published

This guide documents, step by step, how an accessible (tagged) PDF was produced
from a LaTeX document (a multi-page CV with tables, lists, and section
headings), plus the general options available if you are not using LaTeX, or
are working without help from an AI assistant. It is written so a person with
no prior accessibility-tagging experience can follow it end to end.

---

## 1. What "accessible PDF" actually means

A PDF is accessible when it has a **tag tree** (also called a "structure
tree") layered on top of the visible page content. The tag tree tells screen
readers and other assistive technology:

- The reading order of the content (not just its visual position on the page)
- Which text is a heading vs. a paragraph vs. a list item vs. a table cell
- What images mean, via alternate ("alt") text
- The document's title and language, so screen readers announce them correctly

A plain PDF produced by ordinary `pdflatex`, Microsoft Word "Print to PDF," or
most PDF export tools has **none of this** — it's just shapes and glyphs on a
page. Screen readers either fail entirely or read the content in a jumbled,
meaningless order (e.g., reading straight across a two-column table instead of
row by row).

You can check whether a PDF is currently tagged with:

```
pdfinfo yourfile.pdf | grep -i tagged
```

`Tagged: no` means it has no accessibility structure at all. This guide
explains how to get to `Tagged: yes` — and, more importantly, how to check
that the tags that were added are actually *correct* (headings tagged as
headings, tables tagged as tables), not just present.

---

## 2. If your document is LaTeX: use LuaLaTeX's native tagging

### 2.1 Why not the `pdflatex` + `tagpdf` package route

There are two ways to get PDF tagging out of LaTeX:

1. The **`tagpdf` package**, loaded the old-fashioned way with `\usepackage{tagpdf}`.
2. The **LaTeX kernel's built-in experimental tagging**, activated via
   `\DocumentMetadata{...}` at the very top of the file, combined with the
   **LuaLaTeX** engine (not `pdflatex`, not `xelatex`).

Option 1 is the more "obvious" one to reach for, but in practice it is
fragile: it broke immediately and unrecoverably on a `letter`-class
document, producing cascading "Undefined control sequence" and "Missing
`\begin{document}`" errors. It does not reliably support common document
classes beyond `article`.

Option 2 (the kernel's native mechanism) is newer, still labeled
experimental, but far more robust. **This is the method used successfully in
this project and is the one this guide documents.**

### 2.2 Step 1 — Add `\DocumentMetadata` as the literal first line

At the very top of your `.tex` file — **before** `\documentclass` — add:

```latex
\DocumentMetadata{lang=en-US,testphase={tagpdf,phase-III,table,tabular}}
\documentclass[12pt]{article}
```

This line must be the first thing in the file. If anything (even a comment)
precedes it, or if it appears after `\documentclass`, LaTeX will throw an
error.

**What the keys mean:**

- `lang=en-US` — sets the document's declared language, required for
  accessibility (screen readers use it to pick pronunciation rules).
- `testphase=tagpdf` — turns on the basic experimental tagging engine. Alone,
  this tags plain paragraphs, links, footnotes, and (with `phase-III`, below)
  lists — but **not** section headings or tables.
- `testphase=phase-III` — loads additional modules bundled under "Phase III"
  of the LaTeX accessibility project, including sectioning support
  (`\section`, `\subsection`, etc.) and list support (`itemize`,
  `enumerate`).
- `testphase=table,tabular` — loads modules that tag plain `tabular` and
  `longtable` content as real PDF tables (`/Table`, `/TR` for table row,
  `/TD` for table cell), which is essential if your document has any tables
  (as most CVs and resumes do).

All of these keys can be combined in one comma-separated list inside a single
set of braces, as shown above. You do not need separate `\DocumentMetadata`
lines.

**How this was actually discovered**: the documented key name
`tagging=on` (which appears in some blog posts) does **not exist** in
current (2024) TeX Live kernels. The real key names were found by directly
inspecting the LaTeX kernel's own source file:

```
/usr/local/texlive/2024/texmf-dist/tex/latex/latex-lab/documentmetadata-support.ltx
/usr/local/texlive/2024/texmf-dist/tex/latex/latex-lab/phase-III-latex-lab-testphase.ltx
```

If a key doesn't behave as expected, grep these files (or the equivalent
path in your own TeX Live installation) for the string `testphase` to see
what values are actually recognized by your installed kernel version.

### 2.3 Step 2 — Compile with `lualatex`, not `pdflatex`

This is not optional. The tagging mechanism relies on LuaTeX engine
features. Building the exact same file with `pdflatex` will either silently
ignore the tagging directives or error out — it will not produce a tagged
PDF.

If your document uses BibTeX (as most CVs with a bibliography do), the full
build sequence is:

```bash
lualatex -interaction=nonstopmode yourfile.tex
bibtex yourfile
lualatex -interaction=nonstopmode yourfile.tex
lualatex -interaction=nonstopmode yourfile.tex
```

Two `lualatex` passes after `bibtex` are needed — one to pull in the
resolved citations, one more to fix up cross-references and page numbers that
shifted as a result.

### 2.4 Step 3 — Set the document title, author, language, and "display title" flag via `hyperref`

Add (or update) a `\hypersetup` call in your preamble:

```latex
\usepackage[colorlinks=true]{hyperref}
\hypersetup{
  pdftitle={Curriculum Vitae - Jane Q. Public},
  pdfauthor={Jane Q. Public},
  pdflang={en-US},
  pdfdisplaydoctitle=true
}
```

Each key matters for a distinct accessibility requirement:

- `pdftitle` — sets the actual document title metadata. Without this,
  screen readers announce the filename (e.g., "cv dot pdf") instead of a
  meaningful title.
- `pdfauthor` — sets author metadata (good practice, not strictly required
  for accessibility, but expected).
- `pdflang` — sets the document-level language tag (redundant with
  `\DocumentMetadata{lang=...}` above, but harmless and worth setting in both
  places for older PDF readers that only look at one).
- `pdfdisplaydoctitle=true` — this is the one people most often miss. Setting
  `pdftitle` alone is **not enough**: without this flag, PDF viewers will
  still show the *filename* in the window/tab title bar instead of the
  document's actual title. This flag sets the PDF's
  `ViewerPreferences/DisplayDocTitle` entry to `true`, which is a distinct,
  separately-checked requirement under WCAG 2.4.2 ("Page Titled") and PDF/UA.

You can verify all four took effect after building with:

```bash
pdfinfo yourfile.pdf | grep -iE "title|tagged"
```

and, for the display-title flag specifically (which `pdfinfo` does not show),
with a small Python script using the `pikepdf` library (`pip install
pikepdf`):

```python
import pikepdf
pdf = pikepdf.open("yourfile.pdf")
print(pdf.Root.get("/ViewerPreferences"))
# Should print: pikepdf.Dictionary({ "/DisplayDocTitle": True })
```

### 2.5 Step 4 — Add alt text to any images

Any meaningful image (a logo, a photo, a signature) needs alternate text so a
screen reader can describe it. With `hyperref` loaded, add an `alt=` key
directly to the `\includegraphics` call:

```latex
\includegraphics[height=0.91in,alt={Handwritten signature of Jane Q. Public}]{signature.png}
```

Purely decorative images (a horizontal rule used as a page divider, for
example) do not need alt text and should ideally be left untagged/marked as
an artifact, but for a typical CV or letter the only image is usually a
signature or a photo, and it should always get real alt text describing what
it depicts, not what it looks like technically (i.e., "Handwritten signature
of Jane Q. Public," not "PNG image, 300dpi, 1.2in tall").

### 2.6 Step 5 — Verify what actually got tagged (do not just trust "zero errors")

Getting a clean compile with no LaTeX errors does **not** guarantee correct
tagging — the experimental modules can silently fail to tag specific
constructs while still producing a perfectly good-looking, error-free PDF.
This project ran into exactly that: table content was rendered but not
tagged in an early attempt, then in a separate incident an entire table
temporarily disappeared from the rendered page (see Section 2.7 below) with
zero LaTeX errors reported.

**Do not skip verification.** Use `pikepdf` to open the structure tree and
count what tag types are actually present:

```python
import pikepdf
from collections import Counter

pdf = pikepdf.open("yourfile.pdf")
counts = Counter()
for obj in pdf.objects:
    if isinstance(obj, pikepdf.Dictionary) and "/S" in obj:
        counts[str(obj.get("/S"))] += 1
print(counts)
```

For a CV with headings, a bibliography-style numbered list, and a few
tables, you should see something like:

```
Counter({
  '/text-unit': 509, '/text': 507, '/Lbl': 440, '/LI': 402, '/LBody': 402,
  '/TD': 119, '/Sect': 38, '/enumerate': 35, '/TR': 32, '/Link': 31,
  '/section': 12, '/subsection': 12, '/subsubsection': 14, '/itemize': 8,
  '/Table': 4, '/Document': 1
})
```

The tags to specifically look for:

| Tag(s)                              | Confirms                                    |
|--------------------------------------|----------------------------------------------|
| `/Sect`, `/section`, `/subsection`   | Section headings are tagged as headings, not just large bold text |
| `/Table`, `/TR`, `/TD`               | Tables are tagged as real tables, not a jumble of text |
| `/LI`, `/Lbl`, `/LBody`, `/itemize`, `/enumerate` | Bulleted/numbered lists are tagged as lists |
| `/Link`, `/GoTo`                     | Hyperlinks are tagged and navigable          |

If any of these are missing (e.g., zero `/Table` tags despite having tables
in the document), the corresponding content type is **not** actually
accessible yet, even though the PDF opens fine and `Tagged: yes` is reported
at the whole-document level. `Tagged: yes` only means *some* tag structure
exists — it does not certify that every content type in the document is
properly tagged.

### 2.7 A specific, real trap: custom heading styling can silently disable heading tagging

If your document customizes section heading appearance (color, small caps,
a decorative rule under the heading, etc.) using the popular **`titlesec`**
package, be aware: **`titlesec` is fundamentally incompatible with the
kernel's experimental section-tagging patch.** It completely replaces the
internal `\@startsection`/`\@sect` machinery that the tagging patch depends
on, so section headings will silently stop being tagged — with no error, no
warning, just missing `/Sect` tags in the structure tree.

The fix used in this project: remove `titlesec` and reimplement the same
visual styling using the kernel's own `\@startsection` primitive directly.
For example, to reproduce "large, small-caps, colored section headings with
a horizontal rule underneath":

```latex
\usepackage{xcolor}
\definecolor{accent}{RGB}{27,54,93}

\makeatletter
\renewcommand\section{\@startsection{section}{1}{0pt}%
  {1.4em}%                                        % space before
  {0.6em}%                                         % space after (see warning below)
  {\normalfont\Large\scshape\color{accent}}}       % style of the heading text
\makeatother

% A separate command to draw the rule, called manually after each \section:
\newcommand{\sectionrule}{\par\vspace{-0.3em}\noindent\rule{\linewidth}{0.8pt}\vspace{0.3em}\par}
```

Then in the body of the document:

```latex
\section{Education}
\sectionrule
... table or content here ...
```

**Critical gotcha discovered the hard way**: the fifth argument to
`\@startsection` (the "space after" value) must be **positive**. A negative
value is LaTeX's built-in signal for a "run-in" heading — meaning the
paragraph immediately following the heading is typeset as a continuation of
the *same line* as the heading, rather than starting fresh below it. This
caused an entire table to be silently swallowed into the same horizontal
line as a section heading, pushing it hundreds of points off the right edge
of the page, so it visually disappeared from the rendered PDF with **zero
LaTeX errors** — only an easy-to-miss "Overfull \hbox (461pt too wide)"
warning buried in the build log. Always use a positive value here unless you
specifically want run-in-style headings.

Similarly, any custom command that inserts decorative material right after a
heading (like the `\sectionrule` rule-drawing command above) must force
itself onto its own paragraph with `\par` on both sides. If it doesn't, the
very next thing in the document (a table, a paragraph, anything) can get
merged onto the same line as the decoration, with the same silent
off-page-content failure mode described above.

**Lesson for any custom preamble**: after enabling tagging, always visually
render every page of the resulting PDF (not just check for "zero errors")
and compare it side-by-side against the previous, non-tagged version, page
by page. A silent content-disappearance bug like this will not show up in
the compiler's error output — only in the rendered pages themselves.

### 2.8 Known limitation: the experimental table module can behave unpredictably

The `table,tabular` testphase modules are explicitly experimental. In this
project, they were retested after fixing the run-in-heading bug above and
worked correctly, producing valid `/Table`/`/TR`/`/TD` tags with no visible
regressions — but this should not be assumed to work flawlessly for every
possible table layout. After enabling it, always:

1. Rebuild with the full multi-pass sequence (Section 2.3).
2. Check the LaTeX build log for new or unusually large "Overfull \hbox"
   warnings (anything reporting more than roughly 50pt of overfull content is
   worth investigating — it often means content is being pushed off the
   page).
3. Visually render and inspect every page (see Section 4 below), not just
   the ones you assume are affected.
4. Confirm `/Table`, `/TR`, `/TD` counts in the structure tree roughly match
   the number of actual tables and rows in your document.

If the table module causes problems in your specific document that you
cannot resolve, it is safe to drop `table,tabular` from the `testphase` list
and keep just `tagpdf,phase-III` — you will still get properly tagged
section headings, subsections, and lists, which is a substantial
accessibility improvement even without table tagging. A partially-tagged,
visually-correct PDF is always better than a fully-tagged PDF with missing
content.

---

## 3. If you are not using LaTeX (or have no AI assistant to help)

Everything above assumes you are comfortable editing LaTeX source and
running commands in a terminal. If that's not your situation — for example,
you're working entirely in Microsoft Word, or you only have access to a
plain PDF someone else gave you — here are the realistic paths, roughly
ordered from best to most limited.

### 3.1 Best option: Microsoft Word's built-in accessibility tools

If you have the original document as a Word (`.docx`) file, or can recreate
it in Word:

1. **Set the document title**: File → Info → and fill in the "Title" field
   under Properties (not just the filename).
2. **Set the document language**: select all text (Ctrl/Cmd+A) → Review tab
   → Language → Set Proofing Language → choose the correct language, click
   "Set As Default" if asked.
3. **Use real heading styles, not manual bold/large text**: for every
   section title, apply Word's built-in "Heading 1," "Heading 2," etc.
   styles from the Home tab's Styles gallery — do not just make text bold
   and bigger by hand. Screen readers only recognize headings tagged this
   way.
4. **Add alt text to every image**: right-click the image → "Edit Alt Text"
   (or View → Alt Text) → write a plain-language description of what the
   image shows or means (e.g., "Signature of Jane Q. Public," not "image1.png").
5. **Mark table header rows**: click into the table → Table Design tab →
   check "Header Row." This ensures the first row is announced as column
   headers when a screen reader reads down a column, rather than being read
   as an ordinary row of cells.
6. **Run the built-in Accessibility Checker**: Review tab → Check
   Accessibility. Fix every item it flags — it will catch missing alt text,
   missing header rows, and other structural issues you may have missed.
7. **Export as a tagged PDF**: File → Save As → choose PDF → click
   "Options" → make sure the checkbox "Document structure tags for
   accessibility" is checked before saving. This is the step people most
   often skip; without it, Word will produce an ordinary untagged PDF even
   if everything inside the Word document itself was done correctly.

### 3.2 If you already have an untagged PDF and no source file: Adobe Acrobat Pro

Adobe Acrobat **Reader** (the free version) cannot add tags. You need
**Acrobat Pro** (a paid product; check whether your employer/institution has
a license before purchasing one yourself).

1. Open the PDF in Acrobat Pro.
2. Go to Tools → Accessibility → "Autotag Document" (or "Make Accessible,"
   depending on your Acrobat version) — this runs an automated first pass
   that adds a baseline tag structure.
3. Open the "Accessibility Checker" (Tools → Accessibility → Accessibility
   Check) and work through every flagged issue one at a time — this
   typically includes: setting the document title, setting the language,
   adding alt text to images (Acrobat will prompt you image-by-image),
   confirming table headers are marked, and confirming heading levels are
   correctly nested (no skipping, e.g., an `H1` followed directly by an
   `H3` with no `H2`).
4. Use the "Tags" panel (View → Show/Hide → Navigation Panes → Tags) to
   manually inspect and, if necessary, drag-and-drop reorder or retype
   individual tags — the automated pass frequently mis-tags complex tables
   or misses reading-order issues in multi-column layouts, and these must be
   fixed by hand.
5. Re-run the Accessibility Checker until it reports no remaining issues,
   then save.

### 3.3 If you have neither Acrobat Pro nor Word: what you can still do

- If you can get the document into **any** modern word processor (Google
  Docs, LibreOffice Writer, Apple Pages), the same principles from Section
  3.1 apply: use real heading styles, add alt text, mark table headers, set
  the title in the document properties, and export/print to PDF using an
  export option that explicitly mentions "tagged PDF" or "accessible PDF" if
  one is offered. Not all of these tools support tagged PDF export equally
  well — test the result with `pdfinfo` (`Tagged: yes`/`no`) or by opening it
  in a screen reader if you have access to one (VoiceOver on macOS,
  ctrl+cmd+F5, is a candidate for spot-checking).
- If none of the above is available to you, and you must ship a completely
  plain, untagged PDF, at minimum still add basic document metadata (title,
  author, language) through whatever export dialog you have — this does not
  make the PDF accessible, but it is better than nothing, and it is
  typically the one accessibility improvement available in even the most
  limited export tools.
- As a last resort for a document you cannot edit at all, a validator tool
  like **veraPDF** (free, open source, https://verapdf.org/) can at least
  tell you precisely which PDF/UA accessibility rules the document fails, if
  you need to document/report the gap to someone else who can fix it — but
  veraPDF only validates, it does not repair anything.

---

## 4. Final checklist (applies whichever method you used)

Before considering a PDF "accessible" and calling the work done, confirm
all of the following:

- [ ] `pdfinfo yourfile.pdf` reports `Tagged: yes`
- [ ] The document has a meaningful `Title` (not the filename) — check with
      `pdfinfo yourfile.pdf | grep -i title`
- [ ] The `Lang` is set correctly — check with `pdfinfo yourfile.pdf | grep -i lang`,
      or with the `pikepdf` script in Section 2.4 for the `DisplayDocTitle`
      viewer-preference flag specifically
- [ ] Every meaningful image has real, descriptive alt text (not the
      filename, not "image")
- [ ] Every section/subsection heading is tagged as a heading (verify with
      the `pikepdf` structure-tree script in Section 2.6 — look for
      `/Sect`, `/H1`-equivalent, or the heading-command-named tags)
- [ ] Every table is tagged as a real table (`/Table`, `/TR`, `/TD` present),
      not just visually laid out to look like one
- [ ] Every bulleted or numbered list is tagged as a list (`/LI`, `/Lbl`,
      `/itemize` or `/enumerate` present)
- [ ] You have visually re-rendered and compared every page of the final
      PDF against the pre-tagging version, to catch any silent
      content-loss regressions introduced while adding tags
- [ ] (If applicable) You ran the tool's built-in accessibility checker
      (Word's Accessibility Checker, Acrobat Pro's Accessibility Check, or
      veraPDF) and resolved every item it reported
- [ ] You ran an independent, dedicated PDF/UA compliance checker (see
      Section 5) against the final PDF — not just the export tool's own
      built-in checker — and resolved or documented every finding

---

## 5. Run an independent compliance checker before shipping

Whatever tool produced your tags — LuaLaTeX, Word, or Acrobat — its own
"zero errors" report only means *that tool* didn't notice a problem. It is
not a substitute for running the final PDF through a dedicated, independent
PDF/UA and WCAG conformance checker before you consider the document done or
send it out for official review. Several such tools exist, ranging from free
and open source to full commercial remediation suites:

**Free / open source**

- **veraPDF** (https://verapdf.org/) — the free, open-source, industry
  reference validator for PDF/UA and PDF/A conformance, developed for
  European and US national libraries/archives. Command-line and GUI. This
  is the tool already referenced elsewhere in this guide, and a reasonable
  default first check.
- **PAC (PDF Accessibility Checker)** (https://pac.pdf-accessibility.org/) —
  free, Windows-only, produced by the PDF Association/access4all. Widely
  used in government and publishing accessibility workflows; gives a
  detailed, human-readable PDF/UA-matterhorn-protocol report and can
  preview the reading order and tag tree visually.
- **PAVE (PDF Accessibility Validation Engine)**
  (https://pave-pdf.org/) — free, browser-based, from the DIAGRAM Center.
  Useful when you don't want to install anything, and can also do light
  in-browser remediation (adding alt text, fixing reading order) if the
  checker finds problems.
- **Microsoft Word's built-in Accessibility Checker** (free with Office,
  `Review > Check Accessibility`) — not a substitute for a real PDF/UA
  checker, but worth running on the source document *before* exporting to
  PDF, since it catches missing alt text, heading structure, and reading
  order problems earlier and more cheaply than a post-export PDF check.

**Commercial**

- **Adobe Acrobat Pro's Accessibility Checker** (`Full Check`, included
  with an Acrobat Pro subscription) — the most common commercial option
  since it's paired directly with Acrobat's remediation tools (tag tree
  editor, reading order tool, alt-text panel) for fixing whatever it finds.
- **CommonLook PDF Validator / CommonLook Office**
  (https://commonlook.com/) — commercial, widely used in enterprise and
  government document-remediation pipelines; validates against PDF/UA,
  WCAG, and Section 508, and integrates with a bulk remediation workflow
  for organizations processing many documents.
- **axesPDF for Validating / axesPDF QuickFix**
  (https://www.axes4.com/) — commercial German accessibility-tools suite;
  the validator checks PDF/UA conformance, and QuickFix pairs with it to
  batch-repair common issues.
- **Foxit PDF Editor's Accessibility Checker** — commercial, bundled with
  Foxit's PDF editing suite if you're already using Foxit rather than
  Acrobat.

At minimum, run veraPDF or PAC against the final PDF — both are free — and
resolve or explicitly document (with a stated reason) every failure before
distributing the document or reporting it as accessible.
