# Outside Window on a shared screen

Outside Window supports native [TRMNL Mashups](https://help.trmnl.com/en/articles/10168132-mashups).
Combine it with other installed plugins while keeping its own configuration,
collector, webhook and repository.

## Choose a size

| View | Template | Use |
| --- | --- | --- |
| Full screen | [`full.liquid`](../src/full.liquid) | Dedicated screen with the most detail |
| Left or right half | [`half_vertical.liquid`](../src/half_vertical.liquid) | Tall panel alongside another half or two quarters |
| Top or bottom half | [`half_horizontal.liquid`](../src/half_horizontal.liquid) | Wide, compact panel |
| Quarter | [`quadrant.liquid`](../src/quadrant.liquid) | Brief summary in a three- or four-plugin layout |

A quarter is useful for the best outdoor window and its weather. Use a vertical half for more forecast rows.

Horizontal halves and quarters intentionally show fewer rows than the full view.
Counts in the summary can describe more items than are visible in the small panel.

## Suggested combinations

Workday: top right, alongside Workday Windows and Digital Product Sales. At home: bottom left, below Family Day.

![Synthetic combined preview](https://raw.githubusercontent.com/JirakJ/trmnl-everyday/main/docs/mashups/work.png)

See the [shared-screen guide and all four presets](https://github.com/JirakJ/trmnl-everyday/tree/main/docs/mashups)
and its downloadable interactive preview. The companion plugins are optional;
this plugin can still run on its own.

## Set it up

1. Complete this repository's [installation](../README.md#install) and configure
   each companion plugin using its own repository. Push a real payload to each
   installed plugin instance.
2. Open **Playlists** in TRMNL and use the dropdown beside **Add Plugin** to choose
   the matching split-screen layout.
3. Assign the connected instances to the labeled sections. Follow the small
   position diagram in TRMNL when selecting each section.
4. Refresh the playlist and inspect the generated thumbnail at full size.
   Keep the mashup in your playlist; hide redundant full-screen entries if desired.
5. Keep each collector scheduled and sending to its own webhook. Check the update
   timestamp in every panel, then verify the result on your physical display.

To return to a single-plugin screen, restore its full-screen playlist entry.
No collector changes or combined payload are needed. The account's device refresh
settings determine when the display next requests a screen; a mashup does not make
collection real-time. See [TRMNL refresh behavior](https://help.trmnl.com/en/articles/10113695-how-refresh-rates-work).

## Verification boundary

These templates target the original 800 × 480 display. The recommended combined
presets were rendered and checked in Chromium with synthetic data; private account
setup, real input data and physical e-ink display operation remain unverified.
Smaller panels truncate long text. Keep important detail on a larger panel or
another playlist entry. The demo QR, where present, deliberately points to a
non-working example address.
