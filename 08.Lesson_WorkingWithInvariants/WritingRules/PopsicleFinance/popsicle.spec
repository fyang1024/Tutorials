methods {
    assetsOf(address) returns (uint) envfree;
    balanceOf(address) returns (uint) envfree;
}

rule assetsNotDecreaseAfterDeposit() {
    env e;
    uint assetsBefore = assetsOf(e.msg.sender);
    deposit(e);
    uint assetsAfter = assetsOf(e.msg.sender);
    assert assetsAfter >= assetsBefore;
}

rule assetsNotIncreaseAfterWithdraw() {
    env e;
    uint assetsBefore = assetsOf(e.msg.sender);
    withdraw(e, balanceOf(e.msg.sender));
    uint assetsAfter = assetsOf(e.msg.sender);
    assert assetsAfter <= assetsBefore;
}

rule combinedAssetsUnchangedAferTransfer(address receiver) {
    env e;
    deposit(e);
    uint assetsOfSenderBefore = assetsOf(e.msg.sender);
    uint assetsOfReceiverBefore = assetsOf(receiver);
    transfer(e, receiver, e.msg.value);
    uint assetsOfSenderAfter = assetsOf(e.msg.sender);
    uint assetsOfReceiverAfter = assetsOf(receiver);
    assert assetsOfSenderBefore + assetsOfReceiverBefore == assetsOfSenderAfter + assetsOfReceiverAfter;
}

rule userAssetsIncreaseAfterOwnerJob(address user) {
    env e;
    uint assetsBefore = assetsOf(user);
    OwnerDoItsJobAndEarnsFeesToItsClients(e);
    uint assetsAfter = assetsOf(user);
    assert balanceOf(user) > 0 => assetsAfter > assetsBefore;
}