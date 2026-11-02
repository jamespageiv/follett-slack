"""Builds the Northfield State Slack mock-up as a fully static HTML page (no scripts needed to view).
Edit the STORY DATA section, then run:  python3 build_mockup.py
"""
import html as H

# ============================ STORY DATA ============================
PEOPLE = {
    "emma":   dict(name="Emma M.",   initial="E", color="#7B4FC9", title="Junior · Economics"),
    "priya":  dict(name="Priya S.",  initial="P", color="#D93A3A", title="ECON 2010 Peer Tutor"),
    "marcus": dict(name="Marcus T.", initial="M", color="#2F6FDE", title="ECON 2010 Peer Tutor"),
    "elena":  dict(name="Elena",     initial="E", color="#2E9E5B", title="ECON 2010 classmate"),
    "becca":  dict(name="Becca",     initial="B", color="#1A9A9A", title="NF Ambassador"),
    "wolfie": dict(name="Wolfie",    initial="W", color="#C96442", title="Campus assistant", app=True),
    "jordan": dict(name="Jordan K.", initial="J", color="#8A6D3B", title="First-year"),
    "diego":  dict(name="Diego R.",  initial="D", color="#5A6B7B", title="Intramural soccer captain"),
}
EXTRAS = ["Aiden L.", "Sofia R.", "Noah P.", "Maya C.", "Liam B.", "Ava W.", "Ethan H.",
          "Zoe K.", "Lucas G.", "Chloe D.", "Owen F.", "Grace N.", "Ryan V.", "Isla T."]
GREYS = ["#6B7280", "#9A7B4F", "#4B7F8C", "#8C5A7A", "#5F7A4B", "#7A6A9C"]

# Message fields: who, time, text (HTML allowed), reactions [(emoji, count)], system=True for join notices,
# attach="folder" to show the pinned folder card, button="Apply" for the apply button, pinned_by="Name".
CHANNELS = {
    "general": dict(
        member_count=2140, members=["wolfie", "becca", "priya"], pinned=[],
        days=[("Monday, November 16th", [
            dict(who="wolfie", time="8:00 AM", text="Good morning, Wolfpack! Spring registration opens <b>Mon Nov 30</b>. Need help planning? Just ask me."),
        ])]),
    "econ-2010-study-group": dict(
        member_count=14, members=["priya", "marcus", "elena", "emma"], stack=["priya", "marcus", "elena"],
        pinned_bar="Learning Commons 214 booked Wed 9 AM",
        pinned=[
            dict(type="message", who="priya", text="Learning Commons 214 booked Wed 9 AM"),
            dict(type="folder", name="Chapter 7 notes",
                 files=["Ch7_Elasticity_Slides.pdf", "Ch7_Practice_Problems.pdf", "Ch7_Summary_Notes.docx"]),
        ],
        days=[("Tuesday, November 17th", [
            dict(who="priya", time="5:12 PM", text="Quiz night Thursday 7 PM, I'll bring snacks", reactions=[("🙌", 6)]),
            dict(who="marcus", time="5:20 PM", text="Who has the Ch. 7 notes?"),
            dict(who="emma", time="5:31 PM", text="joined #econ-2010-study-group.", system=True),
            dict(who="wolfie", time="5:31 PM", text="Welcome Emma! Chapter 7 notes are in the pinned folder.", attach="folder"),
        ])]),
    "first-year-wolves": dict(
        member_count=1312, members=["wolfie", "jordan", "emma"],
        pinned=[dict(type="message", who="wolfie", text="Campus map and move-in tips")],
        days=[
            ("Monday, August 24th", [
                dict(who="wolfie", time="9:00 AM", text="Welcome to the Wolfpack, first-years! 🐺 The campus map and move-in tips are pinned."),
            ]),
            ("Tuesday, November 17th", [
                dict(who="jordan", time="4:48 PM", text="Anyone want to walk to the first home game together?", reactions=[("🙋", 9)]),
                dict(who="emma", time="5:33 PM", text="joined #first-year-wolves.", system=True),
            ]),
        ]),
    "intramural-soccer": dict(
        member_count=86, members=["diego", "emma"], pinned=[],
        days=[("Tuesday, November 17th", [
            dict(who="diego", time="2:10 PM", text="Spring rosters open Monday. Practice is Tuesday at 7 PM on Field 3. ⚽", reactions=[("⚽", 12)]),
            dict(who="emma", time="5:33 PM", text="joined #intramural-soccer.", system=True),
        ])]),
    "nftridelta": dict(
        member_count=48, members=["priya", "elena"], pinned=[],
        days=[("Thursday, November 19th", [
            dict(who="priya", time="5:48 PM", text="Student section is open seating tomorrow for <b>Wolves vs. Lakeshore</b>. Gates open at 6."),
            dict(who="elena", time="5:52 PM", text="I'm in. Meet at Gate B at 6:15?", reactions=[("👍", 7), ("🐺", 3)]),
        ])]),
    "nf-ambassadors": dict(
        member_count=112, members=["becca", "wolfie"],
        pinned=[dict(type="message", who="wolfie", text="How the Ambassador program works")],
        days=[
            ("Monday, November 2nd", [
                dict(who="wolfie", time="10:00 AM", pinned_by="Becca", button="Apply",
                     text="<b>How the Ambassador program works</b><br>Earn Pack Points and potential income by sharing Wolfpack content with your network. Click Apply to get started."),
            ]),
            ("Saturday, November 21st", [
                dict(who="becca", time="9:40 AM", text="Posted my Wolfpack haul today. Spring applications are open.", reactions=[("🔥", 14), ("🐺", 6)]),
            ]),
        ]),
}
CHANNEL_ORDER = ["general", "econ-2010-study-group", "first-year-wolves", "intramural-soccer", "nftridelta", "nf-ambassadors"]
DEFAULT_CHANNEL = "econ-2010-study-group"
DMS = ["wolfie", "becca", "priya"]
WORKSPACE = "Northfield State"
# ====================================================================

