# Machine Learning Engineer Nanodegree
# Capstone Project
## MACHINE LEARNING IN PRODUCT CATEGORIZATION: APPLICATION OF A SUPERVISED LEARNING MODEL IN A REAL E-COMMERCE DATASET

### Install

This project requires **Python 3.5** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

### Code

Template code is provided in the `src/product_categorizer.ipynb` notebook file. You will also be required to use the included `src/adjust_category.py`, `src/constants.py`, `src/dsLib.py` and `src/mlLib.py` Python files and the `dataset/zxpd_201712121136_12011_38441474.tar.gz` dataset file to run the project.

### Run

In a terminal or command window, navigate to the project directory `product_categorizer/src` and run the following commands:

```bash
jupyter notebook boston_housing.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

```bash
cd dataset
tar xvf zxpd_201712121136_12011_38441474.tar.gz
```
This will decompress the dataset.

### Data

The original dataset belongs to Walmart, consists of 2,625,975 products and can be found on [Zanox Marketplace](https://publisher.zanox.com).

However, for storage reasons, we will remain only the availabe products for sale, 1,244,371 products.

After preprocessing that, we will have a modified dataset with 1,228,176 products and this format:

**Main Features**

0. `NAME`: product name;
1. `BRAND`: product manufacturer brand;

**Auxiliar Features**

2. `GENDER`: if the product is for men, women...
3. `ROOM`: if the product is for kitchen, office...
4. `VEHICLE`: if the product is related to cars, motorcycles...
5. `CONSOLE`: if the product is related to PlayStation, XBox...
6. `DEVICE`: if the product is related to smartphones, tablets...
7. `PET`: if the product is related to dogs, cats...
8. `MATTRESS`: if the product is related to single, double...
9. `CUP`: if the product is related to water, beer...

**Target Variable**

10. `CATEGORY`: product category path.

### Udacity Review

0. [Capstone proposal](https://review.udacity.com/#!/reviews/915449)
1. [Capstone project #1](https://review.udacity.com/#!/reviews/1027271)
2. [Capstone project #2]((https://review.udacity.com/#!/reviews/1044802)
