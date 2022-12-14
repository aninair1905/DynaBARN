# DynaBARN
Repository for [DynaBARN](https://cs.gmu.edu/~xxiao2/Research/DynaBARN/DynaBARN.html). This code can be used to generate various DynaBARN environments of obstacles with different motion profiles. The 60 premade DynaBARN environments are at https://tufts.box.com/s/0dsoen9yno1qrnpj0l75eni7kmjdcx7c
The Gazebo world files are under the folder titled 'DynaBARN_worlds_60'. The plugin files are under 'all_cylinder_plugins'.
To simulate the 60 premade DynaBARN worlds, export the location of the plugins to the plugin path variable using 
```
export GAZEBO_PLUGIN_PATH=/path/to/plugins/testplugin/all_cylinder_plugins
```
Then simulate the environment using 
```
gazebo world_{world number}.world
```
## Example Worlds

![combined_big](https://user-images.githubusercontent.com/46573631/186241202-04005054-4157-46e2-b602-7565d62e8ba4.gif)


<!-- Easy World:


https://user-images.githubusercontent.com/46573631/185812166-b76cddd9-d2ca-4fd8-9a64-c41cc706c32e.mp4


Medium World:


https://user-images.githubusercontent.com/46573631/185812169-6a711fa1-8616-484b-a1df-7e8b1ccbf1d3.mp4


Hard World:


https://user-images.githubusercontent.com/46573631/185812175-7e8c0e44-5bd3-4981-8738-a84f4accdd21.mp4

 -->


## Requirements
* Python 2
* NumPy
* Matplotlib
* SciPy
## Using this repository
After cloning this repository onto your computer, create two folders called "plugins" and "worlds" in the same directory. 
There are a few arguments for creating the trajectories and worlds:
* --save_dir and --plugin_dir are the directories for the world files and plugins, respectively
* --min_object and --max_object are the minimum and maximum number of obstacles in each world
* --n_worlds are the number of worlds to generate 
* --min_speed and --max_speed are the minimum and maximum speeds between each waypoint in the trajectories for each obstacle
* --min_std and --max_std are the minimum and maximum standard deviations in speed between each waypoint
* --difficulty is the difficulty to label each trajectory, but it is not necessary
