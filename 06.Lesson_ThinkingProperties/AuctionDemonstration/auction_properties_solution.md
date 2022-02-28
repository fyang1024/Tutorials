## Token Reverse Auction System Properties

### Overview of the system

It is a token reverse auction system. It is a combination of two sub-systems, i.e., a token and a reverse auction system.

The token sub-system keeps track of a map from token owner to their token balance and the total supply of the token. It has 4 functions:

1. mint a certain amount of tokens to a token owner's address
2. transfer a certain amount of tokens from sender to receiver
3. get the balance of a token owner
4. get the total supply

The reverse auction sub-system keeps track of a map from auction id to auction. An auction has a prize, a payment, a winner, a bid expiry time and an end time. It also has an "owner" who has privilege to perform certain functions. It has 4 functions as well:

1. create a new auction. Only the "owner" can perform this function. The "owner" can only specify the payment of the auction. The new auction always has a prize of the max value of uint256, and its winner is the owner for now. The bid expiry is 0 initially. The end time is 1 day later than the time when the auction is created.
2. make a bid to an existing auction. The bidder specifies a new prize which has to be lower than the current prize. The bidder will transfer the payment tokens to the current winner first. Once that's done, the prize of the auction will be updated to the new prize specified by the bidder. And the winner will become the bidder. The bid expiry will be updated to 1 hour later than the bidding time.
3. close an auction. Anyone can call it, but it's more likely the winner of the auction will call it to receive the prize. It has to be called on an auction that's already bid, and it has to be called before the bid expiry and the end time. It also requires that current prize multiply by 2 won't exceed the max value of uint256 and the result of multiplication plus current total supply of the token won't exceed the max value of the uint256. If all the checks pass, it will mint the prize tokens to the winner and delete the auction.
4. get an auction details given an auction id.

That's how the system works.

I will break down the properties into the 5 categories based on [Certora's presentation](https://github.com/fyang1024/Tutorials/blob/master/06.Lesson_ThinkingProperties/Categorizing_Properties.pdf)

### Valid states

The token itself doesn't have any states.

The auction has 3 valid (implicit) states:

1. Non-existing
2. New
3. Bid but not expired
4. Bid and expired

### State transitions

The initial state is always Non-existing. 

Once the owner creates a new auction, the new auction's state is New. 

Once someone makes a bid to the auction successfully, its state becomes Bid but not expired.

Once the current time goes past the auction's end time or no one has made a new bid within an hour, its state becomes Bid and expired.

However, anyone can still bid on an auction that's bid and expired, which might turn its state back to bid but not expired if the end time is not reached yet, or its state remains bid and expired otherwise.

Anyone can close an auction that's bid and expired, and the auction becomes Non-existing again.

No one can close an auction that's not in bid and expired state.

### Variable transitions

There are 4 state variables:

1. the total supply of the token
2. a map from token owner address to its balance
3. the owner of the system
4. a map from auction id to auction

The initial total supply is 0, and no one has any token.

The mint function call should increase the balance of the target address and also increase the total supply by the same amount.

The transfer function reduces the sender's balance while increasing the receiver's balance by the same amount, but the total supply should remain unchanged.

The owner of the system should never be changed once set.

An auction's prize can only decrease but never increase.

An auction's payment should never change once created.

A New auction's winner should always be the system owner.

A New auction's bid expiry should always be 0.

An existing auction's end time should never be 0.

An existing auction's end time should never be changed.

An existing auction's winner can be changed.

An existing auction's bid expiry can only increase but not decrease

### High-Level Properties

The total supply of the token can only increase but never decrease.

The total supply of the token should remain constant until an auction is closed, because that's the only moment new tokens are mint.

The system owner should never be changed.

### Unit Tests

Skipped