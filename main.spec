# To generate .exe and .app
#
# To generate, do :
#    Windows : pyinstaller --onefile main_local.spec
#
# Other options : --windowed
#
# Check pyinstaller for full documentation
#
# https://stackoverflow.com/questions/28033003/pyinstaller-with-pygame/36456473#36456473
#

block_cipher = None

addedFiles = [ ('tiles_map', 'tiles_map'), ('music_pcm','music_pcm'), ('img', 'img'), ('fonts', 'fonts') ]

a = Analysis(['main.py'],
             pathex=['LDEngine'],
             binaries=None,
             datas=addedFiles,
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mainWindows.exe',
          debug=False,
          strip=False,
          upx=True,
          console=False )
