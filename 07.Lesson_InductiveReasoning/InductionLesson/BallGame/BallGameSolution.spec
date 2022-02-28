
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer3And4() 
	ballAt() !=3 <=> ballAt() != 4

rule neverReachPlayer4(method f) {
	env e;
	calldataarg args;
	require ballAt() != 3 && ballAt() != 4;
	f(e, args);
	assert ballAt() != 4, "The ball should never reach player 4 if it was not already at player 3 or 4";
} 