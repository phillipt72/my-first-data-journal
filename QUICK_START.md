# Quick Start Guide - Standalone Streamlit Dashboard

## For Developers - Building the Executable

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Test the dashboard locally**:
   ```bash
   streamlit run dashboard.py
   ```
   Or use the runner scripts:
   - Windows: `run_dashboard.bat`
   - Linux/macOS: `./run_dashboard.sh`

3. **Build the standalone executable**:
   - Windows: Run `build_standalone.bat`
   - Linux/macOS: Run `./build_standalone.sh`

4. **Find your executable**:
   - Location: `dist/DataJournalDashboard/`
   - The folder contains everything needed to run

5. **Distribute**:
   - Compress the `DataJournalDashboard` folder
   - Share with your users

---

## For End Users - Running the Dashboard

### No Python? No Problem!

1. **Extract** the compressed file you received
2. **Navigate** to the `DataJournalDashboard` folder
3. **Run** the executable:
   - Windows: Double-click `DataJournalDashboard.exe`
   - Linux/macOS: Run `./DataJournalDashboard` in terminal

The dashboard will automatically open in your web browser!

### Features
- ✅ Works completely offline
- ✅ No installation required
- ✅ Interactive charts and filters
- ✅ Export filtered data
- ✅ All data included

### Requirements
- Windows 10+, macOS 10.14+, or Linux
- Web browser (Chrome, Firefox, Edge, Safari)
- No internet connection needed

---

## Troubleshooting

### Dashboard won't start
- Check if port 8501 is available
- Try closing other applications
- Check antivirus isn't blocking the executable

### Browser doesn't open
- Manually open: `http://localhost:8501`
- Try a different browser

### "Data file not found" error
- Ensure `sample_data.csv` is in the same folder as the executable
- Re-extract the compressed file

---

## Need More Help?

See the full documentation: [README_STREAMLIT_STANDALONE.md](README_STREAMLIT_STANDALONE.md)
