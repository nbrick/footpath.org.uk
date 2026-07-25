# -*- coding: utf-8 -*-
"""Regenerate footpath.org.uk index.html with the full set of England & Wales
highway authorities. Verified links are rendered as real anchors; everything
else gets a red 'Link needed' placeholder. Single source of truth lives here."""

from pathlib import Path

# Output lands next to this script, so the build works from any directory.
OUT_DIR = Path(__file__).resolve().parent

# --- Authorities we have a verified reporting link for -----------------------
DONE = {
    "Barnsley": "https://www.barnsley.gov.uk/services/parks-and-open-spaces/public-footpaths-and-rights-of-way/using-a-public-right-of-way/",
    "Bath and North East Somerset": "https://www.bathnes.gov.uk/report-problem-public-right-way",
    "Bedford": "https://www.bedford.gov.uk/parking-roads-and-travel/public-rights-way/public-rights-way-overview",
    "Bolton": "https://www.bolton.gov.uk/walking-cycling-rights-way/public-right-way",
    "Buckinghamshire": "https://www.buckinghamshire.gov.uk/environment/countryside-and-public-rights-of-way/public-rights-of-way/report-an-issue-with-a-public-footpath-bridleway-or-byway/",
    "Bury": "https://www.bury.gov.uk/index.aspx?articleid=11283",
    "Caerphilly": "https://eforms.caerphilly.gov.uk/forms/webCAHWPRW101.aspx",
    "Calderdale": "https://new.calderdale.gov.uk/streets-and-transport/public-rights-way",
    "Cambridgeshire": "https://www.cambridgeshire.gov.uk/residents/libraries-leisure-culture/countryside-access/rights-of-way",
    "Cardiff": "https://www.cardiffcouncilforms.co.uk/article/1699",
    "Ceredigion": "https://www.ceredigion.gov.uk/resident/coast-countryside/public-rights-of-way/path-management/",
    "Cheshire East": "https://www.cheshireeast.gov.uk/leisure,_culture_and_tourism/public_rights_of_way/contact_public_rights_of_way.aspx",
    "Cheshire West and Chester": "https://www.cheshirewestandchester.gov.uk/residents/transport-and-roads/public-rights-of-way",
    "Conwy": "https://www.conwy.gov.uk/en/Resident/Leisure-sport-and-health/Coast-and-Countryside/Public-Rights-of-Way.aspx",
    "Cornwall": "https://www.cornwall.gov.uk/environment/countryside/public-rights-of-way/",
    "County Durham": "https://www.durham.gov.uk/article/2751/Report-a-problem-with-a-Public-Right-of-Way",
    "Coventry": "https://www.coventry.gov.uk/rights-way/public-rights-way",
    "Cumberland": "https://www.cumberland.gov.uk/parks-culture-and-leisure/countryside-access",
    "Denbighshire": "https://www.denbighshire.gov.uk/en/parking-roads-and-travel/public-rights-of-way/about-public-rights-of-way.aspx",
    "Derbyshire": "https://www.derbyshire.gov.uk/leisure/countryside/access/rights-of-way/rights-of-way.aspx",
    "Devon": "https://www.devon.gov.uk/roads-and-transport/report-a-problem/report-a-problem-with-a-public-right-of-way/",
    "Dorset": "https://gi.dorsetcouncil.gov.uk/rightsofway/reportproblem",
    "Dudley": "https://www.dudley.gov.uk/residents/parking-and-roads/roads-highways-and-pavements/public-rights-of-way/",
    "East Riding of Yorkshire": "https://www.eastriding.gov.uk/leisure/countryside-and-walks/public-rights-of-way/maintenance-of-public-rights-of-way/",
    "East Sussex": "https://www.eastsussex.gov.uk/leisure-tourism/discover-east-sussex/rights-of-way/problems-on-rights-of-way/report",
    "Essex": "https://www.essexhighways.org/tell-us/public-rights-of-way-issues",
    "Gateshead": "https://www.gateshead.gov.uk/article/4471/Public-rights-of-way",
    "Gloucestershire": "https://www.gloucestershire.gov.uk/prow/report-a-problem/",
    "Gwynedd": "https://www.gwynedd.llyw.cymru/en/Residents/Parking-roads-and-travel/Public-Rights-of-Way/Public-Rights-of-Way.aspx",
    "Hampshire": "https://www.hants.gov.uk/landplanningandenvironment/rightsofway/reportaproblem",
    "Herefordshire": "https://my.herefordshire.gov.uk/service/Highways___Report_a_highways_issue",
    "Hertfordshire": "https://www.hertfordshire.gov.uk/services/highways-roads-and-pavements/report-a-problem/report-a-highway-fault/what-type-of-fault-are-you-reporting.aspx",
    "Hillingdon": "https://www.hillingdon.gov.uk/article/7576/Report-a-public-right-of-way-issue-including-bridleways-and-footpaths",
    "Isle of Anglesey": "https://www.anglesey.gov.wales/en/Residents/Parking-roads-and-travel/Public-rights-of-way/Path-maintenance-looking-after-Angleseys-paths.aspx",
    "Kent": "https://www.kent.gov.uk/environment-waste-and-planning/public-rights-of-way/report-a-problem-on-a-right-of-way",
    "Kirklees": "https://www.kirklees.gov.uk/beta/countryside-parks-and-open-spaces/public-rights-of-way.aspx",
    "Knowsley": "https://www.knowsley.gov.uk/streets-roads-and-transport/roads/public-rights-way",
    "Lancashire": "https://www.lancashire.gov.uk/roads-parking-and-travel/report-it/public-right-of-way/",
    "Leeds": "https://www.leeds.gov.uk/parks-and-countryside/public-rights-of-way/report-a-problem-with-a-public-right-of-way",
    "Leicestershire": "https://leicestershirecc-self.achieveservice.com/service/report-it",
    "Lincolnshire": "https://www.lincolnshire.gov.uk/coast-countryside/public-rights-way/3",
    "Liverpool": "https://liverpool.gov.uk/parking-roads-and-travel/public-rights-of-way/",
    "Merthyr Tydfil": "https://www.merthyr.gov.uk/do-it-online/report/rights-of-way/",
    "Milton Keynes": "https://www.milton-keynes.gov.uk/environment-parks-and-open-spaces/rights-way/public-rights-way",
    "Monmouthshire": "https://access.monmouthshire.gov.uk/standardmap.aspx",
    "Newcastle upon Tyne": "https://new.newcastle.gov.uk/travel/management/rightsofway/report",
    "Newport": "https://www.newport.gov.uk/our-city/see-and-do/green-spaces/public-rights-way",
    "Norfolk": "https://www.norfolk.gov.uk/roads-and-transport/roads/report-a-problem",
    "North Lincolnshire": "https://www.northlincs.gov.uk/planning-and-environment/access-to-the-countryside/",
    "North Northamptonshire": "https://www.northnorthants.gov.uk/rights-way-and-searches/report-public-right-way-issue",
    "North Somerset": "https://www.n-somerset.gov.uk/my-services/libraries-leisure-open-spaces/parks-countryside/public-rights-way/report-issue-public-right-way",
    "North Yorkshire": "https://www.northyorks.gov.uk/roads-parking-and-travel/public-rights-way/rights-way-maintenance",
    "Northumberland": "https://www.northumberland.gov.uk/about-council/digital-maps/public-rights-way-northumberland",
    "Nottinghamshire": "https://www.nottinghamshire.gov.uk/planning-and-environment/walking-cycling-and-rights-of-way/rights-of-way/report-problem",
    "Oldham": "https://www.oldham.gov.uk/info/201054/roads_streets_and_pavements/523/public_rights_of_way",
    "Oxfordshire": "https://www.oxfordshire.gov.uk/residents/environment-and-planning/countryside/countryside-access/public-rights-way/report-footpath-issue",
    "Peterborough": "https://www.peterborough.gov.uk/residents/transport-and-streets/public-rights-of-way",
    "Powys": "https://en.powys.gov.uk/article/2589/Report-a-concern-with-a-right-of-way",
    "Rhondda Cynon Taf": "https://www.rctcbc.gov.uk/EN/Resident/PlanningandBuildingControl/Countryside/PublicRightsofWay/ReportanissuewithaPublicRightofWay.aspx",
    "Rochdale": "https://www.rochdale.gov.uk/environment-pests/rights-way",
    "Rotherham": "https://www.rotherham.gov.uk/rights-way/public-rights-of-way",
    "Salford": "https://www.salford.gov.uk/parking-roads-and-travel/footpaths-and-pavements/public-rights-of-way/",
    "Sandwell": "https://www.sandwell.gov.uk/roads-travel-parking/public-rights-way-prow",
    "Sheffield": "https://www.sheffield.gov.uk/roads-pavements/prow",
    "Shropshire": "https://next.shropshire.gov.uk/outdoor-partnerships/report-a-rights-of-way-issue-and-feedback/",
    "Solihull": "https://solihullcouncil.custhelp.com/app/smbc/dio/report_it/forms/transport_highways/report_prow",
    "Somerset": "https://www.somerset.gov.uk/roads-travel-and-parking/report-a-problem-with-a-public-right-of-way/",
    "South Gloucestershire": "https://beta.southglos.gov.uk/public-rights-of-way/",
    "South Tyneside": "https://www.southtyneside.gov.uk/article/12906/Report-a-problem-with-a-path-public-right-of-way",
    "Staffordshire": "https://prow.staffordshire.gov.uk/standardmap.aspx",
    "Stockport": "https://www.stockport.gov.uk/topic/stockport-public-rights-of-way",
    "Suffolk": "https://www.suffolk.gov.uk/roads-and-transport/public-rights-of-way-in-suffolk/report-a-public-right-of-way-issue",
    "Surrey": "https://www.surreycc.gov.uk/culture-and-leisure/countryside/management/footpaths-byways-and-bridleways/report-a-problem",
    "Swansea": "https://www.swansea.gov.uk/contactcountrysideaccess?lang=en",
    "Tameside": "https://www.tameside.gov.uk/rightsofway",
    "Trafford": "https://www.trafford.gov.uk/streets-roads-and-transport/roads-highways-and-pavements/public-rights-way-prow/about-public-rights-way-prow",
    "Wakefield": "https://myaccount.wakefield.gov.uk/forms/footpaths-and-bridleways/",
    "Walsall": "https://go.walsall.gov.uk/roads-parking-and-travel/public-rights-of-way-prow",
    "Warwickshire": "https://rightsofway.warwickshire.gov.uk/",
    "West Sussex": "https://www.westsussex.gov.uk/land-waste-and-housing/public-paths-and-the-countryside/public-rights-of-way/report-a-problem-with-a-right-of-way/",
    "Westmorland and Furness": "https://www.westmorlandandfurness.gov.uk/parks-culture-and-leisure/countryside-access-and-rights-way",
    "Wigan": "https://www.wigan.gov.uk/Resident/Parking-Roads-Travel/Public-rights-of-way/Report-a-problem.aspx",
    "Wiltshire": "https://www.wiltshire.gov.uk/recreation-rights-of-way",
    "Wirral": "https://my.wirral.gov.uk/service/Public_Right_of_Way_problem",
    "Worcestershire": "https://capublic.worcestershire.gov.uk/PROWPublic/PROWFault.aspx",
    "York": "https://www.york.gov.uk/ReportPROWProblem",
}

