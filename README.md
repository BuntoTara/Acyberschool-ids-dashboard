# 🛡️AcyberSchool Capstone: Intrusion Detection System Dashboard

## 🎓 Student: Steve Keyai Saagsi  
**Institution:** AcyberSchool  
**Program:** Cybersecurity  
**Project Type:** Final Capstone Project

---

##  Project Overview

This project implements a machine learning–based **Intrusion Detection System (IDS)** using a Random Forest classifier, trained on the **ISCX 2017 dataset**. It achieves **99.97% accuracy** in detecting malicious network traffic.

An interactive **Streamlit dashboard** allows users to:
-  Upload network traffic logs (CSV/XLSX)
- 🛡️ un automated threat detection using a trained model
-  Visualize traffic anomalies
-  Generate incident summary reports

---

## Technologies Used

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python 3     | Core programming language        |
| Streamlit    | Dashboard UI                     |
| Scikit-learn | Machine learning model (Random Forest) |
| Pandas       | Data processing                  |
| Seaborn      | Visualization                    |
| Jinja2       | Report templating                |
| Joblib       | Model loading                    |
| Docker       | Containerized deployment         |
| Jenkins      | Continuous Integration / Delivery |

---

##  Project Structure

---

##  Dataset

- **Dataset**: ISCX 2017 Intrusion Detection Evaluation
- Subsets used:
  - `Monday-WorkingHours.pcap_ISCX.csv` – normal traffic
  - `Wednesday-workingHours.pcap_ISCX.csv` – mixed traffic (attacks)

---

##  How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/BuntoTara/Acyberschool-ids-dashboard.git
   cd Acyberschool-ids-dashboard
