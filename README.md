# MLOps architecture example
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub issues](https://img.shields.io/github/issues/esalvucci/kubeflow-example)

## About
This project is intended to provide an example of MLOps architecture. It uses the code of a 
[Kaggle Notebook](https://www.kaggle.com/francoisraucent/forecasting-electricity-consumption-of-germany)
as use case example. The original code has been edited such to adapt it for the example in this project.

You can find the documentation about how each technology is used in the [doc](doc) folder 

In this project is used preferably Free Software (except for Google Cloud Build).

## Technologies
Use the following links to read the detailed documentation about how each technology is used in this project.

* [MLFlow](doc/mlflow) - Used to track the experiments log, the model versions and to store them in a Model Registry
* [Kubeflow](doc/kubeflow) - Used to orchestrate the ML workflow
* [Google Cloud Build](doc/kubeflow) - Used to build a CI pipeline 

## Licence
This project is licensed under the GPLv3 Licence - see the [LICENSE](LICENSE) file for details