methods {
	// envfree methods
	getFullContenderDetails(address) returns(uint8, bool, uint256) envfree
	getFullVoterDetails(address) returns(uint8, bool, bool, uint256, bool) envfree
	getPointsOfContender(address) returns(uint256) envfree
	// env-dependent methods
	vote(address, address, address) returns(bool)
}

function getVoterRegistered(address voter) returns bool {
	uint8 age;
	bool registered;
	bool voted;
	uint256 vote_attempts;
	bool blocked;
	age, registered, voted, vote_attempts, blocked = getFullVoterDetails(voter);
	return registered;
}

function getVoterVoted(address voter) returns bool {
	uint8 age;
	bool registered;
	bool voted;
	uint256 vote_attempts;
	bool blocked;
	age, registered, voted, vote_attempts, blocked = getFullVoterDetails(voter);
	return voted;
}

function getVoterBlocked(address voter) returns bool {
	uint8 age;
	bool registered;
	bool voted;
	uint256 vote_attempts;
	bool blocked;
	age, registered, voted, vote_attempts, blocked = getFullVoterDetails(voter);
	return blocked;
}

function getVoterAttempts(address voter) returns uint256 {
	uint8 age;
	bool registered;
	bool voted;
	uint256 vote_attempts;
	bool blocked;
	age, registered, voted, vote_attempts, blocked = getFullVoterDetails(voter);
	return vote_attempts;
}

function getContenderRegistered(address contender) returns bool {
	uint8 age;
	bool registered;
	uint256 points;
	age, registered, points = getFullContenderDetails(contender);
	return registered;
}

definition unRegisteredVoter(address voter) returns bool =
!getVoterRegistered(voter);

definition registeredYetVotedVoter(address voter) returns bool =
getVoterRegistered(voter) &&
!getVoterVoted(voter);

definition legitRegisteredVotedVoter(address voter) returns bool =
getVoterRegistered(voter) &&
getVoterVoted(voter) &&
!getVoterBlocked(voter);

definition blockedVoter(address voter) returns bool =
getVoterRegistered(voter) &&
getVoterVoted(voter) &&
getVoterBlocked(voter);

invariant voterVotedMeansAtemptsNotZero(address voter)
	getVoterAttempts(voter) != 0 <=> getVoterVoted(voter)
		&&
		getVoterAttempts(voter) == 0 <=> !getVoterVoted(voter)
		
invariant voterAttempsLessThanFour(address voter)
	getVoterAttempts(voter) <= 3
	{
		preserved {
			requireInvariant voterVotedMeansAtemptsNotZero(voter);
		}
	}

invariant blockedVoterHas3Attempts(address voter)
	getVoterAttempts(voter) == 3 <=> getVoterBlocked(voter)
		&&
		getVoterAttempts(voter) < 3 <=> !getVoterBlocked(voter)
	{
		preserved {
			requireInvariant voterVotedMeansAtemptsNotZero(voter);
		}
	}

// Checks that each voted contender receieves the correct amount of points after each vote
rule correctPointsIncreaseToContenders(address first, address second, address third) {
	env e;
	uint256 firstPointsBefore = getPointsOfContender(first);
	uint256 secondPointsBefore = getPointsOfContender(second);
	uint256 thirdPointsBefore = getPointsOfContender(third);
	
	vote(e, first, second, third);
	uint256 firstPointsAfter = getPointsOfContender(first);
	uint256 secondPointsAfter = getPointsOfContender(second);
	uint256 thirdPointsAfter = getPointsOfContender(third);
	
	assert(firstPointsAfter - firstPointsBefore == 3, "first choice receieved other amount than 3 points");
	assert(secondPointsAfter - secondPointsBefore == 2, "second choice receieved other amount than 2 points");
	assert(thirdPointsAfter - thirdPointsBefore == 1, "third choice receieved other amount than 1 points");
	
}

