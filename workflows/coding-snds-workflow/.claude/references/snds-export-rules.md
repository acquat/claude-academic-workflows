# SNDS Output-Export Rules — Cited Reference (generic)

**What this is:** the verified legal + operational rules for exporting aggregated results
(tables, figures, model output, maps) out of the French SNDS secure environment. Every rule is
either **CONFIRMED** (verbatim quote from an official primary source; ≥ 2 independent official
sources for every numeric threshold) or **UNCONFIRMED** (no primary source — ask your
CNAM/SNDS référent; default to suppression). Compiled 2026-06-10; all sources accessed
2026-06-10. **Re-verify before a major export campaign — these texts move** (the référentiel
changed in 2024). Coding rules distilled from this doc: `.claude/rules/export-compliance.md`;
mechanical gate: `snds-export-checklist.md` (same folder).

> **THE CENTRAL FINDING.** For the **CNAM portal**, the binding rule is **qualitative, not
> numeric**: only **anonymous** results may leave (G29/WP29 three criteria), and every export
> is reviewed **case-by-case by a security expert**. No official text publishes a numeric gate
> for the CNAM portal; the Health Data Hub states no quantified consensus rules exist for it.
> The familiar numbers — **"< 11" per cell, the 85 % dominance rule, the two-cell secret
> secondaire** — are real and primary-sourced, but come from **other channels** (ATIH/ScanSanté
> dissemination, the CASD portal, INSEE business/fiscal statistics). They are what a reviewer
> will most plausibly apply by analogy → treat **≥ 11 units per exported cell/bin/point** as
> the safe-harbor default. **If your access is via CASD**, the CASD guide below is your
> *literal* operative ruleset, not an analogy.

---

## 1. Legal & contractual hierarchy

### 1.1 Référentiel de sécurité SNDS — arrêté du 6 mai 2024 ★ CONFIRMED
**Arrêté du 6 mai 2024 relatif au référentiel de sécurité applicable au Système national des
données de santé** (NOR TSSE2407926A, JO 8 May 2024),
https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049516244
- §4.5 « Sorties des données » : > « Seules des données anonymes peuvent faire l'objet d'une
  sortie par un utilisateur en dehors de l'environnement maitrisé »
- §1 definitions : > « **Sortie de données** : opération réalisée par un utilisateur qui
  consiste à exporter des données en dehors de l'environnement maitrisé. … » ;
  > « **Anonymisation** : processus empêchant toute ré-identification directe ou indirecte de
  > personnes physiques. »
- Article 2 : > « L'arrêté du 22 mars 2017 … est abrogé. »

⚠️ **Version trap:** the widely-cited arrêté du **22 mars 2017** is **abrogated** — cite the
2024 text. (Some documents, incl. the CNAM CGU v4.0, still point to the 2017 arrêté.)

### 1.2 CNIL MR-005 (méthodologie de référence, intérêt public) ★ CONFIRMED
https://www.cnil.fr/sites/cnil/files/atoms/files/mr-005_methodologie_de_reference-traitements_de_donnees_du_snds_et_des_rpu_interet_public.pdf
- §10.3 : > « Seuls des résultats anonymes peuvent être exportés. »
- **SEC-EXP-1** : > « Seuls des jeux de données anonymes peuvent faire l'objet d'une
  exportation hors de la solution sécurisée ou d'un espace de travail. Le processus
  d'anonymisation doit produire un jeu de données conforme aux trois critères définis par
  l'avis du G29 n° 05/2014 ou à tout avis ultérieur du CEPD relatif à l'anonymisation. Cette
  conformité doit être documentée. »
- **SEC-EXP-2** : > « Les exports de données doivent être soumis à la validation préalable
  d'un responsable afin d'en avaliser le principe, notamment au regard de l'exigence
  SEC-EXP-1. »
