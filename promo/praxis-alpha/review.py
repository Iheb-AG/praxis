"""Run the unchanged skill review with an installed-font path for Arch Linux."""
import importlib.util
import os
from pathlib import Path

skill=Path(os.environ.get('MOTIONMAXXING_SKILL',Path.home()/'.codex/skills/motionmaxxing'))
spec=importlib.util.spec_from_file_location('motionmaxxing_look',skill/'scripts/look.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# The upstream defaults cover macOS and Debian paths. Gates remain unchanged.
module.FONTS += ['/usr/share/fonts/TTF/DejaVuSansMono.ttf',str(Path(__file__).resolve().parent/'runtime/hero3d/fonts/Inter-Bold-Latin.ttf')]
if __name__=='__main__':
    module.main()
