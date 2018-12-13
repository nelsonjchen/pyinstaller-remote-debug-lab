# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None
ptvsd_data_files = collect_data_files('ptvsd', True)

a = Analysis(['main_debug_ptvsd.py'],
             pathex=['C:\\Users\\Nelson\\Documents\\pyinstaller-remote-debug-lab'],
             binaries=[],
             datas=ptvsd_data_files,
             hiddenimports=[''],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main_debug_ptvsd',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main_debug_ptvsd')