# Short descriptor of where a verified link lands. Default = dedicated RoW form.
DESC = {
    "Barnsley": "Rights-of-way page — links to the report form",
    "Bedford": "Rights-of-way page — links to the report form",
    "Bolton": "Rights-of-way page — email and phone",
    "Bury": "Rights-of-way page — links to the report form",
    "Calderdale": "Rights-of-way page — general council contact only",
    "Cambridgeshire": "Rights-of-way page — links to the report form",
    "Ceredigion": "Email and phone — no online form",
    "Cheshire East": "Rights-of-way contact page — form, email or phone",
    "Cheshire West and Chester": "Rights-of-way page — links to the report form",
    "Conwy": "Rights-of-way page — links to the report form",
    "Cornwall": "Rights-of-way page — links to the report form",
    "Coventry": "Rights-of-way page — email and phone",
    "Cumberland": "Countryside access page — links to the report form",
    "Denbighshire": "Rights-of-way page",
    "Derbyshire": "Rights-of-way page — links to the report form",
    "Dudley": "Rights-of-way page — links to the report form",
    "East Riding of Yorkshire": "Rights-of-way page — phone and email",
    "Gateshead": "Rights-of-way page",
    "Gwynedd": "Rights-of-way page — links to the report form",
    "Herefordshire": "Highways report form",
    "Hertfordshire": "Highway fault form — choose “Public rights of way”",
    "Isle of Anglesey": "Path maintenance page — phone or general online form",
    "Kirklees": "Rights-of-way page — email and phone",
    "Knowsley": "Rights-of-way page — phone and email",
    "Lancashire": "Email report — no online form",
    "Leicestershire": "Council report-it portal — covers rights of way",
    "Liverpool": "Rights-of-way page — links to the contact form",
    "Milton Keynes": "Rights-of-way page — phone, no online form",
    "Monmouthshire": "Interactive rights-of-way map — sign-in needed to report",
    "Newport": "Rights-of-way page",
    "Norfolk": "Roads and transport report form",
    "North Lincolnshire": "Countryside access page — links to the report form",
    "North Yorkshire": "Rights-of-way page — links to the report form",
    "Northumberland": "Rights-of-way page — links to the report form",
    "Oldham": "Rights-of-way page — links to the report form",
    "Peterborough": "Rights-of-way page — email and phone",
    "Rochdale": "Rights-of-way page — email and phone",
    "Rotherham": "Rights-of-way page — links to the report form",
    "Salford": "Rights-of-way page — links to the report form",
    "Sandwell": "Rights-of-way page — email",
    "Sheffield": "Rights-of-way page — email or general enquiry form",
    "South Gloucestershire": "Rights-of-way page — email and phone",
    "Staffordshire": "Interactive rights-of-way map — sign-in needed to report",
    "Stockport": "Rights-of-way hub — links onward to report",
    "Swansea": "Email — no online form",
    "Tameside": "Rights-of-way page — links to the report form",
    "Trafford": "Rights-of-way page",
    "Walsall": "Rights-of-way page — email and phone",
    "Warwickshire": "Interactive rights-of-way map — report via “New issue”",
    "Westmorland and Furness": "Rights-of-way page — links to the report form",
    "Wiltshire": "Rights-of-way page — links to the report form",
    "Wirral": "Report form — account optional",
    "York": "Rights-of-way page — email and phone",
}
DEFAULT_DESC = "Rights-of-way report form"

