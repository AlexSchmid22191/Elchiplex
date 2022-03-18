# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\Elchiplex.py'],
             pathex=['C:\\Users\\Alex\\PycharmProjects\\Omniplex'],
             binaries=[],
             datas=[('src/Interface/style.qss', 'Interface'),
                    ('src/Interface/Icons', 'Interface/Icons'),
                     ('src/Interface/Fonts', 'Interface/Fonts')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Elchiplex',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='src/Interface/Icons/Logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ElchiPlex')
