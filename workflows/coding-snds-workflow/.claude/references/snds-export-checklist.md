# SNDS Pre-Export Checklist — run before EVERY « demande de sortie »

**Companion to** `snds-export-rules.md` (same folder — rule numbers refer to its §4 ledger).
Tick every box; if a box cannot be ticked, fix or suppress before submitting. **When in doubt:
more suppression, not less** — and ask your CNAM/SNDS référent. Default gate = ≥ 11 (replace
with your DUA's confirmed value, recorded in `snds-data.md`).

## A. Inventory & framing
- [ ] **A1.** Every file in the export is listed (tables, figures, programs, README); nothing
      rides along unreviewed. *(rule 2)*
- [ ] **A2.** One line per file: content, source tables, unit of analysis →
      `00_README_export.txt`.
- [ ] **A3.** Nothing is individual-scale: no row-per-patient/provider/facility, no per-unit
      scatter, no per-provider effect vector. *(rules 1, 12, 13)*
- [ ] **A4.** No identifiers anywhere (incl. titles, footnotes, filenames): `BEN_NIR_PSA`,
      `BEN_NIR_ANO`, `BEN_IDT_ANO`, `NIR_ANO_17`, `PFS_PRE_NUM`, `ETB_PRE_FIN`, `ETA_NUM`,
      commune codes, or potential-identifier crossings. *(rule 12)*

## B. Counts — the ≥ 11 double gate
- [ ] **B1.** Every count cell ≥ 11 units — including the implied complement of displayed
      categories. *(rules 4, 8)*
- [ ] **B2.** Every event count shown or **recoverable** (N × rate; margin minus shown cells)
      is ≥ 11, or exactly 0 and masked/footnoted. *(rules 4, 9)*
- [ ] **B3.** Every rate/percentage: denominator ≥ 11 AND implied numerator ≥ 11 (or masked 0).
      *(rule 9)*
- [ ] **B4.** No 0 % / 100 % (or ≳ 90 % quasi-unanimous) cell on a sensitive characteristic
      within a recognizable subgroup. *(rule 8)*
- [ ] **B5.** Masked cells not recomputable by sum/difference from margins, other exported
      tables, or **previously exported** tables: ≥ 2 masks per affected row/column or margins
      dropped; checked across the table *family*. *(rule 6)*
- [ ] **B6.** €/amount/volume cells: no single contributor ≥ 85 % of the cell. *(rule 7)*
- [ ] **B7.** Facility-level cells: ≥ 3 facilities per displayed cell (analogy — référent Q7)
      and ≥ 11 stays/events. *(rules 4, 7)*

## C. Figures
- [ ] **C1.** Every plotted point/bin/bar rests on ≥ 11 units (and ≥ 11 events for outcome
      series); sub-threshold bins suppressed (gap + footnote), not plotted.
- [ ] **C2.** No mark = one individual (patient or provider); binned versions only.
- [ ] **C3.** No min/max/outlier marks; box plots without outliers; p1/p99 only if each tail
      ≥ 11. *(rule 10)*
- [ ] **C4.** Flat formats only (PDF/PNG/RTF); no data-embedding formats (`.sge`, Stata LIVE
      `.gph`, plot-object RDS, Excel pivot caches). *(rule 10)*
- [ ] **C5.** Underlying per-bin count table exists in the **reviewer annex** (not for
      publication). *(rules 10, 14)*
- [ ] **C6.** Maps: every shaded zone passes B1–B4; failing zones greyed out; no overlapping
      geographies for the same indicator without a differencing check; per-zone annex. *(rule 11)*

## D. Models
- [ ] **D1.** Every model table prints N and number of clusters/groups. *(rule 14)*
- [ ] **D2.** No saturated specification whose coefficients are recoverable cell means over
      < 11 obs.
- [ ] **D3.** Random/fixed effects exported only as distributional summaries over ≥ 11 units
      per bin — never the per-unit vector. *(rules 12, 13)*

## E. Programs, logs, metadata
- [ ] **E1.** Exported code contains no data (no hard-coded IDs, no pasted output in comments).
      *(rule 15)*
- [ ] **E2.** No raw logs; clean run-summary instead. *(rule 15)*
- [ ] **E3.** Titles/footnotes/headers carry no IDs and no sub-threshold Ns; document metadata
      cleaned.

## F. Request package & submission
- [ ] **F1.** Package = outputs + `00_README_export.txt` + reviewer count annex (per-cell Ns;
      for € cells, max-contribution control sheet — flagged "control file, not for release").
- [ ] **F2.** README states: "All cells/bins/points ≥ [threshold]; secondary suppression
      applied; no individual-level data; no identifiers."
- [ ] **F3.** Turnaround & formats unconfirmed for your channel → if deadline-critical,
      contact the référent before submitting. *(rule 16)*
- [ ] **F4.** Judgment calls listed in the README with the choice made.

## G. Afterwards
- [ ] **G1.** Archive the submitted package + date + reviewer feedback (e.g.
      `.claude/quality_reports/`); fold reviewer remarks into `snds-export-rules.md` and
      `snds-data.md` as new rules.
- [ ] **G2.** Publication stage: cite the data source; nothing identifying. *(rule 17)*