SLACK_SVG = ('<svg viewBox="0 0 54 54" class="slogo"><path fill="#36C5F0" d="M19.7 0a5.4 5.4 0 0 0 0 10.8h5.4V5.4A5.4 5.4 0 0 0 19.7 0m0 14.4H5.4a5.4 5.4 0 0 0 0 10.8h14.3a5.4 5.4 0 0 0 0-10.8"/>'
             '<path fill="#2EB67D" d="M54 19.8a5.4 5.4 0 0 0-10.8 0v5.4h5.4a5.4 5.4 0 0 0 5.4-5.4m-14.4 0V5.4a5.4 5.4 0 0 0-10.8 0v14.4a5.4 5.4 0 0 0 10.8 0"/>'
             '<path fill="#ECB22E" d="M34.2 54a5.4 5.4 0 0 0 0-10.8h-5.4v5.4a5.4 5.4 0 0 0 5.4 5.4m0-14.4h14.4a5.4 5.4 0 0 0 0-10.8H34.2a5.4 5.4 0 0 0 0 10.8"/>'
             '<path fill="#E01E5A" d="M0 34.2a5.4 5.4 0 0 0 10.8 0v-5.4H5.4A5.4 5.4 0 0 0 0 34.2m14.4 0v14.4a5.4 5.4 0 0 0 10.8 0V34.2a5.4 5.4 0 0 0-10.8 0"/></svg>')


def cid(c): return "ch-" + c


def av(p, cls="av"):
    return f'<span class="{cls}" style="background:{p["color"]}">{p["initial"]}</span>'


def app_tag(p): return '<span class="apptag">APP</span>' if p.get("app") else ""


def sidebar(active):
    chans = "".join(
        f'<a href="#{cid(c)}" class="sb-item{" sb-active" if c == active else ""}"><span class="hash">#</span>{c}</a>'
        for c in CHANNEL_ORDER)
    dms = "".join(f'<div class="sb-item">{av(PEOPLE[k], "av-xs")}{PEOPLE[k]["name"]}{app_tag(PEOPLE[k])}</div>' for k in DMS)
    return f'''<aside class="sidebar">
  <div class="sb-head"><span class="ws-icon">N</span><span class="ws-name">{WORKSPACE}</span></div>
  <nav class="sb-nav">
    <div class="sb-sec">▾ Channels</div>{chans}
    <div class="sb-sec">▾ Direct messages</div>{dms}
    <div class="sb-sec">▾ Apps</div><div class="sb-item">{av(PEOPLE["wolfie"], "av-xs")}Wolfie</div>
  </nav></aside>'''


