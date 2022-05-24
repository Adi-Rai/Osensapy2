# Osensapy2
My version of Osensapy package to run in Julia. <br />
Download this package by running: "pip install git+https://github.com/Adi-Rai/Osensapy2.git" <br />
After downloading this package in your preferred python environment, set the PyCall environment to the same path. <br />
For eg: ENV["PYTHON"] = raw"C:\Users\<your_name>\anaconda3\python.exe" <br />
Then rebuild the PyCall library using Pkg.build("PyCall") <br />
This package can then be imported in Julia using : pyimport("osensapy2'). <br />
