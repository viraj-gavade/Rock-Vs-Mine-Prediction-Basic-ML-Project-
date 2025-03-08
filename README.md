# 🚀 Rock vs Mine Detection ML Project

This is my first **Machine Learning** project where I built a **Rock vs Mine Detection System** using **Logistic Regression**. The model predicts whether an object is a **rock** or a **mine** based on sonar data.

## 📌 Features
- ✅ Uses **Sonar dataset** for classification
- ✅ Implements **Logistic Regression** algorithm
- ✅ Achieves **high accuracy on test data**
- ✅ Simple **predictive system** for underwater object detection

## 📊 Dataset
The dataset contains **60 numerical features** extracted from sonar signals bounced off different objects.
- **R** → Represents **Rock**
- **M** → Represents **Mine**

The dataset is split into:
- [Training set](https://raw.githubusercontent.com/viraj-gavade/rock-vs-mine/main/sonar_train.csv)
- [Test set](https://raw.githubusercontent.com/viraj-gavade/rock-vs-mine/main/sonar_test.csv)

## 🔧 Installation & Setup
To run this project:

1. Clone the repository:
   ```bash
   git clone https://github.com/viraj-gavade/rock-vs-mine.git
   cd rock-vs-mine
   ```

2. Install dependencies:
   ```bash
   pip install numpy pandas scikit-learn matplotlib jupyter
   ```

3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Rock_vs_Mine_Detection.ipynb
   ```

## 🏆 Results
- **Training Accuracy**: 83.5%
- **Test Accuracy**: 76.2%

## 📸 Sample Prediction
If the input is:
```python
input_data = (0.0200, 0.0371, 0.0428, 0.0207, 0.0954, 0.0986, 0.1539, 0.1601, 0.3109, 0.2111, 0.1609, 0.1582, 0.2238, 0.0645, 0.0660, 0.2273, 0.3100, 0.2999, 0.5078, 0.4797, 0.5783, 0.5071, 0.4328, 0.5550, 0.6711, 0.6415, 0.7104, 0.8080, 0.6791, 0.3857, 0.1307, 0.2604, 0.5121, 0.7547, 0.8537, 0.8507, 0.6692, 0.6097, 0.4943, 0.2744, 0.0510, 0.2834, 0.2825, 0.4256, 0.2641, 0.1386, 0.1051, 0.1343, 0.0383, 0.0324, 0.0232, 0.0027, 0.0065, 0.0159, 0.0072, 0.0167, 0.0180, 0.0084, 0.0090, 0.0032)
```

The model outputs:
```
The Object is A Rock!
```

## 🌟 Future Improvements
- Try **different ML algorithms** (Random Forest, SVM, Neural Networks)
- Implement **hyperparameter tuning** to improve accuracy
- Deploy the model as a **web app** using Flask or Streamlit
- Add data visualization for better understanding of feature importance
- Implement cross-validation for more reliable performance metrics

## 💡 Learnings
- ✔ Understanding of **data preprocessing**
- ✔ Working with **pandas & NumPy**
- ✔ Implementing **train-test split & logistic regression**
- ✔ Model evaluation techniques

## 🛠️ Project Structure
```
rock-vs-mine/
├── Rock_vs_Mine_Detection.ipynb
├── sonar_train.csv
├── sonar_test.csv
├── README.md
└── requirements.txt
```

## 📌 Author
**Viraj Gavade**


⭐ If you find this project helpful, please consider giving it a star on GitHub! ⭐
