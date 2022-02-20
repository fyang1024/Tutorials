# format: <relative/path/to/solidity/file>:<contrac_name> --verify <contract_name>:<relative/path/to/spec/file>
#!/bin/bash
if [ "$#" -eq 3 ]
then 
  certoraRun ./"$1".sol:MeetingScheduler --verify MeetingScheduler:./meetings.spec \
    --solc solc8.7 \
    --rule "$2" \
    --msg "$3"
elif [ "$#" -eq 2 ]
then
  certoraRun ./"$1".sol:MeetingScheduler --verify MeetingScheduler:./meetings.spec \
    --solc solc8.7 \
    --msg "$2"
else
  echo "You need to supply 2 or 3 arguments"
fi  

# At the end of each line a backsalsh (\) is used for line continuation - to split overly long lines.
# more on backslash before new line here: https://superuser.com/questions/794963/in-a-linux-shell-why-does-backslash-newline-not-introduce-whitespace#:~:text=The%20Backslash%2Dnewline%20is%20used,purposes%20of%20executing%20the%20script.

# The $1 is the first argument given to the script, so we can change the msg of a run without changing the actual script
# more on $1 here: https://bash.cyberciti.biz/guide/$1