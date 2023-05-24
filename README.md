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

Pouria Yazdian Anari, and AMPrj team
National Institutes of Health
May 2023
THIS SOFTWARE IS PROVIDED BY THE AUTHOR(S) ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Contact
## Pouria Yazdian 
1. Twitter: @Pouriayazdian
2. Email: pouria.yazdian@nih.gov
