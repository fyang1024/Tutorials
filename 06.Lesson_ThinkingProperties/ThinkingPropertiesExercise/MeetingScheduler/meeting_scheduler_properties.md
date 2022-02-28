# Properties for MeetingScheduler

## Overview of the system

The system keeps track of a map from meeting id to meeting. Each meeting has 5 states:

1. UNINITIALIZED
2. PENDING
3. STARTED
4. ENDED
5. CANCELLED

It has a set of functions that update the meeting: 

1. scheduleMeeting
2. startMeeting
3. cancelMeeting
4. endMeeting
5. joinMeeting

And it other functions to query meeting data

---

## Properties

1. ***Valid State*** - `meetingUninitialized(uint256 meetingId) =>` </br>
    `getStartTimeById(meetingId) == 0 &&` </br>
	`getEndTimeById(meetingId) == 0 &&` </br>
	`getStateById(meetingId) == 0 &&` </br>
	`getNumOfParticipants(meetingId) == 0 &&` </br>
	`getOrganizer(meetingId) == 0`

2. ***Valid State*** - `meetingPending(uint256 meetingId) =>` </br>
    `getStartTimeById(meetingId) > 0 &&` </br>
	`getEndTimeById(meetingId) > getStartTimeById(meetingId) &&` </br>
	`getStateById(meetingId) == 1 &&` </br>
	`getNumOfParticipents(meetingId) == 0 &&` </br>
	`getOrganizer(meetingId) != 0`

3. ***Valid State*** - `meetingStarted(uint256 meetingId) =>` </br>
    `getStartTimeById(meetingId) > 0 &&` </br>
	`getEndTimeById(meetingId) > getStartTimeById(meetingId) &&` </br>
	`getStateById(meetingId) == 2 &&` </br>
	`getOrganizer(meetingId) != 0`

4. ***Valid State*** - `meetingEnded(uint256 meetingId) =>` </br>
    `getStartTimeById(meetingId) > 0 &&` </br>
	`getEndTimeById(meetingId) > getStartTimeById(meetingId) &&` </br>
	`getStateById(meetingId) == 3 &&` </br>
	`getOrganizer(meetingId) != 0`

5. ***Valid State*** - `meetingCancelled(uint256 meetingId) =>` </br>
    `getStartTimeById(meetingId) > 0 &&` </br>
	`getEndTimeById(meetingId) > getStartTimeById(meetingId) &&` </br>
	`getStateById(meetingId) == 4 &&` </br>
	`getOrganizer(meetingId) != 0`

6. ***State Transition*** - The initial state is always UNINITIALIZED.

7. ***State Transition*** - From UNINITIALIZED, a meeting's state can only transition to PENDING

8. ***State Transition*** - From PENDING, a meeting's state can transition to either STARTED or CANCELLED

9. ***State Transition*** - From STARTED, a meeting's state can transition to ENDED

10. ***State Transition*** - Both CANCELLED and ENDED are final states, which means they cannot transition to other states anymore

11. ***State Transition*** - joinMeeting should not change the meeting's state

12. ***Variable transition*** - A meeting's numOfParticipents should increase by 1 after joinMeeting is called

13. ***High-level properties*** - A meeting's startTime, endTime and organizer should remain constant once scheduled

14. ***High-level properties*** - A meeting's numOfParticipents should never decrease

15. ***High-level properties*** - A meeting's startTime is always before the endTime

---
## prioritizing

I think all the properties have similar priorities in this case. If any of them is not met, the state/data becomes equally corrupt.
