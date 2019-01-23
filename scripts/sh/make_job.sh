#!/bin/sh
# Author: abpwrs
# Created: Wed Jun  6 12:01:23 CDT 2018

# script input validation
if [[ ${#} -ne 1 ]]; then
# example usage
  echo "Usage: ${0} name_without_spaces"
  echo "Example: ${0} random_forest"
  exit -1
fi


# Standard job setup
FILENAME="$1.job"

# Makes a general job_output directory in your home dir
# only need this one for the first run of the script
mkdir /Users/${USER}/job_output
# makes a dir for your spesific job
mkdir /Users/${USER}/job_output/${1}

cat > ${FILENAME} << EOF 
#!/bin/sh
# Author: ${USER}
# Created: $(date)


# Argon Arguments
# https://wiki.uiowa.edu/display/hpcdocs/Basic+Job+Submission

# set name to be the same as the file
#$ -N ${1}

# set queue (default to UI)
#$ -q UI

# set max wall-runtime to be one day -- you may need to change this depending on your problem
#$ -l h_rt=24:00:00

# an example environment configuration (see docs for more details)
#$ -pe smp 16

# set standard output of file
#$ -o /Users/${USER}/job_output/${1}/${1}_output

# set standard error output file
#$ -e /Users/${USER}/job_output/${1}/${1}_error

# set my email address
#$ -M alexander-powers@uiowa.edu

# set when I want emails (b: beginning, e: end, a: aborted, s: suspended)
#$ -m beas

# script here:




EOF

chmod 700 $FILENAME

