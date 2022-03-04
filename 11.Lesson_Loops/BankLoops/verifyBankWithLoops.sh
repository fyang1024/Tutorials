certoraRun BankWithLoops.sol:Bank --verify Bank:Loops.spec \
--solc solc7.6 \
--send_only \
--optimistic_loop \
--loop_iter 3 \
--msg "$1"