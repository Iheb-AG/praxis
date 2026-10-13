# Source provenance

Target: `synthetic_cortex_m3`; MCU: `PRAXIS-DEMO-M3`; package: `Fixture:QFP-16`; board revision: `synthetic-1`; silicon: `fictional-v1`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Every artifact row references one complete metadata row below. Reconstruct its exact path by concatenating the referenced directory prefix and File; a dash in the prefix registry means the empty prefix. The manifest also retains the expanded registry.

| ID | Prefix | File | SHA-256 | Metadata |
| --- | --- | --- | --- | --- |
| definitions | prefix_003 | peripherals.json | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 | metadata_005 |
| header | prefix_002 | demo_m3.h | 5a851a24246dafdc9dfef6b8b7ec6a42f2314e51adf18542ae5d0a91cc52c46a | metadata_003 |
| profile | prefix_001 | profile.json | df9855c1fdad1671abf293f3465fa62e8255f58cc64bfbf72475684bd8ad7d48 | metadata_001 |
| schematic | prefix_002 | netlist.xml | 873429cdc5d32d228ac6489e895a62a3bcce795132e9da17a64e5cd480b7ff2d | metadata_002 |
| vendor_blocks | prefix_002 | vendor_blocks.h | 510095cbd22f7e85954597b1d3a7f21ff19ac0cbf6a4ed0100e07068d0b792ee | metadata_004 |

## Shared path prefixes

| Prefix | Exact directory prefix |
| --- | --- |
| prefix_001 | — |
| prefix_002 | raw/ |
| prefix_003 | reviewed/ |

## Shared source metadata

| Metadata | Authority | Version | License | Origin |
| --- | --- | --- | --- | --- |
| metadata_001 | configuration | 1 | MIT | Local target profile |
| metadata_002 | connectivity | synthetic-v1 | MIT | Hand-authored KiCad XML-shaped synthetic fixture; no CAD export or physical board claimed |
| metadata_003 | declarations | synthetic-v1 | MIT | Authored fictional register declarations |
| metadata_004 | declarations | synthetic-v1 | MIT | Authored fictional vendor structures, not ARM core registers |
| metadata_005 | semantics | synthetic-v1 | MIT | Empty reviewed operating definitions; all discovered blocks are declarations only |

Editorial reviewer: Praxis synthetic fixture authors. Basis: Reviewed as fictional parser test data only; no real device semantics or physical qualification..

Editorial review is not independent hardware sign-off. See [[index]].
