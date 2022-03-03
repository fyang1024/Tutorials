# Sparta Protocol Properties

## Properties

1. ***Variable Transition*** - `add_liquidity()` causes `balanceOf(e.msg.sender)` increases
1. ***Variable Transition*** - `add_liquidity()` causes `totalSupply()` increases
1. ***Variable Transition*** - `remove_liquidity(uint256)` causes `balanceOf(e.msg.sender)` decreases
1. ***Variable Transition*** - `remove_liquidity()` causes `balanceOf(e.msg.sender)` decreases

## Priorities

They are all high priorities