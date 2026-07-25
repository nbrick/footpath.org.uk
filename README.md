# footpath.org.uk

A signpost, not a form. It routes a person who's found a blocked public right of
way straight to the correct highway authority's own reporting page. There's no
form, no account and no database here — the report goes to the council, not
through this site.

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

## Current state

The repo is public and the site is live at
`https://nbrick.github.io/footpath.org.uk/`, served by GitHub Pages from `main`
at the repo root.

`index.html` carries `<meta name="robots" content="noindex, nofollow">`, so it
stays out of search results while coverage is still being filled in. There is
deliberately no `CNAME` and no custom domain yet — see the launch steps below.

Every link on the site was opened and confirmed by hand before it went up. A
wrong link is worse than no link, because it sends someone reporting a real
obstruction to the wrong place. Rows nobody has checked say so plainly rather
than guessing.

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

## Still to do

- **A contact address on the project domain.** The footer currently sends people
  to GitHub issues, which needs an account most visitors won't have — walkers,
  not developers. `hello@footpath.org.uk` (or similar) as the primary route, with
  GitHub kept as a secondary. Deliberately deferred until the domain and DNS
  exist at launch, so the alias can live on the project domain and be re-pointed
  if it attracts spam.
- **Link coverage.** 120 of 175 authorities still unchecked.
- **Inner London.** Twelve boroughs are flagged as having no definitive map. If
  that's right, "Not checked yet" misrepresents them and they need their own row
  state; the claim needs confirming first.
- **Google Fonts.** The page pulls Bricolage Grotesque from
  `fonts.googleapis.com`, so every visitor's browser contacts Google before the
  page renders. Worth self-hosting the font or dropping it, both to remove the
  third-party request and to stop the page depending on someone else's CDN.

## Credit

A complement to the Ramblers (https://www.ramblers.org.uk/report-it), who do the
long-term work of campaigning for paths and recording lost ones. This site just
does the narrow job of fast routing.
