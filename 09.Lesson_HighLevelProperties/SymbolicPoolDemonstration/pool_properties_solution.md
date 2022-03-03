# Pool Properties

## Overview

This is a asset pool which allows users to deposit/withdraw the asset to/from the pool. 
The pool provides flash loan service for a service fee.

## Properties

1. ***High-level*** - `sharesToAmount(amountToShares(a)) == a`
2. ***High-level*** - `amountToShares(sharesToAmount(s)) == s`
3. ***High-level*** - `totalSupply() == 0 <=> asset.balanceOf(address(this)) == 0`
4. ***Variable transitions*** - `deposit(uint256)` called => `balanceOf(msg.sender)` increases and `totalSupply()` increases by the same amount
5. ***Variable transitions*** - `withdraw(uint256)` called => `balanceOf(msg.sender)` decreases and `totalSupply()` decreases by the same amount
6. ***High-level*** - `flashLoan(address, uint256)` called => `asset.balanceOf(address(this))` increases and `totalSupply()` remains the same and `balanceOf(msg.sender)` remains the same

## Priorities

I think they are equally important.