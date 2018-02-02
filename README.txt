1) All the files required are under the folder PCA in the submission

2) The source code is a file named PCA.py (Python version 2.7) and it can be run using the command 

	python PCA.py

3)If scikit is not installed, it can be installed using the following command

	sudo pip install -U scikit-learn

4)If a new dataset is to be read, add the dataset file to folder PCA and in the source code in file PCA.py, call function PCA with the new dataset name. For example if the new file is demo_pca.txt, replace lines 102,103 and 104 in PCA.py to 

	PCA(‘demo_pca.txt’)