"""
Streamlit Dashboard - Standalone Distribution Example

This dashboard demonstrates how to create a Streamlit application that can be
packaged as a standalone executable with bundled data for offline use.
"""

import sys
import os
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px


# Get the directory where the script is located
# This ensures data files are found when running as standalone executable
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    application_path = os.path.dirname(sys.executable)
else:
    # Running as script
    application_path = os.path.dirname(os.path.abspath(__file__))


def load_data():
    """Load the sample data from the bundled CSV file."""
    data_path = os.path.join(application_path, 'sample_data.csv')
    
    # Check if file exists
    if not os.path.exists(data_path):
        st.error(f"Data file not found at: {data_path}")
        st.info("Creating sample data...")
        # Create sample data if not found
        df = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
            'Value': [50 + i * 0.5 + (i % 10) * 2 for i in range(100)],
            'Category': ['A' if i % 3 == 0 else 'B' if i % 3 == 1 else 'C' for i in range(100)]
        })
        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)
        df['Date'] = pd.to_datetime(df['Date'])
    
    return df


def main():
    """Main dashboard application."""
    
    # Page configuration
    st.set_page_config(
        page_title="Data Journal Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title and description
    st.title("📊 Data Journal Dashboard")
    st.markdown("""
    ### Standalone Streamlit Dashboard
    
    This dashboard demonstrates:
    - 📦 Bundled data for offline use
    - 🖥️ Standalone executable distribution
    - 📈 Interactive visualizations
    - 🎨 Modern UI with Streamlit
    """)
    
    # Load data
    with st.spinner("Loading data..."):
        df = load_data()
    
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Category filter
    categories = df['Category'].unique().tolist()
    selected_categories = st.sidebar.multiselect(
        "Select Categories",
        options=categories,
        default=categories
    )
    
    # Date range filter
    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()
    
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Apply filters
    filtered_df = df[df['Category'].isin(selected_categories)]
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df['Date'].dt.date >= start_date) & 
            (filtered_df['Date'].dt.date <= end_date)
        ]
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Records",
            value=len(filtered_df),
            delta=len(filtered_df) - len(df)
        )
    
    with col2:
        st.metric(
            label="Average Value",
            value=f"{filtered_df['Value'].mean():.2f}",
            delta=f"{filtered_df['Value'].mean() - df['Value'].mean():.2f}"
        )
    
    with col3:
        st.metric(
            label="Max Value",
            value=f"{filtered_df['Value'].max():.2f}"
        )
    
    with col4:
        st.metric(
            label="Min Value",
            value=f"{filtered_df['Value'].min():.2f}"
        )
    
    # Visualizations
    st.header("📈 Visualizations")
    
    # Time series chart
    st.subheader("Value Over Time")
    fig1 = px.line(
        filtered_df,
        x='Date',
        y='Value',
        color='Category',
        title='Value Trends by Category'
    )
    fig1.update_layout(hovermode='x unified')
    st.plotly_chart(fig1, use_container_width=True)
    
    # Distribution chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Value Distribution")
        fig2 = px.histogram(
            filtered_df,
            x='Value',
            color='Category',
            nbins=20,
            title='Distribution of Values'
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        st.subheader("Category Breakdown")
        category_counts = filtered_df['Category'].value_counts()
        fig3 = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title='Records by Category'
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    # Data table
    st.header("📋 Data Table")
    st.dataframe(
        filtered_df.sort_values('Date', ascending=False),
        use_container_width=True,
        height=300
    )
    
    # Export functionality
    st.header("💾 Export Data")
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv"
    )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Note:** This dashboard runs completely offline with bundled data.
    No internet connection required after installation!
    """)


if __name__ == "__main__":
    main()
