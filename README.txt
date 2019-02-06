# This folder contains the source code for the projects in the Machine Learning is Fun! book.

# To run these projects, you'll need to first install Python 3.6 and quite a few Python libraries.
# I recommend using the pre-configured virtual machine to run the examples if you aren't experienced
# in installing Python libraries.

# If you want to configure your own Linux machine from scratch instead of using the provided VM for some reason,
# you can follow the same approach used to configure the Ubuntu 18.04 virtual machine. Here are those commands:

# Install the required base libraries and development environment.
sudo apt install -y --fix-missing build-essential

cmake
gfortran
git
wget
curl


libgraphicsmagick1-dev
libavcodec-dev
libavformat-dev
libgtk2.0-dev
libjpeg-dev
liblapack-dev
libswscale-dev
pkg-config
software-properties-common

# installed:
npm
python3
python3-pip
python3-dev
python3-tk
zip

# Install the Python libraries used by the examples
cd ~/Desktop/project_code/
pip3 install -r requirements.txt

# Install the large English language model for spaCy
python3 -m spacy download en_core_web_lg
python3 -m spacy link en_core_web_lg en

# Install the Rasa NLU Trainer application used to create training data.
npm i -g rasa-nlu-trainer

# Install fastText and the fastText Python bindings (not available on pip)
# DONE
cd ~/
git clone https://github.com/facebookresearch/fastText.git
cd fastText
make
sudo cp fasttext /usr/local/bin
pip3 install .

# Install the Mask R-CNN library (not available on pip)
cd ~/
git clone https://github.com/matterport/Mask_RCNN.git
cd Mask_RCNN
pip3 install -r requirements.txt
cd ..
git clone https://github.com/waleedka/coco
cd coco/PythonAPI
sudo python3 setup.py install
cd ../..
sudo python3 setup.py install

