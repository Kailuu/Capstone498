# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Interface.py'],
             pathex=['C:\\Users\\Kailuu\\desktop\\capstone498\\local functions'],
             binaries=[],
             datas=[('*.py', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [ ('wheelofgod.png', 'downloadphoto.png', 'untitled_artwork.png')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Interface',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )