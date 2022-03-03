methods {
	// envfree methods
	balanceOf(address) returns(uint256) envfree
	totalSupply() returns(uint256) envfree
	// env-dependent methods
	add_liquidity() returns(uint256)
	remove_liquidity(uint)
	transfer(address, uint256) returns(bool)
}

rule balanceIncreasesAfterAddLiquidity() {
	env e;
	uint256 balanceBefore = balanceOf(e.msg.sender);
	uint256 units = add_liquidity(e);
	uint256 balanceAfter = balanceOf(e.msg.sender);
	assert balanceBefore + units == balanceAfter;
}

rule balanceDecreasesAfterRemoveLiquidity(uint units) {
	env e;
	uint256 balanceBefore = balanceOf(e.msg.sender);
	remove_liquidity(e, units);
	uint256 balanceAfter = balanceOf(e.msg.sender);
	assert balanceBefore - units == balanceAfter;
}

rule totalSupplyIncreasesAfterAddLiquidity() {
	env e;
	uint256 totalSupplyBefore = totalSupply();
	uint256 units = add_liquidity(e);
	uint256 totalSupplyAfter = totalSupply();
	assert totalSupplyBefore + units == totalSupplyAfter;
}

rule totalSupplyDecreasesAfterRemoveLiquidity(uint units) {
	env e;
	uint256 totalSupplyBefore = totalSupply();
	remove_liquidity(e, units);
	uint256 totalSupplyAfter = totalSupply();
	assert totalSupplyBefore - units == totalSupplyAfter;
}

// @note ERC20 properties are skipped