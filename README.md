# Epidemic Simulation
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BaileyDalton007/Epidemic-Simulator)


A graphical interface to simulate epidemic outbreaks in a closed population through adjustable parameters

![image](https://user-images.githubusercontent.com/59097689/152481544-e865bef6-cb45-47db-b9a0-51c8f01fd237.png)

## Installation


Clone the repository and run ```app.py```
## Usage


### Population Viewer

The left side of the window is the matplotlib display of the population.  
Blue points are healthy, red are currently infected, and gray points are dead and cannot infect other points.  
To select a patient zero, click on a healthy point in the population, and they will display as infected.

![image](https://user-images.githubusercontent.com/59097689/152481742-c44d7ae8-dad0-41dc-9c73-76b08c448363.png)

### Population Generation

Under the ```Data``` tab are the controls to generate population sets.   
The population slider determines the size of the population.
The random seed input takes an integer and uses it as a seed to produce the random positions of the points with ```np.random.seed()```. This allows for population reproducibility for population and seed are the same. If no seed is input the default value is 0

![image](https://user-images.githubusercontent.com/59097689/152482746-68431e60-e42b-45b5-a199-6dfb24a40091.png)

### Disease Modification

Under the ```Disease``` tab are the controls to modify the properties of the disease itself.   
The spread radius is the distance from an infected point where the disease can be spread and is visualized with the red circle displayed around infected points in the population viewer. The default value is zero.   
Infection length is the length of simulation days that an infection will last. After being infected, a point will stay infected for the time specified and will return to being healthy after, if still living. The Default value is 1 day.    
The rate of infection is the chance that a point within the spread radius will become infected. On a day-by-day basis and will compound if a healthy point is within the spread radii of multiple infected points.   
The mortality rate is the chance that an infected point will die. Also works on a day-by-day basis.

![image](https://user-images.githubusercontent.com/59097689/152483436-1200b363-9663-405d-8960-171a6e929d61.png)

### Simulation Operations

The ```Simulation``` tab has the controls for running and saving the simulation.   
Days of Simulation is an integer input for the number of days the simulation will run at a time. The default value is 1 day.   
The Start Simulation button starts the simulation for the defined number of days and will display the result in the population viewer.
Save Current Simulation as CSV saves the data of the current run of the simulation in the file ```SimOutput.csv```.

![image](https://user-images.githubusercontent.com/59097689/152484905-6cae3199-5244-49c4-be85-4ce274eb494c.png)


## Output Data
After a simulation is saved, it will be output as a CSV file that can be analyzed will other data visualization tools. Below is raw output data.

![image](https://user-images.githubusercontent.com/59097689/152485885-7710ccca-f1e0-43ce-ba66-b6bef511ef99.png)

```(x, y)``` is the randomly generated position for each point from 0 to 1.   
```Status``` is an array of a point's status of each day simulated. 0 - healthy; 1 - infected; 2 - dead.   
```InfTime``` is the array of a point's history of the day in which it was infected. A value of -1 means that the point is not currently infected.

## Future Work
I am about done with my work on this application, although contributions are welcome.   
I plan to work on a CLI to parse the CSV and visualize the data in different ways, hopefully, I get to that eventually.

### Written in Python 3.7.6
## License
[MIT](https://choosealicense.com/licenses/mit/)