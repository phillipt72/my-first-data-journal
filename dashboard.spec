# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Specification File for Streamlit Dashboard

This file configures how PyInstaller packages the Streamlit dashboard
into a standalone executable with all dependencies and data bundled.

Usage:
    pyinstaller dashboard.spec

The resulting executable will be in the 'dist' folder.
"""

import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import streamlit
import plotly

# Collect Streamlit data files and submodules
streamlit_datas = collect_data_files('streamlit')
streamlit_hiddenimports = collect_submodules('streamlit')

# Collect Plotly data files
plotly_datas = collect_data_files('plotly')

block_cipher = None

a = Analysis(
    ['dashboard.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Bundle the sample data
        ('sample_data.csv', '.'),
        # Bundle Streamlit configuration
        ('.streamlit/config.toml', '.streamlit'),
        # Bundle Streamlit static files
        *streamlit_datas,
        # Bundle Plotly data
        *plotly_datas,
    ],
    hiddenimports=[
        *streamlit_hiddenimports,
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit.components.v1',
        'plotly',
        'plotly.express',
        'pandas',
        'numpy',
        'pyarrow',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='DataJournalDashboard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Keep console visible for Streamlit output
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add your own icon file here if desired
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DataJournalDashboard',
)
