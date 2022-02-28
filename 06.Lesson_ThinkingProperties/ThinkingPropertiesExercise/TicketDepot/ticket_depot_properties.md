# Properties for MeetingScheduler

## Overview of the system

The system allows users to create events and sell/buy tickets for the events. Users can also re-sell tickets.
It has the following state variables:

1. numEvents
2. owner
3. transactionFee
4. eventsMap 
5. offerings

An Event has the following structure
```
    {  
		address owner;  
		uint64 ticketPrice;  
		uint16 ticketsRemaining;  
		mapping(uint16 => address) attendees;  
	}
```
The Offering has the following structure    
```
    {  
		address buyer;
		uint64 price;
		uint256 deadline;
	}
```

---
## Properties

1. ***Variable Transition*** - The initial value of numEvents should be 0.

2. ***Variable Transition*** - The owner value should not be 0

3. ***Variable Transition*** - The transactionFee can be any uint64 value

4. ***Variable Transition*** - Once `createEvent(uint64 _ticketPrice, uint16 _ticketsAvailable)` is called, `numEvents` should increase by 1, `eventsMap[eventID]` should return the new event, and the ticket price and tickets available should be as specified in the parameters. The `eventID` is the return value of function call.

5. ***Variable Transition*** - Once `buyNewTicket(uint16 _eventID, address _attendee)` is called successfully, `numEvents` should remain the same,  `eventsMap[_eventID].ticketsRemaining` should decrease by 1, `eventsMap[_eventID].attendees[ticketID]` should be the `_attendee` passed in, `eventsMap[_eventID].owner` should receive the `eventsMap[_eventID].ticketPrice`, and the owner should receive the transactionFee.

6. ***Variable Transition*** - Once `offerTicket` is called successfully, `numEvents` should remain the same. `eventsMap` should not be affected. `offerings` map should have a new entry with details passed from the parameters. The reseller will receive a transaction fee.

7. ***Variable Transition*** - Once `buyOfferedTicket` is called successfully. The event's attendee should be updated to the buyer. The offering should be deleted

8. ***High-level*** - `numEvents` can only increase

9. ***High-level*** - `owner` never change

10. ***High-level*** - No more than available tickets can be sold for an event

11. ***High-level*** - Only the event attendee can resell a ticket

12. ***High-level*** - Only enough fund has been paid can buy a new ticket or ticket offered

13. ***High-level*** - Transaction fee never changes

---
## prioritizing

Apart from property 9, everything else is high priority