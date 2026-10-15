# Source provenance

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Every artifact row references one complete metadata row below. Reconstruct its exact path by concatenating the referenced directory prefix and File; a dash in the prefix registry means the empty prefix. The manifest also retains the expanded registry.

| ID | Prefix | File | SHA-256 | Metadata |
| --- | --- | --- | --- | --- |
| acquisition_lock | prefix_001 | acquisition-lock.json | 7eb5b8cfe8fc1ffa5f68c9c559bce7680580cbbf0f7bda24ccd60e6969e46128 | metadata_002 |
| cmsis_compiler_h | prefix_002 | cmsis_compiler.h | b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8 | metadata_005 |
| cmsis_gcc_h | prefix_002 | cmsis_gcc.h | 43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617 | metadata_006 |
| cmsis_version_h | prefix_002 | cmsis_version.h | 184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3 | metadata_007 |
| core_cm3_h | prefix_002 | core_cm3.h | c9937781259a8897adf514445441c68570087d6a72a558d8a4afe75cdb62dbd2 | metadata_008 |
| definitions | prefix_001 | definitions.json | 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 | metadata_012 |
| header | prefix_002 | stm32f103xb.h | d9c7c613d9fea74220892b4fbc3e80617493acad82a04bafadab2b4a7198399c | metadata_010 |
| license_cmsis_txt | prefix_002 | LICENSE-CMSIS.txt | b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1 | metadata_003 |
| license_st_md | prefix_002 | LICENSE-ST.md | b645e89bbfb6accf914cf7adca011712bf90055391fdd55f2af6439d98aa36d4 | metadata_004 |
| mpu_armv7_h | prefix_002 | mpu_armv7.h | 29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372 | metadata_009 |
| profile | prefix_001 | profile.json | c5069e385a714da38f2b751523a6adac40005d58586667a937cb5436cb57138b | metadata_001 |
| system_stm32f1xx_h | prefix_002 | system_stm32f1xx.h | a54dfbb3480c672f532d472a6e84bcf34df6551771d2e9966c5a3503c676b6ab | metadata_011 |

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
| metadata_003 | configuration | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/LICENSE.txt |
| metadata_004 | configuration | c8e9a4a4f16b6d2cb2a2083cbe5161025280fb22 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f1/c8e9a4a4f16b6d2cb2a2083cbe5161025280fb22/License.md |
| metadata_005 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_compiler.h |
| metadata_006 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_gcc.h |
| metadata_007 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_version.h |
| metadata_008 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/core_cm3.h |
| metadata_009 | declarations | CMSIS_5/5.9.0 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/mpu_armv7.h |
| metadata_010 | declarations | c8e9a4a4f16b6d2cb2a2083cbe5161025280fb22 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f1/c8e9a4a4f16b6d2cb2a2083cbe5161025280fb22/Include/stm32f103xb.h |
| metadata_011 | declarations | c8e9a4a4f16b6d2cb2a2083cbe5161025280fb22 | Apache-2.0; see retained upstream license | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f1/c8e9a4a4f16b6d2cb2a2083cbe5161025280fb22/Include/system_stm32f1xx.h |
| metadata_012 | semantics | 1 | MIT | Empty operating definitions; no peripheral operating review claimed |

Editorial reviewer: Praxis experimental compiler scope review. Basis: Review covers source identity, licensed structural extraction and honest absence of board/operating evidence only. It does not certify package availability, electrical facts or initialization semantics..

Editorial review is not independent hardware sign-off. See [[index]].
