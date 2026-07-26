# footpath.org.uk

A signpost, not a form. It routes a person who's found a blocked public right of
way straight to the correct highway authority's own reporting page. There's no
form, no account and no database here — the report goes to the council, not
through this site.

Covers every highway authority in England and Wales. Scotland and Northern
Ireland have separate systems and aren't included.

## What's in here

- `index.html` — the whole site (one self-contained file)
- `robots.txt` — generated, and tied to the noindex flag (see below)
- `CNAME` — claims `footpath.org.uk` for GitHub Pages
- `build_page.py` — regenerates `index.html` and `robots.txt`; the single source
  of truth for the authority list, links, ordering and the noindex flag
- `README.md` — this file

`build_page.py` writes only `index.html` and `robots.txt`, so rebuilding never
touches `CNAME`.

## Current state

**Live at `https://footpath.org.uk`**, served by GitHub Pages from `main` at the
repo root. All four entry points — apex and `www`, over HTTP and HTTPS — end on
`https://footpath.org.uk/`, with Enforce HTTPS on.

DNS is on Cloudflare: four `A` records to GitHub's Pages IPs plus a `www` CNAME,
all **DNS only** rather than proxied, because proxying blocks GitHub from issuing
its TLS certificate. Cloudflare Email Routing forwards `wrong-link@` and
`wronglink@` to a real inbox; it was chosen over the registrar's own forwarding
because it applies Sender Rewriting, so forwarded mail still passes SPF instead
of landing in the destination's spam folder.

`index.html` still carries `<meta name="robots" content="noindex, nofollow">`.
The domain is claimed and the site is served from it, but it stays out of search
until that flag is deliberately turned off.

Every link on the site was opened and confirmed by hand before it went up. A
wrong link is worse than no link, because it sends someone reporting a real
obstruction to the wrong place. Rows nobody has checked say so plainly rather
than guessing.

Coverage is better than the row count suggests, because the list is worked in
order of how much path network each authority looks after: **123 of 175 rows,
but about 95% of the estimated network**. Wales is at 18 of 22.

## Ordering, and the network estimates

The list is sorted by `PROW_KM`, a rough estimate of each authority's
rights-of-way network in kilometres, largest first. Alphabetical put Barking and
Dagenham at the top and buried North Yorkshire; this puts the places people
actually walk first. The coverage note above the list says so, because a list of
place names in a non-obvious order needs to explain itself.

**Those numbers are estimates and are never displayed.** This is the one place
in the project where an unchecked figure is safe: being wrong changes a row's
position, not where a report goes. There is no authoritative per-authority
dataset — Ordnance Survey's FOI231141 gives national totals only and disclaims
being authoritative — so they were estimated, then sanity-checked against those
totals, landing within about 1% for England.

Individual figures can still be badly out. Warrington was estimated at 400km and
states 136 miles; Knowsley was estimated at 200km and states 53km. Both are
metropolitan boroughs, so that group probably runs high. Figures marked
`# stated` came from a council's own page — worth capturing whenever one is
spotted, since every link check is a chance to replace a guess.

`CHECKED` records the ISO date each link was last opened and confirmed. Absent
means no confirmed check. Nothing renders it yet; it exists so a recheck can run
oldest-first, and so the footer's hand-typed "links last checked" can eventually
be derived from data. Sort a recheck queue by date rather than by list position —
positions move whenever an estimate is corrected.

## National parks

In seven of the thirteen national parks the **park authority**, not the highway
authority, looks after the rights of way and takes the reports. In the other six
the councils keep it. There is no rule to infer — the function is delegated by
agreement, so each park had to be read individually, and assuming either way
would have been wrong about half the time.

| Park authority takes the report | Councils keep it |
| --- | --- |
| Bannau Brycheiniog, Dartmoor, Exmoor, Lake District, North York Moors, Yorkshire Dales, Pembrokeshire Coast | Eryri, South Downs, Peak District, New Forest, Northumberland, the Broads |

This is handled in two places, both generated from the same `NATIONAL_PARKS`
list in `build_page.py` so they cannot drift apart:

- **A search panel** appears when someone searches a park or a place inside one.
  Unlike the Scotland and Northern Ireland panels, these are *additive* —
  searching "Pembrokeshire" shows the council row and the park note together,
  because which one is needed depends on where the path is.
