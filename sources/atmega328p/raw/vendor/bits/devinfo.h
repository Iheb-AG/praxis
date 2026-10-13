/* Copyright (c) 2025  Georg-Johann Lay
   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:

   * Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the
     distribution.
   * Neither the name of the copyright holders nor the names of
     contributors may be used to endorse or promote products derived
     from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE. */

/* include/bits/devinfo.h.  Generated from devinfo.h.in by configure. */

#ifndef __BITS_DEVINFO_H_
#define __BITS_DEVINFO_H_

#if 0 || defined(__AVR_AVR16DU14__) || defined(__AVR_AVR16DU20__) || defined(__AVR_AVR16DU28__) || defined(__AVR_AVR16DU32__) || defined(__AVR_AVR32DU14__) || defined(__AVR_AVR32DU20__) || defined(__AVR_AVR32DU28__) || defined(__AVR_AVR32DU32__) || defined(__AVR_AVR64DU28__) || defined(__AVR_AVR64DU32__) || defined(__AVR_AVR32DA28__) || defined(__AVR_AVR32DA32__) || defined(__AVR_AVR32DA48__) || defined(__AVR_AVR64DA28__) || defined(__AVR_AVR64DA32__) || defined(__AVR_AVR64DA48__) || defined(__AVR_AVR64DA64__) || defined(__AVR_AVR128DA28__) || defined(__AVR_AVR128DA32__) || defined(__AVR_AVR128DA48__) || defined(__AVR_AVR128DA64__) || defined(__AVR_AVR32DA28S__) || defined(__AVR_AVR32DA32S__) || defined(__AVR_AVR32DA48S__) || defined(__AVR_AVR64DA28S__) || defined(__AVR_AVR64DA32S__) || defined(__AVR_AVR64DA48S__) || defined(__AVR_AVR64DA64S__) || defined(__AVR_AVR128DA28S__) || defined(__AVR_AVR128DA32S__) || defined(__AVR_AVR128DA48S__) || defined(__AVR_AVR128DA64S__) || defined(__AVR_AVR32DB28__) || defined(__AVR_AVR32DB32__) || defined(__AVR_AVR32DB48__) || defined(__AVR_AVR64DB28__) || defined(__AVR_AVR64DB32__) || defined(__AVR_AVR64DB48__) || defined(__AVR_AVR64DB64__) || defined(__AVR_AVR128DB28__) || defined(__AVR_AVR128DB32__) || defined(__AVR_AVR128DB48__) || defined(__AVR_AVR128DB64__) || defined(__AVR_AVR16DD14__) || defined(__AVR_AVR16DD20__) || defined(__AVR_AVR16DD28__) || defined(__AVR_AVR16DD32__) || defined(__AVR_AVR32DD14__) || defined(__AVR_AVR32DD20__) || defined(__AVR_AVR32DD28__) || defined(__AVR_AVR32DD32__) || defined(__AVR_AVR64DD14__) || defined(__AVR_AVR64DD20__) || defined(__AVR_AVR64DD28__) || defined(__AVR_AVR64DD32__)
#define __AVR_Dx__
#endif

#if 0 || defined(__AVR_AVR16EA28__) || defined(__AVR_AVR16EA32__) || defined(__AVR_AVR16EA48__) || defined(__AVR_AVR16EB14__) || defined(__AVR_AVR16EB20__) || defined(__AVR_AVR16EB28__) || defined(__AVR_AVR16EB32__) || defined(__AVR_AVR32EA28__) || defined(__AVR_AVR32EA32__) || defined(__AVR_AVR32EA48__) || defined(__AVR_AVR32EB14__) || defined(__AVR_AVR32EB20__) || defined(__AVR_AVR32EB28__) || defined(__AVR_AVR32EB32__) || defined(__AVR_AVR64EA28__) || defined(__AVR_AVR64EA32__) || defined(__AVR_AVR64EA48__)
#define __AVR_Ex__
#endif

#if 0 || defined(__AVR_AVR16LA14__) || defined(__AVR_AVR16LA20__) || defined(__AVR_AVR16LA28__) || defined(__AVR_AVR16LA32__) || defined(__AVR_AVR32LA14__) || defined(__AVR_AVR32LA20__) || defined(__AVR_AVR32LA28__) || defined(__AVR_AVR32LA32__)
#define __AVR_Lx__
#endif

