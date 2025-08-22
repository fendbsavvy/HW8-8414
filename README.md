# Cognitive SOAR - From Prediction to Attribution

## Project Overview
The SOAR was developed to extend the original application by enhancing it from a simple binary classification URL detector to add threat actor attribution.

- **Classification**: First a binary classification model detects whether a URL is **Malicious** or **Benign**.  
- **Attribution**: If the URL is malicious, attribute it to one of three threat actors: *State-Sponsored*, *Organized Cybercrime*, or *Hacktivist*  

---

## Technology Stack
- **Python**
- **Streamlit** (UI)
- **PyCaret** (ML framework)
- **Docker** (containerization)

---

## Dual-Model Architecture


1. **Classification Model** (`phishing_url_detector`)  
   - Built with PyCaret’s classification module.  
   - Predicts whether the URL is **MALICIOUS** or **BENIGN**.  

2. **Clustering Model** (`threat_actor_profiler`)  
   - Built with PyCaret’s clustering module.  
   - Used only if the URL is malicious.  
   - Groups malicious URLs into 3 clusters, representing three threat actor profile:  
     - **Cluster 0 → Hacktivist**  
       - Hacktivists engage in hacking activities for political or social reasons. Often target high-profile organizations in order to bring attention to their   	 cause. 
       - URL contains political keywords
     - **Cluster 1 → Organized Crime**
       - Motivated by financial gain and typically target financial institutions or businesses. 
       - URLs having IP addresses, uses shortening services, having abnormal URL  
     - **Cluster 2 → State-Sponsored**  
       - Motivated by political gain and typically have the resources and skills to carry out sophisticated attacks. 
       -  Uses Prefix Suffix, valid SSL cert

---

**Usage Instructions**
    (train_model.py)
    1. Train classification model → saved as `phishing_url_detector`.  
    2. Train clustering model → saved as `threat_actor_profiler`.
    3. Access web application http://<IP `or localhost`>:8501.  
    4. Select the characteristics of the suspicious URL from the side menu.
    5. Select Gemini as GenAI Provide
    6. Click "Analyze & Initiate Response" button
    7. Allow the model to complete analysis, view results in the analysis tabs.






