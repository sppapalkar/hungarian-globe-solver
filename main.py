#Imports
import os, re, sys, time, logging
from dotenv import load_dotenv
from src.util import display_path
from src.bfs import bfs
from src.astar import a_star, calc_heuristic
from src.rbfs import RecursiveBfs

# Load Env variables
load_dotenv()
input_file_path = os.getenv('INPUT_FILE_PATH')
algorithm = os.getenv('ALGORITHM')

# Display File Path
def read_file(file_path, initial_state, goal_state):
    #   Local declarations 
        pattern = '.*?\\((.*?),\\s\\((.*?)\\),\\s.*?\\((.*?)\\)\\)'# Regex Pattern
        
        with open(file_path,'r') as f:
            for line in f:
                match_ob = re.search(pattern,line)
                if match_ob:
                    initial_state.append([int(org) for org in 
                                        match_ob.group(2).split(',')])# Reading Initial State
                    goal_state.append([int(dest) for dest in 
                                        match_ob.group(3).split(',')])# Reading Goal State

# Display final results
def dispay_results(solution, time):
    print('\nAlgorithm: {}'.format(algorithm))
    print('No of States Expanded: ',solution['explored'])
    print('Max Size of Queue: ',solution['max_length'])
    print('Final Path Length: ',solution['state']['cost'])
    print('Final Path: ',display_path(solution['state']['moves']))
    print('Time Elapsed: ',(time))

# Find the solution path using various algorithms
def find_path():
    initial_state = []
    goal_state = []
    read_file(input_file_path, initial_state, goal_state)

    if algorithm=='BFS':
        start_time = time.time()
        solution = bfs(initial_state,goal_state)
        end_time = time.time()
        dispay_results(solution, (end_time - start_time))
    elif algorithm=='ASTAR':
        start_time = time.time()
        solution = a_star(initial_state,goal_state)
        end_time = time.time()
        dispay_results(solution, (end_time - start_time))
    elif algorithm == 'RBFS':
        ob = RecursiveBfs(initial_state, goal_state)
        start_time = time.time()
        initial_st = {'state':initial_state, 'cost':0, 'h_cost':0, 'alt_cost':0, 'moves':[0]}
        ob.calc_heuristic(initial_st)
        ob.rbfs(initial_st, 99999)
        end_time = time.time()
        print('Time Elapsed: ',(end_time-start_time))
    else:
        print('Invalid Algorithm')

if __name__ == "__main__":
    find_path()


