Tutorial and examples for using Apache Spark
=============================================

This repository contains jupyter notebooks and examples data-sets for my Apache Spark tutorial.

_NOTE: Please note that the tutorial is still under active development, so please make sure you update (pull) it on the day of the workshop_

### Prerequisites

Required skills:

- Confident user of `python` programming language including the use of `map`, `filter` and `reduce` functions and `lambda` expressions.
- Basic skills in using Linux based operating systems 

_If you need a bush-up the_ `python` _part please check  out he following tutorials:_ [Python2 Tutorial](http://www.python-course.eu/lambda.php) _or_ [Python Functions - map ...](http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php).


(Highly) Recommended skills:

- Familiarity with ipython/jupyter notebooks (<https://jupyter.org/>)
- Familiarity the Databricks platform (see below)
- Experience with `python` packages such as `pandas` and `scikit-learn`
- Basic understanding of Machine Learning concepts such as: classification, regression, linear models, training and testing sets, cross validation, parameter turning

Helpful skills:

- Experience with `python` packages such as `numpy` and  `matplotlib`
- Experience with R 
- Exposure to functional programming
- Exposure to SQL and RDBMS (Relational Data Management Systems)
- Basic understanding of Hadoop Map-Reduce and Hadoop HDFS
- Basic experience with using public cloud services (AWS or Google Cloud)

### Running on Databricks Community Platform.

The easiest to run the examples is to use the [Databricks Platform](https://databricks.com/), which provides a cloud based analytics platform  for data science and  engineering. Databricks was founded by the team who created Apache Spark, and works with the open source community to continue to expand the project.

In addition to the commercial platform Databricks offers a **free** [Community Edition](https://databricks.com/product/faq/community-edition), which is a great way to learn both the Databricks Platform, Apache Spark and to run this tutorial.

To sign up for a **free** account go to: <https://community.cloud.databricks.com/>

To learn how to use Databricks Platform please familiarize yourself with the [Getting Started](https://docs.databricks.com/user-guide/getting-started.html) guide. 

You may also like to check out some of the featured notebooks, for example  [Introduction to Apache Spark on Databricks](https://docs.databricks.com/_static/notebooks/gentle-introduction-to-apache-spark.html).

_If it seems a bit complicated, do not panic - we well cover the basic at the workshop._

To setup the Databricks Platform for the tutorial:

1. In your `Workspace` create a folder named `spark-tutorial`
2. Import to `spark-tutorial` the notebook from this URL: <https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/setup/0.1_Setup_DataBricks.ipynb>  (or from the file in `setup/0.1_Setup_DataBricks.ipynb`) 
3. Run the notebook with `Run All` on the default cluster `MyCluster` - it should run without errors
4. `Restart` `MyCluster`

To verify that the setup if correct and run you first tutorial notebook:

1. Import to `spark-tutorial` the notebook from this URL: <https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/0.1_Welcome.ipynb> (or from the file in `notebooks/0.1_Welcome.ipynb`) 
2. `Run All` the notebook - it should run without errors (the and the output should be like [this](https://piotrszul.github.io/spark-tutorial/databricks/0.1_Welcome.html)
3. Please, have a look through the notebook to familiarize yourself with different ways of using the notebook to: run python code, shell commands and visualize the results. 

To run the rest of the tutorial follow the steps above for other notebooks in the `notebooks` directory. 

Here are the URLs to copy:


* [1.1_RDD-Basics.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/1.1_RDD-Basics.ipynb)
* [1.2_RDD_Data-Processing.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/1.2_RDD_Data-Processing.ipynb)
* [1.3_RDD_Text-Processing.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/1.3_RDD_Text-Processing.ipynb)
* [2.1_StructuredData-Introduction.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/2.1_StructuredData-Introduction.ipynb)
* [2.2_StructuredData-Formats.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/2.2_StructuredData-Formats.ipynb)
* [2.3_StructuredData-Analyzing.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/2.3_StructuredData-Analyzing.ipynb)
* [3.1_ML-Introduction.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/3.1_ML-Introduction.ipynb)
* [3.2_ML_Classification-Text.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/3.2_ML_Classification-Text.ipynb)
* [3.3_ML_Classification-Categorical.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/3.3_ML_Classification-Categorical.ipynb)
* [4.1_SparkR-Introduction.html](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/R/4.1_SparkR-Introduction.html)
* [5.1_BigData_Genomics-Clustering.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/5.1_BigData_Genomics-Clustering.ipynb)
* [5.2_BigData_Genomics_Visualise.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/5.2_BigData_Genomics_Visualise.ipynb)



### Running locally with Docker

You can also run the tutorial notebooks on your computer with the [Docker Platform](https://www.docker.com/what-docker).

First you need to install Docker Community Edition for you computer and OS from <https://www.docker.com>.

Once the installation is successful you need to download the Docker image with the tutorial to your machine.

_WARNING: The image size is about 5GB so you will need to have at least that amount of free disk space. The download size is also a few giga-bytes so be mindful of your Internet usage and the time it may take to finish._

To download the image at the command prompt type:

    docker pull piotrszul/spark-tutorial
       
Once the download is complete you can start your local pyspark enabled jupyter notebook with:

    docker run -it  -p 8888:8888  piotrszul/spark-tutorial

If all is good you should see the following output:
    
    [I 02:41:57.564 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
    [W 02:41:57.895 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
    [W 02:41:57.896 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using authentication. This is highly insecure and not recommended.
    [I 02:41:57.903 NotebookApp] Serving notebooks from local directory: /home/jovyan/spark-tutorial/notebooks
    [I 02:41:57.903 NotebookApp] 0 active kernels 
    [I 02:41:57.903 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:8888/
    [I 02:41:57.903 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

You can navigate your browser now to: <http://localhost:8888/> to see the list of the tutorial notebooks.

1. Open the `0.1_Welcome.ipynb` and run all the cells with `Cell\Run All` - it should run without errors (the and the output should be like [this](https://piotrszul.github.io/spark-tutorial/notebooks/0.1_Welcome.html)
2. Please, have a look through the notebook to familiarize yourself with the different ways of using the notebook to: run python code, shell commands and visualize the results.

**IMPORTANT**

**When you are done with the notebook close it with** `File\Close and Halt`**. ONLY ONE pyspark notebook may be running at any given time.**

To stop the `jupyter` server press `[Ctrl+C]` twice at the console window.

You can start it again at any time with the `docker run ...` command above.

_NOTE: Every time you use_ `docker run ...` _the server will start from the clean image, without any changes that you might have made. If you want to preserve your changes use the --name option when you run the server for the first time and then_ `start` _command to connect to it again, e.g.: _

    # run a server (container) named `my-server` for the first time:
    
    docker run -it  -p 8888:8888 --name 'my-server' piotrszul/spark-tutorial 
    
    # do some work and stop the server
    # to start `my-server` again use: 
    
    docker start -i 'my-server'
    
_NOTE: Please note that the_ `piotrszul/spark-tutorial` _image is still under active development, so please make sure you update (pull) it on the day of the workshop. The update is incremental so the download size should not exceed 100MB)_

### Look at HTML version

Just go [https://piotrszul.github.io/spark-tutorial/](https://piotrszul.github.io/spark-tutorial/).

### Running the on big data on Google Cloud

The [5.1_BigData_Genomics-Clustering.ipynb](https://raw.githubusercontent.com/piotrszul/spark-tutorial/master/notebooks/5.1_BigData_Genomics-Clustering.ipynb) example can be run on the entire chromosome 22 data (or potentially the entire genome) with Google Cloud  `Dataproc` service. 

The instruction is available in [google-cloud/README.md](google-cloud/README.md)

### References

All data sets used in this tutorial are described in [data/README.md](data/README.md)

[Apache Spark](http://spark.apache.org/):

- [Python API Docs](http://spark.apache.org/docs/latest/api/python/index.html)
- [Spark Programming Guide](http://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [Spark SQL Programming Guide](http://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Spark ML Programming Guide](http://spark.apache.org/docs/latest/ml-guide.html)
- [Spark R Programming Guide](http://spark.apache.org/docs/latest/sparkr.html)

[Google Cloud](https://cloud.google.com/)
    
- [Public Datasets](https://cloud.google.com/public-datasets/)
- [1000 Genomes Public Dataset](http://googlegenomics.readthedocs.io/en/latest/use_cases/discover_public_data/1000_genomes.html)
    
Other interesting sites:

- [Kaggle](https://www.kaggle.com/) - data science competitions with (sometime huge) prizes + interesting data sets
- [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/index.php) - many interesting machine learning data sets 
    




