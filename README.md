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

That rebuilds the whole page — moving the row from "Not checked yet" to a
working link and updating the counts. Verify every URL by actually opening the
authority's page first; a wrong link is worse than none.

## Still to do

- **Link coverage.** 107 of 175 authorities still unchecked. Some councils block
  automated fetching with a 403, so those need opening in a browser by hand.
- **Inner London — decided: treat as ordinary rows.** The source list flags twelve
  boroughs as having no definitive map, but that doesn't survive checking.
  Wildlife and Countryside Act 1981 s.66 defines "surveying authority" to include
  London borough councils with no inner-London exclusion, and the s.53 duty to
  keep a definitive map under continuous review has no London carve-out. What is
  true is narrower: Highways Act 1980 s.130A excludes inner London authorities
  from the obstruction-notice procedure. So whether a given borough has recorded
  paths is a question of fact per borough, not a legal blanket, and each gets
  checked like anywhere else. A distinct row state is still the right answer for
  an authority with genuinely no recorded network — but only once that is
  verified, not on the source list's say-so.
- **The denominator.** Some authorities may never have a reporting link, so
  "n of 175" measures against a target that cannot be reached. Decision for now
  is to leave it at 175 rather than adjust it on an assumption. Worth revisiting
  at launch, where the count probably doesn't need the prominence it currently
  has.
- **A contact address on the project domain.** The footer currently sends people
  to GitHub issues, which needs an account most visitors won't have — walkers,
  not developers. `hello@footpath.org.uk` (or similar) as the primary route, with
  GitHub kept as a secondary. Deliberately deferred until the domain and DNS
  exist at launch, so the alias can live on the project domain and be re-pointed
  if it attracts spam.
- **Google Fonts.** The page pulls Bricolage Grotesque from
  `fonts.googleapis.com`, so every visitor's browser contacts Google before the
  page renders. Worth self-hosting the font or dropping it, both to remove the
  third-party request and to stop the page depending on someone else's CDN.

## Ideas worth building

Roughly in order of value per hour of work.

- **What to do when nothing happens.** The site currently stops at "here is the
  form", and that is where people give up. Two levers are worth stating plainly,
  both verified against legislation.gov.uk:
  - **Highways Act 1980 s.130A** — any person may serve notice on the highway
    authority requiring it to secure removal of an obstruction, and the authority
    must respond within **one month**. Hardly anyone knows this exists. It turns
    an ignored report into a formal clock.
  - **Highways Act 1980 s.134** — where a path is ploughed, the occupier must
    reinstate it within **14 days** of first disturbance for sowing, or **24
    hours** otherwise (extendable by the authority up to 28 days). Failure is an
    offence carrying a level 3 fine. Ploughing is the commonest rural obstruction
    and most walkers assume nothing can be done about it.
- **Place, not council.** The list asks which authority you want; the user knows
  where they were walking. In two-tier areas that mismatch is exactly where
  reports go astray — someone in the Peak District near Sheffield needs
  Derbyshire and will type "Sheffield". A bundled place-name or postcode-district
  to authority lookup (ONS publish the data) would turn the question into "where
  were you?". Biggest improvement to the core job, and the most work.
- **Publish the links as data.** The scarce asset is not the page, it is the
  hand-verified links — nobody else has these, because everyone else
  pattern-matches council URLs. Emitting `authorities.json` from the same build
  costs almost nothing and lets the Ramblers, OpenStreetMap or any walking app
  consume it.
- **Grid reference helper.** The hardest field on any council form is "exactly
  where". Browser geolocation converted to an OS grid reference in-page, with
  nothing transmitted anywhere.
- **Order the list by something more useful than the alphabet.** Sorting by
  length of rights-of-way network would put the authorities where blocked paths
  actually happen at the top — currently Barking and Dagenham leads and North
  Yorkshire, with the largest network in England outside the national parks, is
  buried. Two caveats. The figures need sourcing per authority (Rights of Way
  Improvement Plans and Defra survey data both carry them, so it is 175 more
  things to verify and get wrong). And alphabetical is what people expect from a
  list they might scan, so any other order probably has to be stated on the page
  rather than left to be inferred. A cheaper variant: keep the alphabet and show
  network length as row metadata instead.

### Deliberately not doing

Collecting, forwarding or tracking reports. The Ramblers tried it with Pathwatch
and retired it because authorities wouldn't accept third-party submissions — and
it would cost the one claim this site can make cleanly.

## Credit

A complement to the Ramblers (https://www.ramblers.org.uk/report-it), who do the
long-term work of campaigning for paths and recording lost ones. This site just
does the narrow job of fast routing.