def message(c, m):
    p = PEOPLE[m["who"]]
    if m.get("system"):
        return f'<div class="msg">{av(p)}<div><span class="mname">{p["name"]}</span> <span class="mtime">{m["time"]}</span><div class="mtext muted">{H.escape(m["text"])}</div></div></div>'
    reacts = "".join(f'<span class="react">{e} <b>{n}</b></span>' for e, n in m.get("reactions", []))
    attach = ""
    folder = next((x for x in CHANNELS[c]["pinned"] if x["type"] == "folder"), None)
    if m.get("attach") == "folder" and folder:
        attach = (f'<a href="#{cid(c)}-pins" class="folder-card"><span class="folder-ic">📁</span>'
                  f'<span><b>{folder["name"]}</b><br><span class="muted small">{len(folder["files"])} files · Pinned in this channel</span></span></a>')
    btn = f'<div><a href="#{cid(c)}-apply" class="btn-go">{m["button"]}</a></div>' if m.get("button") else ""
    pin = f'<div class="muted tiny">📌 Pinned by {m["pinned_by"]}</div>' if m.get("pinned_by") else ""
    return (f'<div class="msg{" msg-pinned" if m.get("pinned_by") else ""}">{av(p)}<div class="mbody">{pin}'
            f'<div><span class="mname">{p["name"]}</span>{app_tag(p)} <span class="mtime">{m["time"]}</span></div>'
            f'<div class="mtext">{m["text"]}</div>{attach}{btn}<div>{reacts}</div></div></div>')


def pins_panel(c):
    ch = CHANNELS[c]
    if not ch["pinned"]:
        return '<div class="muted">No pinned items yet.</div>'
    out = []
    for p in ch["pinned"]:
        if p["type"] == "folder":
            files = "".join(f'<li>{"📄" if f.endswith(".pdf") else "📝"} <span class="link">{f}</span></li>' for f in p["files"])
            out.append(f'<div class="pin-card"><div class="row"><span class="folder-ic">📁</span><b>{p["name"]}</b></div><ul class="files">{files}</ul></div>')
        else:
            q = PEOPLE[p["who"]]
            out.append(f'<div class="pin-card row">{av(q)}<div><span class="mname">{q["name"]}</span>{app_tag(q)}<div class="mtext">{p["text"]}</div></div></div>')
    return "".join(out)


def members_modal(c):
    ch = CHANNELS[c]
    named = [PEOPLE[k] for k in ch["members"]]
    fill = max(min(ch["member_count"], 14) - len(named), 0)
    extras = [dict(name=n, initial=n[0], color=GREYS[i % len(GREYS)], title="Student") for i, n in enumerate(EXTRAS[:fill])]
    rows = "".join(f'<li class="row">{av(p, "av-sm")}<div><b>{p["name"]}</b>{app_tag(p)}<div class="muted small">{p["title"]}</div></div></li>' for p in named + extras)
    return (f'<div id="{cid(c)}-members" class="overlay"><div class="modal"><div class="modal-head"><b class="big">{ch["member_count"]:,} members in #{c}</b>'
            f'<a href="#{cid(c)}" class="close">×</a></div><ul class="mlist">{rows}</ul></div></div>')


def apply_modal(c):
    return f'''<div id="{cid(c)}-apply" class="overlay"><div class="modal wide">
  <div class="modal-head"><span class="row">{av(PEOPLE["wolfie"], "av-sm")}<b class="big">Apply: NF Ambassador</b></span><a href="#{cid(c)}" class="close">×</a></div>
  <div class="form">
    <label>Full name<input value="Emma M."></label>
    <label>Class year<select><option>First-year</option><option>Sophomore</option><option selected>Junior</option><option>Senior</option></select></label>
    <label>Social handle you'd share from<input placeholder="@emma.wolfpack"></label>
    <label>Why do you want to be an Ambassador?<textarea rows="3" placeholder="A sentence or two"></textarea></label>
    <div class="form-actions"><a href="#{cid(c)}" class="btn-ghost">Cancel</a><a href="#{cid(c)}-applied" class="btn-go">Submit</a></div>
  </div></div></div>
<div id="{cid(c)}-applied" class="overlay"><div class="modal wide center"><div class="huge">🐺</div><b class="big">Application received!</b>
  <div class="muted">Becca and the Ambassador team will follow up in #nf-ambassadors.</div><div><a href="#{cid(c)}" class="btn-go">Done</a></div></div></div>'''


