# Properties for PopsicleFinance

## Overview of the system

The system is a combination of ERC20 token and liquidity pool. Hence it has all the ERC20 properties.
As a liquidity pool, it allows user to make deposits, withdraw deposits and collect the user's share of fees collected. It keeps track of a map from user's address to the user data (fees collected per share and rewards)

To save time, this doc skips all the properties of ERC20, since that's pretty wellknown and standard. I will focus on the properties of the liquidity pool.

I will describe the properties based on the method names and variable names rather than the actual implementation. 

---

## Properties

1. ***Variable transition*** - Once user makes a deposit, user's share (represented by the ERC20 token balance) should increase accordingly. The total shares should increase as well. The `totalFeesEarnedPerShare` should decrease since the total shares have increased. User's `feesCollectedPerShare` should remain the same. User's reward should NOT decrease. User's asset in the system should increase.

2. ***Variable transition*** - Once user withdraws its shares, user's shares should decrease accordingly. The total shares should decrease as well. The `totalFeesEarnedPerShare` should increase since the total shares have decreased. User's `feesCollectedPerShare` should remain the same. User's reward should decrease. User's asset in the system should decrease.

3. ***Variable transition*** - Once user collect fees, user's shares should remain the same. The total shares should remain the same. The `totalFeesEarnedPerShare` should remain the same. User's `feesCollectedPerShare` should increase. User's reward decrease. User's asset in the system should decrease.

4. ***Variable transition*** - When owner do its job and earn fees to its clients, `totalFeesEarnedPerShare` should increase. Everything else should remain the same. User's asset in the system should increase

5. ***High-level properties*** - `totalFeesEarnedPerShare` should never decrease

6. ***High-level properties*** - `owner` should never change

---

## prioritizing

Apart from property 6, which is low-level property, everything else is high-level property