- **SEC-EXP-3** : > « Les exports doivent faire l'objet d'une surveillance automatique ou
  manuelle par un opérateur spécialisé afin d'en vérifier le caractère anonyme. Dans le cas où
  cette surveillance est automatique, tout export identifié comme non conforme doit faire
  l'objet d'une remontée d'alerte et d'une mise en quarantaine dans un espace cloisonné et
  dédié, puis doit être vérifié manuellement par un responsable spécifiquement formé et
  habilité. »

G29 three criteria (Avis 05/2014): **individualisation**, **corrélation**, **inférence**.
MR-006 (intérêt légitime — commercial actors) carries identical SEC-EXP text; public-research
projects cite **MR-005** or their own CNIL authorization. **[YOUR PROJECT]: locate your CNIL
authorization decision / MR-005 récépissé and check for project-specific export conditions —
record in `snds-data.md`.**

### 1.3 CNAM portal CGU v4.0 ★ CONFIRMED
Doc page: https://documentation-snds.health-data-hub.fr/snds/cnam/contexte_reglementaire/1-cgu_4.0
PDF: https://gitlab.com/healthdatahub/applications-du-hdh/documentation-snds/-/raw/master/snds/files/CNAM_NEW/contexte_reglementaire/1-cgu_4.0.pdf
The Utilisateur commits to:
> « N'exporter vers un système ne faisant pas partie du SNDS élargi, que des données anonymes
> du SDNS, » *(sic)* — and —
> « En cas de publication, ne pas publier de Données permettant l'identification directe ou
> indirecte des personnes »
> « Il s'engage en cas de publication à citer la source des Données et respecter l'intégrité
> des Données fournies. »

