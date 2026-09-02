import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Donor Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Donor Behavior & Campaign Performance Dashboard")
st.markdown("Interactive analysis of donor contributions pre and post June 2026 campaign.")

# --- DATA GENERATION & SIMULATION ---
@st.cache_data
def load_data():
    np.random.seed(42)
    n_records = 5000
    dates = pd.date_range(start="2026-01-01", periods=n_records, freq="h")
    base_amounts = np.random.exponential(scale=50, size=n_records) + 5
    
    # Marketing channels allocation
    channels = np.random.choice(['Email', 'Social Media', 'Direct Mail'], size=n_records, p=[0.4, 0.3, 0.3])
    
    df = pd.DataFrame({
        'donor_id': np.random.randint(1000, 1500, size=n_records),
        'donation_date': dates,
        'amount': np.round(base_amounts, 2),
        'channel': channels
    })
    
    df['period'] = np.where(df['donation_date'] >= "2026-06-01", 'Post-Event', 'Pre-Event')
    
    # Differential post-campaign impact per channel
    df.loc[(df['period'] == 'Post-Event') & (df['channel'] == 'Social Media'), 'amount'] *= 1.6
    df.loc[(df['period'] == 'Post-Event') & (df['channel'] == 'Email'), 'amount'] *= 1.25

    # Truncate to start of month for time-series aggregation
    df['month_start'] = df['donation_date'].dt.to_period('M').dt.to_timestamp()
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")
selected_channel = st.sidebar.multiselect(
    "Select Marketing Channel:",
    options=df['channel'].unique(),
    default=df['channel'].unique()
)

filtered_df = df[df['channel'].isin(selected_channel)]

# --- KEY PERFORMANCE INDICATORS (KPIs) ---
col1, col2, col3, col4 = st.columns(4)

total_rev = filtered_df['amount'].sum()
avg_don = filtered_df['amount'].mean()
total_donors = filtered_df['donor_id'].nunique()
total_txs = len(filtered_df)

col1.metric("Total Revenue", f"${total_rev:,.2f}")
col2.metric("Average Donation", f"${avg_don:,.2f}")
col3.metric("Unique Donors", f"{total_donors:,}")
col4.metric("Total Transactions", f"{total_txs:,}")

st.divider()

# --- SECTION 1: OVERALL PERFORMANCE & TENDENCY ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Average Donation Size: Pre vs Post Event")
    avg_period = filtered_df.groupby('period')['amount'].mean().reset_index()
    fig_bar = px.bar(
        avg_period,
        x='period',
        y='amount',
        color='period',
        color_discrete_sequence=['#7209b7', '#4361ee'],
        labels={'amount': 'Average Donation ($)', 'period': 'Period'},
        category_orders={'period': ['Pre-Event', 'Post-Event']},
        text_auto='.2f'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    st.subheader("Monthly Trend: Average Donation Evolution")
    monthly_metrics = filtered_df.groupby('month_start')['amount'].mean().reset_index()
    fig_line = px.line(
        monthly_metrics,
        x='month_start',
        y='amount',
        markers=True,
        labels={'month_start': 'Date', 'amount': 'Avg Donation ($)'}
    )
    # Highlight campaign launch date
    fig_line.add_vline(
        x=pd.to_datetime("2026-06-01").timestamp() * 1000, 
        line_dash="dash", 
        line_color="red"
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# --- SECTION 2: DEEP CHANNEL PERFORMANCE ANALYSIS ---
st.subheader("Channel Effectiveness & Revenue Performance")

# Interactive tabs for distribution (%) vs absolute revenue ($)
tab1, tab2 = st.tabs(["Channel Share (%)", "Monthly Revenue Trend by Channel ($)"])

pre_df = filtered_df[filtered_df['period'] == 'Pre-Event']
post_df = filtered_df[filtered_df['period'] == 'Post-Event']

# TAB 1: RELATIVE CHANNEL CONTRIBUTION (%) PRE VS POST
with tab1:
    st.markdown("#### **Relative Contribution (%) Pre vs Post Campaign**")
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("##### **Pre-Event Share (%)**")
        fig_pie_pre = px.pie(
            pre_df,
            names='channel',
            values='amount',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie_pre, use_container_width=True)

    with col_p2:
        st.markdown("##### **Post-Event Share (%)**")
        fig_pie_post = px.pie(
            post_df,
            names='channel',
            values='amount',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie_post, use_container_width=True)

# TAB 2: MONTHLY REVENUE BY CHANNEL ($)
with tab2:
    st.markdown("#### **Monthly Total Revenue ($) per Channel**")
    
    # Monthly revenue aggregation per channel to eliminate timeframe bias
    monthly_channel_rev = filtered_df.groupby(['month_start', 'channel'])['amount'].sum().reset_index()
    
    fig_monthly_channel = px.bar(
        monthly_channel_rev,
        x='month_start',
        y='amount',
        color='channel',
        barmode='group',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        labels={'amount': 'Total Revenue ($)', 'month_start': 'Month', 'channel': 'Marketing Channel'},
        title="Monthly Revenue by Channel (Compare performance across months without time bias)"
    )
    
    # Highlight campaign launch date
    fig_monthly_channel.add_vline(
        x=pd.to_datetime("2026-06-01").timestamp() * 1000, 
        line_dash="dash", 
        line_color="red"
    )
    
    st.plotly_chart(fig_monthly_channel, use_container_width=True)
