# train_model.py
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


def generate_synthetic_data(num_samples=500):
    """Generates a synthetic dataset of phishing and benign URL features."""
    print("Generating synthetic dataset...")

    features = [
        'having_IP_Address', 'URL_Length', 'Shortining_Service',
        'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
        'having_Sub_Domain', 'SSLfinal_State', 'URL_of_Anchor', 'Links_in_tags',
        'SFH', 'Abnormal_URL', 'has_political_keyword'
    ]

    """num_phishing = num_samples // 2
    num_benign = num_samples - num_phishing"""

    num_benign = num_samples // 2
    num_phishing = num_samples - num_benign
    num_per_threat = num_phishing // 3

    """ phishing_data = {
        'having_IP_Address': np.random.choice([1, -1], num_phishing, p=[0.3, 0.7]),
        'URL_Length': np.random.choice([1, 0, -1], num_phishing, p=[0.5, 0.4, 0.1]),
        'Shortining_Service': np.random.choice([1, -1], num_phishing, p=[0.6, 0.4]),
        'having_At_Symbol': np.random.choice([1, -1], num_phishing, p=[0.4, 0.6]),
        'double_slash_redirecting': np.random.choice([1, -1], num_phishing, p=[0.3, 0.7]),
        'Prefix_Suffix': np.random.choice([1, -1], num_phishing, p=[0.7, 0.3]),
        'having_Sub_Domain': np.random.choice([1, 0, -1], num_phishing, p=[0.6, 0.3, 0.1]),
        'SSLfinal_State': np.random.choice([-1, 0, 1], num_phishing, p=[0.6, 0.3, 0.1]),
        'URL_of_Anchor': np.random.choice([-1, 0, 1], num_phishing, p=[0.5, 0.3, 0.2]),
        'Links_in_tags': np.random.choice([-1, 0, 1], num_phishing, p=[0.4, 0.4, 0.2]),
        'SFH': np.random.choice([-1, 0, 1], num_phishing, p=[0.7, 0.2, 0.1]),
        'Abnormal_URL': np.random.choice([1, -1], num_phishing, p=[0.5, 0.5])
    }"""



    state_sponsored = {
        'having_IP_Address': np.random.choice([1, -1], num_per_threat, p=[0.1, 0.9]),
        'URL_Length': np.random.choice([1, 0, -1], num_per_threat, p=[0.2, 0.5, 0.3]),
        'Shortining_Service': np.random.choice([1, -1], num_per_threat, p=[0.2, 0.8]),
        'having_At_Symbol': np.random.choice([1, -1], num_per_threat, p=[0.1, 0.9]),
        'double_slash_redirecting': np.random.choice([1, -1], num_per_threat, p=[0.1, 0.9]),
        'Prefix_Suffix': np.full(num_per_threat,1),
        'having_Sub_Domain': np.random.choice([1, 0, -1], num_per_threat, p=[0.2, 0.5, 0.3]),
        'SSLfinal_State': np.full(num_per_threat,1),
        'URL_of_Anchor': np.random.choice([-1, 0, 1], num_per_threat, p=[0.2, 0.3, 0.5]),
        'Links_in_tags': np.random.choice([-1, 0, 1], num_per_threat, p=[0.2, 0.3, 0.5]),
        'SFH': np.random.choice([-1, 0, 1], num_per_threat, p=[0.2, 0.3, 0.5]),
        'Abnormal_URL': np.random.choice([1, -1], num_per_threat, p=[0.3, 0.7]),
        'has_political_keyword': np.full(num_per_threat,-1)

    }


    organized_crime = {
        'having_IP_Address': np.full(num_per_threat,1),
        'URL_Length': np.random.choice([1, 0, -1], num_per_threat, p=[0.5, 0.4, 0.1]),
        'Shortining_Service': np.full(num_per_threat,1),
        'having_At_Symbol': np.random.choice([1, -1], num_per_threat, p=[0.4, 0.6]),
        'double_slash_redirecting': np.random.choice([1, -1], num_per_threat, p=[0.3, 0.7]),
        'Prefix_Suffix': np.random.choice([1, -1], num_per_threat, p=[0.7, 0.3]),
        'having_Sub_Domain': np.random.choice([1, 0, -1], num_per_threat, p=[0.6, 0.3, 0.1]),
        'SSLfinal_State': np.random.choice([-1, 0, 1], num_per_threat, p=[0.6, 0.3, 0.1]),
        'URL_of_Anchor': np.random.choice([-1, 0, 1], num_per_threat, p=[0.5, 0.3, 0.2]),
        'Links_in_tags': np.random.choice([-1, 0, 1], num_per_threat, p=[0.4, 0.4, 0.2]),
        'SFH': np.random.choice([-1, 0, 1], num_per_threat, p=[0.7, 0.2, 0.1]),
        'Abnormal_URL': np.full(num_per_threat,1),
        'has_political_keyword': np.full(num_per_threat,-1)

    }



    hacktivist = {
        'having_IP_Address': np.random.choice([1, -1], num_per_threat, p=[0.6, 0.4]),
        'URL_Length': np.random.choice([1, 0, -1], num_per_threat, p=[0.7, 0.2, 0.1]),
        'Shortining_Service': np.random.choice([1, -1], num_per_threat, p=[0.7, 0.3]),
        'having_At_Symbol': np.random.choice([1, -1], num_per_threat, p=[0.5, 0.5]),
        'double_slash_redirecting': np.random.choice([1, -1], num_per_threat, p=[0.5, 0.5]),
        'Prefix_Suffix': np.random.choice([1, -1], num_per_threat, p=[0.8, 0.2]),
        'having_Sub_Domain': np.random.choice([1, 0, -1], num_per_threat, p=[0.7, 0.2, 0.1]),
        'SSLfinal_State': np.random.choice([-1, 0, 1], num_per_threat, p=[0.7, 0.2, 0.1]),
        'URL_of_Anchor': np.random.choice([-1, 0, 1], num_per_threat, p=[0.6, 0.2, 0.2]),
        'Links_in_tags': np.random.choice([-1, 0, 1], num_per_threat, p=[0.6, 0.2, 0.2]),
        'SFH': np.random.choice([-1, 0, 1], num_per_threat, p=[0.8, 0.1, 0.1]),
        'Abnormal_URL': np.random.choice([1, -1], num_per_threat, p=[0.7, 0.3]),
        'has_political_keyword': np.full(num_per_threat,1)

    }


    benign_data = {
        'having_IP_Address': np.random.choice([1, -1], num_benign, p=[0.05, 0.95]),
        'URL_Length': np.random.choice([1, 0, -1], num_benign, p=[0.1, 0.6, 0.3]),
        'Shortining_Service': np.random.choice([1, -1], num_benign, p=[0.1, 0.9]),
        'having_At_Symbol': np.random.choice([1, -1], num_benign, p=[0.05, 0.95]),
        'double_slash_redirecting': np.random.choice([1, -1], num_benign, p=[0.05, 0.95]),
        'Prefix_Suffix': np.random.choice([1, -1], num_benign, p=[0.1, 0.9]),
        'having_Sub_Domain': np.random.choice([1, 0, -1], num_benign, p=[0.1, 0.4, 0.5]),
        'SSLfinal_State': np.random.choice([-1, 0, 1], num_benign, p=[0.05, 0.15, 0.8]),
        'URL_of_Anchor': np.random.choice([-1, 0, 1], num_benign, p=[0.1, 0.2, 0.7]),
        'Links_in_tags': np.random.choice([-1, 0, 1], num_benign, p=[0.1, 0.2, 0.7]),
        'SFH': np.random.choice([-1, 0, 1], num_benign, p=[0.1, 0.1, 0.8]),
        'Abnormal_URL': np.random.choice([1, -1], num_benign, p=[0.1, 0.9]),
        'has_political_keyword': np.full(num_benign,-1)
    }

    """ df_phishing = pd.DataFrame(phishing_data)
    df_benign = pd.DataFrame(benign_data)

    df_phishing['label'] = 1
    df_benign['label'] = 0

    final_df = pd.concat([df_phishing, df_benign], ignore_index=True)
    return final_df.sample(frac=1).reset_index(drop=True)"""


    df_state = pd.DataFrame(state_sponsored)
    df_state["label"] = 1
    df_state["threat_actor"] = "state_sponsored"

    df_crime = pd.DataFrame(organized_crime)
    df_crime["label"] = 1
    df_crime["threat_actor"] = "organized_crime"

    df_hacktivist = pd.DataFrame(hacktivist)
    df_hacktivist["label"] = 1
    df_hacktivist["threat_actor"] = "hacktivist"

    df_benign = pd.DataFrame(benign_data)
    df_benign["label"] = 0
    df_benign["threat_actor"] = "none"


    final_df = pd.concat([df_state, df_crime, df_hacktivist, df_benign], ignore_index=True)
    return final_df.sample(frac=1).reset_index(drop=True)




