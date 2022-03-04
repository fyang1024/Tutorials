certoraRun Loops.sol:Loops --verify Loops:LoopsUnrolling.spec \
--solc solc8.11 \
--loop_iter 10 \
--send_only \
--msg "$1"