#!/usr/bin/env bash

# checks user input
userOptions() {
  # quits program when "q" is entered
  if [[ $1 = exit ]]; then
    echo -e "\n Quitting Menu \n"
  fi

  # calls launchMenu function again when a char is entered besides "q"
  if [[ $1 = [a-zA-z] ]]; then
    launchMenu
  fi

  # programs
  if [[ $1 = 1 ]]; then
    python ./arithmetic_formatter.py
  elif [[ $1 = 2 ]]; then
    python ./shortest_algorithm.py
  elif [[ $1 = 3 ]]; then
    python ./sudoku_solver.py
  elif [[ $1 = 4 ]]; then
    python ./vector_space.py
  fi
}

#launch menu options
launchMenu() {
  if $1; then
    echo -e "\n Please Enter a Valid Option \n"
  fi

  echo -e "\n Select a Script To Run"
  echo -e "########################\n"

  echo -e "1 -> Arithmetic Formatter"
  echo -e "2 -> Shortest Path Algorithm"
  echo -e "3 -> Sudoku Solver"
  echo -e "4 -> Vector Space"
  echo -e "\"exit\" -> exit \n"

  read -r userInput

  userOptions "$userInput"
}

launchMenu
