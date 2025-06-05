# Age_Detection_CNN

Recently, many applications from biometrics, to entertainment use the information extracted from face images that contain information about age, gender, ethnic background, and emotional state. Automatic age estimation from facial images is one of the popular and challenging tasks that have different fields of applications such as controlling the content of the watched media depending on the customer's age.

So facial feature analysis has been a topic of interest mainly due to its applicability and Deep Learning techniques are now making it possible for face analysis to be not just a dream but a reality. This simple practice dataset can get you more acquainted with application of deep learning in age detection.

## Project Structure

- `AGE_Detection.ipynb`: Jupyter notebook for training the age detection model.
- `AGE_Detection_load&Predict.ipynb`: Jupyter notebook for loading and predicting with the model (original version).
- `predict_age.py`: Python script to predict age from an image path using the command line.
- `Age_detection.h5`: The trained Keras model file (generated after running `AGE_Detection.ipynb`).
- `train.csv`: CSV file containing image IDs and their age classes (MIDDLE, YOUNG, OLD). (Needs to be provided by the user)
- `DataSet/Train/`: Directory containing the training images. (Needs to be populated by the user)

## Setup

1.  **Clone the repository (if applicable).**
2.  **Create a Python virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    A `requirements.txt` file is provided. Install the packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file will include:
    - tensorflow
    - pandas
    - numpy
    - matplotlib (for the notebooks)
    - Pillow (for image manipulation, often a Keras dependency)

## Training the Model

1.  **Prepare your dataset:**
    *   Ensure you have a `train.csv` file in the root directory. This file should have two columns: `ID` (image filename) and `Class` (age category: YOUNG, MIDDLE, OLD).
    *   Place your training images in a directory structure like `DataSet/Train/`. The image filenames in this directory should correspond to the `ID` column in `train.csv`.
    *   *(Note: The training notebook `AGE_Detection.ipynb` currently has a hardcoded path for `train_dir`. For full reproducibility, this should be changed to a relative path like `'DataSet/Train/'` as suggested in step 5 of the overall plan. This README assumes this change will be made or the user will adapt the path).*
2.  **Run the training notebook:**
    Open and run all cells in `AGE_Detection.ipynb` using Jupyter Notebook or JupyterLab. This will train the model and save it as `Age_detection.h5` in the root directory.

## Predicting Age

Once the model (`Age_detection.h5`) is trained and saved, you can use the `predict_age.py` script:

```bash
python predict_age.py path/to/your/image.jpg
```

Replace `path/to/your/image.jpg` with the actual path to the image you want to classify. The script will output the predicted age category (Young, Middle, Old).

**Example:**
If you have an image named `test_image.jpg` in the same directory as the script:
```bash
python predict_age.py test_image.jpg
```
Output:
```
The predicted age category is: Young
```
(or Middle, or Old, depending on the image)
