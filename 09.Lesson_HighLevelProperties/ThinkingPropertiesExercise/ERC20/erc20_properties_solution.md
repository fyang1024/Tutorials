# ERC20 Properties

## Properties

1. ***High-level*** - `totalSupply()` never changes
2. ***High-level*** - `decimals()` is 18 and never changes
3. ***High-level*** - `name()` never changes
4. ***High-level*** - `symbol()` never Changes
5. ***High-level*** - `balanceOf(user) <= totalSupply()`
6. ***Variable Transition*** - `transfer` increases the receiver's balance and reduce the sender's balance by the same amount
7. ***Variable Transition*** - `transferFrom` increases the to's balance and reduce the from's balance by the same amount
8. ***Variable Transition*** - `transferFrom` reduces the allowance by the amount sent
9. ***Variable Transition*** - `increaseAllowance` increases the spender's allowance
9. ***Variable Transition*** - `decreaseAllowance` decreases the spender's allowance

## Priorities
3 and 4 are low priorities, all the other are high priorities
