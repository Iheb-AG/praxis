# Source provenance

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Every artifact row references one complete metadata row below. Reconstruct its exact path by concatenating the referenced directory prefix and File; a dash in the prefix registry means the empty prefix. The manifest also retains the expanded registry.

| ID | Prefix | File | SHA-256 | Metadata |
| --- | --- | --- | --- | --- |
| acquisition_lock | prefix_001 | acquisition-lock.json | 0fcbc3fc1f31782857d0ae3ce3a366d9d23f577eb0815da2e2515f8c2da1ab87 | metadata_002 |
| cachel1_armv7_h | prefix_002 | cachel1_armv7.h | 2e336a64f60a9c0eaf5a08e2c4845d94da86c3fd84d219d0d0c9f530e63bc9c3 | metadata_007 |
| cmsis_compiler_h | prefix_002 | cmsis_compiler.h | b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8 | metadata_008 |
| cmsis_gcc_h | prefix_002 | cmsis_gcc.h | 43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617 | metadata_009 |
| cmsis_version_h | prefix_002 | cmsis_version.h | 184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3 | metadata_010 |
| core_cm7_h | prefix_002 | core_cm7.h | e974d0a91752487d0154457cd422c37667328e9ddb7ba4fa2fed479a63577f63 | metadata_011 |
| definitions | prefix_001 | definitions.json | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 | metadata_013 |
| header | prefix_002 | stm32h743xx.h | 9a4ea0860707868a1cc562140ba214d535fb5a64fde91b451b2767276eef7e03 | metadata_005 |
| license_cmsis_txt | prefix_002 | LICENSE-CMSIS.txt | b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1 | metadata_004 |
| license_st_md | prefix_002 | LICENSE-ST.md | 053a83960032ab6bbd2231a3b6300bde3b4e526dcf11a61394907c0bdaacd713 | metadata_003 |
| mpu_armv7_h | prefix_002 | mpu_armv7.h | 29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372 | metadata_012 |
| profile | prefix_001 | profile.json | 12eb63f926c780eeecbc9cd7ebc7a2432b20bcd5bae7f078cbecb9c8ec2c0dee | metadata_001 |
| system_stm32h7xx_h | prefix_002 | system_stm32h7xx.h | e77e7dfe5ff780928c28cf37576135050e5af7bf31776400ac700e8b917d24be | metadata_006 |

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
| metadata_003 | configuration | 81db1ec63cdc191fae1565b772da3ea5aa29a683 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-h7/81db1ec63cdc191fae1565b772da3ea5aa29a683/LICENSE.md |
| metadata_004 | configuration | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/LICENSE.txt |
| metadata_005 | declarations | 81db1ec63cdc191fae1565b772da3ea5aa29a683 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-h7/81db1ec63cdc191fae1565b772da3ea5aa29a683/Include/stm32h743xx.h |
| metadata_006 | declarations | 81db1ec63cdc191fae1565b772da3ea5aa29a683 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-h7/81db1ec63cdc191fae1565b772da3ea5aa29a683/Include/system_stm32h7xx.h |
| metadata_007 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cachel1_armv7.h |
| metadata_008 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_compiler.h |
| metadata_009 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_gcc.h |
| metadata_010 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_version.h |
| metadata_011 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/core_cm7.h |
| metadata_012 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/mpu_armv7.h |
| metadata_013 | semantics | 1 | MIT | Empty operating definitions; no peripheral operating review claimed |

Editorial reviewer: Praxis experimental compiler scope review. Basis: Review covers source identity, licensed structural extraction and honest absence of board/operating evidence only. It does not certify package availability, electrical facts or initialization semantics..

Editorial review is not independent hardware sign-off. See [[index]].
