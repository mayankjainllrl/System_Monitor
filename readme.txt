Credential: This repository is developed by Mayank Jain.
Contact: mayankjainllrl@gmail.com

This app monitors how much % of CPU and memory of our PC is used by our container.

Steps:


1. Install docker and run any container of your choice 
	(whose usage you want to track).


2. You can use my container also. 
	Command for pulling my container is given below.

   Pull it using: 
	"docker pull mayankjainllrl/sample_docker_app" 
	(make sure to login to docker first)
   I have also provided the Dockerfile and app code for my container in this repository.


3. While running the container make sure to provide it a name with "--name" and remember it.

Example:
	docker run -p 8888:5000 --name test mayankjainllrl/sample_docker_app
	
	here you can replace test with any name you desire 
	also you can specify any app you want to track by 
	replacing mayankjainllrl/sample_docker_app with your app name.


4. Now head to monitor_app_files folder I have provided requirements.txt. 
   You can create a new virtual environment using it so that app runs smoothly on your PC too. 


5. Run the python file and enter the name (step 3) of your container when asked by program.


Note:
	I have set the ylim to 2% only if  your app is using more percentage of CPU and memory you can increase it as per your needs.
	If you have pulled my app and using it for testing. Refresh page several times to visualize greater change in monitor. 