def channel_view(c):
    ch = CHANNELS[c]
    stack_keys = ch.get("stack") or ch["members"][:3]
    stack = "".join(av(PEOPLE[k], "av-stack") for k in stack_keys)
    bar = ""
    if ch.get("pinned_bar"):
        bar = (f'<a href="#{cid(c)}-pins" class="pinbar">📌 <b>Pinned:</b>&nbsp;{ch["pinned_bar"]}'
               f'<span class="pinbar-more">{len(ch["pinned"])} pinned items</span></a>')
    days = "".join(
        f'<div class="daydiv"><span>{label}</span></div>' + "".join(message(c, m) for m in msgs)
        for label, msgs in ch["days"])
    pin_count = f" {len(ch['pinned'])}" if ch["pinned"] else ""
    extra_modal = apply_modal(c) if any(m.get("button") for _, ms in ch["days"] for m in ms) else ""
    return f'''<section id="{cid(c)}" class="view ws-view">
  <div class="topbar"><div class="search">🔍 Search {WORKSPACE}</div><span class="me" style="background:{PEOPLE["emma"]["color"]}">E</span></div>
  <div class="ws-body">{sidebar(c)}
  <main class="chan">
    <header class="chan-head"><div class="chan-title"><span class="muted">#</span>{c} <span class="muted small">⌄</span></div>
      <a href="#{cid(c)}-members" class="mem-btn"><span class="stack">{stack}</span><b>{ch["member_count"]:,}</b></a></header>
    <div class="tabs"><a href="#{cid(c)}" class="tab tab-msgs">Messages</a><a href="#{cid(c)}-pins" class="tab tab-pins">📌 Pins{pin_count}</a></div>
    {bar}
    <div class="msgs">{days}</div>
    <div id="{cid(c)}-pins" class="pins">{pins_panel(c)}</div>
    <div class="composer">Message #{c}</div>
  </main></div>
  {members_modal(c)}{extra_modal}
</section>'''


def cards_view():
    inv = "".join(av(PEOPLE[k], "av-stack big-stack") for k in ["priya", "marcus", "elena"]) + '<span class="av-stack big-stack plus">+11</span>'
    return f'''<section id="cards" class="view cards-view">
  <div class="cards-grid">
    <div><div class="cap">Tue Nov 17, 5:30 PM · Invite card</div>
      <div class="invite">
        <div class="invite-head">{SLACK_SVG}# {WORKSPACE} on Slack</div>
        <div class="invite-body">
          <div class="invite-title">econ-2010-study-group</div>
          <div class="muted">14 members · <b class="green">3 from your section</b></div>
          <div class="stack invite-stack">{inv}</div>
          <div>Priya, Marcus, Elena</div>
          <a href="#{cid("econ-2010-study-group")}" class="btn-join">Join</a>
        </div></div></div>
    <div><div class="cap">Channel links in the thread</div>
      <div class="bubble">In <a class="chanlink" href="#{cid("nftridelta")}">{SLACK_SVG}#NFTriDelta</a> (Slack), Priya, Elena and 5 others from your channels are discussing plans to sit in the open student section.</div>
      <div class="bubble">The Northfield State Ambassador program lets you earn Pack Points and potential income when you share Wolfpack content with your network. You can see it in action in <a class="chanlink" href="#{cid("nf-ambassadors")}">{SLACK_SVG}#nf-ambassadors</a> on Slack, and apply to get started.</div>
    </div>
  </div>
</section>'''


