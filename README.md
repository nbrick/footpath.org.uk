# footpath.org.uk

A signpost, not a form. It routes a person who's found a blocked public right of
way straight to the correct highway authority's own reporting page. It collects
nothing and stores nothing.

Covers every highway authority in England and Wales. Scotland and Northern
Ireland have separate systems and aren't included.

## What's in here

- `index.html` — the whole site (one self-contained file)
- `robots.txt` — asks crawlers to stay away (see note below on when it applies)
- `build_page.py` — regenerates `index.html`; the single source of truth for the
  authority list, links, and the noindex flag
- `README.md` — this file

There is deliberately **no `CNAME` file** in this bundle, so the site stays on
the github.io URL and doesn't try to claim footpath.org.uk yet.

## Before you publish: two things to know

1. **Pages from a private repo needs a paid plan.** On a free personal account,
   GitHub Pages only works from a *public* repo. A private repo can publish Pages
   only on GitHub Pro/Team/Enterprise.
2. **The published site is public either way.** A private repo hides your source
   code, not the page — anyone with the URL can view a Pages site. Genuinely
   access-restricted Pages is Enterprise-only.

If you want it truly non-public while it's this incomplete, don't enable Pages at
all yet — just open `index.html` in a browser to preview locally. Zero exposure,
no plan needed.

## Publish to the github.io URL

With repo `nbrick/footpath.org.uk`, the site will live at
`https://nbrick.github.io/footpath.org.uk/`.

1. Upload `index.html`, `robots.txt`, `build_page.py`, `README.md` to the repo.
2. Settings -> Pages -> Source: Deploy from a branch, Branch: `main`,
   folder: `/ (root)` -> Save.
3. Do NOT set a Custom domain yet, and don't add a `CNAME` file.

(Private repo -> you'll need Pro or above for step 2. Otherwise set the repo to
Public.)

## Keeping it out of search for now

`index.html` carries a `<meta name="robots" content="noindex, nofollow">` tag.
That is the thing that actually keeps the preview out of Google.

`robots.txt` is included for later: crawlers read robots.txt only from a site's
host root. On `nbrick.github.io/footpath.org.uk/` that root is
`nbrick.github.io/robots.txt` — which this repo doesn't control — so the
robots.txt here has no effect on the github.io preview. It starts working once
the site is served from `footpath.org.uk/` at its own root.

Neither noindex nor robots.txt stops a determined scraper; they only ask
well-behaved crawlers to stay away.

## When you're ready for the real domain

1. In `build_page.py`, set `NOINDEX = False`, then run `python3 build_page.py`
   to drop the noindex tag so the site can be indexed.
2. Add a `CNAME` file at the repo root containing one line: `footpath.org.uk`.
3. Settings -> Pages -> Custom domain -> `footpath.org.uk` -> Save.
4. DNS at your provider — apex `@` as four A records: `185.199.108.153`,
   `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (optionally the
   AAAA IPv6 records too), and a CNAME for `www` -> `nbrick.github.io`.
5. Tick Enforce HTTPS once DNS has propagated.

## Updating the authority links

Don't hand-edit `index.html`. Add the authority to the `DONE` dict in
`build_page.py` with its verified reporting URL, then:

    python3 build_page.py

That rebuilds the whole page — moving the row from a red "Link needed" marker to
a working link and updating the counts. Verify every URL by actually opening the
authority's page first; a wrong link is worse than none.

## Credit

A complement to the Ramblers (https://www.ramblers.org.uk/report-it), who do the
long-term work of campaigning for paths and recording lost ones. This site just
does the narrow job of fast routing.