# Extra filter keywords for authorities people search by another name.
ALIASES = {
    "Bath and North East Somerset": "banes",
    "Kingston upon Hull": "hull",
    "County Durham": "durham",
    "Isle of Anglesey": "anglesey ynys mon",
    "Rhondda Cynon Taf": "rct",
    "Bristol": "city of bristol",
    "Telford and Wrekin": "telford",
    "Windsor and Maidenhead": "royal borough windsor",
    "Kingston upon Thames": "royal kingston thames",
    "Kensington and Chelsea": "royal borough kensington",
}

# --- Wales: the 22 principal areas (all highway authorities) ------------------
WALES = [
    "Blaenau Gwent", "Bridgend", "Caerphilly", "Cardiff", "Carmarthenshire",
    "Ceredigion", "Conwy", "Denbighshire", "Flintshire", "Gwynedd",
    "Isle of Anglesey", "Merthyr Tydfil", "Monmouthshire", "Neath Port Talbot",
    "Newport", "Pembrokeshire", "Powys", "Rhondda Cynon Taf", "Swansea",
    "Torfaen", "Vale of Glamorgan", "Wrexham",
]

# --- England: county councils (two-tier), unitaries, met boroughs, London -----
ENGLAND = [
    # County councils (21)
    "Cambridgeshire", "Derbyshire", "Devon", "East Sussex", "Essex",
    "Gloucestershire", "Hampshire", "Hertfordshire", "Kent", "Lancashire",
    "Leicestershire", "Lincolnshire", "Norfolk", "Nottinghamshire", "Oxfordshire",
    "Staffordshire", "Suffolk", "Surrey", "Warwickshire", "West Sussex",
    "Worcestershire",
    # Non-metropolitan unitary authorities
    "Bath and North East Somerset", "Bedford", "Blackburn with Darwen",
    "Blackpool", "Bournemouth, Christchurch and Poole", "Bracknell Forest",
    "Brighton and Hove", "Bristol", "Buckinghamshire", "Central Bedfordshire",
    "Cheshire East", "Cheshire West and Chester", "Cornwall", "County Durham",
    "Cumberland", "Darlington", "Derby", "Dorset", "East Riding of Yorkshire",
    "Halton", "Hartlepool", "Herefordshire", "Isle of Wight", "Isles of Scilly",
    "Kingston upon Hull", "Leicester", "Luton", "Medway", "Middlesbrough",
    "Milton Keynes", "North East Lincolnshire", "North Lincolnshire",
    "North Northamptonshire", "North Somerset", "North Yorkshire",
    "Northumberland", "Nottingham", "Peterborough", "Plymouth", "Portsmouth",
    "Reading", "Redcar and Cleveland", "Rutland", "Shropshire", "Slough",
    "Somerset", "South Gloucestershire", "Southampton", "Southend-on-Sea",
    "Stockton-on-Tees", "Stoke-on-Trent", "Swindon", "Telford and Wrekin",
    "Thurrock", "Torbay", "Warrington", "West Berkshire", "West Northamptonshire",
    "Westmorland and Furness", "Wiltshire", "Windsor and Maidenhead", "Wokingham",
    "York",
    # Metropolitan boroughs (36)
    "Barnsley", "Birmingham", "Bolton", "Bradford", "Bury", "Calderdale",
    "Coventry", "Doncaster", "Dudley", "Gateshead", "Kirklees", "Knowsley",
    "Leeds", "Liverpool", "Manchester", "Newcastle upon Tyne", "North Tyneside",
    "Oldham", "Rochdale", "Rotherham", "Salford", "Sandwell", "Sefton",
    "Sheffield", "Solihull", "South Tyneside", "St Helens", "Stockport",
    "Sunderland", "Tameside", "Trafford", "Wakefield", "Walsall", "Wigan",
    "Wirral", "Wolverhampton",
    # London boroughs (32) + City of London
    "Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden",
    "City of London", "Croydon", "Ealing", "Enfield", "Greenwich", "Hackney",
    "Hammersmith and Fulham", "Haringey", "Harrow", "Havering", "Hillingdon",
    "Hounslow", "Islington", "Kensington and Chelsea", "Kingston upon Thames",
    "Lambeth", "Lewisham", "Merton", "Newham", "Redbridge",
    "Richmond upon Thames", "Southwark", "Sutton", "Tower Hamlets",
    "Waltham Forest", "Wandsworth", "Westminster",
]