- **A note under the affected rows**, for anyone scrolling rather than searching.
  Only rows whose park takes the reports get one; where the councils keep the
  function the row was already right.

Adding a park means adding one entry to `NATIONAL_PARKS`. Set `authorities` to
an empty list where the councils keep the function, and omit `url` where the
answer is a row in the list rather than another website.

## Keeping it out of search

One flag controls both halves. `NOINDEX = True` in `build_page.py` puts
`<meta name="robots" content="noindex, nofollow">` in the page **and** makes
`robots.txt` say `Disallow: /`. `NOINDEX = False` removes the tag and opens
robots.txt in the same build.

They are tied together deliberately, because they are not independent.
`Disallow: /` stops a crawler fetching the page at all, so it never sees the
noindex tag either — turning off one without the other would look like launching
and change nothing. Worse, a disallowed URL can still be indexed bare from an
external link, with the meta tag unreadable, which is the exact outcome the flag
exists to prevent.

Note that `robots.txt` only became live when the site moved to its own domain.
On the old `nbrick.github.io/footpath.org.uk/` path, crawlers read
`nbrick.github.io/robots.txt` instead, so the file here did nothing.

Neither control stops a determined scraper; they only ask well-behaved crawlers
to stay away.

## Going live

Everything is done except the flag.

- ✅ `CNAME` at the repo root, and the custom domain set in Settings → Pages
- ✅ DNS on Cloudflare: four apex `A` records to `185.199.108.153`, `.109.153`,
  `.110.153`, `.111.153`, plus `www` as a CNAME to `nbrick.github.io`, all
  **DNS only** rather than proxied
- ✅ Certificate issued, Enforce HTTPS on, all four entry points converging
- ✅ `wrong-link@footpath.org.uk` forwarding and tested
- ⬜ **Set `NOINDEX = False` in `build_page.py`, rebuild, push.** That is launch.

Keep the Cloudflare records **DNS only**. Proxying blocks GitHub from issuing its
certificate, and Cloudflare's AI-crawler features can append directives to
`robots.txt` on proxied hostnames — which would silently override the flag above.

## Updating the authority links

Don't hand-edit `index.html`. Add the authority to the `DONE` dict in
`build_page.py` with its verified reporting URL, then:

    python3 build_page.py

That rebuilds the whole page — moving the row from "Not checked yet" to a
working link and updating the counts. Verify every URL by actually opening the
authority's page first; a wrong link is worse than none.

## Still to do

- **Link coverage.** 52 of 175 authorities still unchecked, together holding
  about 4% of the estimated network. The largest single gaps are West
  Northamptonshire and Bradford; Wales is four short of complete. Many councils
  block automated fetching with a 403, so those need opening in a browser.
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
- **A contact address — done, recorded here for the reasoning.**
  `wrong-link@footpath.org.uk` is live in the footer, with `wronglink@` as a
  second alias so a dropped hyphen doesn't bounce. Only the hyphenated form is
  published; it parses faster than the run-together version.

  **Named for its purpose, not generically, on purpose.** A `hello@` or
  `contact@` address will receive blocked-path reports, and the moment this site
  starts accepting those it has become Pathwatch — the model that failed because
  authorities won't act on third-party reports. `corrections@` was rejected as
  ambiguous: on a site about paths it could be read as corrections to the
  definitive map. Anything starting "report" was rejected outright, since that is
  the word someone with a blocked path is scanning for.

  The GitHub issues link stays alongside it as a secondary route — it also does
  the provenance work of showing the site is maintained in the open.

  The address alone isn't enough, so the footer also says plainly that a blocked
  path needs reporting to the authority and that a report sent here would go
  nowhere. An autoreply saying the same would catch the rest.
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
- **Replace the network estimates with stated figures.** The ordering works, but
  it rests on guesses that can be out by a factor of two or four. Every link
  check is a chance to capture a council's own figure; see the ordering section
  above.

### Deliberately not doing

Collecting, forwarding or tracking reports. The Ramblers tried it with Pathwatch
and retired it because authorities wouldn't accept third-party submissions — and
it would cost the one claim this site can make cleanly.

## Credit

A complement to the Ramblers (https://www.ramblers.org.uk/report-it), who do the
long-term work of campaigning for paths and recording lost ones. This site just
does the narrow job of fast routing.
