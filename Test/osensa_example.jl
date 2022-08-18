#Import Julia Libraries
using SerialPorts, PyCall,Pkg

#Setting the Python distribution I want PyCall to use 
ENV["PYTHON"] = raw"C:\ProgramData\Anaconda3\python.exe"

#Rebuilding PyCall to use new Python distribution
Pkg.build("PyCall")

#ENV["PYTHON"] = raw"C:\ProgramData\Anaconda3\python.exe" & Pkg.build("PyCall") can be commented after running the code once

#Importing Osensapy library in Julia 
osensa = pyimport("Osensapy2")

#Creating an object (trans) of Osensa Transmitter class 
trans =  osensa.Transmitter("COM8", 247, baudrate = 115200)

#Read the temperature 
println(trans.read_channel_temp("A"))