# --- Out of scope: Scotland and Northern Ireland -----------------------------
# Deliberately NOT rows in the list. Both run on entirely different law, so
# listing them would imply a reporting route that this site hasn't checked and
# would distort the coverage count. But someone searching "Highland" or
# "Belfast" deserves an answer, not "no authority by that name".
SCOTLAND = [
    "Aberdeen City", "Aberdeenshire", "Angus", "Argyll and Bute",
    "City of Edinburgh", "Clackmannanshire", "Dumfries and Galloway",
    "Dundee City", "East Ayrshire", "East Dunbartonshire", "East Lothian",
    "East Renfrewshire", "Falkirk", "Fife", "Glasgow City", "Highland",
    "Inverclyde", "Midlothian", "Moray", "Na h-Eileanan Siar", "North Ayrshire",
    "North Lanarkshire", "Orkney Islands", "Perth and Kinross", "Renfrewshire",
    "Scottish Borders", "Shetland Islands", "South Ayrshire", "South Lanarkshire",
    "Stirling", "West Dunbartonshire", "West Lothian",
    # the two national park authorities are access authorities too
    "Cairngorms", "Loch Lomond and The Trossachs",
]
SCOTLAND_ALIASES = [
    "scotland", "scottish", "inverness", "perth", "skye", "western isles",
    "outer hebrides", "lewis", "harris", "mull", "arran", "ayr", "trossachs",
    "galloway", "lochaber", "hebrides", "ben nevis", "cairngorm",
]

NORTHERN_IRELAND = [
    "Antrim and Newtownabbey", "Ards and North Down",
    "Armagh City, Banbridge and Craigavon", "Belfast",
    "Causeway Coast and Glens", "Derry City and Strabane",
    "Fermanagh and Omagh", "Lisburn and Castlereagh", "Mid and East Antrim",
    "Mid Ulster", "Newry, Mourne and Down",
]
NORTHERN_IRELAND_ALIASES = [
    "northern ireland", "ulster", "londonderry", "ballymena", "bangor",
    "coleraine", "enniskillen", "tyrone", "mourne", "sperrins", "antrim coast",
]


def offscope_haystack(names, aliases):
    """Pipe-separated match strings for the out-of-scope search panels."""
    seen = [n.lower().replace(",", "") for n in names] + list(aliases)
    return "|".join(sorted(set(seen)))


# --- Assemble, de-dupe, tag nation, sort -------------------------------------
records = {}
for name in ENGLAND:
    records[name] = "England"
