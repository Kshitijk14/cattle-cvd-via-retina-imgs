# Image Classification for Cattle CVD Detection via Retina Images

This project focuses on identifying cardiovascular disease (CVD) in cattle using image classification techniques applied to retina images. The workflow combines deep learning, advanced preprocessing methods, and model interpretability techniques to address the problem.

## Features

- **Retina image preprocessing**: Enhancements include green channel extraction, CLAHE, vessel detection, and enhancement.
- **Deep learning-based classification**: Models tried include CNN, ResNet50v2, VGG16, and ResNet101 (final choice).
- **Model interpretability**: Grad-CAM visualizations to explain predictions.
- **Pipeline management**: Implemented using DVC.
- **Interactive application**: Flask-based interface for predictions.

## Challenges and Issues Faced

1. **Data imbalance in predictions**:
   - Despite a balanced dataset, the model exhibits drastic disparities in precision, recall, and F1 score between the two classes. One class often has no samples predicted correctly. This issue remains unresolved.

2. **Data preprocessing complexities**:
   - Transforming retina images to extract relevant features for model input required iterative tuning of preprocessing techniques (e.g., vessel enhancement and green channel extraction).

3. **Model selection**:
   - Multiple architectures were trialed, requiring extensive hyperparameter tuning to achieve optimal performance.

4. **Interpretability**:
   - Ensuring model predictions were explainable using Grad-CAM posed challenges in handling edge cases and incorrect predictions.

## Project Structure

The project follows a modular design:

1. **notebooks/**:
   - Trials and experiments are logged in `trials_v1` and `trials_v2` notebooks.
2. **src/cnnClassifier/**:
   - Contains modules for training, evaluation, and prediction pipelines.
3. **main.py**:
   - Main entry point for running the pipeline and predictions.
4. **config.yaml**:
   - Configuration for data, model, and preprocessing settings.
5. **params.yaml**:
   - Model hyperparameters and training parameters.
6. **dvc.yaml**:
   - DVC pipeline configuration.

## Preprocessing Workflow

1. **Original Retina Image** →
2. **Green Channel Extraction** →
3. **CLAHE (Contrast Limited Adaptive Histogram Equalization)** →
4. **Vessel Detection** →
5. **Image Enhancement** →
6. **Input to Deep Learning Model**

## Models Tried

1. CNN
2. ResNet50v2
3. VGG16
4. ResNet101 (**Final Model**)

## Installation and Setup

1. Create and Activate virtual environment:
   ```bash
   python -m venev eve
   .\env\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize DVC:
   ```bash
   dvc init
   ```

## Usage

### Training and Monitoring

1. Start TensorBoard for monitoring:
   ```bash
   tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
   ```

2. Run the pipeline using DVC:
   ```bash
   dvc repro
   ```

3. Visualize pipeline dependencies:
   ```bash
   dvc dag
   ```

### Running the Application

#### Local Development

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Access the application:
   - Main interface: `http://127.0.0.1:8080/`
   - Prediction endpoint: `http://127.0.0.1:8080/predict/`

#### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t cattle-cvd-classifier .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 cattle-cvd-classifier
   ```

## Model Interpretability

- Grad-CAM visualizations are implemented to provide insights into model predictions by highlighting the areas in retina images that influence the decision-making process.

## Contributing

Feel free to open issues and pull requests for model improvements, bug fixes, or additional features.

---

### Note
- Documented challenges, preprocessing methods, and pipeline creation steps are detailed to facilitate reproducibility.
- Contributions are welcome to address the unresolved class imbalance issue.
