# Hungarian Globe Solver

## About the Globe
The Globe puzzle is a spherical tile rotation puzzle similar to a Rubik's Cube. The puzzle presents as a globe with three intersecting rings containing 12 tiles each. The rings are arraigned perpendicularly to one-another with one ring corresponding to the equator, and the other two corresponding to lines of longitude. The rings rotate freely with each tile occupying 30 of either latitude or longitude. In normal latitude and longitude the globe is divided into Noth and South Hemispheres with latitude being defined relative to the equator, while longitude is divided into East and West hemispheres relative to the prime meridian. <be/>

<p align="center">
  <img src="https://cdn.globalauctionplatform.com/7fb92bd3-fc51-47f3-8252-a5540102caf3/6d65dd0a-443c-4ceb-bf31-d15b90acbf09/540x360.jpg" />
</p>

For the sake of simplicity we use a notation where latitude coordinates run from 0° at the north pole to 180° at the south. Longitude goes for 360° around the globe. Thus in this coordinate system the vertical rings run along longitude 0° to 180° and 90° to 270°, and the equator ring contains tiles at latitude 90°. The vertical rings intersect at the "North  Pole" (latitude 0°, longitude 0°) and the "South Pole" (latitude 180° and longitude 180°). And they intersect with the equator at the following points: (90°, 0°), (90°, 180°), (90°, 90°), and (90°, 270°). The tiles on the rings are numbered as follows: <br>

* Longitude 0/180: (0°, 0°), (30°, 0°), (60°, 0°), (90°, 0°), (120°, 0°), (150°, 0°), (180°, 180°), (150°, 180°), (120°, 180°), (90°, 180°), (60°, 180°), (30°, 180°)

* Longitude 90/270:  (0°, 0°), (30°, 90°), (60°, 90°), (90°, 90°), (120°, 90°), (150°, 90°), (180°, 180°), (150°, 270°), (120°, 270°), (90°, 270°), (60°, 270°), (30°, 270°)

* Equator: (90°, 0°), (90°, 30°), (90°, 60°), (90°, 90°), (90°, 120°), (90°, 150°), (90°, 180°), (90°, 210°), (90°, 240°), (90°, 270°), (90°, 300°), (90°, 330°)

## Input Files
The data 'folder' contains a set of files that describe marble puzzles. Each line of the file looks as follows:
<br/> <br/>
<code>Tile(30-180, (90,270), Exact(30,180))</code>
<br/><br/>
This specifies a single tile. In this case we have a tile with ID "30-180" that is currently at latitude and longitude (90,270) and which has an exact target coordinates of latitude and longitude (30,180) to match. A puzzle is complete when all of its tiles are at their target locations.

## Algorithms
In this project, the globe is solved using 3 algorithms: <br/>
1. Breadth First Search(BFS) <br/>
2. A* Algorithm (ASTAR) <br/>
3. Recursive Breadth First Search (RBFS) <br/>

Algorithm can be changed by changing the 'ALGORITHM' environment variable in '.env' file. 