for name in WALES:
    records[name] = "Wales"

authorities = sorted(records.keys(), key=lambda s: s.lower())

total = len(authorities)
done_count = sum(1 for a in authorities if a in DONE)
todo_count = total - done_count

# --- Publishing flags --------------------------------------------------------
# Keep the preview out of search engines while it's a work in progress.
# Set to False before the real launch so the page can be indexed.
NOINDEX = True
noindex_tag = ('<meta name="robots" content="noindex, nofollow">\n'
               if NOINDEX else '')


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


scotland_hay = esc(offscope_haystack(SCOTLAND, SCOTLAND_ALIASES))
ni_hay = esc(offscope_haystack(NORTHERN_IRELAND, NORTHERN_IRELAND_ALIASES))


def haystack(name):
    base = name.lower().replace(",", "")
    if name in ALIASES:
        base += " " + ALIASES[name]
    return base


rows = []
for name in authorities:
    nation = records[name]
    hay = esc(haystack(name))
    disp = name.replace("&", "&amp;")
    if name in DONE:
        url = esc(DONE[name])
        desc = esc(DESC.get(name, DEFAULT_DESC))
        rows.append(
            f'''    <li class="done">
      <a class="row" href="{url}" target="_blank" rel="noopener noreferrer" data-name="{hay}">
        <span class="name">{disp}</span>
        <span class="meta"><span class="tag">{nation}</span> {desc}</span>
        <span class="go">Report a problem &rarr;</span>
      </a>
    </li>''')
    else:
        rows.append(
            f'''    <li class="todo">
      <div class="row row--todo" data-name="{hay}">
        <span class="name">{disp}</span>
        <span class="meta"><span class="tag">{nation}</span> we haven&rsquo;t checked this one yet</span>
        <span class="go go--todo" role="img" aria-label="Reporting link not checked yet">Not checked yet</span>
      </div>
    </li>''')

rows_html = "\n".join(rows)

