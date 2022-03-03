# Borda Properties

1. ***High-level*** - `registerVoter(uint8 age) == true`  iff. `getFullVoterDetails(address voter)` return 0s
2. ***High-level*** - ``registerVoter(uint8 age) == true`  iff. `getFullContenderDetails(address contender)` return 0s
3. ***High-level*** - voter.vote_attempts < 3 <=> voter.black_listed == false
4. ***High-level*** - voter.vote_attempts <= 3
5. ***High-level*** - voter.vote_attempts == 3 <=> voter.black_listed == true
6. ***High-level*** - hasVoted(voter) == false <=> voter.vote_attempts == 0
7. ***High-level*** - hasVoted(voter) == true <=> voter.vote_attempts > 0
8. ***Variable Transition*** - `vote(address, address, address)` success implies 3 contenders' points increase by 3, 2, 1 respectively
9. ***Variable Transition*** - if `registerVoter(uint8 age) == true`, then `getFullVoterDetails(msg.sender)` should return the voter details correctly
10. ***Variable Transition*** - if `registerContender(uint8 age) == true`, then `getFullContenderDetails(msg.sender)` should return the contender correctly

## Priorities

All the high-level properties have higher priorities than others.