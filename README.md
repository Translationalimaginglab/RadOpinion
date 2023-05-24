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

## Contributing
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

Also, please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before you begin contributing.

For major changes, please open an issue first to discuss what you would like to change.


## License
This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.


## Contact
## Pouria Yazdian 
1. Twitter: @Pouriayazdian
2. Email: pouria.yazdian@nih.gov
