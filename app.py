import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dictionary for image-based identification
dairy_data = {
    "milk.jpg": {
        "name": "Milk",
        "nutrients": "Calories: ~42 kcal | Protein: 3.4g | Fat: 1g (skim), 3.3g (whole) | Carbohydrates: 5g | Calcium: 120mg | Vitamin D: Present | Vitamin B12: 0.4µg | Phosphorus: 100mg",
        "benefits": "Strong bones, muscle growth, better immunity."
    },
    "curd2.jpg": {
        "name": "Curd (Yogurt)",
        "nutrients": "Calories: ~60 kcal | Protein: 3.5g | Fat: 3g | Carbohydrates: 4-5g | Calcium: 80-100mg | Probiotics: Yes! | Vitamin B12: 0.3µg | Phosphorus: 90mg",
        "benefits": "Aids digestion, boosts immunity, good for gut health."
    },
    "butter1.jpg": {
        "name": "Butter",
        "nutrients": "Calories: ~717 kcal | Protein: 0.85g | Fat: 81g | Carbohydrates: 0g | Calcium: 24mg | Vitamin A: 684µg | Vitamin D: Small | Cholesterol: 215mg",
        "benefits": "Provides energy, improves skin health, but should be consumed in moderation."
    },
    "cheese2.jpg": {
        "name": "Cheese",
        "nutrients": "Calories: ~350-400 kcal | Protein: 25g | Fat: 30g | Carbohydrates: 1-3g | Calcium: 700mg | Vitamin B12: 1.5µg | Phosphorus: 500mg | Sodium: High (~600mg)",
        "benefits": "Strengthens bones, high in protein, but should be eaten in moderation due to high sodium."
    },
    "paneer3.jpg": {
        "name": "Paneer",
        "nutrients": "Calories: ~265 kcal | Protein: 18g | Fat: 20g | Carbohydrates: 1-2g | Calcium: 200mg | Vitamin B12: 0.7µg | Phosphorus: 120mg",
        "benefits": "Great for muscle growth, weight loss (if eaten in moderation), and bone health."
    }
}

# Function to clean and validate data
def clean_data(df):
    required_columns = {'Product Name', 'Storage Temperature (°C)', 'pH Level', 'Bacterial Count (CFU/mL)'}
    if not required_columns.issubset(df.columns):
        st.error(f"❌ Error: Required columns missing. Ensure dataset has {required_columns}.")
        return None
    df = df[['Product Name', 'Storage Temperature (°C)', 'pH Level', 'Bacterial Count (CFU/mL)']].copy()
    df.dropna(inplace=True)
    return df

# Function for EDA visualization
def plot_data(df):
    st.subheader("📊 Data Distribution")
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    sns.histplot(df['Storage Temperature (°C)'], bins=10, kde=True, ax=axes[0])
    axes[0].set_title("Temperature Distribution")

    sns.histplot(df['pH Level'], bins=10, kde=True, ax=axes[1])
    axes[1].set_title("pH Level Distribution")

    sns.histplot(df['Bacterial Count (CFU/mL)'], bins=10, kde=True, ax=axes[2])
    axes[2].set_title("Bacterial Count Distribution")

    st.pyplot(fig)

# Spoilage Prediction
def predict_spoilage(temp, pH, bacteria):
    if temp > 7 or pH < 4.5 or bacteria > 20000:
        return "⚠️ High Spoilage Risk!"
    return "✅ Product is Safe."

# Main App
def main():
    st.set_page_config(page_title="VMART Dairy Analyzer", page_icon="🥛", layout="centered")

    menu = ["🏠 Home", "🔍 Product Identifier", "🧪 Spoilage Prediction"]
    choice = st.sidebar.selectbox("Choose a Page", menu)

    if choice == "🏠 Home":
        st.title("VMART Dairy Analyzer")
        st.markdown("Analyze spoilage and identify dairy products using image recognition!")
        st.markdown("<br><br><h4>POWERED BY :- AKASH.K, KEVIN KATTAKAYAM, YASH.N.T</h4>", unsafe_allow_html=True)

    elif choice == "🔍 Product Identifier":
        st.title("🔍 Identify Dairy Product from Image")
        uploaded_img = st.file_uploader("📷 Upload Dairy Product Image", type=["jpg", "jpeg", "png"])
        if uploaded_img:
            file_name = uploaded_img.name.lower()
            st.image(uploaded_img, width=300)

            if file_name in dairy_data:
                data = dairy_data[file_name]
                st.success(f"✅ It's {data['name']}!")
                st.markdown(f"### 🧪 Nutrients (For 100 Gram):\n{data['nutrients'].replace('|', '<br>')}", unsafe_allow_html=True)
                st.markdown(f"### 🛑 Health Benefits:\n{data['benefits']}")
            else:
                st.error("❌ Unknown Dairy Product!")

    elif choice == "🧪 Spoilage Prediction":
        st.title("🥛 Dairy Product Spoilage Prediction")
        uploaded_file = st.file_uploader("📂 Upload your dataset (.csv)", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")

            cleaned_df = clean_data(df)
            if cleaned_df is not None:
                st.subheader("📊 Dataset Overview")
                st.write(cleaned_df.head())

                product_options = cleaned_df['Product Name'].unique().tolist()
                selected_product = st.selectbox("🧃 Which dairy product is this?", product_options)
                st.write(f"📝 You selected: **{selected_product}**")

                plot_data(cleaned_df)

                st.subheader("🧪 Spoilage Prediction")
                temp = st.slider("Temperature (°C)", float(cleaned_df['Storage Temperature (°C)'].min()), float(cleaned_df['Storage Temperature (°C)'].max()), 5.0)
                pH = st.slider("pH Level", float(cleaned_df['pH Level'].min()), float(cleaned_df['pH Level'].max()), 5.5)
                bacteria = st.number_input("Bacterial Count", int(cleaned_df['Bacterial Count (CFU/mL)'].min()), int(cleaned_df['Bacterial Count (CFU/mL)'].max()), 10000)

                if st.button("Predict"):
                    result = predict_spoilage(temp, pH, bacteria)
                    st.subheader(result)

if __name__ == "__main__":
    main()
