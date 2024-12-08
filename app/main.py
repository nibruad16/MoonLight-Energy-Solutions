import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes  

def load_data(dataset_name):
    if dataset_name == "Benin":
        data = pd.read_csv('/home/nibruad/Documents/Data Sets/data (1)/data/benin-malanville.csv')
    elif dataset_name == "Sierra Leone":
        data = pd.read_csv('/home/nibruad/Documents/Data Sets/data (1)/data/sierraleone-bumbuna.csv')
    elif dataset_name == "Togo":
        data = pd.read_csv('/home/nibruad/Documents/Data Sets/data (1)/data/togo-dapaong_qc.csv')
    else:
        data = None
    return data

def create_visualizations(data, visualization_type, x_col=None, y_col=None):
    if visualization_type == "Correlation Heatmap":
       
        numeric_data = data.select_dtypes(include=[float, int])
        
        fig, ax = plt.subplots(figsize=(12, 10)) 
        sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", ax=ax, annot_kws={"size": 10}, fmt=".2f")  # Adjust font size and format
        plt.xticks(rotation=45, ha='right')  
        plt.yticks(rotation=0)  
        st.pyplot(fig)
        st.write(
            "**Correlation Heatmap:** This visualization shows the correlation between different variables in the dataset. "
            "Positive correlations are indicated by warmer colors, while negative correlations are indicated by cooler colors."
        )

    elif visualization_type == "Time-series Analysis":
        fig, ax = plt.subplots()
        ax.plot(data["Timestamp"], data[x_col])
        ax.set_xlabel("Timestamp")
        ax.set_ylabel(x_col)
        st.pyplot(fig)
        st.write(f"**Time-series Analysis:** This plot shows the trend of {x_col} over time.")

    elif visualization_type == "Wind and Solar Speed Analysis":
        # Wind Rose
        ax = WindroseAxes.from_ax()
        ax.bar(data["WD"], data["WS"], normed=True, opening=0.8, edgecolor="white")
        ax.set_legend()
        st.pyplot(plt.gcf())
        st.write(
            "**Wind Rose:** This visualization shows the distribution of wind speed and direction. "
            "The length of each bar represents the frequency of wind blowing from that direction, "
            "and the color indicates the wind speed."
        )

        
        fig, ax = plt.subplots()
        ax.plot(data["Timestamp"], data["GHI"])
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("GHI (Solar Speed)")
        st.pyplot(fig)
        st.write("**Solar Speed:** This plot shows the variation of solar speed (represented by GHI) over time.")

    elif visualization_type == "Outlier Detection":
        fig, ax = plt.subplots()
        sns.boxplot(x=data[x_col], ax=ax)
        st.pyplot(fig)
        st.write(
            f"**Outlier Detection:** This box plot helps identify potential outliers in the {x_col} data. "
            "Points outside the whiskers of the box plot are considered outliers."
        )

def main():
    st.title("Solar Radiation Data Analysis Dashboard")

    dataset_names = ["Benin", "Sierra Leone", "Togo"]
    selected_datasets = st.sidebar.multiselect("Select Datasets", dataset_names, default=dataset_names)

    visualization_type = st.sidebar.selectbox(
        "Select Visualization",
        [
            "Correlation Heatmap",
            "Time-series Analysis",
            "Wind and Solar Speed Analysis",
            "Outlier Detection",
        ],
    )

    x_col = None  
    y_col = None

    if visualization_type == "Correlation Heatmap":
        pass  
    elif visualization_type == "Time-series Analysis":
        x_col = st.sidebar.selectbox("Select Variable", ["GHI", "DNI", "DHI", "Tamb", "WS"])
    elif visualization_type == "Wind and Solar Speed Analysis":
        pass  
    elif visualization_type == "Outlier Detection":
        x_col = st.sidebar.selectbox("Select Variable", ["GHI", "DNI", "DHI", "Tamb", "WS"])

    for dataset_name in selected_datasets:
        st.subheader(f"Visualizations for {dataset_name}")
        data = load_data(dataset_name)
        if data is not None:
            
            if 'Timestamp' in data.columns:
                data['Timestamp'] = pd.to_datetime(data['Timestamp'])
            create_visualizations(data, visualization_type, x_col, y_col=None)    
        else:
            st.write(f"Could not load data for {dataset_name}. Please check the file path.")

if __name__ == "__main__":
    main()
