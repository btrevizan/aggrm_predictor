# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['/Users/bernardo/Documents/codelab/aggrm_predictor'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy.core._dtype_ctypes',
                            'sklearn.utils._cython_blas',
                            'sklearn.tree',
                            'sklearn.neighbors.typedefs',
                            'sklearn.neighbors.quad_tree',
                            'sklearn.tree._utils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += Tree('regressors', prefix='regressors')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

app = BUNDLE(exe,
             name='AggrM Predictor.app',
             icon='img/icon.ico',
             bundle_identifier='com.bernardo.research.aggr_method.app',
             info_plist={
                'NSHighResolutionCapable': 'True'
             },)
