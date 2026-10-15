# Source provenance

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Every artifact row references one complete metadata row below. Reconstruct its exact path by concatenating the referenced directory prefix and File; a dash in the prefix registry means the empty prefix. The manifest also retains the expanded registry.

| ID | Prefix | File | SHA-256 | Metadata |
| --- | --- | --- | --- | --- |
| acquisition_lock | prefix_001 | acquisition-lock.json | 4dba2173503a026acf81f46893aacdd3353231cb00315d391f0708fd9fc64853 | metadata_002 |
| cmsis_compiler_h | prefix_002 | cmsis_compiler.h | b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8 | metadata_007 |
| cmsis_gcc_h | prefix_002 | cmsis_gcc.h | 43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617 | metadata_008 |
| cmsis_version_h | prefix_002 | cmsis_version.h | 184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3 | metadata_009 |
| core_cm0plus_h | prefix_002 | core_cm0plus.h | a09fa9c6b8b21d1920bce15b98aa56182b027e9278cca0b154812bac2aea3cfa | metadata_010 |
| definitions | prefix_001 | definitions.json | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 | metadata_012 |
| header | prefix_002 | stm32g071xx.h | 0b19058af668cff72649ae3871f6729b0fa68c6e81794cefbd1b0d63e0943fb3 | metadata_005 |
| license_cmsis_txt | prefix_002 | LICENSE-CMSIS.txt | b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1 | metadata_004 |
| license_st_md | prefix_002 | LICENSE-ST.md | c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4 | metadata_003 |
| mpu_armv7_h | prefix_002 | mpu_armv7.h | 29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372 | metadata_011 |
| profile | prefix_001 | profile.json | 0e5b98c233654fbbacc1b1defc80e106d6e9caeb94c7f9ede5521364a0611de9 | metadata_001 |
| system_stm32g0xx_h | prefix_002 | system_stm32g0xx.h | 20ee999e4431472a7c351e2412537aa0ef7f5f5e499a21a92c1d4cc21f84ebf1 | metadata_006 |

## Shared path prefixes

| Prefix | Exact directory prefix |
| --- | --- |
| prefix_001 | — |
| prefix_002 | raw/ |

## Shared source metadata

| Metadata | Authority | Version | License | Origin |
| --- | --- | --- | --- | --- |
| metadata_001 | configuration | 1 | MIT | Local target profile |
| metadata_002 | configuration | 1 | MIT (metadata); upstream file licenses retained | Exact source URLs, commits and downloaded SHA-256 values |
| metadata_003 | configuration | 7c77b7cbcee497dfbb5cc08f9562a80515e78013 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-g0/7c77b7cbcee497dfbb5cc08f9562a80515e78013/LICENSE.md |
| metadata_004 | configuration | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/LICENSE.txt |
| metadata_005 | declarations | 7c77b7cbcee497dfbb5cc08f9562a80515e78013 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-g0/7c77b7cbcee497dfbb5cc08f9562a80515e78013/Include/stm32g071xx.h |
| metadata_006 | declarations | 7c77b7cbcee497dfbb5cc08f9562a80515e78013 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-g0/7c77b7cbcee497dfbb5cc08f9562a80515e78013/Include/system_stm32g0xx.h |
| metadata_007 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_compiler.h |
| metadata_008 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_gcc.h |
| metadata_009 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_version.h |
| metadata_010 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/core_cm0plus.h |
| metadata_011 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/mpu_armv7.h |
| metadata_012 | semantics | 1 | MIT | Empty operating definitions; no peripheral operating review claimed |

Editorial reviewer: Praxis experimental compiler scope review. Basis: Review covers source identity, licensed structural extraction and honest absence of board/operating evidence only. It does not certify package availability, electrical facts or initialization semantics..

Editorial review is not independent hardware sign-off. See [[index]].
