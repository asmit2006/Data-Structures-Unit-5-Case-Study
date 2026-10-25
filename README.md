# Data-Structures-Unit-5-Case-Study

# Case Study: GPS / Navigation System Using a Weighted Graph

## Aim
Model a city map as a weighted graph and use a graph algorithm to find the shortest route between two locations.

## Concepts
- **Vertices:** city locations such as a station, hospital, mall, university, or airport.
- **Edges:** roads connecting locations.
- **Weights:** road distances in kilometres.
- **Dijkstra's algorithm:** computes the minimum-distance path when edge weights are non-negative.

## Features
- Sample city road network is loaded automatically.
- Display locations, roads, and distances.
- Find the shortest route between two locations.
- Add locations and add/update roads interactively.
- Reports when a route cannot be found.

## Requirements
Python 3.x. No external packages are required.

## Run
```bash
python gps_navigation.py
```

Choose **Find shortest route** and enter exact location names, for example `Central Station` and `Airport`.

## Example
The sample graph includes roads such as Central Station–City Mall (3 km), City Mall–City Hospital (2 km), and City Hospital–University (4 km). The program computes the route and total distance based on the graph.

## Complexity
With the adjacency-list representation and a priority queue, Dijkstra's algorithm runs in approximately **O((V + E) log V)**, where `V` is the number of locations and `E` is the number of roads.

## Limitation
This is an educational simulation using sample distances. It does not use live GPS coordinates, traffic, turn restrictions, or real-time road data.
