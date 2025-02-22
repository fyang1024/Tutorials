methods {
	getTokenAtIndex(uint256) returns(address) envfree
	getIdOfToken(address) returns(uint256) envfree
	getReserveCount() returns(uint256) envfree
	addReserve(address, address, address, uint256) envfree
	removeReserve(address) envfree
}

invariant correlatedLists(uint256 i, address t)
	((i == 0 && t != 0) =>(getTokenAtIndex(i) == t => getIdOfToken(t) == i)) &&
		((i != 0 && t != 0) =>(getIdOfToken(t) == i <=> getTokenAtIndex(i) == t))
	{
		preserved addReserve(address token, address stableToken, address varToken, uint256 fee) {
			require token != 0;
			bool alreadyAdded = getTokenAtIndex(getIdOfToken(token)) != 0 || getTokenAtIndex(0) == token;
			require !alreadyAdded;
		}
		
		preserved removeReserve(address token) {
			// make sure different token have different ids, otherwise the invariant will be violated by havocing
			require token == t || getIdOfToken(token) != i;
		}
	}

// @note this is not an invariant, as it might not be true after removeReserve is called
rule noTokenSavedAtReserveCountOrFurther(uint256 i, address token, address stableToken, address varToken, uint256 fee) {
	require i >= getReserveCount() => getTokenAtIndex(i) == 0;
	addReserve(token, stableToken, varToken, fee);
	assert i >= getReserveCount() => getTokenAtIndex(i) == 0;
}

invariant injectivityOfId(address t1, address t2)
	(getIdOfToken(t1) != 0 && getIdOfToken(t1) == getIdOfToken(t2)) => t1 == t2
	{
		preserved addReserve(address token, address stableToken, address varToken, uint256 fee) {
			require token != 0;
			bool alreadyAdded = getTokenAtIndex(getIdOfToken(token)) != 0 || getTokenAtIndex(0) == token;
			require !alreadyAdded;
		}
		
		preserved removeReserve(address token) {
			require getTokenAtIndex(getIdOfToken(token)) != 0;
		}
	}

rule independencyOfTokensOnRemove(address t1, address t2) {
	require t1 != t2 && t1 != 0 && t2 != 0;
	uint256 id1 = getIdOfToken(t1);
	uint256 id2 = getIdOfToken(t2);
	require id1 != id2;
	require getTokenAtIndex(id1) == t1;
	require getTokenAtIndex(id2) == t2;
	
	removeReserve(t2);
	
	assert getIdOfToken(t1) == id1 && getTokenAtIndex(id1) == t1;
}

rule nonViewFunctionChangesReserveCountByOne(method f) {
	require
		f.selector == addReserve(address, address, address, uint256).selector ||
		f.selector == removeReserve(address).selector;
	uint256 reserveCountBefore = getReserveCount();
	env e;
	calldataarg args;
	f(e, args);
	uint256 reserveCountAfter = getReserveCount();
	assert
		f.selector == addReserve(address, address, address, uint256).selector => reserveCountAfter == reserveCountBefore + 1 &&
		f.selector == removeReserve(address).selector => reserveCountAfter == reserveCountBefore - 1;
}