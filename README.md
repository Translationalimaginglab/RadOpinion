# RadOpinion

## Description
RadOpinion is a web-based platform developed by the Translational Imaging Lab. It serves as a Medical Decision Support System that facilitates dynamic questionnaire generation and DICOM image visualization, with an aim to improve qualitative radiologic research and studies.

The application is built primarily using Python, HTML, and Batchfile scripting.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installing

1. Clone the repository to your local machine.
```bash
git clone https://github.com/Translationalimaginglab/RadOpinion.git
```
2. Navigate to the cloned repository.
```bash
cd RadOpinion
```
3. We recommend setting up a virtual environment to manage dependencies. Here's how to create one using venv:
```bash
python -m venv .venv
```
4. Activate the virtual environment. On Windows:
```bash
.\.venv\Scripts\activate
```
5. Install the project dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
## Usage

1. Start the Django server:
```bash
python .\manage.py runserver 8008
```
2. Open your browser and navigate to `http://localhost:8008/login/` to use the application.

Note: A batch file for deployment is provided in the repository. This can be used on a Windows machine by simply executing the `Deploy.bat` file.

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.


## Contact
## Pouria Yazdian 
1. Twitter: @Pouriayazdian
2. Email: pouria.yazdian@nih.gov
