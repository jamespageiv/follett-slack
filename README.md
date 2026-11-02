# Northfield State on Slack: Campus OS Mock-up

A clickable, static recreation of the **Northfield State** Slack workspace for the Campus OS student story (Emma, fall 2026). It needs no scripts, so it works in any browser, artifact viewer or GitHub Pages.

## View it
Open `index.html` in a browser. To get a shareable link, turn on GitHub Pages (Settings → Pages → Deploy from branch → `main` / root).

- **Slack workspace view:** channels #general, #econ-2010-study-group (default), #first-year-wolves, #intramural-soccer, #nftridelta, #nf-ambassadors
- **Text-thread cards view:** the Nov 17 invite card and the #NFTriDelta / #nf-ambassadors channel links
- Clickable: channel switching, Pins tab, Chapter 7 notes folder, member list, Ambassador **Apply** form, **Join** on the invite card
- The two view buttons sit faintly in the top-left and appear on hover, so they stay out of screenshots

### Deep links (useful for screenshots)
| Screen | Link |
|---|---|
| Study group | `index.html#ch-econ-2010-study-group` |
| Study group pins | `index.html#ch-econ-2010-study-group-pins` |
| Members list | `index.html#ch-econ-2010-study-group-members` |
| Ambassador apply form | `index.html#ch-nf-ambassadors-apply` |
| Text-thread cards | `index.html#cards` |

## Editing
All story content (people, avatar colors, channels, messages, times, reactions, pins) is in the **STORY DATA** section at the top of `build_mockup.py`. Edit it, then rebuild:

```bash
python3 build_mockup.py   # regenerates index.html
```

You can also edit `index.html` directly for quick tweaks, but those changes are overwritten the next time you rebuild.

## Source
Built from *Campus OS Student Story: Script and Slack Mock-up Brief*. All names, channels and numbers are fictional sample data.
