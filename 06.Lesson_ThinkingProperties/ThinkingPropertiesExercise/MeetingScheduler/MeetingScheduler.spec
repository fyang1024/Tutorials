
methods {
	// envfree methods
	getStartTimeById(uint256) returns (uint256) envfree
	getEndTimeById(uint256) returns (uint256) envfree
	getStateById(uint256) returns (uint8) envfree
	getNumOfParticipents(uint256) returns (uint256) envfree
	// env-dependent methods
	scheduleMeeting(uint256, uint256, uint256)
    startMeeting(uint256)
    endMeeting(uint256)
    cancelMeeting(uint256)
    joinMeeting(uint256)
}

definition meetingUninitialized(uint256 meetingId) returns bool = 
	getStartTimeById(meetingId) == 0 && 
	getEndTimeById(meetingId) == 0 && 
	getStateById(meetingId) == 0 && 
	getNumOfParticipents(meetingId) == 0;

definition meetingPending(uint256 meetingId) returns bool = 
	getStartTimeById(meetingId) > 0 && 
	getEndTimeById(meetingId) > getStartTimeById(meetingId) && 
	getStateById(meetingId) == 1 && 
	getNumOfParticipents(meetingId) == 0;

definition meetingStarted(uint256 meetingId) returns bool = 
	getStartTimeById(meetingId) > 0 && 
	getEndTimeById(meetingId) > getStartTimeById(meetingId) && 
	getStateById(meetingId) == 2;

definition meetingEnded(uint256 meetingId) returns bool = 
	getStartTimeById(meetingId) > 0 && 
	getEndTimeById(meetingId) > getStartTimeById(meetingId) && 
	getStateById(meetingId) == 3;

definition meetingCancelled(uint256 meetingId) returns bool = 
	getStartTimeById(meetingId) > 0 && 
	getEndTimeById(meetingId) > getStartTimeById(meetingId) && 
	getStateById(meetingId) == 4;


rule meetingPendingAfterScheduled(uint256 meetingId, uint256 startTime, uint256 endTime) {
	env e;
    scheduleMeeting(e, meetingId, startTime, endTime);
	assert meetingPending(meetingId), "the meeting should be in pending state after scheduling";
}

rule meetingStartedAfterStarting(uint256 meetingId) {
	env e;
    require meetingPending(meetingId);
    startMeeting(e, meetingId);
	assert meetingStarted(meetingId), "the meeting should be in started state after starting";
}


rule meetingEndedAfterEnding(uint256 meetingId) {
	env e;
    require meetingStarted(meetingId);
    require e.block.timestamp > getEndTimeById(meetingId);
    endMeeting(e, meetingId);
	assert meetingEnded(meetingId), "the meeting should be in ended state after ending";
}

rule meetingCancelledAfterCancelling(uint256 meetingId) {
	env e;
    require meetingPending(meetingId);
    cancelMeeting(e, meetingId);
	assert meetingCancelled(meetingId), "the meeting should be in cancelled state after cancelling";
}

rule meetingStartedAfterJoining(uint256 meetingId) {
	env e;
    require meetingStarted(meetingId);
    joinMeeting(e, meetingId);
	assert meetingStarted(meetingId), "the meeting should be in started state after joining";
}