#if 0 || defined(__AVR_AVR32SD20__) || defined(__AVR_AVR32SD28__) || defined(__AVR_AVR32SD32__)
#define __AVR_Sx__
#endif

/* util/setbaud.h uses BAUD to specify the baud rate.
   This clashes with BAUD as used in many avr/io*.h headers.
   The following macro is used by avr/io.h for improved
   diagnostics when BAUD is defined in such a context.  */

#if 0 || defined(__AVR_ATxmega8E5__) || defined(__AVR_ATxmega16A4__) || defined(__AVR_ATxmega16A4U__) || defined(__AVR_ATxmega16C4__) || defined(__AVR_ATxmega16D4__) || defined(__AVR_ATxmega16E5__) || defined(__AVR_ATxmega32A4__) || defined(__AVR_ATxmega32A4U__) || defined(__AVR_ATxmega32C3__) || defined(__AVR_ATxmega32C4__) || defined(__AVR_ATxmega32D3__) || defined(__AVR_ATxmega32D4__) || defined(__AVR_ATxmega32E5__) || defined(__AVR_ATtiny202__) || defined(__AVR_ATtiny204__) || defined(__AVR_ATtiny212__) || defined(__AVR_ATtiny214__) || defined(__AVR_ATtiny402__) || defined(__AVR_ATtiny404__) || defined(__AVR_ATtiny406__) || defined(__AVR_ATtiny412__) || defined(__AVR_ATtiny414__) || defined(__AVR_ATtiny416__) || defined(__AVR_ATtiny416auto__) || defined(__AVR_ATtiny417__) || defined(__AVR_ATtiny424__) || defined(__AVR_ATtiny426__) || defined(__AVR_ATtiny427__) || defined(__AVR_ATtiny804__) || defined(__AVR_ATtiny806__) || defined(__AVR_ATtiny807__) || defined(__AVR_ATtiny814__) || defined(__AVR_ATtiny816__) || defined(__AVR_ATtiny817__) || defined(__AVR_ATtiny824__) || defined(__AVR_ATtiny826__) || defined(__AVR_ATtiny827__) || defined(__AVR_ATtiny1604__) || defined(__AVR_ATtiny1606__) || defined(__AVR_ATtiny1607__) || defined(__AVR_ATtiny1614__) || defined(__AVR_ATtiny1616__) || defined(__AVR_ATtiny1617__) || defined(__AVR_ATtiny1624__) || defined(__AVR_ATtiny1626__) || defined(__AVR_ATtiny1627__) || defined(__AVR_ATtiny3214__) || defined(__AVR_ATtiny3216__) || defined(__AVR_ATtiny3217__) || defined(__AVR_ATtiny3224__) || defined(__AVR_ATtiny3226__) || defined(__AVR_ATtiny3227__) || defined(__AVR_ATmega808__) || defined(__AVR_ATmega809__) || defined(__AVR_ATmega1608__) || defined(__AVR_ATmega1609__) || defined(__AVR_ATmega3208__) || defined(__AVR_ATmega3209__) || defined(__AVR_ATmega4808__) || defined(__AVR_ATmega4809__) || defined(__AVR_ATxmega64A3__) || defined(__AVR_ATxmega64A3U__) || defined(__AVR_ATxmega64A4U__) || defined(__AVR_ATxmega64B1__) || defined(__AVR_ATxmega64B3__) || defined(__AVR_ATxmega64C3__) || defined(__AVR_ATxmega64D3__) || defined(__AVR_ATxmega64D4__) || defined(__AVR_ATxmega64A1__) || defined(__AVR_ATxmega64A1U__) || defined(__AVR_ATxmega128A3__) || defined(__AVR_ATxmega128A3U__) || defined(__AVR_ATxmega128B1__) || defined(__AVR_ATxmega128B3__) || defined(__AVR_ATxmega128C3__) || defined(__AVR_ATxmega128D3__) || defined(__AVR_ATxmega128D4__) || defined(__AVR_ATxmega192A3__) || defined(__AVR_ATxmega192A3U__) || defined(__AVR_ATxmega192C3__) || defined(__AVR_ATxmega192D3__) || defined(__AVR_ATxmega256A3__) || defined(__AVR_ATxmega256A3U__) || defined(__AVR_ATxmega256A3B__) || defined(__AVR_ATxmega256A3BU__) || defined(__AVR_ATxmega256C3__) || defined(__AVR_ATxmega256D3__) || defined(__AVR_ATxmega384C3__) || defined(__AVR_ATxmega384D3__) || defined(__AVR_ATxmega128A1__) || defined(__AVR_ATxmega128A1U__) || defined(__AVR_ATxmega128A4U__) || defined(__AVR_AVR32SD20__) || defined(__AVR_AVR32SD28__) || defined(__AVR_AVR32SD32__) || defined(__AVR_AVR16LA14__) || defined(__AVR_AVR16LA20__) || defined(__AVR_AVR16LA28__) || defined(__AVR_AVR16LA32__) || defined(__AVR_AVR32LA14__) || defined(__AVR_AVR32LA20__) || defined(__AVR_AVR32LA28__) || defined(__AVR_AVR32LA32__) || defined(__AVR_AVR16DU14__) || defined(__AVR_AVR16DU20__) || defined(__AVR_AVR16DU28__) || defined(__AVR_AVR16DU32__) || defined(__AVR_AVR32DU14__) || defined(__AVR_AVR32DU20__) || defined(__AVR_AVR32DU28__) || defined(__AVR_AVR32DU32__) || defined(__AVR_AVR64DU28__) || defined(__AVR_AVR64DU32__) || defined(__AVR_AVR32DA28__) || defined(__AVR_AVR32DA32__) || defined(__AVR_AVR32DA48__) || defined(__AVR_AVR64DA28__) || defined(__AVR_AVR64DA32__) || defined(__AVR_AVR64DA48__) || defined(__AVR_AVR64DA64__) || defined(__AVR_AVR128DA28__) || defined(__AVR_AVR128DA32__) || defined(__AVR_AVR128DA48__) || defined(__AVR_AVR128DA64__) || defined(__AVR_AVR32DA28S__) || defined(__AVR_AVR32DA32S__) || defined(__AVR_AVR32DA48S__) || defined(__AVR_AVR64DA28S__) || defined(__AVR_AVR64DA32S__) || defined(__AVR_AVR64DA48S__) || defined(__AVR_AVR64DA64S__) || defined(__AVR_AVR128DA28S__) || defined(__AVR_AVR128DA32S__) || defined(__AVR_AVR128DA48S__) || defined(__AVR_AVR128DA64S__) || defined(__AVR_AVR32DB28__) || defined(__AVR_AVR32DB32__) || defined(__AVR_AVR32DB48__) || defined(__AVR_AVR64DB28__) || defined(__AVR_AVR64DB32__) || defined(__AVR_AVR64DB48__) || defined(__AVR_AVR64DB64__) || defined(__AVR_AVR128DB28__) || defined(__AVR_AVR128DB32__) || defined(__AVR_AVR128DB48__) || defined(__AVR_AVR128DB64__) || defined(__AVR_AVR16DD14__) || defined(__AVR_AVR16DD20__) || defined(__AVR_AVR16DD28__) || defined(__AVR_AVR16DD32__) || defined(__AVR_AVR32DD14__) || defined(__AVR_AVR32DD20__) || defined(__AVR_AVR32DD28__) || defined(__AVR_AVR32DD32__) || defined(__AVR_AVR64DD14__) || defined(__AVR_AVR64DD20__) || defined(__AVR_AVR64DD28__) || defined(__AVR_AVR64DD32__) || defined(__AVR_AVR16EA28__) || defined(__AVR_AVR16EA32__) || defined(__AVR_AVR16EA48__) || defined(__AVR_AVR16EB14__) || defined(__AVR_AVR16EB20__) || defined(__AVR_AVR16EB28__) || defined(__AVR_AVR16EB32__) || defined(__AVR_AVR32EA28__) || defined(__AVR_AVR32EA32__) || defined(__AVR_AVR32EA48__) || defined(__AVR_AVR32EB14__) || defined(__AVR_AVR32EB20__) || defined(__AVR_AVR32EB28__) || defined(__AVR_AVR32EB32__) || defined(__AVR_AVR64EA28__) || defined(__AVR_AVR64EA32__) || defined(__AVR_AVR64EA48__)
#define __AVR_IO_H_USES_BAUD__
#endif

#endif /* __BITS_DEVINFO_H_ */