def train(): 
    from pycaret.classification import setup, compare_models, finalize_model, save_model, plot_model

    model_path = 'models/phishing_url_detector'
    plot_path = 'models/feature_importance.png'

    if os.path.exists(model_path + '.pkl'):
        print("Model and plot already exist. Skipping training.")
        return

    data = generate_synthetic_data()
    os.makedirs('data', exist_ok=True)
    data.to_csv('data/phishing_synthetic.csv', index=False)

    print("Initializing PyCaret Setup...")
    s = setup(data=data.drop(columns=["threat_actor"]), target='label', session_id=42, verbose=False)

    print("Comparing models...")
    best_model = compare_models(n_select=1, include=['rf', 'et', 'lightgbm'])

    print("Finalizing model...")
    final_model = finalize_model(best_model)

    # NEW: Plot feature importance and save it to a file
    print("Saving feature importance plot...")
    os.makedirs('models', exist_ok=True)
    plot_model(final_model, plot='feature', save=True)
    # PyCaret saves it as 'Feature Importance.png', let's rename it
    os.rename('Feature Importance.png', plot_path)

    print("Saving model...")
    save_model(final_model, model_path)
    print(f"Model and plot saved successfully.")


def cluster():
    from pycaret.clustering import setup, create_model, assign_model, plot_model, save_model

    cluster_path = 'models/threat_actor_profiler'
    cluster_plot_path = 'models/Silhouette_plot.png'

    if os.path.exists(cluster_path + '.pkl'):
        print("Model and plot already exist. Skipping training.")
        return

    phishing_df = generate_synthetic_data(num_samples=1000)
    data_c = phishing_df[phishing_df["label"] == 1].copy()
    os.makedirs('data', exist_ok=True)
    data_c.to_csv('data/clustering_synthetic.csv', index=False)


    print("Initializing PyCaret Setup...")
    cs = setup(data=data_c.drop(columns=["label", "threat_actor"]), session_id=42, normalize=True, verbose=False)

    print("Creating model...")
    kmeans = create_model("kmeans", num_clusters=3)

    # plot 
    print("Saving plot...")
    os.makedirs("models", exist_ok=True)
    plot_model(kmeans, plot="silhouette", save=True)
    os.rename('Silhouette Plot.png', cluster_plot_path)

    print("Asigning clusters...")
    clusters = assign_model(kmeans)

    clusterings = data_c.copy()
    clusterings["Cluster"] = clusters["Cluster"].values
    print(pd.crosstab(clusterings["Cluster"], clusterings["threat_actor"]))

    print("Saving model...")
    save_model(kmeans, cluster_path)
    print(f"Model and plot saved successfully.")

if __name__ == "__main__":
    train()
    cluster()