CSS = """
*{box-sizing:border-box}html,body{margin:0;height:100%}
body{font-family:Lato,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1D1C1D;background:#1a1d21;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.view{display:none;height:100vh}
.view:target,.view:has(:target){display:flex}
body:not(:has(:target)) #DEFAULT{display:flex}
.ws-view{flex-direction:column}
.topbar{height:40px;flex-shrink:0;background:#350D36;display:flex;align-items:center;justify-content:center;position:relative}
.search{width:100%;max-width:560px;background:rgba(255,255,255,.2);color:rgba(255,255,255,.85);border-radius:6px;padding:4px 12px;font-size:13px}
.me{position:absolute;right:16px;width:28px;height:28px;border-radius:6px;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.ws-body{display:flex;flex:1;min-height:0}
.sidebar{width:260px;flex-shrink:0;background:#3F0E40;color:#CFC3CF;font-size:15px;display:flex;flex-direction:column}
.sb-head{display:flex;align-items:center;gap:8px;padding:12px 16px;border-bottom:1px solid rgba(255,255,255,.1)}
.ws-icon{width:36px;height:36px;border-radius:8px;background:#C96442;color:#fff;font-weight:900;font-size:18px;display:flex;align-items:center;justify-content:center}
.ws-name{color:#fff;font-weight:800;font-size:17px}
.sb-nav{padding:10px 8px;overflow-y:auto}
.sb-sec{padding:6px 8px;margin-top:10px;font-size:14px}
.sb-item{display:flex;align-items:center;gap:8px;padding:4px 12px;border-radius:6px}
a.sb-item:hover{background:rgba(255,255,255,.1)}
.sb-active{background:#1164A3;color:#fff}.hash{opacity:.7}
.av,.av-xs,.av-sm,.av-stack{display:inline-flex;align-items:center;justify-content:center;color:#fff;font-weight:700;border-radius:8px;flex-shrink:0}
.av{width:36px;height:36px;font-size:15px}.av-sm{width:32px;height:32px;font-size:14px}
.av-xs{width:20px;height:20px;font-size:11px;border-radius:4px}
.av-stack{width:24px;height:24px;font-size:11px;border-radius:6px;box-shadow:0 0 0 2px #fff;margin-left:-6px}
.av-stack:first-child{margin-left:0}
.big-stack{width:36px;height:36px;font-size:15px;margin-left:-8px}.plus{background:#E8E8E8;color:#616061}
.apptag{display:inline-block;background:#E8E8E8;color:#616061;font-size:10px;font-weight:700;border-radius:3px;padding:0 4px;margin-left:6px;vertical-align:2px}
.sidebar .apptag{background:rgba(255,255,255,.15);color:#fff}
.chan{flex:1;min-width:0;display:flex;flex-direction:column;background:#fff}
.chan-head{display:flex;align-items:center;justify-content:space-between;padding:10px 20px;border-bottom:1px solid #E2E2E2}
.chan-title{font-size:18px;font-weight:800}
.mem-btn{display:flex;align-items:center;gap:6px;border:1px solid #E2E2E2;border-radius:6px;padding:3px 8px 3px 4px;color:#616061;font-size:14px}
.mem-btn:hover{background:#f8f8f8}.stack{display:inline-flex;align-items:center}
.tabs{display:flex;gap:20px;padding:0 20px;border-bottom:1px solid #E2E2E2;font-size:14px}
.tab{padding:8px 0;border-bottom:2px solid transparent;color:#616061}
.tab-msgs{border-color:#1D1C1D;color:#1D1C1D;font-weight:700}
.view:has(.pins:target) .tab-msgs{border-color:transparent;color:#616061;font-weight:400}
.view:has(.pins:target) .tab-pins{border-color:#1D1C1D;color:#1D1C1D;font-weight:700}
.pinbar{display:flex;align-items:center;gap:6px;background:#FEF9EC;border-bottom:1px solid #E2E2E2;padding:8px 20px;font-size:14px}
.pinbar-more{margin-left:auto;color:#1264A3;font-size:13px}
.msgs{flex:1;overflow-y:auto;padding:8px 0;display:flex;flex-direction:column;justify-content:flex-end}
.pins{display:none;flex:1;overflow-y:auto;padding:20px}
.pins:target{display:block}.view:has(.pins:target) .msgs{display:none}
.daydiv{position:relative;text-align:center;margin:14px 0 6px}
.daydiv:before{content:"";position:absolute;left:0;right:0;top:50%;border-top:1px solid #E2E2E2}
.daydiv span{position:relative;background:#fff;border:1px solid #E2E2E2;border-radius:999px;padding:2px 12px;font-size:13px;font-weight:700}
.msg{display:flex;gap:8px;padding:6px 20px}.msg:hover{background:#F8F8F8}
.msg-pinned,.msg-pinned:hover{background:#FEF9EC}
.mname{font-weight:800;font-size:15px}.mtime{font-size:12px;color:#616061;margin-left:4px}
.mtext{font-size:15px;line-height:1.45}.muted{color:#616061}.small{font-size:13px}.tiny{font-size:12px}
.react{display:inline-flex;gap:4px;align-items:center;margin:4px 4px 0 0;border:1px solid #1D9BD1;background:#E8F5FA;color:#1264A3;border-radius:999px;padding:1px 8px;font-size:13px}
.folder-card{display:flex;gap:12px;align-items:center;width:320px;border:1px solid #E2E2E2;border-radius:8px;padding:10px;margin-top:8px;font-size:15px}
.folder-card:hover{background:#F8F8F8}
.folder-ic{width:40px;height:40px;border-radius:6px;background:#FFF4D6;display:inline-flex;align-items:center;justify-content:center;font-size:20px}
.btn-go{display:inline-block;background:#007A5A;color:#fff;font-weight:700;font-size:14px;border-radius:6px;padding:6px 16px;margin-top:8px}
.btn-ghost{display:inline-block;border:1px solid #999;font-weight:700;font-size:14px;border-radius:6px;padding:6px 16px;margin-top:8px}
.composer{margin:0 20px 20px;border:1px solid #999;border-radius:8px;padding:10px 12px;color:#616061;font-size:15px}
.pin-card{border:1px solid #E2E2E2;border-radius:8px;padding:14px;margin-bottom:12px}
.row{display:flex;align-items:center;gap:10px}
.files{list-style:none;padding-left:50px;margin:10px 0 0;font-size:14px;line-height:1.9}.link{color:#1264A3}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);align-items:center;justify-content:center;z-index:10}
.overlay:target{display:flex}
.modal{background:#fff;border-radius:12px;padding:22px;width:400px;box-shadow:0 20px 50px rgba(0,0,0,.3)}
.modal.wide{width:460px}.modal.center{text-align:center;display:flex;flex-direction:column;gap:8px;align-items:center}
.modal-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.big{font-size:19px;font-weight:800}.huge{font-size:34px}.close{font-size:26px;color:#616061}
.mlist{list-style:none;padding:0;margin:0;max-height:380px;overflow-y:auto;display:flex;flex-direction:column;gap:10px;font-size:15px}
.form{display:flex;flex-direction:column;gap:14px;font-size:15px;font-weight:700}
.form input,.form select,.form textarea{display:block;width:100%;margin-top:4px;border:1px solid #999;border-radius:6px;padding:8px 10px;font:inherit;font-weight:400}
.form-actions{display:flex;justify-content:flex-end;gap:8px}
.cards-view{background:#F2F2F7;padding:40px;overflow:auto;height:auto;min-height:100vh}
.cards-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:40px;max-width:900px;margin:0 auto;width:100%}
.cap{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:#616061;margin-bottom:12px}
.invite{width:320px;background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.12)}
.invite-head{display:flex;align-items:center;gap:6px;border-bottom:1px solid #E2E2E2;padding:10px 16px;font-size:13px;font-weight:700;color:#616061}
.invite-body{padding:16px;display:flex;flex-direction:column;gap:8px;font-size:14px}
.invite-title{font-size:18px;font-weight:800}.green{color:#007A5A}.invite-stack{margin:4px 0}
.btn-join{display:block;text-align:center;background:#007A5A;color:#fff;font-weight:700;border-radius:8px;padding:9px;margin-top:8px;font-size:15px}
.bubble{max-width:380px;background:#E9E9EB;border-radius:18px;padding:12px 16px;font-size:16px;line-height:1.4;margin-bottom:16px}
.chanlink{color:#1264A3;font-weight:700;display:inline-flex;align-items:center;gap:4px}
.slogo{width:14px;height:14px;display:inline-block}
.switcher{position:fixed;left:12px;top:6px;z-index:20;display:flex;gap:6px;opacity:.15;transition:opacity .2s}
.switcher:hover{opacity:1}
.switcher a{background:#1D1C1D;color:#fff;font-size:12px;font-weight:700;border-radius:999px;padding:6px 12px}
""".replace("#DEFAULT", "#" + cid(DEFAULT_CHANNEL))


def build():
    views = "".join(channel_view(c) for c in CHANNEL_ORDER) + cards_view()
    page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{WORKSPACE} on Slack – Campus OS Mock-up</title><style>{CSS}</style></head>
<body>{views}
<div class="switcher"><a href="#{cid(DEFAULT_CHANNEL)}">Slack workspace</a><a href="#cards">Text-thread cards</a></div>
</body></html>'''
    with open("index.html", "w") as f:
        f.write(page)
    print("Built index.html", len(page), "bytes")


if __name__ == "__main__":
    build()