### 1.4 Secrecy covers aggregates at any aggregation level ★ CONFIRMED
**INSEE, Guide du secret statistique** (MAJ 09/2025),
https://www.insee.fr/fr/statistiques/fichier/1300624/GUIDE%20DU%20SECRET%20STATISTIQUE%20MAJ%202509.pdf :
> « Le secret statistique s'applique autant aux données individuelles qu'aux résultats agrégés
> obtenus à partir de celles-ci, dès lors que ces résultats agrégés pourraient permettre leur
> réidentification »
Grounded in **Conseil d'État n° 472883, 31 mai 2024**
(https://www.legifrance.gouv.fr/ceta/id/CETATEXT000049631259), cons. 6: lawful « quel que soit
le niveau d'agrégation … qu'à la condition que les personnes … ne puissent pas être
identifiées, directement ou indirectement ».

---

## 2. The export process (CNAM portal) ★ CONFIRMED (turnaround UNCONFIRMED)

- HDH FAQ « Export de données à partir du portail » (#918, answer 26/01/2021):
  https://entraide.health-data-hub.fr/t/export-de-donnees-a-partir-du-portail/918
  > « les exports sur le portail Cnam sont contrôlés au cas par cas par un expert sécurité qui
  > analyse si les données permettraient de remonter à l'individu »
  > « Il n'existe pas de règles quantifiées, établies et consensuelles permettant de répondre
  > précisément à votre question. »
  > « Il est généralement déconseillé d'exporter des données à l'échelle individuelle. »
- Two-stage control: validation préalable by a responsable (SEC-EXP-2) + anonymity surveillance
  with quarantine (SEC-EXP-3) — §1.2.
- **Turnaround / délai: UNCONFIRMED** (no official figure anywhere). **Allowed formats:
  UNCONFIRMED.** Ask your référent; plan days-to-weeks.

---

## 3. The numeric rules and where they actually come from

### 3.1 « < 11 masked » — the French health-data norm ★ CONFIRMED (channel-specific)
- **ATIH (PMSI producer), ScanSanté**: https://www.scansante.fr/utiliser-scansante/propos-de-scansante
  > « À la demande de la Commission nationale de l'informatique et des libertés (Cnil), le
  > contenu de plusieurs restitutions d'activité sur la plateforme ScanSanté est limité. Afin
  > de préserver l'anonymat des informations diffusées, **les effectifs inférieurs à 11 sont
  > masqués** pour tous les utilisateurs (accès libre ou avec identifiant). »
  Corroborated in ATIH's EMOIS-2022 deck (« Masquage des effectifs < 11 »):
  https://www.atih.sante.fr/sites/default/files/public/content/4285/atih_atelier_scansante_emois_2022.pdf
- **CASD, « Règles de confidentialité — Guide utilisateur »** (version 06/2022), §5.23 (PMSI/ATIH):
  https://www.casd.eu/wp/wp-content/uploads/Regles_de_confidentialite_sorties.pdf
  > « **Aucune case ne doit concerner moins de 11 unités** relatives à des nombres de patients,
  > à des nombres de séjours et à des nombres de doses. »
  (Stable across editions — same text in the 07/2019 edition §5.25.)
- Thresholds are **source-specific**, not universal: INSEE business = 3 units; DADS = 5;
  DEPP = 10; fiscal/household = 11; DREES = 5 (individus) / 11 (fiscal); IRDES = 15
  (CASD guides; INSEE Courrier des statistiques N9 2023, https://www.insee.fr/fr/information/7635823).
- **DCIR / CEPIDC distinct thresholds: UNCONFIRMED** (no source publishes one) → default ≥ 11.

### 3.2 Secret secondaire ★ CONFIRMED (doctrine)
CASD 06/2022 §2.3.1.2:
> « il faut appliquer ce que l'on appelle **le secret secondaire** qui vise à empêcher la
> reconstitution, **par somme ou par différence**, des cases masquées. … On doit alors masquer
> deux valeurs pour pouvoir l'exporter tout en respectant le secret secondaire. »
Independent: INSEE Tau-Argus doc (« la pose du secret secondaire »),
https://www.insee.fr/fr/statistiques/fichier/2646243/10-julien-nicolas-gerer-confidentialite-series-statistiques-avec-logiciel-tau-argus.pdf

### 3.3 Dominance (85 %) ★ CONFIRMED for business amounts; health transfer UNCONFIRMED
INSEE: > « aucun résultat, dans le cas général, n'est publié s'il concerne moins de trois
entreprises, **ou si une seule entreprise représente 85 % ou plus de sa valeur** » (« Secret
statistique », https://www.insee.fr/fr/information/1300624; lineage: règle du CNIS 7/7/1960).
CASD health guide §2.3.3 states the concept for amount variables without a number. → Apply the
85 % check to exported € cells by analogy (safe harbor).

### 3.4 Non-inférence / unanimous cells ★ CONFIRMED (principle)
CASD 06/2022 §2.2.3 + §2.3.2 (hospital-diagnosis example): a cell where all (or nearly all)
members of a recognizable group share a diagnosis is **not diffusable** even if the cell count
is large. No quantified rate-denominator rule exists for health data (UNCONFIRMED) → default:
denominator ≥ 11 AND implied numerator ≥ 11; no 0 %/100 % sensitive cells.

### 3.5 Figures, maps, programs, regressions ★ CONFIRMED (CASD channel; best practice elsewhere)
CASD 06/2022 §3: regressions — report N (§3.2); graphs/maps — supply the underlying population
and variable definitions; box-plot outliers « ne doivent pas être identifiés »; Stata LIVE
graphs forbidden (embed data) (§3.3); aggregated tables — supply per-cell effectifs + a
**fichier de contrôle** (max contribution) that the reviewer removes before release (§3.4);
programs exportable only if free of confidential data (§3.1). Maps: INSEE Insee-Méthodes 131
ch. 14 (https://www.insee.fr/fr/statistiques/fichier/3635442/imet131-r-chapitre-14.pdf) —
thresholds apply per zone; beware **différenciation géographique** (overlapping zonings allow
deduction « par soustraction »).

### 3.6 Identifiers & individual-scale outputs ★ CONFIRMED
HDH « Bonnes pratiques en matière d'exportation de résultats agrégés du SNDS » (29/12/2021),
https://entraide.health-data-hub.fr/t/bonnes-pratiques-en-matiere-dexportation-de-resultats-agreges-du-snds-et-risque-de-re-identification/1190 :
> « ne pas restituer de petits effectifs » ; « ne pas sortir d'identifiants de personnes
> bénéficiaires **ou professionnels de santé** » ; « ne pas sortir les variables dites
> identifiants potentiels (le croisement de ces variables présentent un risque de
> ré-identification) » ; « une information de santé sur un individu ne doit pas pouvoir être
> déduite à partir d'autres attributs ».

---

## 4. Summary ledger

| # | Rule | Status | Source |
|---|---|---|---|
| 1 | Only anonymous results may leave (G29 criteria, documented) | CONFIRMED, binding | arrêté 2024 §4.5; MR-005 §10.3+SEC-EXP-1; CGU v4.0 |
| 2 | Case-by-case expert review; validation + surveillance + quarantine | CONFIRMED, binding | MR-005 SEC-EXP-2/3; HDH #918 |
| 3 | No numeric gate published for the CNAM portal | CONFIRMED (absence) | HDH #918 |
| 4 | ≥ 11 per cell (health norm; CASD literal rule for PMSI) | CONFIRMED (channel-specific) → safe-harbor default | ATIH ScanSanté; ATIH EMOIS 2022; CASD §5.23 |
| 5 | DCIR/CEPIDC distinct thresholds | UNCONFIRMED → ≥ 11 default | — |
| 6 | Secret secondaire (mask ≥ 2; no margin reconstruction) | CONFIRMED (doctrine) | CASD §2.3.1.2; INSEE Tau-Argus |
| 7 | 85 % dominance on amounts | CONFIRMED (business) → analogy for € cells | INSEE; CASD |
| 8 | No unanimous/quasi-unanimous sensitive cells | CONFIRMED (principle) | CASD §2.2.3/§2.3.2 |
| 9 | Min denominator for rates | UNCONFIRMED → den ≥ 11 & num ≥ 11 default | — |
| 10 | No outliers/min-max; figures need underlying counts; no data-embedding formats | CONFIRMED (CASD) | CASD §3.3 |
| 11 | Maps: per-zone thresholds; geographic differencing risk | CONFIRMED (principles) | CASD §3.3; INSEE ch. 14 |
| 12 | No patient/professional identifiers; no potential-identifier crossings | CONFIRMED | HDH #1190; CGU |
| 13 | Individual-scale exports discouraged even if "anonymized" | CONFIRMED | HDH #918 |
| 14 | Regressions: report N | CONFIRMED (CASD) | CASD §3.2 |
| 15 | Programs data-free; logs/titles are exports | CONFIRMED (CASD) + arrêté def. | CASD §3.1; arrêté 2024 §1 |
| 16 | Turnaround; allowed formats | UNCONFIRMED — ask référent | — |
| 17 | Publication: cite source; nothing identifying | CONFIRMED, binding | CGU v4.0 |
| 18 | Secrecy covers aggregates at any aggregation level | CONFIRMED | INSEE Guide; CE n°472883 |

## 5. Questions for YOUR référent (ask before the first export)

1. Does the portal's security expert apply a quantified minimum cell size in practice (is ≥ 11
   the working standard)? Is there an internal output-checking guide?
2. Any DCIR / CEPIDC-specific thresholds (esp. rare causes of death)?
3. Expected turnaround per export request; size/format limits; does a per-cell count annex
   speed review?
4. Allowed file formats; are logs or editable-graph formats acceptable?
5. Are binned provider-level summaries acceptable (≥ 11 providers per bin), given health
   professionals are protected?
6. Does YOUR authorization decision impose extra export conditions?
7. Facility-level cells: minimum number of établissements per cell? Dominance rule on facility
   volumes?

*Record every answer in `snds-data.md` and fold it into these rules.*