HTML = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>footpath.org.uk &mdash; report a blocked public right of way</title>
<meta name="description" content="A blocked footpath, bridleway or byway is reported to the highway authority for the area the path runs through &mdash; usually a county or unitary council, and not necessarily the one where you live. Find the right one and go straight to its reporting page. Covers England and Wales.">
{noindex_tag}<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 22'%3E%3Crect width='22' height='22' rx='5' fill='%2320291F'/%3E%3Cpath d='M4 11h11M11 5l6 6-6 6' fill='none' stroke='%23E6AC24' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&display=swap" rel="stylesheet">
<style>
  :root {{
    --paper:      #ECEDE5;
    --paper-2:    #E3E4DA;
    --paper-up:   #F7F8F2;
    --ink:        #20291F;
    --ink-soft:   #545E4C;
    --hair:       #C7C8BA;
    --field:      #FFFFFF;
    --rowmaps:    #C42B6E;
    --rowmaps-dk: #96204F;
    --waymark:    #E6AC24;
    --focus:      #1B5E44;
  }}

  * {{ box-sizing: border-box; }}
  html {{ -webkit-text-size-adjust: 100%; }}

  body {{
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 17px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}

  .wrap {{ max-width: 720px; margin: 0 auto; padding: 0 22px; }}

  a {{ color: var(--rowmaps-dk); text-underline-offset: 2px; }}
  a:focus-visible, .row:focus-visible {{
    outline: 3px solid var(--focus);
    outline-offset: 2px;
    border-radius: 3px;
  }}

  .mast {{
    padding: 18px 0 6px; position: relative;
    display: flex; align-items: center; justify-content: space-between; gap: 14px;
  }}

  .about summary {{
    list-style: none; cursor: pointer;
    font-size: 0.85rem; color: var(--ink-soft);
    border-bottom: 1px dotted #A8AA9A; padding-bottom: 1px;
    white-space: nowrap;
  }}
  .about summary::-webkit-details-marker {{ display: none; }}
  .about summary:hover, .about[open] summary {{ color: var(--ink); border-bottom-color: var(--ink); }}
  .about summary:focus-visible {{ outline: 3px solid var(--focus); outline-offset: 3px; border-radius: 2px; }}
  .about-body {{
    position: absolute; right: 0; top: calc(100% + 6px); z-index: 20;
    width: min(42ch, calc(100vw - 44px));
    background: var(--paper-up); border: 1px solid var(--hair);
    border-radius: 10px; padding: 15px 17px;
    box-shadow: 0 10px 28px rgba(32,41,31,0.14);
    font-size: 0.88rem; color: var(--ink-soft);
  }}
  .about-body p {{ margin: 0 0 9px; }}
  .about-body p:last-child {{ margin-bottom: 0; }}
  .about-body b {{ color: var(--ink); font-weight: 600; }}
  .about-body a {{ color: var(--rowmaps-dk); font-weight: 600; }}
  .brand {{
    display: inline-flex; align-items: center; gap: 9px;
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-weight: 700; font-size: 1.06rem; letter-spacing: -0.01em;
    color: var(--ink); text-decoration: none;
  }}
  .brand svg {{ display: block; }}

  .hero {{ padding: 12px 0 2px; }}
  .hero h1 {{
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-weight: 700;
    font-size: clamp(1.9rem, 6.8vw, 2.7rem);
    line-height: 1.05;
    letter-spacing: -0.025em;
    margin: 0 0 10px;
    max-width: 20ch;
  }}
  .hero p {{
    font-size: 1.06rem; color: var(--ink-soft); margin: 0; max-width: 48ch;
  }}
  .hero strong {{ color: var(--ink); font-weight: 600; }}

  .row-rule {{
    height: 0; border: 0;
    border-top: 3px dashed var(--rowmaps);
    opacity: 0.9;
    margin: 20px 0 16px;
  }}

  .list-head {{
    display: flex; align-items: baseline; justify-content: space-between;
    gap: 12px; flex-wrap: wrap; margin-bottom: 4px;
  }}
  .list-head h2 {{
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-weight: 600; font-size: 1.02rem; letter-spacing: 0.01em;
    text-transform: uppercase; margin: 0; color: var(--ink);
  }}
  .count {{ font-size: 0.85rem; color: var(--ink-soft); }}
  .count b {{ color: var(--ink); font-weight: 700; }}

  .coverage {{
    font-size: 0.83rem; color: var(--ink-soft); margin: 10px 0 0; max-width: 62ch;
  }}

  .controls {{ margin-bottom: 6px; }}
  .filter {{
    width: 100%; font: inherit; font-size: 1.02rem; padding: 13px 15px;
    background: var(--field); border: 1.5px solid #B4B6A6;
    border-radius: 8px; color: var(--ink);
    box-shadow: 0 1px 2px rgba(32,41,31,0.06);
    -webkit-appearance: none; appearance: none;
  }}
  /* drop WebKit's search furniture, but keep the clear button — it's useful here */
  .filter::-webkit-search-decoration,
  .filter::-webkit-search-results-button {{ -webkit-appearance: none; }}
  .filter::placeholder {{ color: var(--ink-soft); }}
  .filter:focus-visible {{ outline: 3px solid var(--focus); outline-offset: 1px; border-color: var(--focus); }}

  ul.authorities {{ list-style: none; margin: 6px 0 0; padding: 0; }}
  ul.authorities li {{ border-top: 1px solid var(--hair); }}
  ul.authorities li:last-child {{ border-bottom: 1px solid var(--hair); }}

  .row {{
    display: grid; grid-template-columns: 1fr auto; align-items: center;
    gap: 10px 16px; padding: 15px 4px 15px 2px;
    text-decoration: none; color: var(--ink);
  }}
  a.row:hover .name {{ text-decoration: underline; text-decoration-color: var(--rowmaps); text-decoration-thickness: 2px; }}
  a.row:hover .go {{ transform: translateX(3px); color: var(--rowmaps-dk); }}

  .name {{ font-weight: 600; font-size: 1.08rem; letter-spacing: -0.01em; }}
  .meta {{ grid-column: 1 / 2; font-size: 0.8rem; color: var(--ink-soft); margin-top: 2px; }}
  .tag {{
    display: inline-block; font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.03em; text-transform: uppercase; color: var(--ink-soft);
    border: 1px solid var(--hair); border-radius: 20px;
    padding: 1px 8px; margin-right: 6px; vertical-align: 1px;
  }}
  .go {{
    grid-column: 2 / 3; grid-row: 1 / 3;
    font-size: 0.92rem; font-weight: 600; color: var(--rowmaps);
    white-space: nowrap; transition: transform .15s ease, color .15s ease;
  }}

  /* not-yet-checked state: recede quietly, don't shout */
  li.todo .name {{ color: var(--ink-soft); font-weight: 500; }}
  .go--todo {{
    color: var(--ink-soft); background: transparent;
    font-size: 0.78rem; font-weight: 600; letter-spacing: 0.02em;
    border: 1px solid var(--hair); border-radius: 20px;
    padding: 3px 11px;
  }}

  .no-match {{ padding: 18px 2px; color: var(--ink-soft); display: none; }}

  /* shown when someone searches a Scottish or NI place: explain, don't dead-end */
  .offscope {{
    display: none;
    margin: 14px 0 0; background: var(--paper-2);
    border-left: 3px solid var(--waymark); border-radius: 0 8px 8px 0;
    padding: 16px 18px;
  }}
  .offscope h3 {{
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-size: 0.98rem; margin: 0 0 6px; font-weight: 600;
  }}
  .offscope p {{ margin: 0; font-size: 0.9rem; color: var(--ink-soft); }}
  .offscope a {{ color: var(--rowmaps-dk); font-weight: 600; }}
  .offscope b {{ color: var(--ink); font-weight: 600; }}

  .prep {{
    margin: 30px 0 0; background: var(--paper-2);
    border-left: 3px solid var(--waymark); border-radius: 0 8px 8px 0;
    padding: 16px 18px;
  }}
  .prep h3 {{
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-size: 0.98rem; margin: 0 0 6px; font-weight: 600;
  }}
  .prep p {{ margin: 0; font-size: 0.92rem; color: var(--ink-soft); }}
  .prep a {{ color: var(--rowmaps-dk); font-weight: 600; }}

  .law {{
    margin: 18px 0 0; background: var(--paper-2);
    border-left: 3px solid var(--rowmaps); border-radius: 0 8px 8px 0;
    padding: 16px 18px;
  }}
  .law h3 {{
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-size: 0.98rem; margin: 0 0 6px; font-weight: 600;
  }}
  .law p {{ margin: 0; font-size: 0.92rem; color: var(--ink-soft); }}
  .law a {{ color: var(--rowmaps-dk); font-weight: 600; }}

  .partner {{
    margin: 18px 0 0; background: var(--paper-2);
    border-left: 3px solid var(--focus); border-radius: 0 8px 8px 0;
    padding: 16px 18px;
  }}
  .partner h3 {{
    font-family: "Bricolage Grotesque", ui-sans-serif, sans-serif;
    font-size: 0.98rem; margin: 0 0 6px; font-weight: 600;
  }}
  .partner p {{ margin: 0; font-size: 0.92rem; color: var(--ink-soft); }}
  .partner a {{ color: var(--rowmaps-dk); font-weight: 600; }}

  footer {{
    margin: 40px 0 56px; border-top: 3px dashed var(--rowmaps);
    padding-top: 20px; font-size: 0.85rem; color: var(--ink-soft);
  }}
  footer p {{ margin: 0 0 10px; max-width: 60ch; }}
  .status {{ font-weight: 600; color: var(--ink); }}

  @media (max-width: 460px) {{
    .go {{ font-size: 0.86rem; }}
    body {{ font-size: 16px; }}
    .brand {{ font-size: 0.98rem; }}
    .about summary {{ font-size: 0.8rem; }}
  }}
  @media (prefers-reduced-motion: reduce) {{
    a.row:hover .go {{ transform: none; }}
    * {{ transition: none !important; }}
  }}
</style>
</head>
<body>
<div class="wrap">

  <header class="mast">
    <a class="brand" href="./">
      <svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true">
        <path d="M4 11 h11 M11 5 l6 6 l-6 6" fill="none" stroke="#E6AC24" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      footpath.org.uk
    </a>
    <details class="about" id="about">
      <summary>About this site</summary>
      <div class="about-body">
        <p><b>A shortcut, nothing more.</b> A blocked path is reported to the highway authority for the area it runs through, and working out which one that is tends to be the slowest part. This site does that bit and then gets out of the way.</p>
        <p><b>Every link is checked by hand.</b> Each one was opened and confirmed to be that authority&rsquo;s own reporting route before it went up. A wrong link is worse than none &mdash; it sends someone reporting a real obstruction to the wrong place &mdash; so rows nobody has checked yet say exactly that instead of guessing.</p>
        <p><b>Independent.</b> Not affiliated with any council, and built in the open on <a href="https://github.com/nbrick/footpath.org.uk" target="_blank" rel="noopener noreferrer">GitHub</a>.</p>
      </div>
    </details>
  </header>

  <section class="hero">
    <h1>Report a blocked public right of way</h1>
    <p>Footpaths, bridleways and byways are kept open by the <strong>highway authority</strong> for the area the path runs through &mdash; usually a county or unitary council.</p>
  </section>

  <hr class="row-rule">

  <div class="list-head">
    <h2>Find the authority</h2>
    <span class="count"><b>{done_count}</b> of {total} linked so far</span>
  </div>
  <div class="controls">
    <input id="filter" class="filter" type="search" name="authority" inputmode="search"
           aria-label="Search for a council or county"
           autocomplete="off" autocorrect="off" autocapitalize="none" spellcheck="false"
           enterkeyhint="search" placeholder="Start typing the council or county where the path is&hellip;">
  </div>

  <p class="coverage">Every highway authority in England and Wales, for paths already recorded on the definitive map. Scotland and Northern Ireland have separate systems and aren&rsquo;t covered. Rows marked &ldquo;Not checked yet&rdquo; are ones nobody has verified a reporting link for &mdash; every link here was opened and confirmed by hand before it went up.</p>

  <ul class="authorities" id="list">
{rows_html}
  </ul>
  <div class="offscope" id="offscope-scotland" data-names="{scotland_hay}">
    <h3>Scotland works differently</h3>
    <p>Not a gap in this list &mdash; a different system. The <a href="https://www.legislation.gov.uk/asp/2003/2/contents" target="_blank" rel="noopener noreferrer">Land Reform (Scotland) Act 2003</a> gives a right of responsible access to most land and water, rather than recording particular routes on a definitive map. Every Scottish council, plus the Cairngorms and Loch Lomond &amp; The Trossachs park authorities, is an <b>access authority</b> with a statutory duty to uphold that right, so an obstruction goes to that authority&rsquo;s access officer. NatureScot&rsquo;s <a href="https://www.nature.scot/enjoying-outdoors/your-access-rights" target="_blank" rel="noopener noreferrer">guide to your access rights</a> explains what the right covers.</p>
  </div>

  <div class="offscope" id="offscope-ni" data-names="{ni_hay}">
    <h3>Northern Ireland works differently</h3>
    <p>Not covered here. Public rights of way are the responsibility of the <b>11 district councils</b> under the <a href="https://www.legislation.gov.uk/nisi/1983/1895/contents" target="_blank" rel="noopener noreferrer">Access to the Countryside (Northern Ireland) Order 1983</a>, which requires them to protect and maintain routes and to keep maps of them. Far fewer paths are legally recorded than in Great Britain, so a path in regular use may have no recorded status at all. nidirect&rsquo;s guide to <a href="https://www.nidirect.gov.uk/articles/public-rights-way" target="_blank" rel="noopener noreferrer">public rights of way</a> is the clearest starting point; your district council&rsquo;s countryside access team is who to contact.</p>
  </div>

  <p class="no-match" id="noMatch">No authority by that name here. Check the spelling, or search that council&rsquo;s own website for &ldquo;report a problem with a public right of way&rdquo;.</p>

  <div class="prep">
    <h3>Worth having ready before you click through</h3>
    <p>A grid reference or <a href="https://what3words.com/" target="_blank" rel="noopener noreferrer">what3words</a> for the exact spot, the path number if you can find it (look it up on <a href="https://www.rowmaps.com/" target="_blank" rel="noopener noreferrer">rowmaps.com</a>), and a photo or two. It&rsquo;s what the authority needs to act on it.</p>
  </div>

  <div class="law">
    <h3>Why the authority has to listen</h3>
    <p>Acting on this isn&rsquo;t discretionary. Under <a href="https://www.legislation.gov.uk/ukpga/1980/66/section/130" target="_blank" rel="noopener noreferrer">section 130 of the Highways Act 1980</a> a highway authority has a duty to &ldquo;assert and protect the rights of the public to the use and enjoyment&rdquo; of its highways, and to prevent them being stopped up or obstructed. Wilfully obstructing free passage along one is an offence in its own right under <a href="https://www.legislation.gov.uk/ukpga/1980/66/section/137" target="_blank" rel="noopener noreferrer">section 137</a>. Which routes count is settled by the definitive map, kept under <a href="https://www.legislation.gov.uk/ukpga/1981/69/part/III" target="_blank" rel="noopener noreferrer">Part III of the Wildlife and Countryside Act 1981</a> &mdash; a path on that map stays a right of way whether or not anyone has walked it lately. GOV.UK has a <a href="https://www.gov.uk/right-of-way-open-access-land" target="_blank" rel="noopener noreferrer">plain-English overview</a>, though it covers England only.</p>
  </div>

  <div class="partner">
    <h3>A complement to the Ramblers, not a replacement</h3>
    <p>The Ramblers do the long-term work &mdash; campaigning to keep paths open and researching lost ones back onto the definitive map. Their <a href="https://www.ramblers.org.uk/report-it" target="_blank" rel="noopener noreferrer">report a path problem</a> guide is the fuller resource, covering escalation and how to record paths that were never mapped. This site does one narrow thing by comparison: get you from a blocked path to the right authority&rsquo;s form as quickly as possible.</p>
  </div>

  <footer>
    <p class="status">{done_count} of {total} authorities linked. The remaining {todo_count} are listed and marked &ldquo;Not checked yet&rdquo; &mdash; each one&rsquo;s reporting link goes up once it&rsquo;s been opened and confirmed.</p>
    <p>An independent project, not affiliated with any council. There&rsquo;s no form here and no account to make &mdash; every link goes to the authority&rsquo;s own website, so your report goes to them rather than through us.</p>
    <p>It&rsquo;s built in the open. The authority list, every verified link and the whole checking history are on <a href="https://github.com/nbrick/footpath.org.uk" target="_blank" rel="noopener noreferrer">GitHub</a>. Found a wrong or dead link? <a href="https://github.com/nbrick/footpath.org.uk/issues" target="_blank" rel="noopener noreferrer">Open an issue</a> &mdash; that&rsquo;s the one thing worth telling us about.</p>
    <p>Authority list reflects local-government structure as of July 2026; it will change as the 2027&ndash;2028 unitary reorganisations take effect. Links last checked July 2026.</p>
  </footer>

</div>

<script>
  (function () {{
    var input = document.getElementById('filter');
    var items = Array.prototype.slice.call(document.querySelectorAll('#list > li'));
    var noMatch = document.getElementById('noMatch');
    var offscope = Array.prototype.slice.call(document.querySelectorAll('.offscope'));

    function apply() {{
      var q = (input.value || '').trim().toLowerCase();
      var shown = 0;
      items.forEach(function (li) {{
        var row = li.querySelector('.row');
        var hay = row.getAttribute('data-name') || '';
        var show = q === '' || hay.indexOf(q) !== -1;
        li.style.display = show ? '' : 'none';
        if (show) shown++;
      }});

      // Scotland / Northern Ireland: answer the question rather than dead-end.
      // Only once nothing here matched, so searching "north" doesn't summon a
      // panel alongside a screen of English results. Three characters minimum.
      var offscopeHit = false;
      offscope.forEach(function (panel) {{
        var names = (panel.getAttribute('data-names') || '').split('|');
        var hit = shown === 0 && q.length >= 3 && names.some(function (n) {{
          return n.indexOf(q) !== -1;
        }});
        panel.style.display = hit ? 'block' : 'none';
        if (hit) offscopeHit = true;
      }});

      noMatch.style.display = (shown === 0 && !offscopeHit) ? 'block' : 'none';
    }}

    input.addEventListener('input', apply);
  }})();

  (function () {{
    var about = document.getElementById('about');
    if (!about) return;
    document.addEventListener('click', function (e) {{
      if (about.open && !about.contains(e.target)) about.open = false;
    }});
    document.addEventListener('keydown', function (e) {{
      if (e.key === 'Escape' && about.open) {{
        about.open = false;
        about.querySelector('summary').focus();
      }}
    }});
  }})();
</script>
</body>
</html>
'''

with open(OUT_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

# robots.txt — effective once the site is served from the domain root
# (footpath.org.uk/robots.txt). On the github.io/<repo>/ project path it is
# not read by crawlers; the noindex meta tag is what keeps the preview private.
ROBOTS = "User-agent: *\nDisallow: /\n"
with open(OUT_DIR / "robots.txt", "w", encoding="utf-8") as f:
    f.write(ROBOTS)

print(f"Total authorities: {total}")
print(f"Linked: {done_count}")
print(f"Needs link: {todo_count}")
