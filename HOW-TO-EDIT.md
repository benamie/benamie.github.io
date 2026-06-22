# How to edit and publish this website

This site is a **Jekyll** site that auto-deploys via **GitHub Pages**. After you push
changes, the live site at <https://benamie.github.io> updates in ~1–2 minutes.

---

## The basic workflow

After you edit and save a file, open Terminal and run:

```bash
cd /Users/elinor/GitHub/benamie.github.io
git add -A
git commit -m "Describe what you changed"
git push
```

That's it. Wait a minute or two, then refresh the live site.

---

## If you edited a PUBLICATION, regenerate first

Publications are built from a script, not edited by hand. **Before** committing, run:

```bash
python3 markdown_generator/gen_pubs.py
```

> ⚠️ This script **wipes and rewrites** everything in `_publications/`.
> So make paper changes in **`markdown_generator/gen_pubs.py`** (the source of truth).
> Hand-edits to files inside `_publications/` are erased the next time the script runs.

Note: the homepage shows each paper's **`citation`** text, so edit the citation line in
the script to change what appears (not just the `title`).

---

## Preview your changes before pushing (optional but recommended)

```bash
bundle exec jekyll serve --livereload
```

Then open <http://localhost:4000/>. Saving a file auto-rebuilds the preview.
Press **Ctrl + C** to stop the server.

- Only run **one** server at a time — a stuck one blocks port 4000.
- If the page won't load, stop everything with `pkill -f jekyll`, then start it again.

---

## Which file do I edit?

| To change…                                            | Edit this file                                   |
|-------------------------------------------------------|--------------------------------------------------|
| Homepage (About, News, Research, Teaching, Team)      | `_pages/about.md`                                |
| Teaching & Mentoring page                             | `_pages/teaching-and-mentoring.md`               |
| Publications (titles, authors, links, order, section) | `markdown_generator/gen_pubs.py` → then run it   |
| Top navigation menu                                   | `_data/navigation.yml`                           |
| Fonts / spacing / colors                              | `assets/css/main.scss`                           |
| Files for download (CV, syllabi, PDFs)                | drop into the `files/` folder                    |

---

## Editing in TextEdit? Two must-do settings

1. **Format → Make Plain Text** (otherwise it saves as RTF and the build breaks).
2. **TextEdit → Settings → uncheck "Smart quotes" and "Smart dashes."**
   Curly quotes break the Liquid `{% %}` code and the YAML at the top of pages.

(If you have VS Code, it's a safer editor for these files.)

---

## Handy git commands

| Command           | What it does                                         |
|-------------------|------------------------------------------------------|
| `git status`      | List which files you've changed                      |
| `git diff`        | Show the exact lines you changed                     |
| `git pull`        | Pull down changes (run this if a `push` is rejected) |
| `git log --oneline -5` | See the last 5 commits                          |

**If `git push` is rejected** (e.g., you also edited on github.com): run `git pull`,
then `git push` again.
